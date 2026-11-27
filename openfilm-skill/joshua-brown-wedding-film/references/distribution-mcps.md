# Distribution, Color-Reference & Autonomous Ad Integrations

This reference documents every external system wired into the OpenFilm wedding production pipeline, including real-world API/MCP realities and safety guardrails.

---

## 1. Pic-Time MCP (Color-Reference Stills + Gallery Delivery)

### Connection
- **Pic-Time Photographer MCP (SSE):** `https://photographermcp-dev.pic-time.com/mcp/sse`

### Role A — Pull Day-Of Reference Stills (Strictly for Color Correction — NEVER Cut Into Video)
1. Connect to `https://photographermcp-dev.pic-time.com/mcp/sse` and locate the wedding's gallery by couple name / date (e.g., `Emma and Alex :: Blooming Hill Farm`).
2. Select **6–10 edited stills** representing each distinct lighting environment of the day:
   - Getting ready (window light)
   - First look / Portraits (shade / overcast / meadow)
   - Ceremony (sun / overcast / indoor)
   - Golden hour
   - Reception / Speeches (tungsten / candlelit)
   - Dance floor / Night exterior
3. Download stills into `<project>/assets/color-refs/` named by phase (`01-getting-ready.jpg` … `06-dance-floor.jpg`). **Do NOT place any `<img>` clip on the video timeline.**
4. Copy `assets/luts/CLOGOrion.cube` (Canon Log/raw) and `assets/luts/Orion.cube` (Rec.709 finish) into `<project>/looks/`.
5. For ACEScct-matched clips, run `openfilm color input <log-clips> canon-clog3` (or `rec709` for SDR), append `url(looks/Orion.cube)` **after** `url(looks/out-rec709.ctf)`, then match each lighting phase:
   ```bash
   openfilm color match <scene-clip-ids...> --to assets/color-refs/<phase>.jpg
   ```
   Verify with `openfilm color look` (luma 90–104/255, warm/cool +0.19 to +0.25, overcast warmed to match daylight, night kept neutral).

### Role B — Uploading Finished Films to Pic-Time Video Delivery
> **Platform Constraint:** Pic-Time's Video Delivery supports up to 90-minute 4K films inside the couple's gallery, while direct video file uploads typically use the **Pic-Time Desktop Uploader app** unless exposed by a tool on `photographermcp-dev.pic-time.com`.

**Workflow:**
- Export Pic-Time-ready 23.976 fps masters into `<wedding>/deliverables/pic-time/`:
  - `01-<couple>-highlight-4k.mp4` (Featured Video)
  - `02-<couple>-ceremony-4k.mp4` (Scene / Featured Video)
  - `03-<couple>-speeches-4k.mp4` (Scene / Featured Video)
  - `04-<couple>-trailer-4k.mp4` (Gallery Header / Clip)
- Check available write tools on `https://photographermcp-dev.pic-time.com/mcp/sse`; if video upload is supported via MCP, push directly, otherwise stage `pic-time-delivery.json` + the folder for one-drag upload into Pic-Time Desktop Uploader and organize gallery metadata via Pic-Time MCP.

---

## 2. Cloudflare R2 (Zero-Egress Master Storage & Public Media URLs)

**Why R2 sits first in publishing:**
- Zero egress fees for high-bitrate 4K archival masters and client downloads.
- Generates stable public HTTPS MP4 URLs (e.g., `https://media.joshuabrownphotography.com/...`) that **Mux** can ingest directly by URL AND **Metricool MCP** requires to attach videos to draft Instagram/TikTok Reels.

**Bucket key convention:**
```text
weddings/<YYYY>/<couple-slug>/
  highlight-4k.mp4
  ceremony-4k.mp4
  speeches-4k.mp4
  trailer-16x9.mp4
  trailer-9x16.mp4
  poster.jpg
  reels/<vendor-slug>-9x16.mp4
  ads/<hook-variant>-9x16.mp4
```

Run `python3 scripts/publish_r2_mux.py --wedding <slug> --year <YYYY> --dir deliverables/` with `R2_ACCOUNT_ID`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`, and `R2_PUBLIC_BASE_URL`.

---

## 3. Mux Video (Adaptive HLS Streaming for Your Website)

`scripts/publish_r2_mux.py` creates Mux assets directly from the uploaded R2 public URLs (no double upload from local disk!) via `POST https://api.mux.com/video/v1/assets`:

- Requests `"playback_policy": ["public"]` (or `"signed"` for private client pages) and `"video_quality": "plus"`.
- Polls until `status == "ready"` and returns:
  - `asset_id`
  - `playback_id`
  - HLS stream: `https://stream.mux.com/<playback_id>.m3u8`
  - Poster frame: `https://image.mux.com/<playback_id>/thumbnail.jpg?width=1920&fit_mode=smartcrop`
  - Hover preview WebP: `https://image.mux.com/<playback_id>/animated.webp?start=10&end=15&width=640`

