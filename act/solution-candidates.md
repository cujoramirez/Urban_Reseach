# Solution Candidates

> ⏸️ **HELD, do not commit to a solution before the Friday, 19 June 2026 refinement.**
> Solutions must **follow the data**, not precede it. List ideas loosely if you must, but make
> no commitments until fieldwork and synthesis are done.

A candidate direction exists, **comfort-aware pedestrian navigation** (a native iOS app),
but it is *not* decided. It must earn its place from what the fieldwork shows, and may be
reshaped or replaced once the challenge statement is refined.

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
