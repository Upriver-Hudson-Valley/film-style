#!/usr/bin/env python3
"""Validate an OpenFilm `film.html` highlight cut directly against Joshua Brown's
corrected 17-film EDITING-SPEC.md §13 QA contract and sequence-grammar.json.

Why this exists alongside `film-style compare`:
  `film-style compare` compares against the original tool-detected baseline
  (~24 cuts/min), which under-counted dark dance-floor cuts. This validator
  checks the exact corrected targets (~30 cuts/min, 1.65s median, 0.48-0.70s
  dissolves, fast last-20% finale, zero never-observed scene transitions, and
  `"Name and Name"` title rule) straight from `film.html`.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

SKILL_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
FRAG_RE = re.compile(r"#t=([0-9.]+)(?:,([0-9.]+))?")


class _FilmParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.track_idx = -1
        self.track_hidden = False
        self.clips: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k: ("" if v is None else v) for k, v in attrs}
        if tag == "section":
            self.track_idx += 1
            self.track_hidden = "hidden" in a
            return
        if self.track_hidden or "disabled" in a:
            return
        if tag in ("video", "iframe", "img", "audio"):
            at = float(a["at"]) if a.get("at") else 0.0
            speed = float(a["speed"]) if a.get("speed") else 1.0
            src = a.get("src", "")
            m = FRAG_RE.search(src)
            t_in = float(m.group(1)) if m else 0.0
            t_out = float(m.group(2)) if (m and m.group(2)) else None
            dur = ((t_out - t_in) / speed) if (t_out is not None and speed > 0) else None
            overrides = []
            if a.get("overrides"):
                try:
                    overrides = json.loads(a["overrides"])
                except json.JSONDecodeError:
                    overrides = []
            self.clips.append({
                "tag": tag,
                "track": self.track_idx,
                "id": a.get("id") or Path(src.split("#")[0]).stem,
                "src": src,
                "at": round(at, 3),
                "duration": round(dur, 3) if dur is not None else None,
                "end": round(at + dur, 3) if dur is not None else None,
                "speed": speed,
                "scene": a.get("data-scene") or None,
                "overrides": overrides,
            })


def _load_never_observed(grammar_path: Path) -> set[tuple[str, str]]:
    if not grammar_path.is_file():
        return set()
    data = json.loads(grammar_path.read_text(encoding="utf-8"))
    pairs: set[tuple[str, str]] = set()
    for item in data.get("never_observed_transitions") or []:
        if isinstance(item, (list, tuple)) and len(item) == 2:
            pairs.add((str(item[0]), str(item[1])))
        elif isinstance(item, dict) and item.get("from") and item.get("to"):
            pairs.add((str(item["from"]), str(item["to"])))
    return pairs


def validate(film_html: Path, grammar_path: Path | None = None) -> dict[str, Any]:
    parser = _FilmParser()
    parser.feed(film_html.read_text(encoding="utf-8"))

    videos = [c for c in parser.clips if c["tag"] == "video" and c["duration"] and c["duration"] > 0]
    videos.sort(key=lambda c: (c["at"], c["track"]))
    pages = [c for c in parser.clips if c["tag"] == "iframe"]
    stills = [c for c in parser.clips if c["tag"] == "img"]

    if not videos:
        return {"ok": False, "errors": ["No timed <video> clips with #t=in,out found in film.html."]}

    runtime = max(c["end"] for c in videos if c["end"] is not None)
    durs = [c["duration"] for c in videos]
    n = len(videos)
    cpm = round(n / (runtime / 60.0), 1) if runtime > 0 else 0.0
    med = round(statistics.median(durs), 2)
    mean = round(statistics.fmean(durs), 2)
    pct_under_3 = round(100.0 * sum(1 for d in durs if d < 3.0) / n, 1)
    holds_4 = [c for c in videos if c["duration"] >= 4.0]
    holds_6 = [c for c in videos if c["duration"] >= 6.0]
    dance_holds_6 = [c for c in holds_6 if (c["scene"] or "").lower() == "dancing"]

    last20_start = runtime * 0.8
    last20_durs = [c["duration"] for c in videos if (c["at"] + c["duration"] / 2) >= last20_start]
    last20_med = round(statistics.median(last20_durs), 2) if last20_durs else None

    first_shot = durs[0]
    first5_avg = round(statistics.fmean(durs[:5]), 2)
    last5_avg = round(statistics.fmean(durs[-5:]), 2)

    # Detect dissolves (overlapping fade-in on video clips) and mid-film fades.
    dissolves: list[float] = []
    bad_dissolves: list[dict[str, Any]] = []
    mid_fades: list[dict[str, Any]] = []
    for i, c in enumerate(videos):
        for ov in c["overrides"]:
            if isinstance(ov, dict) and "fade" in ov and isinstance(ov["fade"], list) and len(ov["fade"]) == 2:
                f_in, f_out = float(ov["fade"][0]), float(ov["fade"][1])
                if f_in > 0 and i > 0:
                    # Check if overlapping with a previous video clip -> dissolve; else mid-film fade-in.
                    prev_overlaps = any(p["at"] < c["at"] < (p["end"] or 0) for p in videos[:i])
                    if prev_overlaps:
                        dissolves.append(f_in)
                        if f_in < 0.45 or f_in > 0.75:
                            bad_dissolves.append({"clip": c["id"], "fade_in_sec": f_in})
                    else:
                        mid_fades.append({"clip": c["id"], "kind": "mid_fade_in", "sec": f_in})
                if f_out > 0 and i < n - 1:
                    next_overlaps = any(c["at"] < nx["at"] < (c["end"] or 0) for nx in videos[i + 1:])
                    if not next_overlaps:
                        mid_fades.append({"clip": c["id"], "kind": "mid_fade_out", "sec": f_out})

    # Check title rule: "Name and Name", never "&".
    title_ampersand_issues: list[str] = []
    for p in pages:
        for ov in p["overrides"]:
            if isinstance(ov, dict) and isinstance(ov.get("text"), str) and "&" in ov["text"]:
                title_ampersand_issues.append(f"{p['id']}: {ov['text']!r} uses '&' instead of 'and'")

    # Check never_observed_transitions if data-scene tags are present.
    never_set = _load_never_observed(grammar_path or (SKILL_DATA_DIR / "sequence-grammar.json"))
    forbidden_hits: list[dict[str, Any]] = []
    seen_scenes = [c["scene"] for c in videos if c["scene"]]
    for a, b in zip(seen_scenes, seen_scenes[1:]):
        if a != b and (a, b) in never_set:
            forbidden_hits.append({"from": a, "to": b})

    issues: list[str] = []
    warnings: list[str] = []

    if not (268 <= runtime <= 411):
        warnings.append(f"Runtime {runtime:.1f}s outside acceptable 268–411s (typical 348–392s).")
    if not (26 <= cpm <= 35):
        issues.append(f"Cuts/min {cpm} outside acceptable 26–35 (target ~30).")
    if not (1.4 <= med <= 1.9):
        issues.append(f"Median shot {med}s outside acceptable 1.4–1.9s (target 1.65s).")
    if not (81 <= pct_under_3 <= 95):
        warnings.append(f"Shots <3s is {pct_under_3}% (acceptable 81–95%, target 88%).")
    if len(holds_6) > 5:
        warnings.append(f"{len(holds_6)} shots ≥6s (acceptable 0–5, target ~2).")
    if dance_holds_6:
        issues.append(f"Found {len(dance_holds_6)} shot(s) ≥6s in dancing (banned — dance floor is a fast montage).")
    if last20_med is not None and last20_med > 1.7:
        warnings.append(f"Final 20% median shot is {last20_med}s (max 1.7s, target 1.5s).")
    if first_shot > 4.3:
        issues.append(f"First shot is {first_shot}s (never >4.3s; target 2.9s).")
    if bad_dissolves:
        issues.append(f"{len(bad_dissolves)} dissolve(s) outside 0.48–0.70s (median 0.55s): {bad_dissolves[:5]}")
    if mid_fades:
        issues.append(f"{len(mid_fades)} mid-film fade(s) detected (MUST be 0): {mid_fades[:5]}")
    if title_ampersand_issues:
        issues.append("Title uses '&' instead of 'and': " + "; ".join(title_ampersand_issues))
    if stills:
        issues.append(f"Found {len(stills)} <img> still clip(s) on timeline (banned — stills are color-reference only): {[s['id'] for s in stills[:5]]}")
    if forbidden_hits:
        issues.append(f"Never-observed scene transitions found: {forbidden_hits}")

    return {
        "ok": len(issues) == 0,
        "film": str(film_html),
        "metrics": {
            "runtime_sec": round(runtime, 2),
            "shot_count": n,
            "still_image_clips": len(stills),
            "cuts_per_min": cpm,
            "median_shot_sec": med,
            "mean_shot_sec": mean,
            "pct_shots_under_3s": pct_under_3,
            "shots_4s_plus": len(holds_4),
            "shots_6s_plus": len(holds_6),
            "median_shot_last_20pct_sec": last20_med,
            "first_shot_sec": first_shot,
            "first5_avg_sec": first5_avg,
            "last5_avg_sec": last5_avg,
            "dissolve_count": len(dissolves),
            "dissolve_median_sec": round(statistics.median(dissolves), 2) if dissolves else None,
        },
        "issues": issues,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate an OpenFilm film.html against Joshua Brown's 17-film EDITING-SPEC.md."
    )
    parser.add_argument("film_html", type=Path, help="Path to OpenFilm film.html")
    parser.add_argument("--grammar", type=Path, default=None, help="Optional path to sequence-grammar.json")
    args = parser.parse_args()

    result = validate(args.film_html, args.grammar)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
