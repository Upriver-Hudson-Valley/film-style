# Wedding Film Editing Spec: Joshua Brown Photography

> **Audience:** Claude and any other editing agent.
> **Purpose:** the single source of truth for how Joshua's wedding films are cut and finished. Read it end to end before you touch footage.
> **Built from:** 17 finished films measured by `film-style` (2,478 detected clips, 627 chapters, 100.6 minutes), plus color, audio, music and loudness passes and a second cut-detection pass added on 2026-11-09.
>
> **Measurement note on pacing.** The tool's cut detector misses cuts in dark and colored-light reception footage: 89 of the 117 "clips" of 6s or more turned out to be fast montages (one 58s "clip" holds 45 shots). A second detector found about 690 real missed cuts (spot-checked by eye: about 83% of its additions are real; the rest are uplight color changes). Pacing numbers in this spec use the corrected count unless labeled "tool count". `analyses/*.json` still hold the original under-counted cut lists.
> **Precedence:** this file wins over every other doc in this workspace. Section 14 lists older claims it corrects.

---

## 0. TLDR: the style in 12 rules

1. **Shape.** About 6 minutes (typical 5:48 to 6:32), about 185 shots, about 30 cuts per minute.
2. **Short by default.** Median shot about 1.65s; close to 90% of shots run under 3s. Real holds are rare: about 7 shots of 4s or more and only 1 to 3 of 6s or more per film.
3. **The finale speeds up, then settles.** The median cut stays near 1.7s through the film, tightens to about 1.5s in the last 20% (dance-floor montage), then the final few shots slow down to land the ending.
4. **Open quiet.** Fade up from black onto nature or the venue (drone, flowers, the building). Put the title "Name and Name" over it in the first 10 seconds. Never open on a person.
5. **Follow the day in order.** Prep, first look, portraits, processional, ceremony, vows, cocktail hour, reception, first dance and speeches, dancing, cake, exit. Do not jump backward in time once the film is moving.
6. **End on the couple alone,** held, at golden hour, dusk or night. Then cut to black.
7. **Transitions:** per film about 90 hard cuts, 35 short dissolves (0.55s) and 21 still-hold cuts. Fades only at the very first and very last frame.
8. **Invisible camera.** 93% of clips are slight handheld or locked off. Drone is for openers. Loose handheld energy belongs only on the dance floor.
9. **Tender is the center.** Tender is the most common mood. Guests appear in more clips than anyone; reactions are the second protagonist.
10. **Observational distance.** Medium-full and full framings dominate. Tight close-ups are rare.
11. **Music carries the film.** Either music only (8 of 17) or a story film with about 2 minutes of vows, letters and speeches laid over other pictures (9 of 17). Cut on action and phrasing, not on the beat grid.
12. **Natural, warm, mid-key color.** One warmth across every daylight condition, night left as night, and the film darkens as the day does.

---

## 1. How to use this spec

**Rule strength**
- **MUST**: seen in at least 15 of 17 films, or breaking it would break the film. Do not deviate without asking Joshua.
- **SHOULD**: the clear majority pattern. Deviate only when the footage or the day forces it, and say why in your notes.
- **AVOID**: rare or absent in the archive. Using it reads as someone else's style.
- **MAY**: an option the archive shows sometimes.

**Reading the numbers**
- "Typical" means the middle half of films (p25 to p75). "Acceptable" means p10 to p90. Landing outside the acceptable band needs a stated reason.
- Medians beat means. Clip-length distributions are long-tailed (a few 15 to 58s holds pull averages up), so target medians and count the long holds separately.

**The day wins over the template.** Pacing follows the wedding. A simple day yields a tighter, shorter film; a complex multi-tradition day earns more runtime and more breath (Isabelle and Michael: 459s, 75 chapters). Carrie and Rose slows down as it goes instead of speeding up. Match the emotional arc of the day you have.

**Agent workflow (do it in this order)**
1. Catalog raw clips with the `shot_description` schema (section 8.1).
2. Cull with the composition and technical rules (section 8.6). Score with `film-style score-clips` if `shot-profile.json` applies.
3. Check coverage against the required-scene list (section 3) and `edit-craft/coverage-checklist.md`.
4. Build the spine in day order (section 3), then the opening (section 4) and closing (section 5).
5. Cut each scene to its recipe (section 11 and `edit-craft/scenes/<label>.md`).
6. Set transitions (section 7), then the audio bed and speech lifts (section 9).
7. Finish color and loudness (section 10).
8. Run the QA checklist (section 13), then `film-style compare <your.fcpxml>`.

---

## 2. Deliverable shape

| Metric | Target | Typical (p25 to p75) | Acceptable (p10 to p90) | Observed range |
|---|---|---|---|---|
| Runtime | 6:00 (359s) | 5:48 to 6:32 (348 to 392s) | 4:28 to 6:51 (268 to 411s) | 3:40 to 7:39 |
| Shot count (corrected) | about 185 | 175 to 200 | 140 to 215 | 95 to 240 |
| Cuts per minute (corrected) | about 30 | 28 to 33 | 26 to 35 | 25 to 40 |
| Median shot (per film, corrected) | 1.7s | 1.6 to 1.8s | 1.4 to 1.9s | 1.3 to 2.0s |
| Mean shot (per film, corrected) | 1.9s | 1.8 to 2.0s | 1.7 to 2.2s | 1.5 to 2.4s |
| Tool count, for reference | 149 clips, 24 cuts/min | | | |
| Chapters (dissolve-bounded segments) | 36 | 25 to 43 | 20 to 53 | 13 to 75 |

