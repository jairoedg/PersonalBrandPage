# Personal Brand Website — Explore Step 4 → Step 5 Architecture Handoff

**Purpose:** Give a fresh session a complete, authoritative handoff from the approved Explore Step 4 engagement into Step 5 Architecture, Strategy & Backlog without reconstructing decisions from conversation history.

**Created:** 2026-09-30  
**Explore Type:** ERC  
**Current status:** Explore Step 4 — PRD & Experience Design: **COMPLETE / APPROVED**  
**Step 5 status:** **Not started**  
**Authority:** Product Owner Jairo Enrique Diaz

---

## 1. Exact current lifecycle state

- Explore Step 1 — Explore Bundle: complete/approved.
- Explore Step 2 — Discovery: complete/approved.
- Explore Step 3 — Ideation: complete/approved; ID-9 approved three distinct concepts.
- Explore Step 4 — PRD & Experience Design: complete/approved.
- Explore Step 5 — Architecture, Strategy & Backlog: not started.
- Govern phase: not started.

The Product Owner approved SD-1 as “All good — proceed toward Step 5,” with SD-2 disposition **Accept as open questions**. This does not authorize Step 5 execution by itself; the new session must inspect Step 5 Gate-in and request explicit authorization before executing architecture work.

---

## 2. Canonical authority hierarchy

Use the repository artifacts directly. Do not reconstruct their content from conversation history.

| Authority | Artifact | Governs |
|---|---|---|
| A3 | `explore/explore-personal-brand-website/domain-analysis.md` | Canonical domain entities, relationships, rules, Evidence/publication, capabilities, mappings, narrative roles/themes, prominence, and lifecycles |
| Derived Step 4 domain input | `explore/domain/personal-brand-website-domain.md` | Locked routing/index input; A3 remains canonical if ambiguity/conflict exists |
| Approved PRD | `explore/prds/personal-brand-website-prd.md` | Approved product definition, R-XXX requirements, NFRs, exclusions, success criterion, constraints, and deferred questions |
| A10 | `explore/design/wireframes-personal-brand-website.md` | Approved eight-screen experience, hierarchy, flows, screen responsibilities, progressive disclosure, accessibility principles, and non-linear journey |
| B4 | `explore/design/ooux.md` | Approved 20-object semantic mapping: 5 Core, 15 Supporting, 0 Boundary; relationships, CTAs, state distinctions, and preservation boundaries |
| B5 | `explore/design/design-language.md` | Approved complete token specification; reserved-token boundaries; no-substitute `type/code` rule |
| B6 | `explore/design/design-system.md` | Approved six-page Figma structure, grids, token verification, and `type/code` accounting exception |
| Part C | `explore/explore-personal-brand-website/risks.md` | Canonical risk inputs, simulated validation, feasibility, lifecycle dispositions, SD-1/SD-2 record, and empty accepted-risk set |
| Architecture Context | `explore/explore-personal-brand-website/architecture-context.md` | Primary Step 5 architecture context: baseline, drivers, constraints, domain sketch, open questions, and A9 carried-forward risks |
| Explore Bundle | `explore/explore-personal-brand-website/explore-bundle.md` | Approved scope, assumptions, existing engagement risks, and source context |
| Technical Feasibility | `explore/explore-personal-brand-website/technical-feasibility.md` | A5 technical risks, constraints, unknowns, and feasibility guardrails |
| Context | `explore/explore-personal-brand-website/context.md` | Problem/context baseline, stakeholders, governance, and system boundary |
| Approved concepts | `explore/explore-personal-brand-website/ideation/personal-brand-website-refined-concepts.md` | Three distinct concept inputs and boundaries; no final direction selected |

A3 must not be superseded or reinterpreted by Step 5 architecture artifacts. Architecture artifacts may propose implementation structures but must preserve the canonical domain model.

---

## 3. Frozen decisions and non-reopenable boundaries

### Domain/content

- `Project` remains the factual/governed engagement record.
- `Project Story` remains a curated public narrative derived from a validated Project.
- Evidence/publication rules remain A3-governed.
- Internal/restricted Evidence is not automatically public.
- Capabilities remain the canonical business-problem-focused taxonomy.
- Preserve Capability-to-Project mappings and qualifications.
- Preserve the qualified Tigo → Avianca → DFA professional-evolution arc.
- Do not create new entities, relationships, capabilities, mappings, narrative roles, prominence decisions, rules, or lifecycle states by inference.

### Product/experience

