# Synthesis

> Status: **FIRST PASS — Field Day 1 only (2026-06-18).** Unlocked 2026-06-19 per the original
> hold. This is provisional: it rests on one daytime session (~10:00–15:00) and on intercepts
> almost entirely on the **main Sudirman trotoar**. A second round (Sat night) and the
> back-street audit are still needed before any finding is firm.
>
> Evidence base: 12 audio intercepts + Tim A/B notulen (16 people: ~10 upper/middle, 6 bottom).
> See `field/transcripts/2026-06-18-intercept-transcripts.md` (ground truth),
> `field/transcripts/2026-06-18-respondent-profiles.md`, `field/data/respondents_2026-06-18.csv`.
>
> ⚠️ The 1–10 scales are mostly the analyst's *interpretation* of transcripts, not asked
> measurements. Use them for direction, not precision.

---

## We engaged…

- **16 people on Field Day 1** across two teams, daytime (~10:00–15:00):
  - *Pedestrians (upper/middle):* daily & weekly commuters, an elderly daily walker, a parent
    with a child, students (SMAN 3), a TJ commuter, a motorbike rider who walks short hops.
  - *Workers / "bottom class":* area & JPO security guards, MITJ staff (incl. tunnel post),
    Satpol PP, a PKL, a GrabCar driver, a local elderly resident (Kebon Melati).
  - *A self-styled urban-planning critic* (File 11) who gave the sharpest design argument.
- **Where:** main trotoar, station forecourts, the JPO, and the Kendal tunnel post. **Not yet:**
  the back-streets one block off Sudirman (the gradient) — only one back-area contact (Kebon Melati).
- **Weather:** the session was captured with Apple Weather screenshots (logged in
  `field/data/weather_2026-06-18.csv`).
- **Photos + videos:** **105 geotagged files** (37 photos, 68 videos, ~7.6 min) logged in
  `field/photos/media-log_2026-06-18.csv`, spanning 10:37–13:45 WIB and tracing the corridor
  from Dukuh Atas (≈−6.201) south to Setiabudi/Semanggi (≈−6.223). Originals kept out of git.

---

## We found… (provisional)

### 1. The main trotoar is broadly judged GOOD — comfort, not the sidewalk itself, is the issue
This is the most important early signal and it **runs against our original framing** (the
"walk in the road *despite* a good sidewalk" bias the mentor flagged). On the main corridor,
respondents repeatedly call the trotoar *enak, lega, luas, manusiawi, bagus*. The critic
(File 11) is blunt: *"Trotoarnya udah bagus… Udah manusiawi? Udah. Udah gede? Udah."* The
problem he names is what comes **on top of** a good sidewalk: climate comfort.

→ Implication: the design opportunity is likely **comfort layered onto an already-decent
corridor** (heat, night safety, micro-hazards), *and* the contrast with the un-revitalised
back-streets — not "fixing" the Sudirman trotoar.

### 2. Heat is the dominant comfort complaint — and framed as a *design* failure
Heat is the single most common pain point (Files 02, 03, 04, 07, 10, 11, 12; multiple notulen).
Nuances:
- People cope rather than avoid: shade-seeking, **umbrellas** (Mba Tangsel, File 05), choosing
  cooler hours, valuing the tree buffer (Files 02, 10).
- The critic's argument (File 11), independently echoed by Satpol PP (File 12) when the
  interviewer raised it: Jakarta's pedestrian design copied **four-season countries**
  (Europe/Japan) — bike lanes, tree planting — instead of tropical heat/rain needs. Trees are
  *"belum cukup efektif"* by day, and **at night the same foliage covers the lamp poles →
  dark**, plus mosquitoes make sitting unpleasant.
- This directly **supports Assumption 4** (heat makes daytime walking unpleasant) and
  **Assumption 5** (umbrellas), and gives a concrete causal story for **Assumptions 7/8/10**
  (heat → timing/route shifts, comfort vote). It strengthens the WeatherKit-join plan.
- **Measured conditions corroborate this** (`field/data/weather_2026-06-18.csv`): across the
  session air temp was **31–33 °C with a feels-like of 33–35 °C** (peaking 35 °C midday) —
  consistently **above the ~27 °C THI threshold** in Assumption 10. UV was **7–8 (High/Very
  High)**, "use sun protection until 4 PM"; humidity 52–61 % (dew point 22–23 °C, muggy); wind
  light (8–11 km/h, little cooling); **0 mm rain**; and the day ran **+3 °C above the average
  daily high**. So the heat complaints land on an objectively hot, sunny, near-windless day.