Corrected ranges are interpolated between the tool count (too low) and the re-detection count (about 17% too high in its additions).

- **Frame rate:** MUST be 23.976 fps (15 of 17 films; the other 2 are 24.0).
- **Aspect:** 9 films are 16:9 (1280x720 masters on Vimeo); 7 are about 1.9:1 widescreen (1364 or 1366 x 720) and 1 is 2:1. See open decision 1 in section 15.
- **Shot count scales with runtime:** hold cuts per minute in the 28 to 33 band rather than chasing a fixed shot count.

---

## 3. Structure and scene order

Scenes appear in day order. "Position" is where the scene first appears, as a fraction of runtime (median across films).

| Order | Scene label | Films | Status | First appears | Runtime share when present | Chapters when present |
|---|---|---|---|---|---|---|
| 1 | getting_ready | 15/17 | MUST | 0% | 11.3% | 3 |
| 2 | establishing | 12/17 | SHOULD | 10% | 5.8% | 2 |
| 3 | first_look | 13/17 | SHOULD if it happened | 16% | 2.7% | 1 |
| 4 | portraits | 17/17 | MUST | 18% | 15.0% | 4 |
| 5 | other (pre-wedding, side rituals) | 8/17 | MAY | 28% | 8.1% | 6 |
| 6 | ceremony_processional | 17/17 | MUST | 32% | 3.7% | 2 |
| 7 | ceremony (guest and family reactions) | 13/17 | SHOULD | 36% | 7.0% | 3 |
| 8 | details | 13/17 | SHOULD | 39% | 4.8% | 2 |
| 9 | ceremony_vows | 13/17 | SHOULD | 43% | 5.2% | 2 |
| 10 | cocktail_hour | 13/17 | SHOULD | 47% | 9.2% | 2 |
| 11 | ceremony_recessional | 9/17 | MAY | 48% | 2.9% | 1 |
| 12 | reception_entrance | 8/17 | MAY | 56% | 3.7% | 1 |
| 13 | speeches | 16/17 | MUST | 64% | 5.2% | 2 |
| 14 | first_dance | 13/17 | SHOULD if it happened | 64% | 4.1% | 3 |
| 15 | toasts | 4/17 | MAY | 65% | 8.7% | 1 |
| 16 | dancing | 15/17 | MUST | 75% | 10.8% | 2 |
| 17 | cake_cutting | 8/17 | MAY | 77% | 3.7% | 1.5 |
| 18 | send_off / exit | 5/17 | MAY (only if there was a planned exit) | 97% | 2.3% | 3 |
| 19 | transition (formal slug bridge) | 6/17 | MAY | 97% | 1.0% | 1 |

**Rules**
- MUST build the spine in chronological day order. Once the film commits forward, it stays forward. The only allowed backward jump is interleaving prep with title shots in the first minute.
- SHOULD build each major scene from 2 to 4 consecutive chapters (scenes loop into themselves: dancing to dancing 65%, getting ready to getting ready 62%, first look to first look 59%).
- **Portraits are the anchor:** the largest block (about 15%) and present in every film. They land early, right after the first look, and return as late held images.
- **Details sit mid-film, not up front:** median first appearance is 39%, because reception decor is the usual detail block. Dress, ring and shoe details live inside getting_ready.
- Strong forward links: recessional to cocktail hour (55%), first dance to dancing, getting ready to first look, first look to portraits.
- AVOID any transition listed in `edit-craft/sequence-grammar.json` under `never_observed_transitions` (for example send_off to getting_ready, dancing to ceremony_processional). If your order produces one, fix the chronology or bridge it with an establishing shot.
- No single scene type should exceed 20% of runtime.

---

## 4. Opening (first 15 seconds)

- MUST open on nature, the venue, or a still detail. **Zero of 17 films open on a person.** First images: black frame fading up (4 films), drone over foliage or venue (4), flowers, grasses or meadow in soft focus (4), venue exterior (2), river (1), branches against sky (1), table detail (1).
- SHOULD fade up from black (12 of 17 films).
- SHOULD place a title within the first ~3% of runtime (11 of 17 films): the couple's first names written as **"Name and Name"** (the word "and", not an ampersand), white type, centered, over an establishing or nature shot (two styles seen: serif, and a thin sans; see section 10.3). The title often spans 2 or 3 shots of 1 to 3s each. Venue name MAY appear as a second line.
- First shot: median 2.9s (typical 2.3 to 3.1s, never over 4.3s). The opening is a sequence of nature and venue shots of 2 to 3.5s each, not one long held shot (the "17.9s opener" in older docs is really 7 shots).
- First 5 shots average 2.4s (typical 1.8 to 2.5s): a touch slower than the body of the film.
- First scene: getting_ready (47%) or establishing (29%). Nothing else is common.
- Camera on opening shots: locked, drone, or slight handheld on a still subject (flowers, a table).

---

## 5. Closing (last 20 seconds)

