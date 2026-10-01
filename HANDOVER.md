# Session Handover — 2026-06-23

## How to use this
At the start of the next session, read this, then DECISIONS.md (newest entries at the bottom),
investigate/synthesis.md, and CLAUDE.md. This is a research workspace; the app lives in a separate
repo. Dates are absolute.

## What the next session is for
Define the app's **user persona(s)** and a **Value Proposition Canvas (VPC)**, grounded in Field
Day 1 evidence. Build personas from real Day-1 respondents; do not invent users. Pair this with
writing the actual pivot concept into `act/`, which still holds an old placeholder.

## Where the project stands
- **Stage: Act.** Concept is a "Waze x JAKI" report-while-you-walk app: pedestrian problems pinned
  on a map, co-located reports cluster into one card with a count, tapping it opens all the reports
  there, duplicates collapse, and prioritisation becomes visible.
- **Field Day 1 done (Thu 18 Jun, daytime).** 16 people, mostly office commuters and transit
  last-mile users on the main Sudirman trotoar, plus workers (area and JPO security, MITJ staff,
  Satpol PP, a PKL, a GrabCar driver). Findings in synthesis.md: heat is the dominant comfort
  barrier (measured feels-like 33-35 C); daytime feels safe, night risk at the JPO and parking
  after about 22:00 is isolation rather than darkness; the kerb-to-zebra ramp hazard; ojol riding
  the trotoar; institutional and ignored-complaint gaps.
- **Primary user signal:** office workers and commuters moving through Sudirman in a rush, to and
  from public transit. Keep it general; the team sampled varied people.
- **Still untested:** the back-street gradient, night and women, rain. Saturday-night fieldwork was
  agreed but has not run yet.

## What the last sessions did (06-20, 06-22, 06-23)
- Finalised the Anies interview questions as a clean, send-ready standalone document:
  `engage/proposal/pertanyaan-wawancara-anies.tex`. Ten open, generative, non-leading questions in
  five themes plus a warm closing question. Plain human Indonesian, no boilerplate, no comments,
  `babel=indonesian`. Not compiled on Overleaf yet; give it one pass.
- Locked the method for expert questions: open and generative (funnel), broad on paper with depth
  drawn out by neutral live probes. No leading, no critique, no fishing for regret or
  self-comparison. Captured in memory and in `guiding-questions.md` §B.
- Anies coordination: the secretary said the team will be informed; they are trying to coordinate
  the interview. No date. Questions ready to send.

## Open items the next session inherits
1. **Canonical question file.** Three versions disagree: `pertanyaan-wawancara-anies.tex` (10,
   latest and cleanest), `lampiran-a-pertanyaan-wawancara.tex` (7), `guiding-questions.md` §B (7).
   Pick one (recommend the 10), retire or sync the others, decide whether it becomes Lampiran A and
   whether `proposal-anies.tex` points to it.
2. **`proposal-anies.tex`** still carries the old challenge ("Make the walking experience in Jakarta
   more comfortable") and old scope (Jakarta Selatan, a station list). Reconcile if it has not
   already been sent.
3. **`act/solution-candidates.md`** still holds the old "comfort-aware navigation" placeholder. The
   Waze x JAKI pivot concept has not been written there. The persona and VPC work should pair with
   writing the concept into `act/`.
4. **Pivot premise unverified.** "JAKI is backlogged, duplicates a key cause" came from a team
   brainstorm with no transcript. Public CRM data shows active follow-up at scale (185,852 reports
   in 2024). Verify before the VPC leans on it; keep Saturday able to disconfirm it.
5. **Saturday-night fieldwork** (gradient, night and women, rain, asked 1-10 plus an ASHRAE vote, a
   neutral reporting probe) still pending.
6. **Nothing is committed to git.** All work sits uncommitted on main.

## Next session plan: personas + VPC
- **Source evidence:** `investigate/field/transcripts/2026-06-18-respondent-profiles.md` and
  `2026-06-18-intercept-transcripts.md` (ground truth), `investigate/field/data/respondents_2026-06-18.csv`
  (scores, mostly interpreted), `synthesis.md` ("Who walks and why" and the findings), and
  `investigate/field/respondent-profile.md` (the fieldwork persona and quota doc).
- **Likely primary persona:** the office worker or commuter walking the Sudirman last-mile in a
  rush (heat, time pressure, meets problems worth reporting). Possible secondary personas: a worker
  who works the corridor; a woman at night (untested, flag as a hypothesis); elderly or disability
  for inclusivity.
- **VPC (Osterwalder):** for each persona, build the Customer Profile (jobs, pains, gains), then the
  Value Map (the app's products and services, pain relievers, gain creators). Every pain and gain
  must trace to a real Day-1 finding; mark anything speculative as a hypothesis to test on Saturday.
- **Two possible segments:** the pedestrian and reporter (primary), and the city or authority that
  acts on reports (the other side of the report-to-action loop). Decide whether the VPC covers one
  or both.
- **Where it lives:** `act/` (for example `act/personas.md` and `act/value-proposition-canvas.md`),
  alongside the pivot concept write-up.

## Guardrails (carry every session)
- No fabricated data. Personas come from real Day-1 respondents. The 1-10 scores are interpreted,
  not measured; no inferential stats on interpreted data.
- Problem stays distinct from solution. The challenge stays problem-level; the app lives in `act/`.
- Data integrity over solution. Do not bend the evidence or Saturday to justify the app; keep it
  able to disconfirm the pivot.
- Scope locked: the Sudirman corridor and its back-streets, named streets only.
- Keep questions neutral and two-sided; reject the "meskipun trotoar bagus" framing. Expert and
  outreach questions stay generative, open, and free of critique innuendo.
- DECISIONS.md is append-only; convert relative dates to absolute.
- Branding: independent team research ("Tim Riset Pijak"), Apple Developer Academy kept minimal;
  the team owns the IP.
- Raw media stays out of git.
- Writing: plain, human, active voice. No boilerplate, no AI tells, no em dashes. The team is strict
  on this.

## Pointers
- Decisions and why: DECISIONS.md (newest at the bottom).
- Evidence: investigate/synthesis.md; raw in investigate/field/.
- Anies questions: engage/proposal/pertanyaan-wawancara-anies.tex (the canonical candidate).
- Repo guide: CLAUDE.md. Memory index: the session's MEMORY context.
