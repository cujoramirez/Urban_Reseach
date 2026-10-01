# Data-Science Analysis Plan

> Purpose: turn Field Day 1 (and the Saturday round) into honest, defensible analysis across
> **three tracks — qualitative, quantitative, sentiment** — without manufacturing rigor.
> Companion to [`synthesis.md`](synthesis.md) and [`affinity-map_2026-06-19.html`](affinity-map_2026-06-19.html).

## 0. Golden rules (read first)
1. **Measured ≠ interpreted.** The 1–10 scores in `field/data/respondents_2026-06-18.csv`
   (`scale_source=interpreted`) were coded by us from transcripts. They are **descriptive leads,
   not measurements**, and must **never** feed an inferential test (t-test, p-value). Doing so
   fakes rigor and is exactly the bias we're guarding against.
2. **Descriptive ≠ causal.** Frequencies and means describe; they don't prove.
3. **Problem-level only.** No solution/app framing in the analysis. Solutions wait for *Act*.
4. State n and uncertainty everywhere. With n≈16 you can only see *large* effects.

## 1. Data inventory & status
| Dataset | File | Status | Good for |
|---|---|---|---|
| Verbatim transcripts (12) | `transcripts/2026-06-18-intercept-transcripts.md` | **Primary/measured** (text) | Qualitative + sentiment |
| Notulen (Tim A/B) | `transcripts/2026-06-18-respondent-profiles.md` | Mixed; some **stated** scales | Qual + a few quant points |
| Respondent scales (16) | `data/respondents_2026-06-18.csv` | Mostly **interpreted** | Descriptive only |
| Weather (6 readings) | `data/weather_2026-06-18.csv` | **Measured** | Quantitative (strong) |
| Media + GPS (105) | `photos/media-log_2026-06-18.csv` | **Measured** (metadata) | Mapping, evidence |
| 5-min counts | — | **Not yet collected** | Quantitative (Saturday) |

---

## 2. Qualitative track
- **Coding scheme:** tag each respondent turn with theme(s) — `heat`, `sidewalk_quality`,
  `safety_day`, `safety_night`, `crossing_ramp`, `ojol_trotoar`, `pkl`, `institutional_gap`,
  `maintenance`, `greenery` — and a role (`pain` / `goal` / `context`).
- **Output:** the affinity clusters (synthesis §"We found"); a frequency table (handout §3).
- **Rigor step (cheap, do it):** have **two coders** tag independently and report
  **Cohen's κ** on a sample of turns. κ>0.6 = acceptable agreement; documents that the themes
  aren't one person's projection. Record the codebook in a `coding_2026-06-18.csv`.

## 3. Quantitative track
### 3a. Now (descriptive only)
- **Weather:** session feels-like 33–35 °C, air 31–33 °C, UV 7–8, 0 mm, +3 °C above avg high.
- **Theme frequency:** heat 7/12, sidewalk-good 6/12, safe-by-day 6/12, night-risk 4/12, etc.
- **Interpreted scales by group** (⚠️ descriptive, interpreted, n small):

  | Group (n) | Comfort | Security | Heat-discomfort |
  |---|---|---|---|
  | Upper/middle (8) | 7.0 | 8.1 | 7.4 |
  | Worker/"bottom" (4) | 7.5 | 6.3 | 5.8 |
  | All (12) | 7.2 | 7.5 | 6.8 |

  Lead to test, **not** a finding: workers may rate **security lower** and **heat lower** than
  commuters (plausibly: they know the security gaps; they're acclimatised/under shelter).

### 3b. Saturday onward (inferential — on MEASURED data)
Collect **asked** 1–10 comfort & safety, an **ASHRAE thermal-sensation vote** (−3…+3), the
group/gender/time-of-day, and **5-min counts** joined to **WeatherKit** heat index. Then:

| Hypothesis | Test | Why this test |
|---|---|---|
| H1 Comfort/safety differ by group (class/gender/day-vs-night) | **Mann–Whitney U** (not t-test) | n small + ordinal Likert → non-normal; MWU is the honest default. Use Welch's t **only** if n grows and scores look ~continuous/normal. |
| H2 Comfort falls as heat index rises | **Spearman ρ**; then ordinal/logistic regression of vote on feels-like | Monotonic, robust to non-normal; regression quantifies the slope |
| H3 Pedestrian volume lower at higher heat | **Spearman ρ** (counts vs heat index); or compare time-window medians | Counts are counts; avoid assuming normality |
| H4 Rain raises sheltering/mode-shift | Compare rain vs dry windows (MWU / χ² on categorical) | Depends on getting a rain window Sat |

- **Power:** n≈16 is underpowered — detects only large effects; report effect sizes
  (rank-biserial for MWU, ρ for correlation) alongside any p-value, and treat p as provisional.
- **Multiple tests:** if running several, note it (Holm correction) — don't p-hack.
- **Tooling:** Python `pandas`+`scipy` (not in the current `.venv` — `pip install scipy pandas`),
  **or** a stdlib-only **permutation test** (no install needed) which is actually ideal for tiny n.
  I can write `analyze.py` to read the CSVs and run descriptives + MWU/permutation on demand.

## 4. Sentiment track
- **Unit:** per respondent × per theme (aspect-based), polarity ∈ {positive, negative, mixed}.
- **Method:** **human-coded is ground truth.** Indonesian here is colloquial and filler-heavy
  (*"eh", "kayak", "gitu"*) — off-the-shelf sentiment models are unreliable on it, so do **not**
  report an automated score as fact. If we use a model/lexicon, it's a *cross-check* against the
  human coding, and we report agreement, not the raw model output.
- **Output:** the sentiment-by-theme chart (handout §4): positive on sidewalk/greenery/day-safety,
  negative on heat / night-isolation / ramp / maintenance.
- **Link to quant:** aspect sentiment should track the interpreted scales (e.g. negative heat
  sentiment ↔ high heat-discomfort score) — a consistency check, not independent evidence.

## 5. Visualisation outputs
- Done: weather line, theme-frequency bars, by-group score table, sentiment-by-theme (handout).
- Next (need libs or the script): GPS track map over the Google Earth image (use
  `photos/media-points_2026-06-18.geojson`); comfort-vs-heat-index scatter (after Saturday);
  counts-by-time-window bars joined to heat index.

## 6. Reproducibility
- One coding CSV per session; raw transcripts/media never edited. Scripts read CSVs, write
  figures/tables — no hand-typed numbers in the report. Keep `scale_source` so interpreted vs
  stated is always visible.