- MUST end on the couple alone. In 15 of 17 films the last real image is the couple walking, embracing or kissing; the other two end on a skyline after the couple walks away, and on cake feeding.
- SHOULD make that last image golden hour, dusk, night or firelight (10 of those 15). The rest end in daylight or soft indoor light.
- SHOULD then end on black: 12 films cut to a black frame or end card (one shows a "JOSHUA BROWN" credit on black), 3 fade the final couple image down to dark, and 2 end on an already dark night or dusk silhouette.
- SHOULD lengthen the last few shots: the last 5 average 3.0s (typical 2.2 to 3.7s) against 1.9s for the film, and 9 of the archive's 33 real 6s-plus holds sit in the final 10%.
- Last scene: portraits (29%), transition slug (24%), send-off (18%). AVOID ending on dancing energy (1 of 17).
- Fade to black on the final cut: 4 of 17. A hard cut to a black frame is the default.
- Mood of the final quintile returns to tender (26% of clips) after the celebratory middle.

---

## 6. Pacing

All numbers in this section use the corrected cut count (3,303 shots across 17 films; see the measurement note at the top).

### 6.1 Shot-length distribution

| Length | Share |
|---|---|
| under 1s | 22.7% |
| 1 to 1.5s | 20.1% |
| 1.5 to 2s | 21.6% |
| 2 to 3s | 23.7% |
| 3 to 4s | 7.6% |
| 4 to 6s | 3.3% |
| 6 to 8s | 0.7% |
| 8s and up | 0.3% |

p10 0.63s · p25 1.04s · **median 1.63s** · p75 2.29s · p90 3.17s · longest real shot about 15s.

- Close to 90% of shots per film run under 3s (typical 83% to 91%).
- Shots of 4s or more: about 7 per film (typical 5 to 11). Shots of 6s or more: about 2 per film (typical 1 to 3).

### 6.2 Position in the film

| Position | Median shot | Shots 5s or longer | Shots under 1.5s |
|---|---|---|---|
| 0 to 10% | 1.88s | 0.7% | 35% |
| 10 to 20% | 1.67s | 2.2% | 40% |
| 20 to 30% | 1.71s | 1.3% | 42% |
| 30 to 40% | 1.63s | 2.1% | 42% |
| 40 to 50% | 1.58s | 1.5% | 44% |
| 50 to 60% | 1.71s | 1.8% | 43% |
| 60 to 70% | 1.71s | 2.2% | 39% |
| 70 to 80% | 1.71s | 2.8% | 38% |
| 80 to 90% | 1.46s | 0.5% | 50% |
| 90 to 100% | 1.46s | 4.8% | 51% |

**Read this as a steady pulse with a fast finale.**
- SHOULD keep the median cut near 1.6 to 1.9s from the opening through 80%.
- The opening 10% is the slowest stretch (1.88s): the patient title sequence.
- The last 20% is the fastest (1.46s, half of all shots under 1.5s): the dance-floor montage.
- The final few shots break that pattern and land long (section 5). The archive's longest real holds cluster in the final 10%.

### 6.3 Real holds (4s and longer)

- About 7 shots of 4s or more and 1 to 3 of 6s or more per film. A film with no 6s shot is normal (p10 is zero).
- Where real 6s-plus holds live: portraits, getting ready, reception entrance, dancing (a single held wide), recessional, vows, speeches and first look, plus the final images.
- What they show: the couple in a landscape, a recessional moment, a face during a speech or reading, a prep moment by a window.
- Mood of real holds: tender most often, then ceremonial and celebratory.
- One hold SHOULD be the payoff of its scene, if it gets one at all. Most scenes get none.
- AVOID holding dance-floor footage. What looks like long dance shots in the tool's data are montages cut at a median 1.7s (p25 1.0s, p75 2.4s).

### 6.4 Scene pacing (median shot length per scene, corrected)

| Tightest | Median (p10 to p90) | | Slower | Median (p10 to p90) |
|---|---|---|---|---|
| cake_cutting | 0.96s (0.42 to 2.40) | | first_dance | 1.71s (0.67 to 3.95) |
| other | 1.33s (0.54 to 2.38) | | ceremony_vows | 1.73s (0.76 to 3.38) |
| ceremony | 1.42s (0.58 to 2.59) | | first_look | 1.75s (0.75 to 3.35) |
| ceremony_processional | 1.42s (0.75 to 2.59) | | details | 1.75s (0.71 to 2.79) |
| toasts | 1.48s (0.58 to 2.46) | | portraits | 1.84s (0.79 to 3.82) |
| cocktail_hour | 1.58s (0.78 to 2.63) | | establishing | 1.88s (0.75 to 3.21) |
| speeches | 1.63s (0.51 to 3.00) | | reception_entrance | 1.92s (0.60 to 2.71) |
| send_off | 1.63s (0.50 to 5.16) | | getting_ready | 1.96s (0.75 to 3.25) |
| dancing | 1.63s (0.50 to 2.79) | | ceremony_recessional | 1.96s (0.71 to 4.17) |
| | | | transition | 2.13s (0.98 to 3.87) |

- Ceremony and processional are reaction cutting: speaker, partner, parents, guests, wide. The audio carries the emotion.
- Cake cutting is a burst of sub-1s angles on one action, joined by dissolves.
- Dancing and send-off have the shortest p10 (0.5s): flash cuts are allowed there and almost nowhere else.
- Getting ready, portraits and recessional are the slowest people scenes, with the most room for a real hold.

---

## 7. Transitions

### 7.1 Mix per film

| Type | Share of boundaries | Per film: median (typical) |
|---|---|---|
| Hard cut | 60% | 90 (82 to 100) |
| Dissolve | 25% | 35 (24 to 42) |
| Still hold | 15% | 21 (16 to 25) |
| Fade in | under 1% | 1 (opening only) |
| Fade out | under 1% | 0 (closing only, 4 of 17 films) |

