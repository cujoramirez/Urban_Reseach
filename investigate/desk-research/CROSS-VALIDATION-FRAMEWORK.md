# Quantitative Cross-Validation Framework

Every field metric, intercept question, and expert question — paired with a **published number
to check it against**. So our observation data and our interview data can be triangulated
against each other *and* against the literature, instead of standing alone.

**Tag key:** ✓ = verified against a fetched source/PDF · ⚠ = provisional (search-summary;
verify the primary before citing). Sources: S1–S14 in `SOURCE-INVENTORY.md` / `notes/`.

> Discipline: a benchmark tells us what "normal/standard" is — it does **not** tell us the
> corridor is good or bad. We compare, then let the field data speak.

---

## A. WHAT TO OBSERVE → benchmark to compare against
For the [audit sheet](../field/instruments/audit-sheet.md) + [tally sheet](../field/instruments/observation-tally-sheet.md).

| We measure | Published benchmark | Source | Tag |
|------------|---------------------|--------|-----|
| Effective sidewalk **width** | **≥ 1,85 m** minimum (national standard) | S13 Bina Marga 2023 | ✓ |
| Sidewalk **dimension vs flow** | Table 3 (dimension by land use + max flow); two-way unit **orang/m/menit** | S13 | ✓ |
| **Crossing spacing** (safe crossing nearby) | **100–200 m** between crossings | S13 | ✓ |
| Is a **protected/grade-separated crossing** warranted? | trigger when **>450 ped/jam/eff-m** on one side | S13 | ✓ |
| **Ramp** slope (accessibility) | **max 8% (1:12)**; drainage cross-fall 2–3% | S13 | ✓ |
| **JPO** clearance | min height **5,1 m** | S13 | ✓ |
| **Pedestrian space / crowding** (LOS) | HCM capacity ~**0,46–0,75 m²/ped** (intl. cross-check) | round-4 lead | ⚠ |
| **Walking pace** (e.g. hurrying exposed/heat) | Asian mean ≈ **1,23 m/s**; ID ~1,2–1,7 m/s | round-4 lead | ⚠ |
| **Shade / heat** at a segment | THI: comfortable **21–24°C**, uncomfortable **>27°C** (measure temp/RH on site) | round-4 lead | ⚠ |
| **Walkability** (segment scoring) | GWI: highly-walkable WI≥70 / waiting-to-walk 50–70; PEQI classes | S9, S6 | ✓ |
| **Last-mile distance** (station→destination) | TOD norm **400 m** (bus/tram) / **800 m** (rail); ITDP 500 m buffer | round-4 lead; S6 | ⚠/✓ |
| **Encroachment** (motorbikes/PKL on sidewalk) | code: must **not reduce effective width** | S13; cf. S1, S10, S12 | ✓ |

**How to use:** score each segment **against the number** (e.g. width 1.4 m → below the 1.85 m
standard), and compare the **main-corridor vs back-street pair**. That converts the gradient from
impression into a measured gap.

---

## B. WHAT TO ASK ON FIELD (intercepts) → quantitative anchor to triangulate
Pair each open question (see [interview-guide](../field/instruments/interview-guide.md)) with a
number we can cross-check the answers against.

| Field question theme | Triangulate against | Source | Tag |
|----------------------|---------------------|--------|-----|
| "Do you use the sidewalk / walk in the road?" | our own **counts** (sidewalk vs road) at that segment | observation | — |
| "What makes it (un)comfortable?" → shade/heat | THI threshold + our on-site temp reading | round-4 lead | ⚠ |
| Comfort vs tolerance | S1 found perception (84.7) > measured condition (64.3) — probe past "it's fine" | S1 | ✓ |
| Last-mile walk / ojol wait | TOD 400/800 m norm; observed ojol wait (cf. Rika/Mutia) | round-4 lead; S11 | ⚠/✓ |
| Crossing safety feeling | crossing spacing 100–200 m; 8.274 crossing crashes (2023) | S13; S14 | ✓ |
| Women's route choice day vs night | KRPA: streets = top harassment site; women 6× more vulnerable; 70,56% worsened | S2 | ✓ |
| Route knowledge before walking | (gap — no benchmark; this is the team's novel question) | — | — |
| Walking as a mode at all | <2% of commute trips are walk+cycle (Jabodetabek) | S7 | ✓ |

**Cross-validation logic:** if intercepts say "I walk in the road because of vendors," the
**counts + encroachment inventory** at that segment should corroborate it; if they don't, that's
a finding (perception ≠ behaviour), not an error.

---

## C. WHAT TO ASK ANIES BASWEDAN (policy expert) → with the numbers in hand
Obstacle-oriented (per mentor). Bring the figure so the question is grounded and specific.

| Ask | The number to anchor it | Source | Tag |
|-----|------------------------|--------|-----|
| What did the 2017–2022 program achieve, and what blocked *more*? | **134 km** revitalized 2017–19; **51 sites / Rp 327 bn** (2019); Sudirman–Thamrin **8–12 m** | S4 | ✓ |
| Why is city-wide sidewalk coverage still low? | **540 km** trotoar vs **6.956 km** road (≈7,8%, 2015) | S6 | ✓ |
| Did widening actually help walkability/ridership? | walkability **+38,98%**; PT users **+15,41%** (TJ Corr-1 24,87→28,70 jt/th) | S9 | ✓ |
| Pedestrian safety — was it a driver? | **8.274** pedestrian crossing-crashes 2023 (ID); 1 ped death/6 days (2014, DKI) | S14; S6 | ✓ |
| PKL decision: clearing the trotoar, moving them to side streets — obstacles? | vendors relocated "to side streets behind the towers" (2018) | S12 | ✓ |
| Why the gradient (wide main vs near-none behind)? | standard is **1,85 m min** everywhere — why unmet off-corridor? | S13 | ✓ |
| What's still unsolved, and what would you prioritize? | (open) | — | — |

---

## D. The triangulation map (how the three data streams check each other)
```
            PUBLISHED BENCHMARK (S13 standard, S6/S9 indices, S2/S14 stats)
                          ▲                     ▲
                          │ compare             │ compare
        OBSERVATION ──────┼─────────────────────┼────── INTERVIEW
        (counts, audit)   │   do they agree?    │   (intercepts + expert)
                          └─────────────────────┘
              agreement = robust finding · disagreement = a real insight to report
```

## E. Remaining quantitative gaps to close (desk or field)
- **⚠ Verify primaries:** Pusiknas pedestrian fatalities (10.428 / 54,84%); walking-speed review;
  thermal THI (Karyono); MRT/TJ 2024 ridership; HCM PLOS thresholds; TOD distance citation.
- **Pull Bina Marga Table 3** (exact dimension-by-flow) and any LOS/capacity table from the PDF.
- **No corridor-specific** number exists for: the back-street gradient (G1), Sudirman-area
  harassment (G8). These the **fieldwork generates** — and now has benchmarks to be measured
  against.