---

## 4. Own Website (`joshuabrownphotography.com`)

Emit `<wedding>/deliverables/website-entry.json` (and optional Markdown/MDX frontmatter) containing:
- Couple names (`"Name and Name"`), venue slug, Hudson Valley / Catskills region, season, wedding date
- Mux `playback_id`s (highlight, trailer, ceremony preview) + R2 poster URL
- Full vendor credit list linked to `/vendors/<slug>` directory pages (SEO + vendor backlink flywheel)
- Documentary story summary in Joshua's grounded, zero-fluff voice

If the website repo is connected locally or via GitHub, open a PR/commit adding the wedding film entry and updating the `/videography` showcase index.

---

## 5. Social Media Publishing via Metricool MCP (**DRAFTS ONLY**)

Metricool provides an official MCP server that reads analytics, finds best posting times, and creates posts & Reels across Instagram, Facebook, TikTok, and YouTube Shorts.

### Mandatory Draft Rule & Media Requirements
- **HARD RULE:** ALWAYS create Metricool posts with **`draft: true`** (never auto-publish or finalize live schedules). Joshua reviews and approves every draft in Metricool Planner.
- **Public MP4 URL:** Supply the **Cloudflare R2 public MP4 URL** produced in Step 2.
- **Vendor handles visible in video + caption:** Every 9:16 social cut (`trailer-9x16.mp4` and every `reels/<vendor-slug>-9x16.mp4`) already displays the vendor's `@handle` on screen via `vendor-tag.html`; mirror the exact `@handles` in the draft caption + note Instagram Collaborator invite targets for Joshua's review.

### Draft Cadence Per Wedding
1. **Draft 1 (Suggested Best Time — Day +1):** 1-Minute Vertical Trailer (`trailer-9x16.mp4`) drafted for Instagram Reels + TikTok + Facebook Reels + YouTube Shorts.
2. **Drafts 2..N (Spaced every 2–3 days at Metricool best time):** Individual Vendor Reels (`reels/<vendor-slug>-9x16.mp4`) with vendor `@handle` mentions and grounded 2–4 sentence documentary captions (5–8 hyper-local Hudson Valley/Catskills tags max; zero hype filler).

---

## 6. Ad Creation via Meta Ads Manager (**PAUSED DRAFTS ONLY**)

### Connection
Use **Meta's official Ads MCP server** (`mcp.facebook.com/ads`, Meta Business OAuth with `ads_read` and `ads_management`).

### Creative Factory in OpenFilm (3-Hook Testing)
From the wedding's best moments, render **3 vertical 9:16 ad variants (15–30s each, 23.976 fps)** in `06-meta-ads/` sharing the same Orion-graded body clips and swapping only the **first 3 seconds (Hook)** + quiet **Recoleta** opening caption:
- **Hook A (Emotional Moment):** Real guest tear/laughter + vow line (*"Your people, not staged poses."*)
- **Hook B (Venue/Region Authority):** Iconic Hudson Valley/Catskills venue frame (*"500+ Hudson Valley & Catskills weddings since 1999."*)
- **Hook C (Documentary Proof):** Prep → kiss → dance floor → couple dusk hold (*"Documentary photo & film. Warm Kodak color. Built to last 20 years."*)

### Campaign Structure & Hard Draft Guardrail
1. **HARD RULE:** ALWAYS create every Campaign, Ad Set, and Ad with **`status: "PAUSED"`** (draft/paused in Ads Manager). **NEVER** set `status: "ACTIVE"` or spend budget autonomously.
2. **Objective:** `OUTCOME_LEADS` (Lead Form or `joshuabrownphotography.com/prices`) or `OUTCOME_ENGAGEMENT` (ThruPlay Video Views for retargeting audiences).
3. **Geo-Targeting:** Engaged couples (24–42) within **NYC Metro + Hudson Valley + Catskills + Westchester + Brooklyn + Northern NJ**.
4. **Compliance:** Batch API calls (avoid Meta `613` rate limits); real documentary footage with Recoleta HTML titles requires no synthetic-media label unless generative AI visuals/voices are added.
5. **Weekly Reporting & Draft Proposals:** Query `ads_read` via Meta Ads MCP + Metricool analytics to report 3-second Hook Rate, ThruPlay cost, CTR, and Cost Per Inquiry — and prepare **new PAUSED draft ads** from the latest wedding's winning organic Reels for Joshua to toggle on in Ads Manager.
