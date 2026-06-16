# Desk-Research Source Inventory

**Scope:** Sudirman corridor, Jakarta (Bundaran HI → Patung Pemuda Membangun / Bundaran
Senayan), pedestrian walking experience, trotoar condition, transit last-mile, the
2017–2022 sidewalk revitalization, and the contrast between the main Sudirman trotoar and the
degraded back-streets one block away.

**Last updated:** 2026-06-16
**Verification rule:** every figure below traces to a fetched URL + an exact quoted passage.
Files are in `sources/`; web-page provenance is in `sources/web-captures.md`; per-source notes
(Task 2) will be in `notes/`. Unverifiable items are logged as GAPS, never filled in.

**Data-type tags:** `QUANT` quantitative · `QUAL` qualitative · `SENT` sentiment/intent ·
`POLICY` policy.
**Origin tags:** academic · government · NGO/civil-society · news · org.
**Scope tags:** `CORRIDOR` (Sudirman/Thamrin specific) · `ADJACENT` (transit node on the
corridor) · `CONTEXT` (broader Jakarta / national, applies only as background).

---

## A. Collected & verified sources

| # | Source (short) | Type & year | Data types | Origin | Scope | File / capture | Verification |
|---|----------------|-------------|-----------|--------|-------|----------------|--------------|
| S1 | Dwisadana & Widjajanti, *Kajian Kualitas Jalur Pejalan Kaki Pasca Revitalisasi di Koridor Jalan Jenderal Sudirman DKI Jakarta*, Teknik PWK 13(1):21–35 | Journal article, 2024 | QUANT, QUAL | Academic (UNDIP) | **CORRIDOR** (Sudirman segment 4) | `sources/undip_sudirman_revitalisasi_2024.pdf` | Full text ✓ |
| S2 | Koalisi Ruang Publik Aman (KRPA), *Survei Pelecehan Seksual di Ruang Publik Selama Pandemi COVID-19* | Survey deck, 2022 | QUANT, SENT | NGO / civil society | **CONTEXT** (national, 34 prov.) | `sources/krpa_survei_2022.pdf` | Full deck ✓ (figures cross-checked against rendered slides 5–6) |
| S3 | Rakhmatulloh & Dewi, *Pengembangan Jalur Pejalan Kaki di Kawasan TOD Dukuh Atas Jakarta*, Jurnal Pengembangan Kota 8(2):132–141, DOI 10.14710/jpk.8.2.132-141 | Journal article, 2020 | QUANT | Academic (UNDIP) | **ADJACENT** (Dukuh Atas, north transit hub of corridor) | `sources/undip_tod_pedestrian.pdf` | Full text ✓ (detail extraction pending in Task 2) |
| S4 | Berita Jakarta / Dinas Bina Marga DKI, *Revitalisasi Trotoar Bangkitkan Budaya Berjalan Kaki* | News (official Pemprov), 18 Oct 2019 | QUANT, POLICY | Government / news | **CORRIDOR** (8–12 m width) + **CONTEXT** (134 km program) | `sources/web-captures.md` → CAP-1 | Page fetched ✓ |
| S5 | Citra Ridhani, *Walkability Index Jalur Pedestrian (Trotoar) di Poros Medan Merdeka-Thamrin-Sudirman Jakarta* (UGM S1 thesis) | Thesis, 2015 | QUANT | Academic (UGM) | **CORRIDOR** (Thamrin–Sudirman axis) | `sources/web-captures.md` → CAP-2 | Abstract/metadata only ⚠ (full text not downloadable), **pre-revitalization baseline** |
| S6 | ITDP Indonesia, *Panduan Desain Fasilitas Pejalan Kaki: DKI Jakarta 2017-2022* (v2.0) | Design guide, Sept 2019 | QUANT, POLICY | NGO advising gov (ITDP/Bina Marga) | **CORRIDOR** (standards) + **CONTEXT** (city data) | `sources/itdp_panduan_pejalan_kaki_jakarta_v2.pdf` + CAP-6 | Full text ✓ (68 pp) |
| S7 | GoodStats → BPS *Survei Komuter Jabodetabek 2023*, modal split | Data journalism, 19 Sep 2024 | QUANT | News/data (primary = BPS) | **CONTEXT** (Jabodetabek) | `sources/web-captures.md` → CAP-3 | Page fetched ✓; primary BPS not yet pulled ⚠ |
| S8 | Urun Daya Kota (UDK), Catatan Kota: *Membaca Rantai Mobilitas Perempuan di Kota* | Essay/article, date n/a | QUAL, SENT | NGO/org | **CONTEXT** (women's mobility, general) | `sources/web-captures.md` → CAP-4 | Existence + framing ✓; body/figures not retrieved ⚠ |
| S9 | Mulyadi, Sihombing, Hendrawan, Vitriana & Nugroho, *Walkability and importance assessment of pedestrian facilities on CBD in capital city of Indonesia*, Transp. Res. Interdiscip. Perspect. 16:100695 | Journal article, 2022 | QUANT, QUAL | Academic (BRIN/POLBAN/PUPR) | **CORRIDOR** (Sudirman–Thamrin CBD) | `sources/sciencedirect_cbd_walkability_road_diet.pdf` | Full text ✓ (via institutional access) |
| S10 | Kompas (Megapolitan), *Jakarta Darurat Parkir: Trotoar Dikuasai Kendaraan* | News, 12 May 2026 | QUAL, SENT | News | **CONTEXT** (city-wide) | `sources/web-captures.md` → CAP-7 | Page fetched ✓; no figures, not corridor-specific ⚠ |
| S11 | Kompas (Megapolitan), *Sulit Dapat Ojol, Warga Menumpuk di Luar Stasiun Sudirman* | News, 20 May 2025 | QUAL, SENT | News | **CORRIDOR-adjacent** (Stasiun Sudirman / Blora / Dukuh Atas) | `sources/web-captures.md` → CAP-8 | Page fetched ✓; named-pedestrian quotes; illustrative not representative ⚠ |
| S12 | Merdeka, *Anies: Trotoar Sudirman-Thamrin bukan tempat jualan PKL* | News, 6 Mar 2018 | POLICY, SENT | News (gov statement) | **CORRIDOR** | `sources/web-captures.md` → CAP-9 | Page fetched ✓ |
| S13 | Bina Marga / PUPR, *Pedoman Perencanaan Teknis Fasilitas Pejalan Kaki* No. 07/P/BM/2023 | National standard, 2023 | QUANT, POLICY | Government (PUPR) | **STANDARD** (benchmark) | `sources/binamarga_07_2023_pedoman_pejalan_kaki.pdf` | Full text ✓ (84 pp) |
| S14 | GoodStats → Korlantas, 2023 pedestrian crash data | Data journalism, 12 Nov 2024 | QUANT | News/data (primary = Korlantas) | **CONTEXT** (national safety) | `sources/web-captures.md` → CAP-10 | 8.274 crossing-crashes ✓; 10.428/54,84% VERIFY ⚠ |
| S15 | Apritasari, *User satisfaction on pathway & street furniture, Thamrin–Sudirman*, IJBESR 4(1):61–72 | Journal article, 2020 | QUAL, SENT | Academic (UMJ) | **CORRIDOR** (Thamrin–Sudirman) | `notes/S15-apritasari-2020-user-satisfaction-thamrin-sudirman.md` | Framing ✓; scores VERIFY ⚠ (garbled index) |
| S16 | Afkara & Kusuma, *Walking distance perception, Jakarta MRT station area*, ISTSDC 2019 (Atlantis) | Conf. paper, 2020 | QUANT | Academic | **CORRIDOR-relevant** (MRT last-mile) | `notes/S16-afkara-2020-walking-distance-mrt.md` | Thresholds ✓ (per authors): 629 m M / 593 m F; 689 office / 547 residential |
| S17 | Arif & Yola, *Sky View Factor & pedestrian thermal comfort, Jakarta sidewalk* (Springer LNCE) | Book chapter, 2021 | QUANT | Academic | **STANDARD-ish** (thermal/SVF) | `notes/S17-arif-2021-sky-view-factor-thermal.md` | Topic ✓; figures paywalled VERIFY ⚠ |
| S18 | Putri & Ellisa, *Reclaiming residual spaces beneath pedestrian bridges, Jakarta*, Evergreen 7(1):126–131 | Journal article, 2020 | QUAL | Academic (UI) | **CONTEXT** (informal use; JPO) | `notes/S18-putri-2020-residual-space-jpo.md` | 324 JPO (2015) ✓; case Lenteng Agung |
| S19 | Napitupulu & Rudiarto, *TOD impact on walkability: Dukuh Atas*, JPWK 21(1):113–129 | Journal article, 2025 | QUAL, QUANT | Academic (UNDIP) | **ADJACENT** (Dukuh Atas) | `notes/S19-napitupulu-2025-tod-dukuh-atas.md` | Full text (diamond OA) ✓; detail extraction pending |

> **Provenance:** S15–S19 + the literature-informed interview bank came from the colleague
> branch `desk-research/seed-literature` (cherry-picked into `main`, then de-slopped + tagged).
> Their independent note on Mulyadi et al. 2022 (= our **S9**) reports the same "~39% / ~15%"
> result, an independent corroboration of S9's verified 38,98% / 15,41%.

### Method / AI-CV-ML sources (how to research + build; see `COMPUTATIONAL-DIRECTION.md`)
These are method/tool sources for a data-science pathway, not Sudirman findings. Scope = METHOD.

| # | Source (short) | Type & year | Stream | File | Verification |
|---|----------------|-------------|--------|------|--------------|
| S20 | Wolf, Vierø & Szell, *CoolWalks*, Sci Rep 15:14911 | Journal, 2025 | shade-aware routing | `notes/S20-coolwalks-2025-shaded-routing.md` | Full text ✓ (arXiv/Sci Rep, OA) |
| S21 | *Comprehensive walkability assessment using big data + deep learning*, Sci Rep | Journal, 2024 | CV walkability from imagery | `notes/S21-naturesr-2024-walkability-deep-learning.md` | Method ✓ (OA); authors/figures VERIFY ⚠ |
| S22 | Saha et al., *Project Sidewalk*, CHI 2019 | Conf. + tool | CV + crowdsourced accessibility | `notes/S22-project-sidewalk-2019.md` | Tool/schema ✓; current stats VERIFY ⚠ |
| S23 | Hosseini et al., *Mapping the walk (Tile2Net)*, CEUS 101:101950 | Journal + OSS, 2023 | CV sidewalk-network mapping | `notes/S23-tile2net-2023-sidewalk-mapping.md` | Method + repo ✓ (open source) |
| S24 | *Pedestrian Route Choice Behaviors by ML*, IJGI 13(5):146 | Journal, 2024 | interpretable ML route choice | `notes/S24-mdpi-2024-route-choice-ml.md` | Exists/OA ✓; figures VERIFY ⚠ |

> **Direction:** S20–S24 underpin `COMPUTATIONAL-DIRECTION.md`, which maps the team's CV/AI
> (Gading) and robotics (Kenrich) skills to executable methods and a comfort-aware app, kept
> HELD until the Friday refinement. They build on S16's open question (model the pathway itself).

### Key verified figures (quick reference: see notes/ for exact passages)
- **S1 (CORRIDOR):** PEQI physical-condition score **64.28** (Class II, "sesuai sebagian besar
  standar desain"); PEQI pedestrian-perception score **84.70** (Class I, "optimal"); combined
  PEQI **74.49** → "dapat diterima pejalan kaki" (acceptable). Category physical scores,
  kelengkapan 61.4 / keselamatan 67.6 / kenyamanan 60.7. Lowest component scores (1/5): active
  building frontage, building block, pedestrian signals, trash bins. Persistent problems:
  motorbikes & street vendors (PKL) on the sidewalk (ineffective bollards), insufficient shade,
  missing pedestrian signals/medians at some crossings, motor-vehicle noise. Pedestrians on
  segment 4 dominated by male office workers aged 19–40; peaks 06:00–09:00 and 15:00–18:00 WIB.
- **S2 (CONTEXT, national):** 4,236 respondents / 34 provinces; 3,037 reported harassment;
  women 78.89%, men 29.6%, other genders 83.33%. Highest **offline** locations (multi-select
  counts): public streets **2,130**, residential areas 797, public transport 693, malls 432,
  workplace 377. *No Jakarta/Sudirman-specific breakdown in the deck.*
- **S4 (CORRIDOR + CONTEXT):** Sudirman–Thamrin trotoar widened to **8–12 m**, completed 2018;
  **134 km** of Jakarta sidewalk revitalized 2017–2019 (Dinas Bina Marga); 2019 = 51 sites,
  Rp 327 billion; 2020 target 47 km.
- **S5 (CORRIDOR, pre-2018 baseline):** GWI ranks Thamrin & Sudirman "pleasure to walk",
  Medan Merdeka "waiting to walk"; 25 pedestrian interviews, 9 parameters.
- **S6 (CONTEXT + standards):** "540 kilometer panjang trotoar DKI Jakarta 2015" vs "6956
  kilometer panjang jalan DKI Jakarta 2015" (Jakarta Dalam Angka 2016) → sidewalk ≈ 7.8% of
  road length (derived). "1 Pedestrian tewas tiap 6 hari di Jakarta" (Ditlantas Polda Metro
  Jaya 2014). QLUE #PedestrianFirst (Aug–Sep 2017): 643 sidewalk-violation complaints, Jakarta
  Barat highest (31%). Method uses 500 m transit buffers (TJ/KRL/MRT/LRT).
- **S7 (CONTEXT):** BPS Komuter Jabodetabek 2023, private vehicle 79.02% (going) / 77.93%
  (return); public transport 19.52% / 20.40%; walking+cycling "<2%". ~10% of Jakarta's
  population were commuters (2019).
- **S8 (CONTEXT, qualitative):** frames women's daily mobility chains and the need for safe,
  comfortable, inclusive urban space; **no statistics and not Sudirman-specific**, use as
  framing only.
- **S9 (CORRIDOR):** road-diet sidewalk revitalization raised GWI walkability **up to 38.98%**
  (Sudirman–Thamrin); post-revit five locations all "highly walkable" (WI 84.35–88.95) vs **2015
  baseline ~64 (Sudirman, "waiting to walk") / ~71 (Thamrin, "walkable")**. Public-transport
  users **+15.41%** (TJ Corridor 1: 24,870,678→28,703,262 pax/yr, 2017→2018). Main obstacles
  named: **sidewalk obstructions** and **sidewalk width**. **NOTE:** S9 corrects S5 (see §B/G3
  and the S5 note).

---

## B. Explicit GAPS: searched, NOT obtained/verified

> These are intentionally left empty rather than filled with unverified numbers.

| Gap | What was sought | Status / blocker | Why it matters |
|-----|-----------------|------------------|----------------|
| G1 | **The "gradient", degraded back-streets one block off Sudirman** | **STILL OPEN.** No source documents this contrast at street level. S6's city-wide 540/6,956 km is the closest proxy, but it is not a back-street measurement | The core research tension; the team's fieldwork fills it |
| G2 | Kompas.id: "**8,71% ruas jalan DKI bertrotoar**" + "revitalisasi trotoar baru **16%**" | Paywalled (HTTP 402). **Partly substituted:** S6 gives verified 540 km trotoar vs 6,956 km road (≈7.8%), same order of magnitude | "Wide Sudirman vs. little sidewalk elsewhere" contrast |
| G3 | ScienceDirect CBD walkability (road diet → walkability/PT ridership) | **FILLED → S9** (full text obtained 2026-06-16 via institutional access). Verified: walkability +38.98%, PT +15.41%. **Also corrected S5** (Sudirman 2015 ≈64 "waiting to walk", not "pleasure to walk") | Quantifies revitalization impact, now citable |
| G4 | **ITDP** design guide + any ITDP Sudirman assessment | **PARTLY FILLED** → S6 (design guide, full text). **Round 2 (2026-06-16): a Sudirman-specific ITDP assessment STILL NOT located**, search returned only academic PEQI/GWI papers already held | Standards (have) + corridor assessment (still want) |
| G5 | **UDK**, Catatan Kota, women's mobility chains | **PARTLY FILLED** → S8 (article existence + framing verified). Full body/figures + Sudirman specificity NOT retrieved | Women's lived-experience / mobility chains |
| G6 | **KCL/Dishub** ">40% sidewalks motor-dominated / 12% sanctioned" | **STILL OPEN, figure not cited.** Round 2: no Dishub primary found; KCL URLs still 404. **Theme** corroborated by S10 (Kompas 2026) + S1, but **not the number** | Sidewalk-occupation data |
| G7 | **BPS / Polri** pedestrian casualty & mobility statistics | **PARTLY FILLED** → casualty "1 killed/6 days" (Ditlantas Polda Metro Jaya 2014, via S6); modal split via S7. Primary Polri/BPS docs not pulled directly | Safety + mobility baseline |
| G8 | KRPA **Jakarta/Sudirman location breakdown** | **STILL OPEN.** S2 deck is national only | Corridor-specific harassment incidence unknown |
| G9 | Jabodetabek commuter / last-mile walking stats (BPS Komuter 2023 primary) | **FILLED (context)** → S7: walk+cycle <2% (BPS 2023). **Round 2:** official BPS *Statistik Transportasi DKI 2023* page found but **HTTP 403** (blocked); figure independently corroborated by a 2nd GoodStats article. Primary still un-fetched | Transit last-mile walking volumes |

---

## C. Leads worth chasing next (prioritized, after the 2026-06-16 gap-chase round)
1. **The gradient itself** (G1), the team's own fieldwork is the realistic source; no desk
   source measures the back-streets one block off Sudirman. Treat as the fieldwork's job.
2. **ScienceDirect CBD paper** (G3), obtain full text (institutional access) to verify the
   road-diet walkability figures before any use.
3. **KCL** (G6), find a working Karsa Insight article URL (site uses JS "Load more"); chase the
   underlying *Dishub DKI* sidewalk-occupation data the snippet referenced, directly.
4. **ITDP Sudirman-specific assessment** (G4 remainder), beyond the design guide, look for an
   ITDP PEQI/Complete-Street evaluation of the Sudirman corridor.
5. **Kompas.id contrast figures** (G2), still worth an open mirror, though S6's 540/6,956 km
   now covers the contrast at city scale.
6. **BPS Silastik primary** (S7 verify), pull the BPS Komuter 2023 microdata/report to confirm
   the modal-split figures directly.
7. **UDK full article** (G5 remainder), retrieve the body of *Membaca Rantai Mobilitas
   Perempuan* for any usable qualitative material.