- The MVP has exactly eight approved screens: Home, Projects, Project Story Detail, Contact, How I Can Help, Leadership, Career Journey, About.
- Preserve the approved A10 flows, progressive disclosure, scannability, non-linear exploration, accessibility principles, and Contact model.
- No runtime personalization, search/filter/sort/pagination, authentication, chatbot, backend form, runtime governance UI, or additional screens.
- Do not turn A10 navigation into domain relationships.
- Do not expose internal Project/Evidence governance.
- The five-minute objective applies to the overall experience, not per screen or forced consumption.

### Design pipeline

- B4 is approved: 5 Core / 15 Supporting / 0 Boundary; all 20 mapped objects remain unchanged.
- B5 is approved: complete token specification; reserved tokens do not create product behavior.
- B6 is approved: six canonical pages, three base grids, seven reference-frame types, and token accounting.
- `type/code` is not a physical Figma Text Style. B6 records 10 physical Text Styles + 1 approved documented `ui-monospace` representation exception, with zero unaccounted missing tokens. No substitute font or placeholder style may be selected.
- Administrative status caveat: the preserved `design-language.md` header may retain its earlier “Figma push pending” wording even though B5 was approved and the Figma push/audit completed. The Product Owner approval and this handoff control the lifecycle status; do not reopen B5 because of that stale header.
- Do not modify Figma design artifacts during Step 5 unless an authorized Step 5 activity requires it and the change is grounded in approved inputs.

### Hypothesis and validation

- A8 Hypothesis was intentionally excluded.
- Do not create, reconstruct, rename, or infer a replacement hypothesis.
- Part C simulated validation used approved outcomes, PRD criteria, A10 constraints, feasibility constraints, and AS-01, AS-02, AS-03, AS-04, AS-05, and AS-07.
- Those scenarios are analytical/simulated evidence only, not empirical validation.

---

## 4. Approved risks and dispositions entering Step 5

Existing risks must be consumed from canonical sources without arbitrary rescoring or status changes:

- Explore Bundle: R-01 through R-06.
- A5: TR-01/TR-04/TR-09, TR-02 through TR-08, and TI-01.
- A9 carried-forward risks: file-model feasibility; publication-control/build-boundary ownership; hosting/deployment complexity; analytics/privacy effects on the runtime boundary.

Part C dispositions:

- **Mitigate / carry forward:** downstream work is required; not completed Step 4 mitigation and not risk acceptance.
- **Monitor / validate later:** later evidence is required; not risk acceptance.
- **Accepted residual-risk set:** empty.
- `STEP4-R-01` Figma TextStyle mutation failure is a contained/resolved Step 4 tooling finding, historically preserved and not an open Step 5 product-readiness risk because no future approved activity currently depends on that MCP mutation.

Any new risk, changed score/status/mitigation, or claimed closure must cite a specific Step 5 finding and be presented for Product Owner review.

---

## 5. Open questions entering Step 5

These are intentionally unresolved questions carried forward from Step 4. Their lifecycle destination is distinguished below; they are not Step 4 defects.

### 5.1 Architecture / solutioning inputs

- frontend stack;
- content representation/CMS versus governed file-based approach;
- publication-control enforcement stage;
- curated-content/build/runtime boundary and ownership;
- hosting provider and operating model;
- deployment, rollback, preview, and release approach;
- architecture implications of analytics/privacy/consent/retention;
- implementation responsive breakpoints — B6 375/768/1440 values are Figma references only;
- formal accessibility conformance implications where architecture needs them;
- representative governed Project/Project Story content validation;
- how the frontend-only boundary satisfies approved requirements.

### 5.2 Later implementation/content inputs

- detailed P1 states/interactions where not required for architecture;
- final copy;
- Project Story preview ordering;
- exact disclosure mechanism;
- Related/Next links;
- final contact values and CV path.

### 5.3 Later validation / Evolve

- behavioral measurement baseline and empirical outcome validation requiring the running product;
- empirical recruiter behavior;
- empirical validation of the five-minute/six-question criterion;
- AS-01 — portfolio improves recruiter engagement versus the CV alone;
- AS-02 — target audience reviews the portfolio during candidate evaluation;
- AS-07 — the approved Recruiter Journey translates effectively into the live experience.

### 5.4 Other lifecycle destinations for active assumptions

- **AS-03** — assess career-material completeness and evidence defensibility during governed content preparation, Project/Project Story modeling, and publication readiness. Do not treat it as globally validated merely because the architecture is defined.
- **AS-04** — evaluate frontend-only MVP sufficiency during Step 5 architecture/solutioning against the approved PRD, constraints, and feasibility findings. Do not defer this architecture-fit question to Evolve.
- **AS-05** — preserve the approved foundations as the governing strategy baseline; review only if a concrete contradiction emerges during Step 5 or later work. It is not an empirical Evolve hypothesis.

