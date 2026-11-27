# Joshua Brown — Personal Wedding Film Style Bible (Empirical 17-Film Spec)

> **Source of truth:** Synthesized directly from Joshua Brown's real 17-film measured corpus (`data/EDITING-SPEC.md`, `data/style-profile.json`, `data/sequence-grammar.json`, `data/shot-selection-rules.json`, `data/coverage-checklist.md`) plus his documentary brand craft (`joshuabrownphotography.com`).
> **Precedence rule:** Whenever older analyzer outputs (`style-guide.md`, `editor-voice.md`) conflict with `data/EDITING-SPEC.md` (due to missed cuts in dark dance-floor footage in the first pass), **`data/EDITING-SPEC.md` ALWAYS wins.**

---

## 1. The Style in 12 Empirical Rules

1. **Shape:** **~6:00** runtime (median **359s**, typical **5:48–6:32**), **~185 shots** (corrected), **~30 cuts/min** (typical 28–33), **23.976 fps** MUST.
2. **Short by default:** Median shot **1.65s** (mean 1.9s); **~88% of shots run under 3s**. Real holds are deliberate and rare: **~7 shots ≥4s** and **1–3 shots ≥6s** per film.
3. **Steady pulse → fast finale → held landing:** Median cut stays **1.6–1.9s** through 80% of the film, tightens to **1.46s** in the final 20% (50% of shots <1.5s on the dance floor), then the final 5 shots lengthen to **~3.0s avg** to land the ending.
4. **Open quiet, never on a person:** Fade up from black (12/17) onto nature, venue, or still detail (**0 of 17 films open on a person**). First shot median **2.9s** (typical 2.3–3.1s, never >4.3s). Put **`"Name and Name"`** (the word `"and"`, never `&`) in white centered type within the first 10 seconds.
5. **Chronological day order (forward only):** `getting_ready` → `establishing` → `first_look` → `portraits` → `ceremony_processional` → `ceremony` → `details` → `ceremony_vows` → `cocktail_hour` → `ceremony_recessional` → `reception_entrance` → `speeches` / `first_dance` / `toasts` → `dancing` → `cake_cutting` → `send_off` / held closing portrait. Zero `never_observed_transitions`.
6. **End on the couple alone, then black:** In 15/17 films the final real image is the couple walking, embracing, or kissing (10/15 at golden hour, dusk, night, or firelight), followed by a **hard cut to black** (12/17; fade out only 4/17). Never end on dance-floor energy.
7. **Transition grammar:** Per film ~90–130 hard cuts (**60%**), **~35 short dissolves** (**25%**, **0.48–0.70s**, median **0.55s** ≈ 13 frames — **MUST NOT use ≥1.0s dissolves**), and **~21 still-hold cuts** (**15%** — live slow-mo/locked video settling cleanly, **NOT still photographs**). Fades ONLY on first frame and last frame (0 mid-film).
8. **Invisible camera (93%):** `slight_handheld` (**59.0%**) for people, `locked` (**33.9%**) for altar wides, establishing, and details. Drone = openers/establishing ONLY (0.5%). Loose handheld = dance floor ONLY (29% of dancing clips). Pans/tilts avoided (<0.5%).
9. **Tender center & community focus:** **Tender (22.1%)** is #1 mood (kinetic only 3.7%). **Guests (28.5%)** are the #1 pictured subject — more than couple (21.1%), bride (19.9%), groom (13.4%), wedding party (12.6%), parents (11.7%). Reactions are the second protagonist.
10. **Observational distance:** `medium-full` (**33%**) + `full` (**30%**) + `no person` (**25%**) + `medium` (**11%**). Tight close-ups are **<1%** (medium-close 2%). Headroom **13–37%** (avg 24%). Reject cut-off heads and severe overexposure; tolerate ~10% slight softness when emotion wins. **Ignore DeepFace emotion labels** (use `shot_description.mood`).
11. **Audio & un-snapped rhythm:** Two modes — **Story film** (9/17: 84–173s spoken audio, median 120s; **first voice enters early at 7–23s**, median **16.6s**, right around the title; vows/letters lifted **over first look 55%, toasts 48%, speeches 28%, portraits 27%, first dance 26%**, while ceremony picture stays music-led) vs. **Music only** (8/17). Mid-tempo ~99–123 BPM (median 112). **MUST NOT snap cuts to the beat grid** (`R = 0.05`) — cut on action, gesture, glance, and phrasing.
12. **Mid-key warm natural color:** Mean luma **90–104/255** (median 96.5 — slightly under middle grey, NOT bright & airy), contrast σ **52–60**, warm/cool **+0.19 to +0.25** (median +0.23), saturation **81–100/255**. **One warmth across all daylight** (overcast warmed to +0.22, never left blue); **night stays neutral** (+0.02); **let the day darken naturally** (106 luma morning → 79 luma evening).