- **Caveat:** because it was dry, the **rain/sheltering assumptions (6, 9) were not testable**
  yesterday. The Saturday forecast carried ~40–50 % rain probability — the night round may finally
  let us observe rain behaviour (or be disrupted by it; plan a contingency).

### 3. Daytime safety is reassuring; night safety is the real concern — and it's *isolation*, not darkness
- By day, nearly everyone says *aman* (Files 02, 04, 06, 10; Mba 1 even reports walking home
  safely at **01:00**). Police presence is mentioned as reassuring (File 04).
- The hotspots are **the upper JPO and parking areas**, **after ~22:00** (Files 09, 12; Mas
  Arief notulen): jambret above, copet/curanmor below. A foreign visitor was robbed at **03:00**
  (~6 months ago).
- Crucial mechanism (File 09): *"Terang sih, di atas terang… cuma sepi."* The risk driver is
  **isolation in a lit-but-deserted** space, not poor lighting. → **Refines, does not simply
  confirm, the safety assumptions**: a lighting-only intervention would miss the point;
  "eyes on the street" / activation matters more.
- Trend: respondents agree crime has **fallen over ~6 months** (Files 09, 12).
- **Counter-flow nuance** (File 03): one walker feels *safer when it's quiet* — opposite to the
  isolation risk above. Comfort vs. crime-safety can pull in opposite directions by crowd level.

### 4. Recurring micro-hazard: the trotoar→zebra-cross ramp is too high/steep/slippery
Independent reports (Files 05 and 10): the drop from kerb to crossing is *terlalu tinggi/curam*
and *licin* — File 05's friend **fell twice** (once during the interview). File 10 (parent)
ties it to fast vehicles from the main road. This is a concrete, observable, **auditable**
accessibility defect — strong candidate for the audit sheet and for photo/CV documentation.

### 5. Pedestrian–vehicle conflict on the sidewalk: ojol/Gojek riding the trotoar
Satpol PP (File 12) and Mas Arief (notulen) both flag **ojol riding onto the trotoar / through
the tunnel**, with near-misses. Note the enforcement gap: Satpol PP handles vendors; motorbikes
are **Dishub's** remit → falls between agencies. This **partially supports Assumption 1**
(obstruction) but reframes it: the obstruction is *moving vehicles*, not just parked ones/vendors.

### 6. Institutional gaps and ignored complaints (a distinct theme)
- **Security responsibility GAP**: each operator (KAI, MRT, area guards) guards only its own
  zone; public space between them is nobody's job (Files 01, 12; Satpam-JPO notulen).
- **Complaints ignored**: Mas Arief and Ibu Lis both report broken/uneven infrastructure
  reported to government but *"gak pernah digubris"*; Ibu Lis feels government ignores small
  problems. → **RESOLVED (2026-06-19):** JAKI is **still used but heavily backlogged**, a key
  cause being **duplicate/overlapping reports** (same spot reported many times). This finding
  triggered the team's pivot toward a Waze×JAKI reporting concept (see `DECISIONS.md` / `HANDOVER.md`).
- **Scam:** UNHCR-impersonation donation scam reported near the tunnel (Mas Arief).

### 7. The corridor is mid-transformation
MITJ staff (File 08): the former car U-turn (once begal-prone) was closed for the MRT/TOD; a new
roundabout ("donat", like Semanggi) is under construction and the **Sudirman statue may be
relocated**. Construction currently causes minor obstruction. Context for why "before/after
Anies" framing keeps surfacing.

