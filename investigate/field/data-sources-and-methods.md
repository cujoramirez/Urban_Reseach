# Data Sources & Extended Methods

What data we collect, where it comes from, who owns it, and how each stream cross-checks another.
Extends the [observation protocol](observation-protocol.md), [interview guide](instruments/interview-guide.md),
and the [audit](instruments/audit-sheet.md) + [tally](instruments/observation-tally-sheet.md) sheets.
For the CV/ML processing of these inputs, see
[`../desk-research/COMPUTATIONAL-DIRECTION.md`](../desk-research/COMPUTATIONAL-DIRECTION.md).

> **Discipline.** Every stream here is research evidence, not a feature. Weather data tests a
> question (*does weather change comfort and behaviour, and how*), it does not assume the answer.
> The rain-notification idea stays HELD in `../../act/solution-candidates.md`. Keep beliefs in
> `../../engage/assumptions.md`, out of the questions.

---

## Data streams

| Stream | What it gives | Source | Owner | Cross-check |
|--------|---------------|--------|-------|-------------|
| Weather (per observation window) | temp, humidity, precip probability, UV, condition | **Apple WeatherKit** (primary; same source the app would use) | Gading | on-site sensor + BMKG |
| Air quality | AQI / PM as a comfort-health factor | WeatherKit AQI where available, else IQAir/BMKG | Gading | on-site note |
| Land-surface temp / heat | where the corridor overheats | Landsat/Sentinel thermal bands | Gading (CV) | sensing walk |
| Building footprints + heights | shade layer (CoolWalks, S20) | OpenStreetMap + open DEM | Gading | street-view shadow |
| Sidewalk + crossing geometry | gradient + routable network | OSM tags + Tile2Net (S23) | Gading | field audit |
| Street imagery | streetscape features (S21, S22) | Google Street View Static API + aerial tiles | Gading | field audit |
| Walk times between points | distance/time context | Google Distance Matrix / Directions | Gading | observed walk time |
| Sensing walk | objective microclimate along the route | wearable temp/humidity/lux + GPS | Kenrich | WeatherKit |
| Pedestrian counts | objective flow by time/weather | CV detector + tracker on clips | Kenrich | hand counts |
| Go-along interviews | lived comfort, segment by segment | walk-with participant + GPS + audio | Sintani when sensitive | intercepts |
| Perception scales | comparable, validated ratings | ASHRAE thermal-comfort vote; perceived safety/comfort scale; NEWS items | whole team | observed behaviour |
| Sentiment / discourse | public talk on heat, flooding, walking | Maps reviews, X/TikTok geotag, nav-app complaints (NLP) | Gading | intercepts |

---

## Weather via Apple WeatherKit (primary)
- **Why WeatherKit:** the team are Apple developers, so research and any later app draw on one
  source; readings are consistent end to end. Log conditions live on iPhone/Apple Watch during
  each observation window.
- **Fields to log per window:** timestamp, temperature, apparent temperature, humidity,
  precipitation probability, precipitation intensity, UV index, condition code, wind.
- **Attribution:** Apple requires showing the Weather trademark + a legal-attribution link
  wherever WeatherKit data appears. Note this for any shared output.
- **Caveat (be honest):** WeatherKit historical/archive depth is limited. For backfilling past
  conditions or long time-series, keep **Open-Meteo** (free hourly history) as a fallback and
  **BMKG** as the official Indonesian cross-check. Record which source each row used.

## Sensing walk protocol (Kenrich)
Turns "comfort" into objective microclimate data along the exact walked route.
1. **Kit:** a small logger (temperature, humidity, lux) + GPS (phone or module), timestamped.
   Optional: heart rate / skin temperature for an exertion proxy.
2. **Route:** walk each paired segment (main corridor and its back-street) at the standard time
   windows (AM peak, midday heat, PM peak, after dark, weekend), at a steady pace.
3. **Logging:** sample every few seconds; tag the segment ID so readings join the audit + tally.
4. **Ground truth:** compare logger readings against WeatherKit at the same time/place; report
   the gap.
5. **Output:** a per-segment microclimate trace (temp/shade/lux) finer than any single weather
   station, feeding the shade/comfort layer and the THI check (>27 C uncomfortable).
6. **Safety/ethics:** same rules as fieldwork (buddy system, female-led sensitive/night, no
   identifying capture of bystanders).

## Validated perception scales (rigor)
- **Thermal comfort:** ASHRAE 7-point sensation vote (cold to hot) at the intercept point.
- **Perceived safety/comfort:** a short ordinal scale, day and night.
- **Environment:** a few NEWS (Neighborhood Environment Walkability Scale) items.
- Using published scales lets us compare across people and against the literature, instead of
  ad-hoc wording.

## How this strengthens the research (triangulation)
Three independent angles per claim: **objective** (sensors, CV, weather), **observed**
(counts, behaviour), **stated** (intercepts, scales). Agreement across angles makes a finding
robust; disagreement is itself a finding. This extends the table in
[`../desk-research/CROSS-VALIDATION-FRAMEWORK.md`](../desk-research/CROSS-VALIDATION-FRAMEWORK.md).

## Discipline reminders
- Log conditions even on comfortable days; absence of an effect is data.
- Sensor and API numbers need ground-truthing against each other.
- A weather-behaviour correlation is a hypothesis tested, not proof of a feature.
- Respect API terms (WeatherKit attribution; Google ToS; OSM licence). Note capture dates for
  imagery.
