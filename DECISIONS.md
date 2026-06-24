# Decision Log

**Append-only.** Add new decisions at the bottom. Never rewrite or delete past entries,
if a decision changes, add a *new* entry that supersedes the old one and note which one it
replaces. This is our shared memory of *why* the project is the way it is.

## Format

```
### YYYY-MM-DD: Short title
- **Decision:** What we decided.
- **Reasoning:** Why. What problem it solves or what it rules out.
- **Owner:** Who is accountable for it.
```

| Date | Decision | Reasoning | Owner |
|------|----------|-----------|-------|
| _example_ | _what we chose_ | _why_ | _name_ |

---

### 2026-06-15: Scope narrowed to the Sudirman corridor (named streets only)
- **Decision:** Scope is the **Sudirman corridor and its immediate back-streets**, referenced
  by **named streets only**. We dropped the earlier framing of "Jakarta Selatan" and the
  list of five station names.
- **Reasoning:** Mentor flagged "Jakarta Selatan" as far too broad to study meaningfully in
  the time we have, and a list of stations scatters our attention. The interesting, studyable
  phenomenon is the **contrast** between the wide, proper Sudirman trotoar and the
  near-nonexistent sidewalks one block behind it, the "gradient." A tight, named-street
  scope lets us actually observe both ends of that contrast.
- **Owner:** Team (scope agreed with mentor Kak Will Chris).

### 2026-06-15 · Mentoring outcome: fix confirmation bias in our method
- **Decision:** Overhaul how we ask questions and handle assumptions:
  1. **Split biased guiding questions into neutral, two-sided pairs.** Example: the leading
     "where do pedestrians walk in the road *despite* a good sidewalk" becomes (1) "How do
     pedestrians move through the Sudirman area?" and (2) "Do pedestrians use the sidewalks
     provided?"
  2. **Make assumptions explicit** in their own file (`engage/assumptions.md`) and keep them
     **out** of the guiding questions.
  3. **Add a comfort-factor question**, "what makes walking feel comfortable?", which we
     had wrongly omitted by assuming discomfort up front.
  4. **Reframe the expert interview around obstacles.** The interview with the former Jakarta
     governor (who ran the 2017–2022 sidewalk program) exists to surface the **obstacles that
     blocked comfortable pedestrian facilities**, not vague "cross-validation."
- **Reasoning:** Mentor flagged heavy confirmation bias, our questions pre-loaded the
  conclusion we wanted. Neutral, two-sided questions and explicit assumptions keep the
  fieldwork honest and let the data surprise us.
- **Owner:** Team.

### 2026-06-16: Field-research plan + instruments locked for the Wed–Fri window
- **Decision:** Run field research **Wed 17 / Thu 18 / Fri 19 June** on the locked Sudirman
  scope, using a fixed instrument set: segment **audit sheet (0–2)**, **observation tally sheet**
  (gradient pairs, 5-min counts), **intercept script**, and the **per-persona interview guide**.
  Resources/timing: weekday AM/PM peaks for commuters; **Thu-night women's intercepts led by
  Sintani** (Cikini–Benhil); **Fri 19** affinity mapping + hypothesis test + challenge refine.
  Expert track (Anies / Karsa City Lab / UDK) pursued via formal proposal + academy intro letter
  (**pending ADA confirmation**); request the letter H-1.
- **Reasoning:** Lock the method before the field so observation/interviews have clear objectives
  (per mentor). Instruments derive from the verified desk-research evidence (see
  `investigate/desk-research/`).
- **Owner:** Team (PIC per Confluence research plan).

### 2026-06-16 · Bias re-check: a leading question slipped back into Confluence
- **Decision:** The *Exploratory Cycle* doc reintroduced the rejected framing, *"…berjalan di
  badan jalan **meskipun** tersedia trotoar yang layak…"*. **Replace it everywhere** with the
  neutral split (how do people move? / do they use the sidewalk?) and keep the comfort question.
  De-biased versions now live in `engage/guiding-questions.md`, `report/main_id.tex` (BAB I), and
  `investigate/field/instruments/interview-guide.md`.
