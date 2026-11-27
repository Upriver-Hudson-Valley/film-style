#!/usr/bin/env python3
"""Load Joshua Brown's personal wedding editing spec and film-style-analyzer
artifacts into one unified OpenFilm production contract JSON.

Precedence order:
  1. Live local files under ~/.film-style-analyzer/ (or --data-root)
  2. Bundled 17-film empirical artifacts in this skill's data/ directory:
       - EDITING-SPEC.md (single source of truth; wins on conflicts)
       - style-profile.json
       - sequence-grammar.json
       - shot-selection-rules.json
       - coverage-checklist.md
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SKILL_DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Corrected QA targets from EDITING-SPEC.md §13 (17-film empirical corpus,
# adjusted for ~690 missed cuts in dark reception footage).
CORRECTED_QA_CONTRACT: dict[str, Any] = {
    "fps": 23.976,
    "runtime_sec": {"target": 359, "typical": [348, 392], "acceptable": [268, 411]},
    "cuts_per_min": {"target": 30, "typical": [28, 33], "acceptable": [26, 35]},
    "shot_count": {"target": 185, "typical": [175, 200], "acceptable": [140, 215]},
    "median_shot_sec": {"target": 1.65, "acceptable": [1.4, 1.9]},
    "mean_shot_sec": {"target": 1.9, "typical": [1.8, 2.0], "acceptable": [1.7, 2.2]},
    "pct_shots_under_3s": {"target": 88, "acceptable": [81, 95]},
    "shots_4s_plus": {"target": 7, "acceptable": [3, 13]},
    "shots_6s_plus": {"target": 2, "acceptable": [0, 5], "never_on_dance_floor": True},
    "median_shot_last_20pct_sec": {"target": 1.5, "max": 1.7},
    "first_shot_sec": {"target": 2.9, "typical": [2.3, 3.1], "acceptable": [0.7, 4.3]},
    "first5_avg_sec": {"target": 2.4, "typical": [1.8, 2.5], "acceptable": [1.4, 2.9]},
    "last5_avg_sec": {"target": 3.0, "typical": [2.2, 3.7], "acceptable": [1.5, 3.9]},
    "opening_rules": {
        "never_open_on_person": True,
        "fade_up_from_black_default": True,
        "title_font": "Recoleta",
        "title_format": "Name and Name (use word 'and', never '&')",
        "title_window_sec": [0, 10],
    },
    "closing_rules": {
        "end_on_couple_alone": True,
        "prefer_fading_light": True,
        "hard_cut_to_black_default": True,
    },
    "transitions": {
        "hard_cut_share_pct": 60,
        "dissolves": {"target": 35, "typical": [24, 42], "length_sec": [0.48, 0.70], "median_sec": 0.55},
        "still_holds": {"target": 21, "typical": [16, 25], "note": "Live slow-mo/locked video settling; NEVER insert <img> still photos"},
        "still_image_clips_allowed": 0,
        "fades": {"first_frame_only_in": True, "last_frame_only_out": True, "mid_film_max": 0},
    },
    "audio": {
        "snap_cuts_to_beats": False,
        "beat_phase_concentration_R": 0.05,
        "story_film": {"speech_sec": [84, 173], "median_speech_sec": 120, "first_words_sec": [7, 23], "median_first_words_sec": 16.6},
        "music_only": {"speech_sec_max": 12},
        "tempo_bpm": {"median": 112, "typical": [99, 123]},
        "loudness": {"integrated_lufs": -14, "tolerance_lu": 1, "true_peak_dbtp_max": -1, "lra_lu": [8, 12]},
    },
    "color": {
        "mean_luma_0_255": [90, 104],
        "contrast_std": [52, 60],
        "warm_cool_index": [0.19, 0.25],
        "saturation_0_255": [81, 100],
        "warm_overcast_to_match_daylight": True,
        "night_stays_neutral": True,
        "let_day_darken_luma": {"opening_fifth": 106, "closing_fifth": 79},
    },
    "framing": {
        "observational_distance": True,
        "medium_full_pct": 33,
        "full_pct": 30,
        "no_person_pct": 25,
        "medium_pct": 11,
        "close_up_pct_max": 1,
        "headroom_pct_typical": [13, 37],
        "ignore_deepface_emotion": True,
    },
}


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_error": f"Failed to parse {path}: {exc}"}


def _read_jsonl(path: Path) -> list[dict[str, Any]] | None:
    if not path.is_file():
        return None
    out: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


def _read_text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _first_existing(candidates: list[Path]) -> Path | None:
    for p in candidates:
        if p.is_file():
            return p
    return None


def load_bundle(data_root: Path, genre: str, *, include_full_tables: bool = False) -> dict[str, Any]:
    genre_root = data_root / genre
    effective_root = genre_root if genre_root.is_dir() else data_root
    craft_dir = effective_root / "edit-craft"

    resolved: dict[str, str] = {}
    missing_local: list[str] = []

    def resolve_json(name: str, candidates: list[Path]) -> dict[str, Any] | None:
        hit = _first_existing(candidates)
        if hit:
            resolved[name] = str(hit)
            return _read_json(hit)
        missing_local.append(str(candidates[0]))
        return None

    def resolve_text(name: str, candidates: list[Path]) -> str | None:
        hit = _first_existing(candidates)
        if hit:
            resolved[name] = str(hit)
            return _read_text(hit)
        missing_local.append(str(candidates[0]))
        return None

    editing_spec_md = resolve_text(
        "editing_spec",
        [effective_root / "EDITING-SPEC.md", SKILL_DATA_DIR / "EDITING-SPEC.md"],
    )
    style_profile = resolve_json(
        "style_profile",
        [effective_root / "style-profile.json", SKILL_DATA_DIR / "style-profile.json"],
    )
    sequence_grammar = resolve_json(
        "sequence_grammar",
        [craft_dir / "sequence-grammar.json", effective_root / "sequence-grammar.json", SKILL_DATA_DIR / "sequence-grammar.json"],
    )
    shot_selection_rules = resolve_json(
        "shot_selection_rules",
        [craft_dir / "shot-selection-rules.json", effective_root / "shot-selection-rules.json", SKILL_DATA_DIR / "shot-selection-rules.json"],
    )
    coverage_checklist_md = resolve_text(
        "coverage_checklist",
        [craft_dir / "coverage-checklist.md", effective_root / "coverage-checklist.md", SKILL_DATA_DIR / "coverage-checklist.md"],
    )

    shot_profile = resolve_json("shot_profile", [data_root / "shot-profile.json"])
    edit_profile = resolve_json("edit_profile", [effective_root / "edit-profile.json"])
    structure_template = resolve_json("structure_template", [effective_root / "structure-template.json"])
    soundbite_profile = resolve_json("soundbite_profile", [effective_root / "soundbite-profile.json"])

    corrections_path = effective_root / "corrections.jsonl"
    corrections = _read_jsonl(corrections_path)
    if corrections is not None:
        resolved["corrections"] = str(corrections_path)
    else:
        missing_local.append(str(corrections_path))

    bundle: dict[str, Any] = {
        "schema_version": "2.0",
        "source_precedence": "EDITING-SPEC.md (17-film corrected empirical spec) > local ~/.film-style-analyzer > bundled skill data/",
        "data_root": str(data_root),
        "genre": genre,
        "resolved_files": resolved,
        "optional_local_missing": missing_local,
        "corrected_qa_contract": CORRECTED_QA_CONTRACT,
        "style_profile_summary": {
            "film_count": (style_profile or {}).get("film_count"),
            "duration": (style_profile or {}).get("duration"),
            "color": (style_profile or {}).get("color"),
            "music": (style_profile or {}).get("music"),
            "scenes_count": len((style_profile or {}).get("scenes") or {}),
        },
        "sequence_grammar_summary": {
            "n_films": (sequence_grammar or {}).get("n_films"),
            "n_transitions_observed": (sequence_grammar or {}).get("n_transitions_observed"),
            "required_scenes": [
                s["label"]
                for s in ((sequence_grammar or {}).get("scene_presence") or [])
                if s.get("policy") == "required"
            ],
            "never_observed_count": len((sequence_grammar or {}).get("never_observed_transitions") or []),
        },
        "shot_selection_scenes": sorted((shot_selection_rules or {}).keys()),
        "shot_profile": shot_profile,
        "edit_profile": edit_profile,
        "structure_template": structure_template,
        "soundbite_profile": soundbite_profile,
        "corrections_count": len(corrections) if corrections is not None else 0,
        "openfilm_defaults": {
            "fps": 23.976,
            "title_font": "Recoleta",
            "allow_still_images_in_video": False,
            "show_vendor_handles_on_social_cuts": True,
            "highlight_viewport": "1920x1080",
            "highlight_render_flags": ["--fps", "23.976", "--4k", "--loudness=-14"],
            "vertical_viewport": "1080x1920",
            "vertical_render_flags": ["--fps", "23.976", "--loudness=-14"],
            "camera_input_default": "canon-clog3",
            "luts": {
                "raw_clog": str(SKILL_DATA_DIR.parent / "assets" / "luts" / "CLOGOrion.cube"),
                "rec709": str(SKILL_DATA_DIR.parent / "assets" / "luts" / "Orion.cube"),
            },
            "integrations": {
                "pic_time_mcp_sse": "https://photographermcp-dev.pic-time.com/mcp/sse",
                "metricool_mode": "draft_only",
                "meta_ads_mode": "paused_draft_only",
            },
            "deliverables": [
                {"dir": "01-highlight-film", "aspect": "16:9", "target_sec": [348, 392]},
                {"dir": "02-ceremony", "aspect": "16:9", "target_sec": "full"},
                {"dir": "03-speeches", "aspect": "16:9", "target_sec": "full"},
                {"dir": "04-trailer", "aspect": "16:9+9:16", "target_sec": [55, 68], "vendor_handles_on_social": True},
                {"dir": "05-vendor-reels", "aspect": "9:16", "target_sec": [25, 45], "vendor_handles_on_social": True},
                {"dir": "06-meta-ads", "aspect": "9:16", "target_sec": [15, 30], "status": "PAUSED"},
            ],
        },
    }

    if include_full_tables:
        bundle["style_profile"] = style_profile
        bundle["sequence_grammar"] = sequence_grammar
        bundle["shot_selection_rules"] = shot_selection_rules
        bundle["editing_spec_markdown"] = editing_spec_md
        bundle["coverage_checklist_markdown"] = coverage_checklist_md

    return bundle


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bundle Joshua Brown's 17-film empirical editing spec & local analyzer data for OpenFilm."
    )
    parser.add_argument(
        "--data-root",
        type=Path,
        default=Path.home() / ".film-style-analyzer",
        help="Path to film-style-analyzer data directory (default: ~/.film-style-analyzer)",
    )
    parser.add_argument("--genre", default="wedding", help="Genre workspace name (default: wedding)")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Embed full style-profile, sequence-grammar, shot-selection-rules, and markdown specs in output JSON",
    )
    parser.add_argument("--out", type=Path, help="Optional file path to write JSON output")
    args = parser.parse_args()

    bundle = load_bundle(args.data_root.expanduser(), args.genre, include_full_tables=args.full)
    payload = json.dumps(bundle, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload + "\n", encoding="utf-8")
        print(f"Wrote OpenFilm style bundle v2.0 → {args.out}")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
