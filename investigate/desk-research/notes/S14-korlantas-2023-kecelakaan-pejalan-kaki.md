# S14 — Pedestrian crash data 2023 (Korlantas Polri, via GoodStats)

## Full citation
GoodStats. (2024, 12 November). *Berbagai Jenis Kecelakaan Lalu Lintas yang Terjadi Sepanjang
Tahun 2023.* Figures attributed to **Korlantas Polri**.

- **URL:** https://goodstats.id/article/berbagai-jenis-kecelakaan-lalu-lintas-yang-terjadi-sepanjang-tahun-2023-9sxTj
- **Capture:** `sources/web-captures.md` → CAP-10
- **Primary:** Korlantas Polri / IRSMS 2023 (not pulled directly).
- **Source type:** Data journalism (secondary) citing police statistics.
- **Accessed:** 2026-06-16

## Scope
**CONTEXT — national.** Safety baseline for the crossing/road-stepping observation and the Anies
interview. Not corridor-specific.

## QUANTITATIVE findings
- **VERIFIED (fetched):** "Kecelakaan yang melibatkan pejalan kaki saat menyeberang … mencapai
  **8.274** di 2023" (Korlantas). Top crash types: loss-of-control 18,961; rear-end 18,638;
  head-on 17,337.
- **VERIFIED (Pusiknas Polri, via `curl -k` — see CAP-11):** "sebanyak **10.428 pejalan kaki
  menjadi korban**" in 2023 (Korlantas data); crossing at random places stated as the **top
  cause**; regional example Polda Jateng 2nd with 152 victims.
- **VERIFY ⚠ still:** the exact **54,84%** careless-crossing share was not found verbatim on the
  Pusiknas page (direction confirmed, exact figure not), and national death totals conflict across
  outlets (~18.357 vs ~27.000). Cite 10.428 + "crossing = top cause"; hold the percentage.

## Why it matters for fieldwork
- Backs the **crossing-behaviour observation**: if a large share of pedestrian crashes nationally
  involve crossing, our segment-level crossing audit (spacing, signals, jaywalking counts) is
  measuring a real safety lever.
- A concrete safety figure to put to the **policy expert** (the obstacle/road-safety angle).

## Flags
- The crossing-crash count (8,274) is verified; the headline "10,428 victims / 54.84% careless"
  is **provisional** — fetch the Pusiknas/Korlantas primary (SSL-blocked here) before reporting.
- Secondary source; for the report, cite Korlantas/IRSMS primary where possible.