---

## 2. Scene Recipes & Multi-Chapter Clustering

Major scenes cluster into **2–4 consecutive chapters** (`dancing → dancing` 65%, `getting_ready → getting_ready` 62%, `first_look → first_look` 59%, `ceremony → ceremony` 52%).

| Order | Scene | Status | Share | Median Shot (p10–p90) | Dissolve % | Dominant Subjects & Craft Note |
|---|---|---|---|---|---|---|
| 1 | `getting_ready` | **MUST** | 11.3% | 1.96s (0.75–3.25) | 20% | Bride + groom parity, dress/ring details, parents. Observational. |
| 2 | `establishing` | SHOULD | 5.8% | 1.88s (0.75–3.21) | 25% | Locked/drone venue, foliage, sky. Quiet breath between indoor blocks. |
| 3 | `first_look` | SHOULD | 2.7% | 1.75s (0.75–3.35) | 27% | Approach → reveal → 2.5–3s reaction breath. Includes parent reveals. Never after 40%. |
| 4 | `portraits` | **MUST** | 15.0% | 1.84s (0.79–3.82) | 17% | **Anchor block** (11–19%). Wide-in-landscape + walking + tighter frames. Still holds live here. |
| 5 | `ceremony_processional` | **MUST** | 3.7% | 1.42s (0.75–2.59) | 32% | Bride with escort, groom reaction, wedding party. Short & punchy. |
| 6 | `ceremony` | SHOULD | 7.0% | 1.42s (0.58–2.59) | 23% | **Tightest scene.** 53% guests & family reactions. |
| 7 | `details` | SHOULD | 4.8% | 1.75s (0.71–2.79) | 17% | Sits mid-film (~39%, reception decor). Locked or rack focus. |
| 8 | `ceremony_vows` | SHOULD | 5.2% | 1.73s (0.76–3.38) | 20% | Couple + officiant in context (never solo officiant), hands, rings, kiss. |
| 9 | `cocktail_hour` | SHOULD | 9.2% | 1.58s (0.78–2.63) | 19% | Fast guest candids, hands, drinks, laughter. |
| 10 | `ceremony_recessional` | MAY | 2.9% | 1.96s (0.71–4.17) | 30% | Energy release walking back down aisle + cheers. |
| 11 | `reception_entrance` | MAY | 3.7% | 1.92s (0.60–2.71) | 26% | **The room reacting** to the couple entering. |
| 12 | `speeches` | **MUST** | 5.2% | 1.63s (0.51–3.00) | 29% | Speaker, couple reaction, guest laughter. Speech audio carries it. |
| 13 | `first_dance` | SHOULD | 4.1% | 1.71s (0.67–3.95) | 43% | 2–3 angles with 0.55s dissolves + parents watching. |
| 14 | `toasts` | MAY | 8.7% | 1.48s (0.58–2.46) | 29% | Raised glasses & clinks only when glasses actually go up. |
| 15 | `dancing` | **MUST** | 10.8% | 1.63s (0.50–2.79) | 35% | **Fast montage** (flash cuts to 0.5s allowed, handheld allowed). **Zero long holds.** |
| 16 | `cake_cutting` | MAY | 3.7% | 0.96s (0.42–2.40) | 60% | Sub-1s multi-angle burst joined by 0.55s dissolves + reactions. |
| 17 | `send_off` | MAY | 2.3% | 1.63s (0.50–5.16) | 40% | Only if planned exit existed. Action → held final couple frame. |

