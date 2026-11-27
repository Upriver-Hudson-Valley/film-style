#!/usr/bin/env python3
"""Upload rendered OpenFilm wedding deliverables to Cloudflare R2 and ingest
selected masters into Mux Video, emitting a unified publish manifest +
joshuabrownphotography.com website entry JSON.

Required environment variables:
  Cloudflare R2 (S3-compatible):
    R2_ACCOUNT_ID
    R2_ACCESS_KEY_ID
    R2_SECRET_ACCESS_KEY
    R2_BUCKET
    R2_PUBLIC_BASE_URL   (e.g. https://media.joshuabrownphotography.com)

  Mux Video (optional if --skip-mux):
    MUX_TOKEN_ID
    MUX_TOKEN_SECRET

Requires `boto3` when uploading to R2 (or use `--dry-run` to preview keys and
URLs without making network calls).
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

VIDEO_EXTS = {".mp4", ".mov", ".webm"}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def _require_env(name: str) -> str:
    val = os.environ.get(name, "").strip()
    if not val:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return val


def _r2_client():
    try:
        import boto3  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "boto3 is required for R2 uploads (`pip install boto3`)."
        ) from exc

    account_id = _require_env("R2_ACCOUNT_ID")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=_require_env("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=_require_env("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
    )


def _mux_request(method: str, path: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    token_id = _require_env("MUX_TOKEN_ID")
    token_secret = _require_env("MUX_TOKEN_SECRET")
    auth = base64.b64encode(f"{token_id}:{token_secret}".encode("utf-8")).decode("ascii")
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        f"https://api.mux.com{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Mux API {method} {path} failed ({exc.code}): {detail}") from exc


def create_mux_asset(source_url: str, *, policy: str = "public", quality: str = "plus",
                     wait: bool = True, timeout_sec: int = 600) -> dict[str, Any]:
    resp = _mux_request(
        "POST",
        "/video/v1/assets",
        {
            "inputs": [{"url": source_url}],
            "playback_policy": [policy],
            "video_quality": quality,
        },
    )
    asset = resp["data"]
    asset_id = asset["id"]

    if wait:
        deadline = time.time() + timeout_sec
        while asset.get("status") not in ("ready", "errored") and time.time() < deadline:
            time.sleep(5)
            asset = _mux_request("GET", f"/video/v1/assets/{asset_id}")["data"]

    playback_ids = asset.get("playback_ids") or []
    playback_id = playback_ids[0]["id"] if playback_ids else None
    return {
        "asset_id": asset_id,
        "status": asset.get("status"),
        "playback_id": playback_id,
        "hls_url": f"https://stream.mux.com/{playback_id}.m3u8" if playback_id else None,
        "poster_url": (
            f"https://image.mux.com/{playback_id}/thumbnail.jpg?width=1920&fit_mode=smartcrop"
            if playback_id else None
        ),
        "preview_webp_url": (
            f"https://image.mux.com/{playback_id}/animated.webp?start=10&end=15&width=640"
            if playback_id else None
        ),
    }


def collect_deliverables(root: Path) -> list[Path]:
    files: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in (VIDEO_EXTS | IMAGE_EXTS):
            files.append(p)
    return files


def should_ingest_mux(rel_posix: str) -> bool:
    name = Path(rel_posix).name.lower()
    if Path(rel_posix).suffix.lower() not in VIDEO_EXTS:
        return False
    # Stream highlight, trailer, ceremony, and speeches on website via Mux.
    return any(tok in name for tok in ("highlight", "trailer", "ceremony", "speeches"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Upload OpenFilm wedding renders to Cloudflare R2 and Mux Video."
    )
    parser.add_argument("--wedding", required=True, help="Wedding slug (e.g. emma-and-alex-blooming-hill)")
    parser.add_argument("--year", required=True, help="Wedding year (e.g. 2026)")
    parser.add_argument("--dir", type=Path, required=True, help="Directory of rendered MP4/image deliverables")
    parser.add_argument("--out", type=Path, default=None, help="Output path for publish-manifest.json")
    parser.add_argument("--mux-policy", choices=("public", "signed"), default="public")
    parser.add_argument("--mux-quality", choices=("basic", "plus", "premium"), default="plus")
    parser.add_argument("--skip-mux", action="store_true", help="Upload to R2 only")
    parser.add_argument("--no-wait-mux", action="store_true", help="Do not poll Mux until ready")
    parser.add_argument("--dry-run", action="store_true", help="Print planned R2 keys & Mux calls without uploading")
    args = parser.parse_args()

    if not args.dir.is_dir():
        print(f"Error: deliverables directory not found: {args.dir}", file=sys.stderr)
        return 2

    files = collect_deliverables(args.dir)
    if not files:
        print(f"Error: no video/image files found under {args.dir}", file=sys.stderr)
        return 2

    public_base = os.environ.get("R2_PUBLIC_BASE_URL", "https://media.example.com").rstrip("/")
    bucket = os.environ.get("R2_BUCKET", "<R2_BUCKET>")
    s3 = None if args.dry_run else _r2_client()

    items: list[dict[str, Any]] = []
    for path in files:
        rel = path.relative_to(args.dir).as_posix()
        r2_key = f"weddings/{args.year}/{args.wedding}/{rel}"
        r2_url = f"{public_base}/{r2_key}"
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"

        record: dict[str, Any] = {
            "local_file": str(path),
            "relative_path": rel,
            "content_type": content_type,
            "size_bytes": path.stat().st_size,
            "r2_bucket": bucket,
            "r2_key": r2_key,
            "r2_public_url": r2_url,
            "mux": None,
        }

        if not args.dry_run:
            assert s3 is not None
            s3.upload_file(
                str(path),
                bucket,
                r2_key,
                ExtraArgs={"ContentType": content_type},
            )

        if not args.skip_mux and should_ingest_mux(rel):
            if args.dry_run:
                record["mux"] = {
                    "planned": True,
                    "source_url": r2_url,
                    "policy": args.mux_policy,
                    "quality": args.mux_quality,
                }
            else:
                record["mux"] = create_mux_asset(
                    r2_url,
                    policy=args.mux_policy,
                    quality=args.mux_quality,
                    wait=not args.no_wait_mux,
                )

        items.append(record)

    manifest = {
        "schema_version": "1.0",
        "wedding_slug": args.wedding,
        "year": args.year,
        "dry_run": args.dry_run,
        "items": items,
        "metricool_ready_urls": [
            {"relative_path": i["relative_path"], "url": i["r2_public_url"]}
            for i in items
            if Path(i["relative_path"]).suffix.lower() in VIDEO_EXTS
            and ("reel" in i["relative_path"].lower() or "9x16" in i["relative_path"].lower() or "trailer" in i["relative_path"].lower())
        ],
    }

    out_path = args.out or (args.dir / "publish-manifest.json")
    out_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote manifest ({len(items)} items, dry_run={args.dry_run}) → {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