- **Reasoning:** The bias the mentor flagged on 15 Jun is recurring because it matches a team
  member's lived experience of central Jakarta; it must be actively guarded against, not assumed
  fixed.
- **Owner:** Team.

### 2026-06-16 · Merge colleague desk-research (branch `desk-research/seed-literature`)
- **Decision:** Cherry-pick the new research from the colleague branch into `main` rather than a
  raw `git merge` (the branch forked from the original scaffold and holds outdated README/
  DECISIONS/guiding-questions/main.tex, so a full merge would revert the evidence base, the
  cross-validation framework, the field-prep, and the stop-slop pass). Added: 5 source notes as
  **S15–S19** (Apritasari 2020, Afkara & Kusuma 2020, Arif & Yola 2021, Putri & Ellisa 2020,
  Napitupulu & Rudiarto 2025), their 5 BibTeX entries, and the literature-informed
  `pedestrian-interview-bank.md`. De-slopped + tagged + integrated into inventory, framework,
  and synthesis.
- **Reasoning:** Their work adds corridor user-satisfaction (S15), Jakarta-specific last-mile
  distances (S16), thermal/SVF (S17), informal-use framing (S18), and a recent Dukuh Atas study
  (S19); their Mulyadi 2022 note independently corroborates our S9.
- **Owner:** Team (sources by colleague; integration on main).

### 2026-06-19 · Field Day 1 done (Thu 18 Jun, daytime) + first-pass synthesis
- **Decision:** Field Day 1 ran **Thu 18 Jun ~10:00–15:00** (not the full Wed–Fri window).
  **16 people** engaged across two teams (~10 upper/middle, 6 bottom): 12 audio intercepts +
  Tim A/B notulen. Data filed under `investigate/field/transcripts/2026-06-18-*` and
  `investigate/field/data/respondents_2026-06-18.csv`; first-pass `investigate/synthesis.md`
  written (the synthesis hold is lifted as of today, 19 Jun).
