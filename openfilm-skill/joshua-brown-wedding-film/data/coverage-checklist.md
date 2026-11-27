# Coverage checklist — pre-flight before assembling a film

Run this checklist *after* you have raw clips cataloged with shot_descriptions but *before* you start sequencing. It tells you whether you have enough footage to assemble a film in this editor's style, what's missing, and what to triage.

The checklist is layered:

1. **Mandatory coverage** — without these, the film will feel incomplete.
2. **Expected coverage** — typical for the day this couple had; missing items are red flags.
3. **Wedding-type-specific coverage** — driven by the metadata fields.
4. **Diversity coverage** — the editor's style needs variety within each scene.

If a check fails, you have two options: get more footage (if possible), or note the gap explicitly so the assembly agent can compensate (e.g., longer establishing shots to cover a thin first_look).

---

## 1. Mandatory coverage (every film needs all of these)

For each, you need at minimum the listed shot count with the listed required vocab fingerprint.

### Getting ready (≥6 raw clips, both bride and groom)

- [ ] At least 3 clips with `subjects=[bride]` or `subjects=[bride, parents]` in `setting=getting_ready_room`
- [ ] At least 2 clips with `subjects=[groom]` or `subjects=[groom, wedding_party]` in `setting=getting_ready_room` or `interior_other`
- [ ] At least 1 detail clip (`subjects=[details_only]`) of dress, shoes, or jewelry in the prep room

**Why it matters:** Prep is the editor's most reliable opening (47% of films open here). Without bride+groom prep parity, the opening will lopsided.

### Portraits (≥8 raw clips, mixed framing)

- [ ] At least 4 `subjects=[couple]` clips with `setting ∈ {exterior_landscape, lawn, garden, tent}`
- [ ] At least 1 wide / landscape framing (where you can see the venue around them)
- [ ] At least 1 tight framing (faces close, shoulders or chest up)
- [ ] At least 1 walking/movement shot (`camera ∈ {gimbal_walk, slight_handheld}`, action like "walking together")

**Why it matters:** Portraits is the highest-runtime scene (15.4% of avg film). It's also in 100% of films. Every wedding gets a portrait block. Without variety in framing, the block feels static.

### Ceremony processional (≥4 raw clips)