Assumptions remain assumptions, especially AS-01, AS-02, AS-03, AS-04, AS-05, and AS-07. Do not promote them into requirements or validated facts.

**Lifecycle boundary:** Step 5 may define architecture/solutioning implications for measurement, content governance, and frontend-only feasibility where required, but it must not claim the post-launch behavioral baseline or empirical product-outcome validation that belongs later in Evolve.

---

## 6. Step 5 workflow sequence

### Gate-in

Verify PRD approval, architecture readiness, complete risk register, complete applicable experience design, and cross-referenced discovery/design artifacts.

### Part 1 — Architecture

Run `explore.proc.architecture-solutioning` through:

- B.0 Domain Onboarding — conditional; skip if a persistent domain profile exists.
- B.1 Context & Design Direction:
  - engagement setup;
  - boundary map and truth hierarchy;
  - design sketch;
  - calibration loop.
- B.2 Consolidated HLD Draft:
  - 14-section HLD;
  - PRD R-XXX/NFR-XXX cross-references;
  - ADRs for significant architecture decisions;
  - decision log and blocker register.
- B.3 Review & Hardening:
  - feedback integration if feedback exists;
  - cross-domain alignment if adjacent HLDs exist;
  - evidence escalation of ASM items;
  - BASE hardening plus applicable extended/domain categories.
- B.4 Finalization & Handoff:
  - simplification audit;
  - terminology/template/cross-reference validation;
  - backport findings;
  - final package;
  - ADR promotion from Proposed to Accepted.

Every B sub-step has a human gate: ARCH-B0, ARCH-B1a/B1b/B1c and B.1 gate, ARCH-B2/B.2 gate, ARCH-B3/B.3 gate, and ARCH-B4/B.4 gate.

### Part 2 — Test and DevOps Strategy

After architecture B.4 PASS or CONDITIONAL PASS, both are mandatory for ERC:

- `explore.proc.test-strategy` — standard 9-step process; output `explore/explore-personal-brand-website/test-strategy.md`.
- `explore.proc.define-devops-strategy` — standard 11-step process; output `explore/explore-personal-brand-website/devops-strategy.md`.

Cross-skill alignment must be checked against HLD and PRD.

### Part 3 — Epic Forming and Tasks

Not automatic. The steering team must explicitly trigger:

> “Let’s form epics from the personal-brand-website Explore outputs.”

Inputs include PRD, HLD, ADRs, Test Strategy, DevOps Strategy, personas/journeys/domain model, risks, and glossary. Epic/task artifacts must not be created before this trigger.

### Part 4 — Govern Readiness

Run the Govern Readiness checklist, close or explicitly defer gaps with owners, run consistency/glossary checks, and present the final handoff package. Govern phase transition remains a separate human decision.

---

## 7. Required Step 5 artifacts and paths

### Architecture package

- `explore/hlds/personal-brand-website-engagement-brief.md`
- `explore/hlds/personal-brand-website-boundary-map.md`
- `explore/hlds/personal-brand-website-truth-hierarchy.md`
- `explore/hlds/personal-brand-website-design-sketch.md`
- `explore/hlds/personal-brand-website-hld.md`
- `explore/hlds/personal-brand-website-decision-log.md`
- `explore/hlds/personal-brand-website-blocker-register.md`
- `explore/hlds/personal-brand-website-feedback-disposition.md` if feedback runs
- `explore/hlds/personal-brand-website-cross-domain-alignment.md` if adjacent HLDs exist
- `explore/hlds/personal-brand-website-backport-findings.md`
- `explore/decisions/personal-brand-website-adr-###-[name].md`

### Strategy artifacts

- `explore/explore-personal-brand-website/test-strategy.md`
- `explore/explore-personal-brand-website/devops-strategy.md`

### Backlog/govern artifacts

- `explore/epics/DFE-[EPIC-ID].md` after explicit epic-forming trigger;
- `explore/glossary.md` update through the prescribed glossary process;
- `discovery.md` status/index updates only when the workflow authorizes them.

No Step 5 artifact exists yet. The HLD and ADR directories currently contain only repository placeholders.

---

## 8. Installed/missing Step 5 skills at handoff creation

Installed during the authorized architecture-solutioning inspection:

- `explore.proc.architecture-solutioning@1.0.1`
- `explore.proc.boundary-mapping@0.1.2`
- `explore.proc.design-sketch@0.1.2`
- `explore.proc.hld-drafting@0.2.1`
- `explore.proc.feedback-integration@0.1.2`
- `explore.proc.socialization-handoff@0.1.2`
- `explore.util.decision-log@0.1.2`
- `explore.util.blocker-register@0.1.2`

