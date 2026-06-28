# Solution Candidates

> ⏸️ **HELD, do not commit to a solution before the Friday, 19 June 2026 refinement.**
> Solutions must **follow the data**, not precede it. List ideas loosely if you must, but make
> no commitments until fieldwork and synthesis are done.

A candidate direction exists, **comfort-aware pedestrian navigation** (a native iOS app),
but it is *not* decided. It must earn its place from what the fieldwork shows, and may be
reshaped or replaced once the challenge statement is refined.

> **Computational pathway:** the method route for this (CV to measure the gradient, a shade/
> comfort layer, interpretable ML, then a routable network for the app) is worked out in
> [`../investigate/desk-research/COMPUTATIONAL-DIRECTION.md`](../investigate/desk-research/COMPUTATIONAL-DIRECTION.md),
> grounded in S20–S24. Still HELD: the data leads, the method follows.

---

## Candidate ideas (parking lot: not decisions)
_(Add loose ideas here. Each must eventually point back to a real finding in
`../investigate/synthesis.md`.)_

- …

---

## Field data → possible app signal (HELD: a map, not a decision)
This shows how the data we are about to collect *could* feed a comfort-aware navigation idea, so
we collect the right things. It does **not** commit us to that idea. Every row needs a real
finding before it counts.

| Pain point we measure | Field data that captures it | Signal an app *could* use |
|-----------------------|-----------------------------|---------------------------|
| Heat / no shade | temp/THI per segment; longest unshaded gap; umbrella-sun + shade-hugging counts | shaded-route preference; "walk before 11:00 / after 16:00" timing hint |
| Rain | rain-shelter clustering; ojol mode-shift in rain; puddle/flood points | covered-route preference; shelter locations; "rain coming, nearest cover" |
| Obstructed/narrow sidewalk | effective width vs 1,85 m; encroachment inventory; road-stepping events | avoid-segment / effective-width-aware routing |
| Unsafe/awkward crossings | crossing spacing vs 100–200 m; jaywalking; warrant breach | safer-crossing routing; flag long gaps |
| Last-mile to transit | station→destination distance vs 400/800 m; ojol wait | last-mile walk/ojol guidance at nodes |
| Safety (esp. women, night) | route choice day vs night; lighting; harassment-prone spots (KRPA lens) | lit/peopled-route option for night |
| Route unknown before walking | "how do you know route condition?" answers | pre-trip route-condition info layer |

> **Discipline:** if the fieldwork shows a pain point is minor, its row dies. The data leads; the
> app follows. Revisit after the Friday refinement.

---

## Solution statement (Act-stage v2 — 2026-06-28, accessibility pivot)

> Working direction after fieldwork + mentoring (Kak Ica and Ci Jessi, 2026-06-26). The *statement*
> targets permanent mobility disability; the user base stays broad (curb-cut effect). Persona still
> thinly evidenced (see `personas.md` Persona 4) — a direction to validate, not a commitment.

**ID:** "Untuk **pengguna dengan disabilitas mobilitas permanen (mis. pengguna kursi roda) di kawasan
Dukuh Atas–Sudirman** yang **ingin bepergian secara mandiri tetapi tidak tahu tempat mana yang
benar-benar bisa diakses — ada ramp, toilet difabel, lift, dan kursi yang cukup**, aplikasi kami
**[Pijak]** menawarkan **peta fasilitas yang menunjukkan tingkat aksesibilitas tiap tempat (ramp,
toilet difabel, lift, ketersediaan & jarak antar-kursi) sebelum mereka berangkat.** Berbeda dengan
**Google/Apple Maps yang hanya tahu rute kendaraan dan tidak memberi tahu apakah suatu tempat ramah
kursi roda**, **[Pijak]** **memberi tahu kondisi aksesibilitas tiap lokasi lebih dulu — sehingga
pengguna bisa merencanakan perjalanan mandiri tanpa harus survei langsung.**"

**EN:** "For **people with permanent mobility disabilities (e.g. wheelchair users) around Dukuh
Atas–Sudirman** who **want to travel independently but can't tell which places are actually
accessible — ramps, accessible toilets, lifts, and enough seating**, our app **[Pijak]** offers **a
facility map that shows each place's accessibility before they set out.** Unlike **Google/Apple Maps,
which only know vehicle routes and never tell you if a place is wheelchair-friendly**, **[Pijak]**
**tells you each location's accessibility up front — so users can plan an independent trip without
surveying it in person.**"

- **[Pijak]** is a placeholder app name (team brand).
- Per the mentor, routing is at most a light **recommendation** ("to reach X, take this TJ, exit this
  door"), not turn-by-turn and not from-home.
- Broad user base (curb-cut): permanent → also benefits temporary (crutches), situational (stroller,
  luggage), and lansia.
