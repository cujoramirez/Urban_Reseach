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
  De-biased versions now live in `engage/guiding-questions.md`, `report/main.tex` (BAB I), and
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