**Per-clip candidate scoring (`data/shot-selection-rules.json`):**
```text
score = 0.30*subject_match + 0.25*setting_match + 0.20*mood_match + 0.15*lighting_match + 0.10*camera_match
```

---

## 3. OpenFilm Color Pipeline (Canon Log + Orion LUTs + Pic-Time Still References)

Joshua shoots **Sony for stills** (edited in warm Kodak film tones and delivered to Pic-Time in 24–48h) and **Canon for 4K video** (raw/Canon Log + Rec.709 B-cam/drone). **Still images are NEVER inserted into videos** — they are pulled from Pic-Time MCP (`https://photographermcp-dev.pic-time.com/mcp/sse`) strictly as color-correction reference frames.

### Bundled LUTs (`assets/luts/` → copied into `<project>/looks/`)
- **`CLOGOrion.cube`** (33×33×33 3D LUT) — Joshua's look LUT for **raw / Canon C-Log** footage (log-to-display contrast with subtle creamy Kodak shadow toe).
- **`Orion.cube`** (33×33×33 3D LUT) — Joshua's look LUT for **Rec.709** footage (subtle lifted film shadow toe + warm Kodak midtones).

### OpenFilm `--of-lut` Chains (Verified Against OpenFilm `src/color/chain.mjs`)