- [ ] At least 1 clip with `subjects ⊇ {bride, parents}` in `setting=aisle` (the bride's entrance)
- [ ] At least 1 reaction shot of the groom (`subjects=[groom]`, `mood ∈ {anticipatory, tender, joyful}`)
- [ ] At least 1 wedding-party walk-down (`subjects=[wedding_party]`, `setting=aisle`)
- [ ] At least 1 wide of the ceremony space with guests

**Why it matters:** 100% of films have a processional. The bride's entrance is the emotional centerpiece of the first half of every film.

### Ceremony vows (≥6 raw clips)

- [ ] At least 2 `subjects=[couple]` at altar showing rings/vows/kiss
- [ ] At least 2 reaction shots of guests, parents, or wedding party watching
- [ ] At least 1 clip of the officiant in context (not solo)
- [ ] At least 1 detail (rings exchanging, hands, eyes)

**Why it matters:** This is the dramatic peak of the first act. Without reaction shots, vows become a static two-shot.

### Reception activity (dancing or first_dance, ≥10 raw clips)

- [ ] At least 4 `setting=dance_floor` clips with `subjects ∈ {couple, guests, wedding_party}`
- [ ] At least 1 spotlit `subjects=[couple]` (first dance)
- [ ] At least 2 reaction crowd shots
- [ ] At least 1 high-energy moment (`mood ∈ {kinetic, celebratory}`)

**Why it matters:** 88% of films have substantial dancing coverage. Even quiet weddings have a 2-3 song stretch.

### Speeches OR toasts (≥4 raw clips)

- [ ] At least 1 person at mic giving a speech (speeches) OR
- [ ] At least 1 raised-glass toast moment (toasts)
- [ ] At least 2 reaction shots of audience listening / responding
- [ ] At least 1 close-up of the couple reacting

**Why it matters:** 94% of films have one or the other. If neither exists in raw footage, the second-half emotional valley gets nothing to anchor it.

---

## 2. Expected coverage (in 60-89% of films)

Missing any of these isn't fatal but is a yellow flag.

### Details (≥4 raw clips)

- [ ] Rings (close-up)
- [ ] Dress hanging or bouquet
- [ ] Invitation suite or programs
- [ ] Decor / ceremony arch close-up

### First look (≥3 raw clips)

- [ ] Approach shot (one partner walking up to the other)
- [ ] Reveal reaction (face turning, seeing)
- [ ] Embrace or first contact

### Establishing (≥3 raw clips)

- [ ] Wide of venue / sky / landscape
- [ ] Detail of weather (foliage, rain, sun, snow)
- [ ] Aerial / drone (optional but used by this editor sparingly)

### Cocktail hour (≥4 raw clips)

- [ ] Guests mingling with drinks
- [ ] Toasting / clinking glasses casually
- [ ] Couple greeting guests

### First dance (≥3 raw clips)

- [ ] Wide of the spotlit couple alone on floor
- [ ] Tight of couple's faces / hands
- [ ] Audience reaction watching

### Ceremony recessional (≥2 raw clips)

- [ ] Couple walking back down aisle as married
- [ ] Cheering / petals / confetti reaction

---

## 3. Wedding-type-specific coverage

These checks fire only based on the film's metadata. Use them to ensure tradition-specific moments are captured.

### If `metadata.ceremony == "religious"`

The Marlene_and_David case (Jewish wedding) shows what's needed:

- [ ] Chuppah construction / detail
- [ ] Ketubah signing
- [ ] Glass break (close-up of foot stepping)
- [ ] Hora chair-lift (couple raised on chairs)
- [ ] Religious officiant in context

For other religious traditions, adapt — Catholic ceremonies need the unity candle, Hindu ceremonies need the saptapadi/seven steps, etc.

### If `metadata.ceremony == "civil"` and `setting includes "outdoor"`

- [ ] Outdoor altar / arch wide
- [ ] Audience seated outdoors with venue context
- [ ] Weather coverage if outdoor (umbrellas if rain, sunshine if sunny)

### If `metadata.weather == "rainy"` (Becca_and_Jason, Carrie_and_Rose)

- [ ] Umbrella-handling clips (clear umbrellas read better than colored)
- [ ] Detail of rain on glass / leaves / petals
- [ ] Indoor backup ceremony space if used

### If `metadata.season == "autumn"`

- [ ] Foliage details (rust leaves, branches, bare trees)
- [ ] Long shadows / golden hour exterior
- [ ] Warm-tone interiors

### If `metadata.season == "winter"`

- [ ] Breath visible in cold-weather exterior
- [ ] Snow detail / footprints
- [ ] Heavy interior lighting (winter light is short)

### If `metadata.time_of_day == "evening"` or `"night"`

- [ ] Candle-lit details
- [ ] Warm interior lighting clips
- [ ] Night exterior establishing (string lights, venue lit up)
- [ ] Send-off lighting (sparklers, fireworks if present)

### If there's a planned send-off

- [ ] Sparkler arch tunnel
- [ ] Getaway car
- [ ] Final couple wave / exit
- [ ] Last shot (wide as they drive off, or held still)

### If there's a same-sex couple (Carrie_and_Rose)

- [ ] Both partners in their own getting_ready coverage
- [ ] Equal-weight first-look (neither hides; both anticipate)
- [ ] Family-of-origin coverage parallel for both partners

---

## 4. Diversity coverage within scenes

Even if you have *enough* clips per scene, you need *varied* clips. Use these checks per scene block:

### For every multi-clip scene

- [ ] At least 2 different camera distances (wide + tight)
- [ ] At least 2 different angles (front + side OR shoulder + over-shoulder)
- [ ] No two consecutive raw clips with identical `subjects` AND `setting` AND `camera` (those will look like a jump cut in the edit)
- [ ] At least 1 reaction shot per emotional beat (not just the action shot)

### For ceremony specifically

- [ ] Coverage from at least 2 camera positions (front-facing the altar + from-the-side)
- [ ] Tight coverage of the officiant + the speakers (vows, exchanges)
- [ ] Wide coverage of the audience perspective

### For dancing specifically

- [ ] Coverage of the couple + at least one other group (parents, wedding party, kids)
- [ ] At least 1 long-lens compressed crowd shot
- [ ] At least 1 close-up of feet/hands moving (kinetic detail)

---

## 5. Audio considerations (currently advisory)

The editor uses subscription-billed local CLI for guide generation; raw audio analysis is currently `--skip-audio` in the analyzer. When audio analysis is enabled in a future pass, add:

- [ ] Sync audio for at least the bride+groom's vows
- [ ] Sync audio for at least one speech
- [ ] Quiet ambient room tone for backgrounds
- [ ] Music cue or playlist of choices (used to drive cut points in dancing/first_dance)

---

## 6. The triage matrix

If your raw footage fails some checks, here's how to compensate:

| Failure | Compensation |
|---|---|
| Thin getting_ready | Extend establishing opener; lean on details montage. |
| No first_look footage | Cut from prep direct to portraits; lengthen portraits block. |
| Thin ceremony reactions | Use guest wides + officiant-reading-vows angles. |
| No speeches/toasts | Replace with extended cocktail_hour candid mingling. |
| No first_dance coverage | Open reception with dancing chapters directly; use parent dance as the slow opener. |
| No send_off | Close on a held portrait or transition slug instead. |
| No establishing options | Use a tight detail (clock, invitation, ring) as a "still life" opener instead. |

---

## 7. The final ship-readiness gate

Before sequencing begins, confirm:

- [ ] You have raw clips for every **mandatory** scene at the listed minimums.
- [ ] You have raw clips for at least 4 of 6 **expected** scenes.
- [ ] Wedding-type-specific tradition coverage is complete (or explicitly waived).
- [ ] Diversity within each scene is met.
- [ ] At least 200 total raw clips have shot_descriptions populated (the editor's films average ~155 in the final cut; you need ~30% surplus to give the assembly agent room to choose).

If you can check all of those, the film is ready to sequence.
