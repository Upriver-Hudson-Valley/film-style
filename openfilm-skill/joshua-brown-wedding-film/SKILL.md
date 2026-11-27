---
name: joshua-brown-wedding-film
description: Edit and publish a complete documentary wedding suite in Joshua Brown's exact measured style (17-film empirical spec) using OpenFilm — loading his editing spec, sequence grammar, and shot-selection rules, color-matching Canon footage to edited Pic-Time stills in ACEScct, and outputting a full 6-minute wedding highlight film (with titles), standalone ceremony and speeches edits, a ~60s trailer, and tagged 9:16 vendor reels, then publishing to Cloudflare R2, Mux, website, Pic-Time, Metricool MCP, and Meta Ads Manager.
---

# Joshua Brown Documentary Wedding Film Workflow (OpenFilm)

## The Result

From one folder of raw wedding video + audio (plus the couple's Pic-Time gallery and vendor roster), produce a cohesive, documentary wedding suite faithful to Joshua Brown's real 17-film editing spec (`data/EDITING-SPEC.md`): tender, observational, invisible camera, warm mid-key natural color, 23.976 fps, ~30 cuts/min with a fast dance-floor finale that settles onto the couple alone.

Deliver five distinct OpenFilm projects (plus optional Meta Ad variants) sharing one linked raw media pool (never re-encode or duplicate camera originals):

1. `01-highlight-film/` (`1920x1080`, render `--fps 23.976 --4k --loudness=-14`) — ~6:00 highlight film (typical 5:48–6:32, ~185 shots), opening on nature/venue with `"Name and Name"` title in the first 10s, chronological day order, ending on the couple alone in fading light then black.
2. `02-ceremony/` (`1920x1080`, `--fps 23.976 --4k --loudness=-14`) — Complete standalone ceremony edit synced to master external audio, clean multi-angle/reaction cutting, minimal opening title.
3. `03-speeches/` (`1920x1080`, `--fps 23.976 --4k --loudness=-14`) — Complete standalone speeches/toasts edit with clean audio, couple/guest reaction cutaways, and editorial `lower-third.html` speaker cards.
4. `04-trailer/` (`1920x1080` + `1080x1920`, `--fps 23.976 --loudness=-14`) — ~60s teaser distilled from the wedding's strongest story-film voice hook, tender human beats, and closing couple hold (9:16 social cut includes on-screen vendor `@handles` via `vendor-tag.html`).
5. `05-vendor-reels/<vendor-slug>/` (`1080x1920`, `--fps 23.976 --loudness=-14`) — 25–45s vertical reels per vendor (venue, florist, planner, HMU, band/DJ, catering) showing their craft lived in by real people, with `vendor-tag.html` on-screen `@handle` overlays in Instagram's safe zone.
6. `06-meta-ads/<hook>/` (`1080x1920`, optional) — 3 hook-variant 15–30s ad cuts created as **PAUSED drafts** in Meta Ads Manager.

## What Defines It

**Tender center of gravity. Observational distance. Guests are the #1 subject. Pure motion video.**
- **ZERO still images in videos:** Never place `<img>` still photographs on the video timeline. Day-of wedding stills downloaded from Pic-Time (`https://photographermcp-dev.pic-time.com/mcp/sse`) are strictly color-grading reference files. (`still_hold` cuts in the spec are calm slow-mo/locked live video clips settling cleanly.)
- **Do NOT** open on a person (0/17 films do). Open quiet on nature/venue/detail, fading up from black, with **`"Name and Name"`** (the word `"and"`, never `&`) in **Recoleta** (white, centered) within the first 10 seconds.
- **Do NOT** cut tightly to the beat grid (`R = 0.05` — cut on action, gesture, glance, and phrasing, never mechanical beat-snapping).
- **Do NOT** use long dissolves (`≥1.0s`), mid-film fades, whip/glitch transitions, tight face close-ups (<1% of frames), or trendy LUTs. Dissolves MUST run **0.48–0.70s** (median **0.55s**, ~13 frames).
- **Show vendor `@handles` on ALL social cuts** (`04-trailer/` 9:16 + `05-vendor-reels/`).

Read `references/style-bible.md` and `data/EDITING-SPEC.md` before cutting. Read `references/distribution-mcps.md` before uploading or creating drafts.

## What Must Be True (Measurable Gates)

1. **Real Style Contract Loaded First**: Run `python3 scripts/load_style_bundle.py` to load `~/.film-style-analyzer/` (falling back to the bundled 17-film `data/` artifacts: `EDITING-SPEC.md`, `style-profile.json`, `sequence-grammar.json`, `shot-selection-rules.json`, `coverage-checklist.md`).
2. **Catalog, Cull & Coverage Gate**:
   - Catalog raw clips with the `shot_description` schema (`subjects`, `action`, `setting`, `lighting`, `camera`, `mood`, `description`) and score candidates per scene using `data/shot-selection-rules.json` (`0.30*subject + 0.25*setting + 0.20*mood + 0.15*lighting + 0.10*camera`).
   - Run `film-style score-clips <footage> --detect-trims` for composition culling (reject cut-off heads and severe overexposure; tolerate ~10% slight softness if emotion wins; **ignore DeepFace emotion labels**, use `shot_description.mood`).
   - Pass `data/coverage-checklist.md` (mandatory spine: `getting_ready`, `portraits`, `ceremony_processional`, `speeches`, `dancing`) and verify **zero** `never_observed_transitions` from `data/sequence-grammar.json`.
   - Transcribe vows/letters/toasts (`openfilm get asr` or WhisperX) so `.vtt` files sit beside every spoken source.
3. **Color Matched to Day-Of Pic-Time Stills + Orion LUTs**:
   - Pull 6–10 edited reference stills across lighting phases via Pic-Time MCP (`https://photographermcp-dev.pic-time.com/mcp/sse`) into `assets/color-refs/`.
   - Copy Joshua's local LUTs from `assets/luts/CLOGOrion.cube` (Canon Log / raw) and `assets/luts/Orion.cube` (Rec.709 finish) into `<project>/looks/` (these `.cube` files are kept local-only and gitignored; if missing, ask Joshua for their local path).
   - **ACEScct + Pic-Time Match + Orion finish (recommended):** Run `openfilm color input <log-clips> canon-clog3` (or `rec709` for SDR/drone), append `url(looks/Orion.cube)` **after** `url(looks/out-rec709.ctf)` so `openfilm color match` preserves it in the `after` slot, then run `openfilm color match <scene-clips...> --to assets/color-refs/<phase>.jpg`. For Canon Log clips graded natively with `CLOGOrion.cube`, apply `looks/CLOGOrion.cube` and verify against the Pic-Time still via `openfilm color look`.
   - Respect Joshua's empirical color law: **mid-key warm** (luma 90–104/255, warm/cool +0.19 to +0.25, sat 81–100), **one warmth across overcast/daylight/golden hour** (warm overcast to match, never leave blue), **night stays neutral** (+0.02 / -0.04), and **let the day darken naturally** from opening (~106 luma) to evening (~79 luma).
4. **Corrected Pacing, Audio & Render QA**:
   - Highlight film targets: **23.976 fps**, **~6:00** (typical 5:48–6:32), **28–33 cuts/min** (~185 shots), **median shot 1.65s** (~88% under 3s), ~7 holds ≥4s, 1–3 holds ≥6s (never on dance floor), final 20% tightening to **~1.46s median** before the last 5 shots slow to **~3.0s avg**, ~35 short dissolves (**0.55s**), ~21 live still-hold cuts, fades ONLY on first/last frame, **0 `<img>` still clips**.
   - Story film audio: first spoken words enter early at **7–23s** (median **16.6s**, right around the title); 84–173s total spoken audio lifted **over other pictures** (first look 55%, portraits 27%, toasts 48%, speeches 28%), while ceremony picture stays music-led.
   - Run `python3 scripts/validate_openfilm_cut.py 01-highlight-film/film.html` (verifies corrected §13 targets directly) AND `openfilm look --full --loudness=-14` (`-14 LUFS ±1`, true peak ≤ `-1 dBTP`, LRA 8–12 LU, zero flashes/black-frame bugs).
5. **Non-Destructive Studio Workflow**: Trim with `#t=in,out`, slow-mo with `speed`, short 0.55s dissolves via overlapping tracks with `overrides` `fade: [0.55, 0]`, titles/lower-thirds/vendor-tags as deterministic `window.film` DOM pages (`templates/`, **Recoleta** font). Never touch locked tracks or clobber Studio `overrides`.
6. **Draft-Only Social & Meta Ads Guardrail (HARD RULE)**:
   - Stage Pic-Time video exports for Desktop Uploader, upload masters + reels to Cloudflare R2 → ingest website masters into Mux.
   - **Metricool MCP:** ALWAYS create social posts as **DRAFTS** in Metricool Planner (never auto-publish live). Include public R2 MP4 URL + vendor `@handles`.
   - **Meta Ads MCP (`mcp.facebook.com/ads`):** ALWAYS create campaigns, ad sets, and ads in **PAUSED / DRAFT** status (never auto-activate or spend).

## Re-Editing an Existing OpenFilm Project

When Joshua opens an already-cut OpenFilm project and asks to re-edit it in his style:

1. **Preserve the previous cut & media**: Copy `film.html` to `film.v1-backup.html` (or increment `v2`, `v3`). Keep all existing linked footage, proxies, `.vtt` transcripts, and music files — do NOT re-ingest raw footage.
2. **Audit v1 first**: Run `python3 scripts/validate_openfilm_cut.py film.v1-backup.html` and report what the previous cut missed (cuts/min, median shot, dissolve lengths, `<img>` stills, `&` title errors, forbidden scene jumps, opening/closing violations).
3. **Rebuild `film.html` from a clean slate**: Do **NOT** incrementally patch the old timeline (patching leaves old pacing, shot selection, and transition habits baked in). Re-score the project's footage catalog against `data/shot-selection-rules.json`, pull Pic-Time color-reference stills, apply the Orion LUT + ACEScct `openfilm color match` pipeline, and construct a fresh `film.html` + `Recoleta` pages.
4. **Validate before rendering**: Loop on `python3 scripts/validate_openfilm_cut.py film.html` until errors = 0, then verify visuals and loudness with `openfilm look --full --loudness=-14`.

## What You Have

- **OpenFilm CLI & Core Skills**: Run `npx -y openfilm@latest`, read `openfilm skill film`, `openfilm skill color`, and `openfilm skill media`.
- **Bundled 17-Film Style Contract (`data/` + `scripts/load_style_bundle.py`)**: Real measured `EDITING-SPEC.md`, `style-profile.json`, `sequence-grammar.json`, `shot-selection-rules.json`, `coverage-checklist.md`. Local-only licensed LUTs (`assets/luts/CLOGOrion.cube`, `assets/luts/Orion.cube`) and optional font files (`assets/fonts/Recoleta-Regular.woff2`) are gitignored and loaded from disk.
- **Editorial HTML Pages (`templates/`)**: `title-card.html` (**Recoleta**, `"Name and Name"`), `lower-third.html`, and `vendor-tag.html` (9:16 Reels safe zone for all social cuts).
- **QA & Hosting (`scripts/`)**: `validate_openfilm_cut.py` (direct `film.html` §13 checker) and `publish_r2_mux.py` (R2 + Mux).
- **MCP Integrations (`references/distribution-mcps.md`)**: Pic-Time MCP (`https://photographermcp-dev.pic-time.com/mcp/sse`), Metricool MCP (drafts only), and Meta Ads MCP (`mcp.facebook.com/ads`, paused/draft only).

## Working With Joshua

1. **Before cutting**: Ask only for missing inputs — raw video/audio folder + camera log format (`CLOGOrion.cube` vs. `canon-clog3` + `Orion.cube`), Pic-Time gallery name, couple names (exact spelling for `"Name and Name"`), venue, date, vendor list (`name`, `role`, `@handle`), Story-film vs. Music-only preference (default: Story film if clear vows/speeches exist), and music track(s).
2. **During cutting**: Build all OpenFilm `film.html` timelines first so Joshua can scrub and tweak live in OpenFilm Studio before 4K rendering. Report exact QA numbers from `validate_openfilm_cut.py` (`cuts/min`, median shot, `<3s` %, dissolve count & length, first speech timestamp, IRE/Kelvin color-match summary, LUFS).
3. **After handoff**: Present the R2/Mux/Website manifest, Pic-Time Desktop Uploader folder, Metricool **draft** links, and Meta Ads **PAUSED draft** campaign IDs for Joshua's review. If Joshua adjusts a cut in Studio, offer `film-style learn-correction` on the before/after FCPXML.
