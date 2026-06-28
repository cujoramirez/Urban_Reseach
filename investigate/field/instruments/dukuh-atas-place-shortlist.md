# Dukuh Atas — Place Audit Shortlist (accessibility pilot)

~14 real destinations around Dukuh Atas to audit with the
[place-accessibility-audit](place-accessibility-audit.md), chosen for variety — the transit
interchange + the "hangout / destination" types Kak Ica and @accessibility.leisure focus on.
Pulled from OSM (`../../spatial/data/dukuh_atas_places.csv`, **111 named places** — real names,
**no invented data**; regenerate with `python -m investigate.spatial.place_shortlist`).

**Place-ID convention:** `PL-DA-NN` (matches the audit sheet).

| ID | Place | Type | Lat, Long | Why include |
|----|-------|------|-----------|-------------|
| PL-DA-01 | MRT Dukuh Atas / Dukuh Atas BNI | station | -6.20080, 106.82279 | the interchange everyone arrives through — lift, platform gap, step-free transfer |
| PL-DA-02 | BNI City (KA Bandara) | station | -6.20159, 106.81972 | airport-rail entry; Kak Ica's "lift far from the platform" pain |
| PL-DA-03 | Sudirman (KRL) | station | -6.20241, 106.82345 | the KRL leg of the interchange |
| PL-DA-04 | Agora Mall | mall | -6.19837, 106.82139 | indoor destination — lift + accessible-toilet test |
| PL-DA-05 | Taman Dukuh Atas | park | -6.20092, 106.82274 | the "taman" use-case; seating + shade (the father's need) |
| PL-DA-06 | Taman Sumenep | park | -6.20127, 106.82655 | quieter park; bench spacing |
| PL-DA-07 | Dukuh Atas Skatepark / Riverview | park | -6.20387, 106.82283 | riverfront public space |
| PL-DA-08 | Toko Kopi Tuku — Dukuh Atas | café | -6.20210, 106.82246 | hangout café right at the MRT exit |
| PL-DA-09 | Starbucks | café | -6.20186, 106.82081 | chain café — entrance/toilet benchmark |
| PL-DA-10 | TOMORO Coffee — Wisma BumiPutera | café | -6.20743, 106.82331 | café inside an office tower (entrance + lift) |
| PL-DA-11 | Kopi Kenangan | café | -6.20538, 106.81744 | west-side café |
| PL-DA-12 | Tony Roma's | restaurant | -6.19899, 106.82267 | sit-down restaurant |
| PL-DA-13 | Pastis | restaurant | -6.20736, 106.82762 | south-east edge restaurant |
| PL-DA-14 | Masjid Jami Al-Falah | worship | -6.20075, 106.82398 | place of worship (ramp / wudu accessibility) |

**Coverage:** 3 transit · 1 mall · 3 parks · 4 cafés · 2 restaurants · 1 worship. The full
111-place list (hotels, more food/worship) is in the CSV if you want to swap any in.

**Tip:** audit the **interchange (PL-DA-01..03) first** — it's the access bottleneck every trip
passes through, and the strongest story for the concept test.

— Tim Riset Pijak