Not installed and required later:

- `explore.proc.test-strategy@0.2.1` — mandatory Part 2 workflow;
- `explore.proc.define-devops-strategy@0.1.3` — mandatory Part 2 workflow;
- `explore.proc.extract-path-to-production@0.1.2` — listed in the Step 5 Loader Protocol;
- `explore.proc.domain-onboarding@0.1.2` — conditional B.0 skill; verify whether persistent profile exists;
- `explore.proc.cross-domain-alignment` — optional only if adjacent HLDs exist; registry lookup did not find it;
- epic-forming process — human-triggered inline process; no separate installed skill was identified.

Installation of any missing workflow skill requires explicit authorization before Step 5 execution.

---

## 9. Fresh-session operating instructions

A new session must:

1. Read this handoff completely.
2. Read the canonical artifacts directly; do not rely on conversation history.
3. Confirm the Step 5 Gate-in state only.
4. Report installed/missing skills and any blockers.
5. Ask for explicit authorization before installing missing Step 5 workflow skills or executing B.0.
6. Do not select a stack, CMS, hosting provider, deployment model, publication-control mechanism, analytics solution, accessibility standard, responsive implementation breakpoints, or any other deferred architecture decision without presenting options and obtaining the required human decision.

---

## 10. Review checklist for this handoff

- [x] Step 4 status and approvals recorded.
- [x] Authority hierarchy recorded.
- [x] A3/A10/B4/B5/B6 preservation boundaries recorded.
- [x] Part C risks, dispositions, and empty acceptance set recorded.
- [x] A8 exclusion and simulated-validation limitation recorded.
- [x] Step 5 open questions separated from actual Step 4 decisions.
- [x] Step 5 sequence, artifacts, gates, and dependencies recorded.
- [x] No Step 5 artifact or architecture decision created.

## 11. Product intent and success-criterion interpretation

The Personal Brand Website is one evidence-based professional portfolio that complements rather than replaces the CV. It is intended to help recruiters and hiring managers understand Jairo's delivery-leadership experience, comparable problems, business outcomes, leadership decisions, personal contribution, and professional evolution.
The approved overall product success criterion is the overall five-minute / six-question relevance-confidence objective.
It is not:
- a per-screen timer;
- a forced-consumption requirement;
- a one-minute target;
- a 30-second target;
- a “before scroll” requirement.
Validation method, behavioral baseline, measurement mechanism, and additional quantitative treatment remain intentionally unresolved downstream.
Authority: approved PRD; risks.md SD-2 Success-measure testability disposition.

## 12. Ideation concepts carried into architecture

The three approved Ideation concepts remain distinct product/design inputs at different conceptual levels. They are not separate PRDs, architecture domains, or a requirement that all three become separate technical mechanisms:
- Credible Story Layers — individual Project Story level: orientation, business context, outcome, Jairo's contribution, and progressively deeper publication-eligible evidence.
- Evidence Paths, Not Funnel — relationships among approved content that support visitor-selected exploration without mandatory sequencing or runtime recommendation.
- Capability and Growth Threads — collective portfolio/evolution level: capabilities supported by stories while preserving the qualified professional-evolution narrative.
Architecture must not convert these concepts into new A3 entities, relationships, services, APIs, databases, personalization mechanisms, or runtime recommendation behavior unless an approved requirement independently requires them.
Creative probe ≠ approved product direction. Earlier Ideation probes such as “first minute,” “before scroll,” or “30 seconds” were not approved as requirements or success criteria.

## 13. MVP proportionality / cost constraint

The Product Owner prefers a simple, reliable, maintainable and low-cost MVP solution.
This is a project constraint and architecture trade-off input, not a Dava.Flow requirement and not authority to weaken approved PRD/A3/A10 requirements.
Architecture should therefore challenge unjustified infrastructure, services, runtime complexity, operational overhead, or hosting cost. More complex options may still be proposed when an approved requirement, quality attribute, risk, or material trade-off justifies them.
Do not equate “low cost” with selecting a specific provider or technology before the relevant architecture gate.

## 14. Prior lifecycle provenance

personal-brand-discovery-to-ideation-handoff.md is supplied as historical lifecycle provenance for what approved Discovery handed into Ideation.
Use it to understand inherited constraints, exclusions, and decision history.
It does not override later approved canonical artifacts. Where it differs from a later approved A3, A10, Ideation, PRD, B4–B6, Part C, or Step 4 completion decision, the later approved canonical state governs.
Do not silently reconcile conflicts; identify them.

**Handoff status:** Ready for a fresh-session Step 5 Gate-in inspection. Not authorization to execute Step 5.