### 8. Who walks & why (Q5) — early picture
Commuters (KRL/MRT/TJ to office/school), an elderly exerciser, a parent, students, plus
service/security workers who *work* the corridor. The motorbike rider (File 07) marks the
edge: for some, walking is only the last short hop from parking — a mode-choice signal relevant
to the heat finding (he'd walk more if it were cooler; night is "enjoy").

### Assumptions ledger — provisional status (update `engage/assumptions.md` after Sat)
| # | Assumption | Day-1 signal |
|---|-----------|--------------|
| 1 | Sidewalks blocked by parked motorbikes/vendors | **Partial / reframed** — main trotoar wide enough; bigger issue is *moving* ojol on trotoar + PKL dilemma |
| 2 | Back-streets have little/no usable sidewalk | **UNTESTED** — almost no back-street sampling yet (gradient gap) |
| 3 | People step into road because sidewalk obstructed/missing | **Not supported on main corridor** — people use & praise the trotoar; test on back-streets |
| 4 | Heat/lack of shade makes daytime walking unpleasant | **Strongly supported** — + measured feels-like 33–35 °C, UV 7–8, day +3 °C above avg |
| 5 | People carry umbrellas for sun/rain | **Supported** (≥1 explicit; probe frequency) |
| 6 | Rain pushes people to ojol/taxi | **Weak/indirect** — sheltering + GrabCar cancellations hint at it; needs rain-window data |
| 7 | Volume drops at midday heat | **Plausible** — stated behaviour; needs the 5-min counts to confirm |
| 8 | In heat people shift to shade/shadier routes | **Supported** (shade-valuing, umbrellas) |
| 9 | Higher rain → more sheltering/cancellation | **Hinted** (File 12 sheltering; driver cancellations) |
| 10 | Comfort falls as heat index rises | **Consistent** — feels-like 33–35 °C (>27 °C THI) on a day of heat complaints; needs paired vote-vs-temp counts to quantify |
| 6/9 | Rain → ojol/sheltering/cancellation | **Untestable yesterday** (0 mm, dry); target on Sat (40–50 % rain forecast) |
| 11 | Air quality affects willingness to walk | **Untested** (one "bebas polusi" positive only) |

---

## Action items…

### Immediate (analysis)
1. **Update `engage/assumptions.md`** Status column from the ledger above (do *not* delete
   refuted ones — a refuted assumption is a finding).
2. **Verify the SMAN 3 notulen duplicates** — confirm true respondent count with the teams
   (several identical 12:20 / 7-10 rows look like template copies).
3. **Treat interpreted scales as provisional**; if the teams have the original on-site scale
   answers, replace the interpreted CSV values and mark `scale_source=stated`.

### Saturday-night round — design it to fill the gaps, not repeat Day 1
4. **Sample the gradient (Q4, Assumption 2):** pair each main-trotoar segment with the
   back-street one block behind it; run the **audit sheet** on both. This is the single biggest
   hole right now.
5. **Night safety:** observe the JPO/parking hotspots after 22:00 — crowd density, "eyes on
   street", lighting-vs-isolation; **women-led intercepts** (Sintani, Cikini–Benhil) to test
   whether the daytime "feels safe" holds for women at night.
6. **Audit the ramp/zebra-cross hazard** (Files 05, 10): measure kerb drop, slope, surface; photograph.
7. **Counts:** run the **5-min counts** across time windows (incl. night) to test
   Assumptions 7/8 and join to **WeatherKit** temp/heat-index.

### Photos & videos — turn them into evidence (currently unused)
8. Build a **photo/video log** (filename → segment_id → timestamp → what it shows). Keep
   originals out of git (see `field/photos/README.md`); link from there.
9. Use them as **evidence**: (a) **back every audit score with a photo** (shade, surface, ramp,
   obstruction); (b) as documentation/illustration of the findings (the ramp hazard,
   ojol-on-trotoar, crowd flow). *(Any computational analysis of the imagery — the
   sidewalk/greenery methods in `desk-research/COMPUTATIONAL-DIRECTION.md`, S21–S24 — is a
   research/analysis method for measuring the corridor, NOT a proposed solution; revisit in Act.)*

### Expert track
10. **Anies interview** (secretary replied 2026-06-19) — finalise logistics and lock the
    **obstacle-oriented** question set from `guiding-questions.md` §B. Day-1 data gives concrete
    hooks to put to him: the 4-season "studi banding" critique, the trotoar→zebra ramp,
    ojol-on-trotoar enforcement (Dishub vs Satpol PP), the inter-agency security gap, and
    ignored maintenance complaints / JAKI.

### Other
11. **JAKI status — DONE (2026-06-19):** still used, heavily backlogged, duplicate-clogged.
    This resolved finding triggered the team pivot (Waze×JAKI reporting concept) — see `HANDOVER.md`.