### 7.2 Dissolves

- **Short.** Median dissolve length 0.55s (all films between 0.48 and 0.70s), about 13 frames at 23.976. MUST NOT use long cross-dissolves (1s or more).
- **Frequent and clustered.** Median gap between dissolves is 3.9s; dissolves come in runs (p25 gap 1.4s) separated by hard-cut passages (p75 gap 10.5s).
- **They mark segment seams.** The tool defines chapters as the stretches between dissolves, so every chapter boundary is a dissolve by construction. Inside a segment, cuts are 80% hard and 20% still hold.
- Where they cluster (share of a scene's boundaries that are dissolves): cake_cutting 60%, first_dance 43%, send_off 40%, dancing 35%, ceremony_processional 32%, ceremony_recessional 30%, speeches and toasts 29%, first_look 27%. Lowest: transition 6%, portraits and details 17%, cocktail_hour 19%, getting_ready 20%, ceremony_vows 20%.
- Use them to: show one continuous action from several angles (cake, a walk down the aisle, lacing a dress); slide between songs or energy levels on the dance floor; soften into and out of reverent stretches; land the final couple images.

### 7.3 Still holds

- A **still hold** is a cut where one side is nearly motionless for the first or last few frames: a slow-motion or locked-off moment settling before or after the cut. These are live video clips, not photographs (checked frame by frame).
- About 21 per film. They concentrate in portraits (21% of all still holds), getting ready, cocktail hour, first look, details and speeches.
- Use them to let a calm frame land: a portrait pose settling, a smile resolving, a detail at rest. The clip around a still hold runs a median 2.2s.

### 7.4 Fades

- MAY fade in from black on the first frame (12 of 17). MAY fade out on the last frame (4 of 17).
- MUST NOT fade to black mid-film.

---

## 8. Shot selection

### 8.1 Catalog schema

Describe every raw clip with the same `shot_description` fields the archive uses:

```json
{
  "subjects": ["bride", "groom", "couple", "guests", "wedding_party", "parents", "family", "officiant", "kids", "details_only"],
  "action": "short verb phrase, e.g. 'lacing dress back'",
  "setting": "exterior_landscape | dance_floor | getting_ready_room | altar | reception_table | ceremony_seating | lawn | interior_other | tent | ballroom | garden | aisle | hallway | vehicle",
  "lighting": "warm_indoor | natural_daylight | overcast | golden_hour | uplighting_warm | uplighting_cool | dim_indoor | night_exterior | candle | dance_floor | mixed_indoor",
  "camera": "slight_handheld | locked | handheld | gimbal_walk | rack_focus | drone | pan | tilt",
  "mood": "tender | candid | joyful | ceremonial | still | anticipatory | celebratory | intimate | kinetic",
  "description": "one plain sentence"
}
```

### 8.2 Mood

| Mood | Share | | Mood | Share |
|---|---|---|---|---|
| tender | 22.1% | | anticipatory | 7.3% |
| candid | 16.5% | | celebratory | 7.2% |
| joyful | 14.7% | | intimate | 5.5% |
| ceremonial | 12.5% | | kinetic | 3.7% |
| still | 10.3% | | | |

**Mood arc by position**
- 0 to 20%: tender 28%, anticipatory 16%, still 15%.
- 20 to 40%: tender 23%, candid 21%, ceremonial 17%.
- 40 to 60%: candid 25%, ceremonial 19%, tender 16%.
- 60 to 80%: tender 19%, joyful 17%, celebratory 14%.
- 80 to 100%: tender 26%, celebratory 16%, joyful 14%, kinetic 11%.

When two candidates are otherwise equal, SHOULD pick the tender one. Kinetic shots are a release valve for the dance floor, not a default.

### 8.3 Who is on screen (share of clips; one clip can hold several subjects)

guests 28.5% · couple 21.1% · bride 19.9% · groom 13.4% · wedding_party 12.6% · details_only 12.3% · parents 11.7% · family 10.1% · officiant 3.7% · kids 2.9%

- The wedding is a community, not a couple. SHOULD cut to reactions (parents, guests, wedding party) throughout. A scene with only couple shots reads as wrong.
- The ceremony scene is mostly guests and family (53% guests). Vows carry the couple and officiant.
- AVOID officiant-only shots without the couple in frame.

### 8.4 Camera

slight_handheld 59.0% · locked 33.9% · handheld 2.8% · gimbal_walk 2.1% · rack_focus 1.3% · drone 0.5% · tilt 0.2% · pan 0.2%

- MUST keep the camera invisible: slight handheld for people, locked for altar wides, establishing and still-life details.
- Drone: openers and establishing only. AVOID drone mid-film.
- Loose handheld: dance floor only (29% of dancing clips; nearly absent elsewhere).
- Gimbal walk: portraits, recessional and couple walks. Rack focus: details.
- AVOID pans and tilts as a primary move.

### 8.5 Light and setting

- Lighting: warm_indoor 30.7%, natural_daylight 28.9%, overcast 18.6%, golden_hour 9.1%, uplighting 5.7%, dim_indoor 2.1%, night_exterior 2.0%, candle 1.8%.
- 87% of clips sit in natural or warm practical light. SHOULD prefer clips where skin tones read naturally; AVOID heavy colored uplighting except as a deliberate dance-floor moment.
- Top settings: exterior_landscape 21.6%, dance_floor 10.5%, getting_ready_room 9.4%, altar 8.1%, reception_table 7.2%, ceremony_seating 7.1%, lawn 7.0%.
- Outdoor landscape is the breath between dense indoor scenes. Reception tables are cut tight (hands, glasses, faces), never long table wides.

### 8.6 Framing, composition and culling (from `shot-profile.json`, 2,478 frames)

- **Framing mix:** medium-full 33%, full 30%, no person 25%, medium 11%, medium-close 2%, close-up under 1%. SHOULD work at an observational distance; tight face close-ups are rare.
- Faces present in 76% of frames; primary face averages about 2% of frame area; 70% face roughly toward camera.
- **Headroom:** typical 13% to 37% of frame height (average 24%). Face center sits in the upper third (y 0.21 to 0.44 of frame height, top = 0).
- **Rule of thirds:** average proximity score 0.63.
- **Exposure:** average brightness 0.38 on a 0 to 1 scale (typical 0.22 to 0.53). Images run slightly dark and soft, not bright.
- **Culling (MUST reject):** cut-off heads (0.5% of the archive), severely overexposed frames (0%), severely underexposed frames (allowed in under 2%, only for intentional night silhouettes).
- **Softness is tolerated:** about 10% of kept frames are soft focus. Emotion and moment beat technical sharpness.
- Ignore the DeepFace emotion labels in `shot-profile.json`: they score 27% of happy wedding frames as "fear". Use the `mood` field from shot descriptions instead.

---

## 9. Audio and music

### 9.1 Two audio modes: pick one per film

| Mode | Films | What it sounds like |
|---|---|---|
| **Story film** | 9 of 17 | Music bed plus 84 to 173s of spoken audio (vows, letters, speeches, toasts). Median 120s, 23% to 42% of runtime. |
| **Music only** | 8 of 17 | Music start to finish. At most 12s of incidental speech. |

Default: story film when the day produced clear vows, letters or speeches; music only when it did not. See open decision 3.

### 9.2 Story-film rules (measured on the 9 story films)

- **Voice enters early.** First spoken words land at a median of 16.6s (8 of 9 films between 7 and 23s, right around the title). One film holds speech until 2:34.
- **Speech arrives in blocks:** 4 to 28 separate passages per film (median 8). The longest unbroken passage runs 26 to 43s (median 37s).
- **Voice rides over other pictures.** Spoken audio sits under first look (55% of that scene's runtime), toasts (48%), speeches (28%), portraits (27%) and first dance (26%). It is nearly absent under the ceremony picture itself (vows 4%, processional 8%). Lift vow and letter audio out of the ceremony and lay it over prep, first look and portraits; let music carry the ceremony picture.
- **Shape across the film:** voice-heavy in the first 20%, light from 40% to 60% (ceremony into cocktail hour), heavy again from 60% to 80% (reception speeches), easing out at the end so the film closes on music.
- SHOULD duck music clearly under speech. During every speech passage the classifier hears speech as the dominant sound.

### 9.3 All films

- **Natural sound is rare:** ambient-only audio is a median 1.3% of runtime (max 11.7%). AVOID long nat-sound breaks.
- **Tempo:** median 112 BPM, typical 99 to 123 BPM. Mid-tempo songs, neither ballads nor dance tracks. (The 162 and 185 BPM readings are most likely double-time reads of slower songs.)
- **Key:** spread across 9 keys; no preference.
- **Energy shape:** the combined music and voice level rises through the first 20% to 40%, dips mid-film (50% to 60%), lifts slightly around 70%, and ends level. The film does not crescendo into its ending.
- **Cuts are NOT locked to the beat.** On the tool's cut list, 17.9% of cuts land within 60 ms of a detected beat, while random cutting would land 22.5% there. Across 3,193 cuts (corrected list) the position of cuts within the beat is nearly uniform (phase concentration R = 0.05 on a 0 to 1 scale). MUST NOT snap cuts to the beat grid by default; cut on action, gesture, glance and musical phrase. `film-style predict-cuts` snaps to beats, so treat its output as a rough grid, not as the style.
- Song count, song sourcing and licensing were not measured. See open decision 5.

### 9.4 Loudness (EBU R128, measured on the delivered files)

| Film-level metric | Median | Observed range |
|---|---|---|
| Integrated loudness | -15.5 LUFS | -31.0 to -9.5 LUFS |
| Loudness range (LRA) | 10.4 LU | 6.0 to 15.5 LU |

The archive has no consistent master level (a 21 dB spread). Until Joshua sets one (open decision 2), master to **-14 LUFS integrated, true peak no higher than -1 dBTP, LRA 8 to 12 LU** and flag it.

---

## 10. Color and finishing

Measured on the delivered 720p files, one frame per clip (2,478 frames). Treat the numbers as relative targets for checking a grade, not as grading-panel settings.

### 10.1 The look in numbers

| Metric (per film) | Median | Typical (p25 to p75) | What it means |
|---|---|---|---|
| Mean luma, 0 to 255 | 96.5 | 90 to 104 | Mid-key, a little under middle grey. Not bright and airy. |
| Luma contrast (standard deviation) | 54.4 | 52 to 60 | Moderate contrast. |
| Warm/cool index, -1 to +1 (mean R minus B) | +0.23 | +0.19 to +0.25 | Warm. 15 of 17 films read warm; 2 read neutral. |
| Saturation, HSV S 0 to 255 | 89 | 81 to 100 | Natural, moderate. |

Tone labels across films: mid-key warm 12, low-key warm 2, mid-key neutral 1, low-key neutral 1, mid-key neutral desaturated 1.

### 10.2 Grading rules

- SHOULD grade warm and natural, with skin reading true first.
- **One warmth across daylight.** Overcast (+0.22), natural daylight (+0.21) and golden hour (+0.22) all sit at nearly the same warmth as warm indoor light (+0.25). Overcast days get warmed to match; they are never left blue.
- **Night stays night.** Night exteriors (+0.02) and cool uplighting (-0.04) stay near neutral. Do not force warmth into them.
- **Let the day get darker.** Median brightness falls from 106 in the first fifth to 79 in the last fifth, and warmth eases from +0.22 to +0.15 as evening arrives. Do not brighten evening scenes to match the afternoon.
- **Saturation:** golden hour and candlelight carry the most (94 to 95); everything else stays moderate. AVOID punchy, high-saturation grades and AVOID a washed-out desaturated look (1 of 17 films).
- AVOID stylized looks (teal and orange, heavy creative LUTs, bleach bypass). The venue and the weather set the color; the grade unifies it.

### 10.3 Reference frames

Look at these thumbnails when matching a grade. Each sits at the archive median for its lighting.

| Lighting | Reference frames (`thumbs/...`) |
|---|---|
| Natural daylight | `Sarah_and_Dave/clip_071.jpg`, `Rachel_and_Jack/clip_024.jpg` |
| Overcast | `Olivia_and_Marc/clip_048.jpg`, `Olivia_and_Marc/clip_118.jpg` |
| Golden hour | `Maddie_Max_final/clip_153.jpg`, `Danielle_and_Anthony/clip_058.jpg` |
| Warm indoor | `Amanda_and_Kenton/clip_006.jpg`, `Jess_and_John/clip_082.jpg` |
| Candle | `Isabelle_and_Michael/clip_101.jpg`, `Danielle_and_Anthony/clip_129.jpg` |
| Warm uplighting | `Isabelle_and_Michael/clip_117.jpg` |
| Night exterior | `Olivia_and_Marc/clip_160.jpg`, `Jess_and_John/clip_036.jpg` |
| Title cards | `Becca_and_Jason/clip_002.jpg` (thin sans), `Danielle_and_Anthony/clip_002.jpg` (serif plus venue line) |

### 10.4 Finishing checklist

- 23.976 fps; aspect per open decision 1; no letterbox bars inside a 16:9 frame.
- Title "Name and Name" in white, centered, over a landscape or venue shot, inside the first 10s. Two observed styles: thin sans-serif, and serif with the venue name in smaller type underneath.
- Fade up from black at the start (default); end on black.
- Loudness per section 9.4.
- Color within the section 10.1 typical bands, checked against the reference frames.

---

## 11. Scene recipes (quick reference)

Each row is the measured fingerprint (shot lengths use the corrected cut count). Full playbooks with anatomy, required shots and anti-patterns live in `edit-craft/scenes/<label>.md`.

| Scene | Median clip (p10 to p90) | Dissolve share | Dominant mood | Dominant subjects | Recipe |
|---|---|---|---|---|---|
| getting_ready | 1.96s (0.75 to 3.25) | 20% | tender, anticipatory | bride, details, groom | Both partners' prep, dress and ring details, parent moments. Observational. |
| establishing | 1.88s (0.75 to 3.21) | 25% | still | details_only | Locked or drone. Long when opening or closing, short mid-film. |
| first_look | 1.75s (0.75 to 3.35) | 27% | tender | bride, couple, groom, parents | Quick build (turn, tap, approach), then let the reaction breathe 2.5 to 3s. Includes parent reveals. Never after 40% of runtime. |
| portraits | 1.84s (0.79 to 3.82) | 17% | tender, joyful | couple, bride, wedding party | Largest block. Mix wide-in-landscape, walking, and tighter frames. Still holds live here. |
| ceremony_processional | 1.42s (0.75 to 2.59) | 32% | ceremonial | parents, bride, guests | Bride with escort, groom reaction, wedding party walks. Short and punchy. |
| ceremony | 1.42s (0.58 to 2.59) | 23% | ceremonial, candid | guests, family | Reaction cutting. Tightest scene in the film. |
| ceremony_vows | 1.73s (0.76 to 3.38) | 20% | ceremonial, tender | couple, officiant | Speaker, listener, hands, rings, kiss. Let vow audio lead. |
| ceremony_recessional | 1.96s (0.71 to 4.17) | 30% | celebratory | couple, guests | Release of energy back down the aisle. |
| details | 1.75s (0.71 to 2.79) | 17% | still | details_only, guests | Reception decor gallery: locked or rack focus. |
| cocktail_hour | 1.58s (0.78 to 2.63) | 19% | candid | guests | Fast mingling. Hands, drinks, laughter. |
| reception_entrance | 1.92s (0.60 to 2.71) | 26% | candid, still | guests, groom, details | The room reacting to the couple as they come in. |
| speeches | 1.63s (0.51 to 3.00) | 29% | tender, candid | guests, wedding party | Speaker, couple reaction, guest laughter. Speech audio carries it. |
| toasts | 1.48s (0.58 to 2.46) | 29% | candid | guests, couple | Raised glasses and clinks. Only when glasses actually go up. |
| first_dance | 1.71s (0.67 to 3.95) | 43% | tender | couple, guests | 2 or 3 angles, dissolves between them, parents watching. |
| dancing | 1.63s (0.50 to 2.79) | 35% | kinetic, tender | guests, bride, parents | Fast montage, flash cuts allowed, handheld allowed. Parents dancing count. No long holds. |
| cake_cutting | 0.96s (0.42 to 2.40) | 60% | joyful | couple | A burst of short angles on one action plus reactions, joined by dissolves. |
| send_off | 1.63s (0.50 to 5.16) | 40% | intimate, tender | couple | Only if there was a planned exit. Action, then a held final image. |
| transition | 2.13s (0.98 to 3.87) | 6% | joyful, still | couple | Formal slug bridge or closing breath. Rare. |
| other | 1.33s (0.54 to 2.38) | 27% | candid | guests, groom | Pre-wedding events, parent dances, cultural rituals. Read its playbook to pick the sub-case. |

---

## 12. Hard rules and anti-patterns

**MUST**
- Day order, forward only.
- Open on nature, venue or a still detail; never a person.
- End on the couple alone in fading light, then black.
- Dissolves 0.48 to 0.70s long.
- Fades only on the first and last frames.
- Include every MUST scene the day contained (portraits, processional, speeches, getting ready, dancing).
- 23.976 fps.

**AVOID**
- Long cross-dissolves (1s or more), dip-to-white, and flashy transitions (whip, glitch, zoom, light leak). The detector found only hard cuts, short dissolves, still holds and fades.
- Drone, gimbal or handheld energy as a default look.
- Heavy LUT looks, teal-and-orange, crushed or lifted-to-grey blacks (section 10).
- Ending on dance-floor energy.
- Openers on a face, a moving subject, or a crowd.
- Officiant-only shots; long reception-table wides; uplighting-heavy clips outside the dance floor.
- Long holds on the dance floor. Dance footage is a fast montage.

---

## 13. QA checklist

Run before calling a cut done. Then run `film-style compare <cut.fcpxml>`. Caution: `compare` scores against the tool count (about 149 clips, 24 cuts/min), which under-counts. A correct cut will read as "too many cuts" there; judge pacing by the corrected targets below.

```json
{
  "runtime_sec":              {"target": 359, "typical": [348, 392], "acceptable": [268, 411]},
  "cuts_per_min":             {"target": 30,  "typical": [28, 33], "acceptable": [26, 35]},
  "median_shot_sec":          {"target": 1.65, "acceptable": [1.4, 1.9]},
  "pct_shots_under_3s":       {"target": 88,  "acceptable": [81, 95]},
  "shots_4s_plus":            {"target": 7,   "acceptable": [3, 13]},
  "shots_6s_plus":            {"target": 2,   "acceptable": [0, 5], "never_on_dance_floor": true},
  "median_shot_last_20pct_sec": {"target": 1.5, "max": 1.7},
  "first_shot_sec":           {"target": 2.9, "acceptable": [0.7, 4.3]},
  "first5_avg_sec":           {"target": 2.4, "acceptable": [1.4, 2.9]},
  "last5_avg_sec":            {"target": 3.0, "acceptable": [1.5, 3.9]},
  "dissolves":                {"target": 35,  "typical": [24, 42], "length_sec": [0.48, 0.70]},
  "still_holds":              {"target": 21,  "typical": [16, 25]},
  "fades":                    {"first_frame_only_in": true, "last_frame_only_out": true, "mid_film_max": 0},
  "portraits_share_pct":      {"typical": [11, 19]},
  "max_single_scene_share_pct": 20,
  "speech_mode":              {"story_film": {"speech_sec": [84, 173], "first_words_sec": [7, 23]}, "music_only": {"speech_sec_max": 12}},
  "color":                    {"mean_luma_0_255": [90, 104], "warm_cool_index": [0.19, 0.25], "saturation_0_255": [81, 100]},
  "loudness":                 {"integrated_lufs": -14, "tolerance_lu": 1, "true_peak_dbtp_max": -1, "lra_lu": [8, 12], "note": "default pending open decision 2"}
}
```

Hard cuts are whatever remains after dissolves and still holds (about 130 per film on the corrected count).

- [ ] Every MUST scene the day contained is present, in day order.
- [ ] No `never_observed_transitions` pairs.
- [ ] Opening shot has no person in it; title "Name and Name" lands in the first ~10s.
- [ ] Final real image is the couple alone in low or fading light; the film ends on black.
- [ ] Reactions (parents, guests) appear in every major scene.
- [ ] Median cut stays 1.6 to 1.9s through 80% of the film, then tightens for the finale.
- [ ] No long holds on the dance floor.
- [ ] Cuts are not snapped to the beat grid.
- [ ] No cut-off heads; no overexposed frames.
- [ ] Color and loudness pass section 10.

---

## 14. Corrections to older docs in this workspace

Agents reading `style-guide.md`, `edit-craft/editor-voice.md` or `edit-craft/README.md` will meet these claims. The data says otherwise; follow this spec.

| Older claim | What the data shows |
|---|---|
| Clip counts, averages and "long holds" everywhere in older docs and `style-profile.json` | Based on a detector that missed about 690 cuts, mostly on dark dance floors. Real pacing is about 30 cuts/min; see the measurement note and section 6. |
| "First cut lands at 4.68s, window 4.0 to 5.5s; do not cut sooner" (style-guide.md, style-profile rules) | 4.68s is a mean inflated by a "17.9s opener" that is really 7 shots. Median first shot is 2.9s and none exceeds 4.3s. |
| "Do not insert sub-1.5s clips after the 80% mark" (style-guide.md) | Half of all shots in the last 20% are under 1.5s. The finale is the fastest stretch. |
| "Clips lengthen monotonically after 70%" (style-guide.md) and "dancing: fewer but longer clips" | The dance-floor "long clips" are montages. The median tightens late; only the final few shots slow down. |
| "Dancing mean 3.88s, median 1.94s; let movement breathe" (editor-voice.md, style-guide.md) | Corrected dancing median is 1.63s with flash cuts down to 0.5s. |
| "Land 20% of cuts on a music beat" (style-profile rules) | 20% is what random cutting produces. Cuts are not beat-locked. |
| "Hold music alone for the first ~42s / 11% before speech" (style-profile rules) | A mean skewed by music-only films. Story films bring voice in at a median 16.6s. |
| "When in doubt, pick the tender close-up" (editor-voice.md) | Close-ups are under 1% of frames. Pick the tender shot at observational distance. |
| "Still hold = a held still photograph" (tool docs, `dissolve_measure.py`, style-profile rules) | Still-hold clips are live slow-motion or locked footage with a calm start or end. |
| "Dissolves happen at chapter boundaries" (editor-voice.md) | Chapters are defined by dissolves, so this is circular. Dissolve spacing and per-scene rates in section 7.2 are the usable facts. |
| "No clip over 7s in any ceremony block" (style-guide.md) | Max observed: processional 13.6s, recessional 12.0s, ceremony 10.7s, vows 7.1s. Some of those are missed cuts; treat the corrected p90 (2.6 to 4.2s) as the working cap and long ceremony holds as rare exceptions. |
| 2,646 clips and 654 chapters (edit-craft docs) | The current archive holds 2,478 clips and 627 chapters. |
| "No color or audio data" (style-profile.json before 2026-11-09) | Backfilled; see sections 9 and 10. |
| Chapter labels on individual clips | Labels belong to dissolve-bounded chapters, so a single clip can carry the wrong label (a 58s dance montage sits in a "portraits" chapter). Trust each clip's own `shot_description.setting` over its chapter label. |

---

## 15. Open decisions for Joshua

These are not measurable from finished films, or the archive is inconsistent. Agents: ask, or use the stated default and flag it.

1. **Aspect ratio.** 9 films deliver at 16:9; 8 deliver wider (about 1.9:1, one at 2:1). Which is the standard going forward? Default until answered: 16:9.
2. **Master loudness.** The archive spans -31 to -9.5 LUFS. Default until answered: -14 LUFS integrated, -1 dBTP true peak.
3. **Story film or music only.** Who decides per wedding, and on what? Default until answered: story film when clear vows, letters or speeches exist.
4. **Title typography.** Two styles appear (thin sans; serif with a venue line). Which font, size and position is current? Default: copy the most recent film's title.
5. **Music.** Number of songs per film, where tracks are licensed from, and any genre preferences. Not measurable from finished films.
6. **Delivery masters.** These measurements come from 720p Vimeo files. Master resolution, codec and bitrate are unknown. Default: deliver at the source resolution, 23.976 fps, H.264 or ProRes per the client's need.
7. **End card.** One film ends on a "JOSHUA BROWN" credit card; the rest end on plain black. Is a credit card standard?
8. **Other lengths.** `edit-craft/macro-templates/` holds 3, 6 and 15 minute blueprints, but every measured film is a highlight film (3:40 to 7:39). The teaser and full-length rules are extrapolated, not measured.

---

## 16. File map

All paths are relative to `~/.film-style-analyzer/wedding/`.

| File | Use it for |
|---|---|
| `EDITING-SPEC.md` | This file. Start here; it wins on conflicts. |
| `style-profile.json` | Machine-readable targets the `film-style` tools read (`compare`, `predict-cuts`). Regenerated 2026-11-09 with color, audio and music. |
| `../shot-profile.json` | Composition and culling preferences used by `score-clips`. |
| `aggregate-stats.json` | Raw pacing, transition and scene aggregates. |
| `analyses/<film>.json` | Per-film, per-clip ground truth: timings, transitions, chapter labels, shot descriptions, color, audio segments, beats. Worked examples. |
| `edit-craft/scenes/<label>.md` | Deep per-scene playbooks (anatomy, required shots, anti-patterns, assembly recipe). Load only the scene you are cutting. |
| `edit-craft/reference-edits/*.md` | Three films walked clip by clip with the reasoning for each cut. |
| `edit-craft/sequence-grammar.json` | Scene-to-scene probabilities and `never_observed_transitions`. |
| `edit-craft/shot-selection-rules.json` | Per-scene scoring weights for picking raw clips. |
| `edit-craft/coverage-checklist.md` | Pre-assembly footage check. |
| `edit-craft/macro-templates/*.json` | Teaser (3 min), highlight (6 min) and full (15 min) blueprints. |
| `thumbs/<film>/clip_NNN.jpg` | One frame per clip for visual reference. |

Rebuild after adding films: `film-style analyze <folder> --music`, then `film-style guide`, `film-style learn-shots --force`, and regenerate this spec.
