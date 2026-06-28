# Place Accessibility Audit (per place)

A printable template for auditing **one destination** (café, mall, station, park, place of worship)
for **mobility accessibility**. Grounded in standards, not opinion — this is the answer to "is there
a standard?":

- **Permen PUPR No. 14/2017** — *Persyaratan Kemudahan Bangunan Gedung* (Indonesia's building-accessibility regulation).
- **UU No. 8/2016** — *Penyandang Disabilitas*.
- **ISO 21542:2021** — *Accessibility and usability of the built environment*.

Print one per place, or replicate into the audit CSV (see [`../data/README.md`](../data/README.md)).
**No invented data** — score only what you verify on site; use **N/A** where a criterion does not
apply; leave blank if unchecked. Always mark the **single biggest barrier** at the end.

## Place identification
- **Place ID:** ________ (e.g. `PL-DA-04`, matches [`dukuh-atas-place-shortlist.md`](dukuh-atas-place-shortlist.md))
- **Name / type:** ____________________  (café / mall / station / park / worship / …)
- **Date / time / auditor(s):** ____________________
- **GPS pin (lat, long):** ____________________
- **Photo reference(s):** ____________________

## Scoring
Score each **0–2**: **0 = absent / fails standard**, **1 = partial / borderline**, **2 = present /
meets standard**. **N/A** only where genuinely not applicable.

| # | Criterion | Standard to verify (don't guess) | 0 | 1 | 2 | Note / measure |
|---|-----------|----------------------------------|---|---|---|----------------|
| 1 | **Step-free approach** from nearest transit/drop-off | continuous path, no unavoidable steps | ☐ | ☐ | ☐ | from: ____ |
| 2 | **Step-free entrance OR ramp** | a ramp exists wherever there is a step | ☐ | ☐ | ☐ | |
| 3 | **Ramp slope** | ≤ **1:12 (~4.8°)** ISO 21542; ≤ 6–7° Permen PUPR. (2 = ≤1:12, 1 = 1:12–1:8, 0 = steeper / none) | ☐ | ☐ | ☐ | slope: ____ |
| 4 | **Entrance door clear width** + easy to open | ≥ **90 cm** clear; auto / light / wave-to-open best | ☐ | ☐ | ☐ | width: ___ cm |
| 5 | **Internal circulation width** | ≥ **120 cm** to pass; ~150 cm to turn | ☐ | ☐ | ☐ | width: ___ cm |
| 6 | **Lift** (if more than one floor is used) | cabin ≥ **110×140 cm**; controls reachable from a chair | ☐ | ☐ | ☐ | |
| 7 | **Accessible toilet** | grab bars + ~**150 cm** turning space + door ≥ 90 cm | ☐ | ☐ | ☐ | |
| 8 | **Seating / rest points** | benches present & frequent (Taman Situ Lembang ~**every 200 m** = the comfort benchmark) | ☐ | ☐ | ☐ | spacing: ___ m |
| 9 | **Accessible parking / drop-off** | marked accessible bay or safe step-free drop-off | ☐ | ☐ | ☐ | |
| 10 | **Guiding block / tactile paving** | continuous, unobstructed (low-vision) | ☐ | ☐ | ☐ | |
| 11 | **Accessibility signage / wayfinding** | clear and present | ☐ | ☐ | ☐ | |
| 12 | **Independent use (dignity test)** | can a wheelchair user enter & use this **without being carried or assisted**? | ☐ | ☐ | ☐ | |

### Barriers (circle all that apply)
unavoidable steps · steep/absent ramp · narrow/heavy door · narrow corridor · no lift ·
no accessible toilet · no seating · blocked tactile path · staff-carry required · other: __________

## Verdict
- **Overall:** ☐ Accessible   ☐ Partially accessible   ☐ Not accessible
- **Single biggest barrier:** ____________________
- **Independent for a wheelchair user?** ☐ Yes   ☐ With help   ☐ No
- **Why it works / fails** (write it the way @accessibility.leisure does — "accessible because A, B, C"): ____________________

## How this feeds the data
Each audited place becomes a **place record** in the accessibility dataset: `id`, `name`, `type`,
geometry, the 12 scores above, `overall` (accessible/partial/not), `biggest_barrier`,
`independent` (yes/help/no), `source: field`, `confidence: high`, photo refs. It extends the
facility-node schema in [`../../spatial/SCHEMA.md`](../../spatial/SCHEMA.md). The app shows
`overall` + the criteria so a user can decide **before** they go.

— Tim Riset Pijak