- **Reasoning / key early signals (provisional):** (1) the **main trotoar is broadly judged
  good** ("lega/manusiawi/bagus") — this *contradicts* the old "walk in the road despite a good
  sidewalk" framing and validates the mentor's bias flag; (2) **heat is the dominant comfort
  complaint**, framed as a design failure (studi banding to 4-season countries); (3) **daytime
  feels safe** (a woman reports walking home safely at 01:00) but **night JPO/parking are
  hotspots** after ~22:00 — driven by *isolation in lit-but-empty* space, not darkness; (4)
  recurring **trotoar→zebra-cross ramp** hazard (a respondent's friend fell twice); (5)
  **ojol riding on the trotoar** + an inter-agency enforcement/security gap; (6) **ignored
  maintenance complaints** (open Q: does JAKI still work?).
- **Caveats logged:** the 1–10 scales in the profiles are mostly **interpreted from transcripts,
  not asked** — treated as provisional. Coverage was almost entirely the **main corridor**; the
  **gradient / back-streets (Q4, Assumption 2) remain untested.**
- **Owner:** Team.

### 2026-06-19 · Second field round scheduled (Sat night) to fill Day-1 gaps
- **Decision:** Run a **second round on Saturday night** (Day 1 was daytime only). Explicit
  objectives, not a repeat: (a) **sample the gradient** — pair each main-trotoar segment with the
  back-street one block behind and audit both; (b) **night safety** at the JPO/parking hotspots
  after 22:00, with **women-led intercepts** (Sintani, Cikini–Benhil) to test whether daytime
  "feels safe" holds for women at night; (c) **audit the ramp/zebra hazard**; (d) **5-min counts**
  across windows incl. night, joined to WeatherKit.
- **Reasoning:** Day 1 left the core scope contrast (the gradient) and the night/comfort/safety
  dimensions under-sampled; lock objectives before the field per mentor guidance.
- **Owner:** Team.

### 2026-06-19 · Anies expert track: secretary replied
- **Decision:** Anies Baswedan's secretary **replied on the morning of 19 Jun** to our proposal
  (`engage/proposal/`). Next step: finalise interview logistics and lock the **obstacle-oriented**
  question set (`engage/guiding-questions.md` §B), now armed with concrete Day-1 hooks (4-season
  "studi banding" critique, the ramp hazard, ojol-on-trotoar enforcement Dishub-vs-Satpol PP, the
  inter-agency security gap, ignored maintenance complaints).
- **Reasoning:** The interview's purpose is to surface the **obstacles** that blocked comfortable
  pedestrian facilities (per 15 Jun mentoring), and Day-1 evidence sharpens what to ask.
- **Owner:** Team. *(Reply content + accept/decline/next-ask to be recorded once shared.)*

### 2026-06-19 · Challenge statement refined after Field Day 1 (problem-level, no solutions)
- **Decision:** Refine the challenge from *"Make the walking experience in the Sudirman area more
  comfortable"* to: **EN** *"Make walking the Sudirman corridor comfortable and safe — through the
  heat of the day, into the night, and beyond the main trotoar to the streets one block behind
  it."* (ID equivalent in `engage/challenge-statement.md`). Status: **proposed, pending team
  confirmation** at the 4 PM session.
- **Reasoning (from `investigate/synthesis.md`):** (1) the old "more comfortable" implied fixing a
  bad sidewalk, but Day-1 data shows the **main trotoar is already judged good** — so the problem
  sits *on top of* a good sidewalk; (2) the **strongest barrier is thermal** (measured 33–35 °C
  feels-like, UV 7–8), held as the strongest signal, not the only one; (3) **"and safe" was added**
  because safety is real and **time-and-place specific** (safe by day, risky at lit-but-isolated
  spots after 22:00); (4) the **gradient** (locked scope) stays in view as the still-open question
  for Saturday.
- **Guardrail (per team direction):** the refined statement is **problem-level only** — no app,
  route, sensor, or feature named. Solutions wait for the *Act* stage, after the gradient/night
  data are in. Heat is not assumed to be the sole problem; keep the wording open to Saturday's data.
- **Owner:** Team.

### 2026-06-19 · BIG PIVOT — direction set toward a "Waze × JAKI" pedestrian reporting concept
- **Decision (team brainstorm; no transcript captured):** Move into a **solution direction**: a
  **report-while-you-walk** app that merges the **Waze** (live, map-based, crowd) and **JAKI**
  (civic complaint) concepts. The framing shift is toward **raising awareness** of pedestrian
  problems through easy in-situ reporting.
- **What prompted it:** verified that **JAKI is still in use but heavily backlogged**; a key cause
  is **duplicate/overlapping reports** — the same spot/problem reported many times by different
  people, which clogs triage.
- **Concept core:** reports are pinned **on a map**; co-located reports **cluster into one card/
  "folder"** showing **how many** reports exist at that spot. Tapping a cluster reveals **all the
  individual reports** there (photos, details) so duplicates collapse into one prioritisable item
  and **what to prioritise** becomes visible (more reports ⇒ higher signal).
- **Status / implications:** This crosses from *Investigate* into *Act*. It **supersedes the
  problem-level-only stance** of the prior entry **for the solution work**, BUT the research
  guardrail still holds for the **data**: Saturday's fieldwork must still *test* the underlying
  assumptions (do pedestrians want to report while walking? is awareness/backlog the real need?
  is duplicate-clustering JAKI's actual failure?) and not be bent to justify the app.
- **Unconfirmed (carry to next session):** whether the locked Sudirman/gradient scope still
  holds; how the formal *challenge statement* (problem) is reconciled with this *solution*;
  whether Saturday's plan/instruments change; relationship to JAKI (complement vs separate);
  privacy/moderation/spam handling.
- **Owner:** Team.

### 2026-06-20 · Anies (ABW) interview questions reworked: generative, non-leading, pivot-aligned
- **Decision:** Replace the Anies interview question set in
  `engage/proposal/lampiran-a-pertanyaan-wawancara.tex` and `engage/guiding-questions.md` §B with
  a **generative (Appreciative Inquiry)** set in four parts: (1) his pedestrian-space philosophy
  and vision; (2) a future "dream" for walking; (3) citizens as co-creators / "urun daya" (our
  project/pivot); (4) advice to young city-builders. Removed every critique-inviting prompt
  ("where did it break down," "what would you do differently," "what blocks citizen reports,"
  "what is still unsolved," "what made it hard to sustain") and every leading phrasing (naming
  "complete street" for him; the "thermal comfort vs aesthetics" contest; asserting the gradient
  as fact; asking him to endorse a "digital solution"). `proposal-anies.tex` left untouched (it
  may already be sent); its older challenge/scope wording is flagged for separate reconciliation.
- **Reasoning:** The prior set was anchored to a pre-fieldwork "obstacles to building sidewalks"
  framing that Day 1 undercut (the main trotoar is judged good), carried critique innuendo toward
  a guest we want to learn from and may partner with (Karsa City Lab), and missed the pivot. Deep
  research established that Anies built Jakarta's citizen-report-to-action backbone (Pergub
  128/2017 CRM; JAKI launched 2019; "Jakarta Kota Kolaborasi"), so he is the strongest source for
  the report→prioritise→fix pipeline behind our concept. Questions are now grounded in his own
  achievements and language (ruang ketiga; "kaki adalah alat transportasi"; ~341 km trotoar +
  200k+ trees; Jembatan Pinisi at Karet–Sudirman; JAKI's gold medal; urun daya; KCL's "policy
  must be felt by residents"). Coverage still serves the refined challenge (comfort, heat, night,
  gradient, for-whom) and the project (participation toward action), with no fabricated data and
  no leading.
- **Owner:** Team.

### 2026-06-20 · Anies questions tightened to research-grade (privileged-knowledge filter)
- **Decision:** Trim the generative Anies set from 13 to **9 research-grade questions**, each
  passing three tests: (1) **privileged** — answerable only by Anies, from decisions he made or
  things he saw inside government, not googleable and not gettable from a pedestrian; (2)
  **research-relevant** — it advances a specific question of ours (the gradient, heat, night, the
  report-to-action pipeline, why facilities get built and kept); (3) **neutral and generative** —
  no leading, no critique. Cut the public-vision/"dream" prompts (ten-year vision,
  vulnerable-groups future, urun-daya future) because his public statements already answer them
  and any urban expert could echo them. Files updated:
  `engage/proposal/lampiran-a-pertanyaan-wawancara.tex` (now 9 questions in three parts) and
  `engage/guiding-questions.md` §B.
- **Reasoning:** A team check asked whether the questions surface knowledge we cannot get from
  Google or ordinary interviews. Half the generative set did not. Time with a former governor
  should extract his tacit, behind-the-scenes reasoning — the prioritisation calculus behind the
  gradient, the real report triage, the design tradeoffs, the hard-won lessons — which is exactly
  what only he holds. Supersedes the question content of the earlier 2026-06-20 generative-rework
  entry; the generative/non-leading/no-critique principles from that entry still hold.
- **Owner:** Team.

### 2026-06-20 · Anies questions broadened to open/generative (funnel method)
- **Decision:** Recast the Anies set from the 9 direct "research-grade" questions to **7 broad,
  open, generative questions** (funnel method): open "what/how" prompts that invite his
  perspective, stories, and ideas, with the specific/privileged detail drawn out through neutral
  **live probes** rather than pointed questions on paper. Files: `lampiran-a-pertanyaan-wawancara.tex`
  (7 questions in three parts) and `guiding-questions.md` §B (questions plus a live-probing note).
- **Reasoning:** The direct set read as audit-like and leading ("how did your team actually decide
  which to act on first"), pinning him to specific decisions and implying scrutiny. Research on
  open, generative interviewing converges on broad, neutral, story-inviting openers that reduce
  bias and let the expert lead, with depth via follow-up probes: Appreciative Inquiry, Spradley's
  grand-tour questions, Vogt's "powerful questions," the funnel technique, episodic/narrative
  interviewing, and elite-interview practice. Supersedes the question content of the
  "research-grade" entry; the generative, non-leading, no-critique principles still hold.
- **Owner:** Team.

### 2026-06-23 · Anies questions finalised as a standalone doc; interview coordination pending
- **Decision:** The Anies question set is finalised as a clean, send-ready standalone document,
  `engage/proposal/pertanyaan-wawancara-anies.tex`: 10 open and generative questions in five themes
  (Jakarta dari masa ke masa; cerita Sudirman; ketertiban dan inklusivitas; data dan teknologi;
  refleksi dan keberlanjutan) plus a warm closing question. Plain, human Indonesian, active voice,
  no boilerplate, no LaTeX comments, `babel=indonesian`. Two older versions still disagree with it:
  `lampiran-a-pertanyaan-wawancara.tex` (7) and `guiding-questions.md` §B (7). Pick one canonical
  next session (recommend the 10) and retire or sync the rest.
- **Status:** Anies's secretary said the team **will be informed**; they are **trying to coordinate**
  the interview. No date yet. The question list is ready to send when asked.
- **Reasoning:** Several rounds of team feedback moved the questions from leading and critique-laden,
  to generative and appreciative, to broad and open (funnel), and finally to plain human phrasing fit
  to hand to the narasumber. See the 2026-06-20 entries for the method history.
- **Owner:** Team.

### 2026-06-24 · Scope tightened to the Dukuh Atas–Semanggi segment (pilot before scaling)
- **Decision:** Narrow the active study and design scope to the **Dukuh Atas to Semanggi** segment
  of the Sudirman corridor, as a first pilot stretch **before scaling up** to more of the corridor.
  This **refines, not replaces**, the 2026-06-15 scope (Sudirman corridor and its back-streets,
  named streets only); the **gradient** (the contrast between the main trotoar and the back-streets
  one block behind) within this segment stays the core research subject.
- **Reasoning:** A tighter, named segment is what the team can actually cover well on foot and on
  Saturday. Field Day 1 evidence already sits along this stretch (the media log runs Dukuh Atas at
  about −6.201 south to Setiabudi/Semanggi at about −6.223), so the personas and VPC are grounded in
  this exact segment. Tightening makes the still-unsampled back-street gradient smaller and reachable.
  "Before we scale up" keeps the door open to extend later without claiming corridor-wide coverage now.
- **Owner:** Team.

### 2026-06-24 · Act stage: personas + Value Proposition Canvas built from Day-1 evidence
- **Decision:** Produced the app's **user personas** and a **Value Proposition Canvas** in `act/`,
  grounded only in Field Day 1 respondents (no invented users). Key calls:
  1. **Three grounded personas** (`act/personas.md`): the commuter in a rush (primary), the unhurried
     well-being walker, and the corridor worker/observer. The **good-samaritan super-reporter** is
     kept as a clearly-labelled **hypothesis archetype**, not a grounded persona, because no such
     person was met in the field (validate Day-2 / Sat).
  2. **VPC** (`act/value-proposition-canvas.md`): the **Customer Profile** (jobs, pains, gains) is
     grounded and tagged to respondents; the **Value Map** (the report-while-you-walk concept) is the
     solution, and every item is a **bet to test**, not a commitment. Primary customer is the
     **commuter-as-pedestrian-reporter**; an **authority/city** canvas is included only as a flagged
     hypothesis to validate with Anies (no authority interviews exist yet).
  3. **Value rests on the evidenced JAKI gap** (no filter by status/location/type; the reporter never
     hears back), per the team's own competitor board. The earlier "JAKI is backlogged because of
     duplicates" premise is **not** leaned on; it is a Saturday hypothesis.
  4. **Safety is framed as environmental factors** (lighting, isolation, sightlines), never as a crime
     map or named offenders, consistent with the Day-1 finding that night risk is isolation, not a
     "dangerous area".
- **Reasoning:** Keeps the Act work honest and disconfirmable: the customer side is evidence, the
  solution side is explicitly bets that Saturday and Day-2 must test or kill. Artifacts also exported
  as Miro paste sheets (`*-miro.txt`) and a visual canvas (`value-proposition-canvas.html` plus two
  PNGs). Personas remain provisional pending team review.
- **Owner:** Team.