1. **Canon Log / Raw clips — ACEScct + Pic-Time Match + `Orion.cube` finish (Recommended for per-scene matching):**
   ```html
   style="--of-lut: url(looks/in-canon-clog3.ctf) url(looks/scene-ceremony.ctf) url(looks/shot-v042.ctf) url(looks/out-rec709.ctf) url(looks/Orion.cube)"
   ```
   - `openfilm color input <log-clips> canon-clog3` sets `in-canon-clog3.ctf` + `out-rec709.ctf`.
   - Append `url(looks/Orion.cube)` **after** `out-rec709.ctf` (OpenFilm's `chain.mjs` keeps post-output `.cube` looks in the `after` slot).
   - Run `openfilm color match <scene-clips...> --to assets/color-refs/<phase>.jpg` — OpenFilm inserts `shot-<id>.ctf` (`ASC_CDL`) cleanly in ACEScct before `out-rec709.ctf`, matching exposure/temperature/tint to your edited Sony still while preserving `Orion.cube` last.
2. **Canon Log / Raw clips — Direct `CLOGOrion.cube` base:**
   - When Canon C-Log / Canon RAW clips should use `CLOGOrion.cube` directly as the log-to-Orion transform (instead of `in-canon-clog3.ctf` + `Orion.cube`), apply `style="--of-lut: url(looks/CLOGOrion.cube)"` and verify scopes/skin tones against the Pic-Time still via `openfilm color look` (note: do **not** run `openfilm color match` directly on a bare `CLOGOrion.cube` chain without a log input wrapper, because `chain.mjs` would prepend `in-rec709.ctf` ahead of `CLOGOrion.cube`).
3. **Rec.709 clips (drone, B-cam, ordinary SDR) — Pic-Time Match + `Orion.cube`:**
   ```html
   style="--of-lut: url(looks/in-rec709.ctf) url(looks/shot-d01.ctf) url(looks/out-rec709.ctf) url(looks/Orion.cube)"
   ```
4. **Verify with `openfilm color look` against §10 empirical targets:**
   - Daylight / Overcast / Golden Hour / Warm Indoor unified at **warm/cool +0.19 to +0.25**, **luma 90–104/255**, **sat 81–100/255**.
   - Overcast warmed to match sunny daylight (never left blue).
   - Night exteriors (+0.02) and cool uplighting (-0.04) kept near neutral.
   - Evening luminance naturally steps down (~106 morning → ~79 evening).

---

## 4. Typography & Adapting the Style to All 5 Deliverables (+ Meta Ads)

- **Title font:** **`Recoleta`** (white `#FFFFFF`, centered over opening nature/venue shots inside the first 10s, always `"Name and Name"` using the word `"and"`, never `&`). Copy licensed `Recoleta-Regular.woff2` / `.otf` into `assets/fonts/` (templates also resolve locally installed macOS `Recoleta` and fall back gracefully to `Fraunces`).
- **Social media cuts rule:** Vendor `@handles` MUST display on-screen via `vendor-tag.html` (in Instagram's safe zone: `bottom ≥ 310px`, `left: 56px`, clear of right-side UI icons) on **all** social media cuts (9:16 trailer + vendor reels).

### 1. Full Highlight Film (`01-highlight-film/`, 16:9, 23.976 fps, ~6:00)
Follow `data/EDITING-SPEC.md` strictly (100% measured contract; pure motion video, zero still images).

### 2. Full Ceremony Edit (`02-ceremony/`, 16:9, 23.976 fps, full length)
- Sync all camera angles to master external audio (lavs + recorder/board).
- Observational multi-angle cutting: stay clean on vows/officiant-with-couple, cut to partner/parent/guest reactions on natural breath pauses (6–15s holds appropriate here since it's a documentary record, not a highlight).
- Opening `title-card.html` (**Recoleta**): `"Name and Name"` + venue/date over quiet establishing shot before processional.

### 3. Full Speeches Edit (`03-speeches/`, 16:9, 23.976 fps, full length)
- Chronological toasts synced to clean board/mic audio.
- Cut to couple and guest table reactions (tight on faces/glasses, never static table wides) on punchlines and tender beats.
- Editorial `lower-third.html` (**Recoleta** speaker name + tracked uppercase role) entering 2s into each speech for 4.5s.

### 4. 1-Minute Trailer (`04-trailer/`, 16:9 + 9:16 vertical social cut, 23.976 fps, 55–68s)
- Distills Joshua's story-film arc into ~30–35 shots (~1.7s median):
  - **0–6s:** Fade from black onto venue/nature → `"Name and Name"` (**Recoleta**) → first voice hook (strongest single vow/toast sentence) landing by ~5–8s.
  - **6–28s:** Rapid tender glimpses of prep, first look reveal, and portraits (1.5–2.2s cuts, observational distance).
  - **28–48s:** Processional glance, guest tears, vow payoff, kiss, recessional cheer.
  - **48–60s:** Brief 8–10s dance-floor burst (1.0–1.4s cuts) → settle onto 1 held golden-hour/dusk couple embrace (3.5–4.5s) → hard cut to black.
- **9:16 social cut:** Overlay `vendor-tag.html` showing featured vendor `@handles` during relevant shots + closing credit card.

### 5. Vendor Reels (`05-vendor-reels/<vendor-slug>/`, 9:16 1080×1920, 23.976 fps, 25–45s)
- Bespoke edit per vendor (Venue, Florist, Planner, HMU, Band/DJ, Catering/Cake, Rentals/Lighting) obeying Joshua's voice: **tender, observational, natural warm Orion color, 0.55s dissolves where appropriate, zero flashy TikTok effects.**
- Show the vendor's craft *creating real human moments* (guests reacting to the space, hands holding the bouquet, candlelit dinner laughter — never sterile catalog pans).
- Overlay `vendor-tag.html` (`ROLE`, `Vendor Name`, `@handle`) in Instagram's safe zone during featured shots + closing credit card with vendor `@handle` + `@joshuabrownphotography`.

### 6. Meta Ad Variants (`06-meta-ads/`, 9:16 1080×1920, 23.976 fps, 15–30s — Created as PAUSED Drafts)
- 3 hook variants sharing the same graded body, swapping only the opening 3s visual + quiet **Recoleta** editorial hook line:
  - **Hook A (Emotion):** Real guest tear/laugh + vow line (*"Your people, not staged poses."*)
  - **Hook B (Region/Venue):** Iconic Hudson Valley/Catskills venue frame (*"500+ Hudson Valley & Catskills weddings since 1999."*)
  - **Hook C (Complete Documentary):** Prep → kiss → dance floor → couple dusk hold (*"Documentary photo & film. Warm Kodak color. Built to last 20 years."*)
