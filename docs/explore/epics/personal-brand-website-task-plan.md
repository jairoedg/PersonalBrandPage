# Task Generation Plan: Personal Brand Website

**Status**: Approved / Complete — Product Owner approval, 2026-10-02
**Date**: 2026-10-02
**Epic source**: [`personal-brand-website-epics.md`](personal-brand-website-epics.md)
**Product posture**: Lean MVP / experimental

## Task-generation rules

- Tasks are bounded delivery outcomes, not another architecture-analysis layer.
- No task selects a Deferred/Open decision by inference.
- Human semantic publication responsibilities are not automated.
- Test and DevOps gates are acceptance criteria within delivery tasks, not separate implementation programmes.
- Local generation and validation are the current MVP target; public production delivery remains conditional on DEC-005/DEC-006.
- Tasks may proceed in parallel where their actual dependencies permit; epochs are planning groupings only.

## Implementation-entry decision prerequisite

Before implementation-dependent tasks execute, Govern must resolve the minimum frontend/build stack and governed-file production representation required for implementation through the applicable approved decision process. The decision must preserve the frontend-only MVP boundary, DEC-002 governed-file direction, DEC-003 publication-safety boundaries, DEC-004 combined-delivery ownership, qualitative accessibility, maintainability/proportional simplicity, and no backend/API/database architecture unless an approved requirement or material risk changes the boundary.

## Shared Task Definition of Ready (DoR)

A task is ready to enter Govern/implementation only when, where applicable:

- approved inputs and dependencies are available;
- required frontend/build or governed-file production decisions have been resolved through the applicable approved gate;
- required human-governed content/input is available;
- no Deferred/Open decision needs to be inferred to start the task;
- acceptance criteria and relevant Test Strategy/DevOps gates are identifiable;
- unresolved dependencies have an owner and escalation condition.

## Shared Task Definition of Done (DoD)

A task is done only when, where applicable:

- its acceptance criteria pass;
- applicable Test Strategy and DevOps gates pass;
- required source/content/output traceability is preserved;
- mandatory publication-integrity and qualitative accessibility constraints remain satisfied;
- human semantic/Content Owner responsibilities remain human-governed;
- no unauthorized architecture or implementation decision was introduced;
- any remaining dependency is recorded with its owner and lifecycle destination.

Task-specific criteria below add to this shared baseline without selecting technology.

## EPIC-001 — Governed Content and Publication Safety

### PBW-T001 — Prepare representative governed content cases

**Outcome**: Representative Project, Project Story, Evidence, lifecycle, publication-classification, Contact/CV, and negative-case scenarios are available for local validation.

**Acceptance criteria**:

- Cases preserve A3 Project/Project Story/Evidence relationships.
- Positive and negative publication cases cover restricted, unclassified, incomplete, incorrectly related, and invalid-lifecycle content.
- Tigo/Avianca/DFA cases remain representative fixtures, not production content or approved public records.
- Fixtures are synthetic or appropriately anonymized and version-controlled.
- No governed-file format/schema is selected by this task.

**Dependencies**: A3, PRD R-002/R-003, HF-002 content dependency.

### PBW-T002 — Implement deterministic structural eligibility validation

**Outcome**: The implementation can deterministically validate machine-checkable publication eligibility before generation.

**Acceptance criteria**:

- Validates lifecycle, classification, references, Evidence sensitivity, relationship integrity, and required structural fields.
- Rejects the approved negative cases.
- Failed validation blocks generation and is not treated as successful eligibility.
- Does not judge Evidence adequacy, attribution, truthful wording, qualification, disclosure, or final publication approval.
- Tooling and enforcement stage remain dependent on the approved frontend/build/content representation.

**Dependencies**: PBW-T001; DEC-002/DEC-003; governed-file format/schema/tooling dependency.

### PBW-T003 — Implement the human publication-governance handoff

**Outcome**: The delivery flow records and respects the boundary between deterministic validation and human semantic/publication approval.

**Acceptance criteria**:

- Curation/Publication Governance remains the governance authority.
- Content Owner approval is required before generation for applicable content.
- Human review covers Evidence adequacy, attribution, truthful wording, narrative qualification, disclosure judgment, semantic publication suitability, and final Content Owner approval. Structural publication eligibility remains governed by deterministic validation.
- No automated task claims to replace human semantic judgment.
- A human disposition cannot waive mandatory publication-integrity or structural-eligibility requirements.

**Dependencies**: DEC-003/DEC-004; Part C Risk Register acceptance recorded; accepted residual-risk set empty where applicable.

### PBW-T004 — Verify publication-safety regression cases

**Outcome**: Structural and governance gates continue to protect public output as content cases evolve.

**Acceptance criteria**:

- Negative publication cases remain blocked.
- Approved eligible cases remain publishable through the local validation path.
- Restricted/internal Evidence cannot enter generated public assets.
- Validation results and human approval state remain traceable.

**Dependencies**: PBW-T001–T003; approved Test Strategy Gate A.

## EPIC-002 — Public Website Experience

### PBW-T005 — Assemble the approved eight-screen experience

**Outcome**: The local MVP presents Home, Projects, Project Story Detail, Contact, How I Can Help, Leadership, Career Journey, and About.

**Acceptance criteria**:

- No additional screen is introduced.
- Screen responsibilities match A10/PRD R-001/R-006.
- Project Stories consume only approved eligible public content.
- Frontend/build stack remains a decision dependency and is not selected by this task.

**Dependencies**: PBW-T001/T003; A10; B5/B6; implementation-entry decision prerequisite.

### PBW-T006 — Implement approved navigation and critical journeys

**Outcome**: The local MVP supports approved entry, skip, revisit, progressive disclosure, related-context, and direct Contact paths.

**Acceptance criteria**:

- Four approved journeys are represented:
  1. Home → Projects → Project Story Detail → Contact;
  2. Direct Contact/CV access;
  3. Supporting-context exploration;
  4. Project Story deep evaluation.
- No mandatory linear funnel is introduced.
- No search, filtering, personalization, chatbot, authentication, or governance UI is introduced.

**Dependencies**: PBW-T005; A10; implementation-entry decision prerequisite.

### PBW-T007 — Implement Contact/CV and external-destination readiness

**Outcome**: Contact, CV, LinkedIn, email, and phone actions are locally validated for the approved experience.

**Acceptance criteria**:

- Approved Contact methods are present and correctly linked.
- CV asset readiness is checked.
- External destinations are treated as links/downloads, not application APIs.
- Alternate approved Contact methods remain available where applicable.
- Final values/path remain governed content readiness dependencies, not invented by implementation.

**Dependencies**: PBW-T005/T006; HF-002 Contact/CV dependency; PRD R-005; implementation-entry decision prerequisite.

### PBW-T008 — Validate qualitative accessibility and responsive usability

**Outcome**: The local MVP meets approved qualitative accessibility and responsive-usability requirements.

**Acceptance criteria**:

- Semantic structure, meaningful headings/link purposes, keyboard navigation, visible focus, logical focus order, descriptive labels, and accessible disclosure behavior are validated.
- Automated checks are supplemented by targeted manual/exploratory validation.
- Responsive behavior is validated proportionately without selecting DEC-008A breakpoints.
- No formal conformance level is invented; DEC-008B remains Deferred/Open.

**Dependencies**: PBW-T005/T006; Test Strategy Gates C; DEC-008A/DEC-008B; implementation-entry decision prerequisite.

## EPIC-003 — MVP Generation, Preview, and Delivery Readiness

### PBW-T009 — Implement local generation/build readiness

**Outcome**: Approved eligible content can be transformed into locally generated website output.

**Acceptance criteria**:

- Generation consumes only content that passed structural and human governance boundaries.
- Generated output is traceable to validated source/content.
- Local validation is sufficient to demonstrate a working MVP path.
- Preview generation is not treated as publication authorization.
- Governed-file production format, schema, build mechanism, and frontend/build stack remain explicit decision dependencies.

**Dependencies**: PBW-T002/T003/T005; DEC-002/DEC-004; BLK-001 if physical mapping becomes necessary; implementation-entry decision prerequisite.

### PBW-T010 — Execute preview/readiness validation

**Outcome**: Generated local/preview output is evaluated against the approved Test Strategy gates.

**Acceptance criteria**:

- Four critical E2E journeys are validated selectively.
- Mandatory qualitative accessibility requirements pass.
- Compatibility/responsive, proportionate security, Contact/CV, and external-destination findings are evaluated.
- Findings are corrected or dispositioned only where the underlying requirement permits disposition.
- No disposition waives publication-integrity or mandatory accessibility requirements.

**Dependencies**: PBW-T008/T009; Test Strategy Gates B/C; no provider or staging environment assumed; implementation-entry decision prerequisite.

### PBW-T011 — Record release/publication authorization boundary

**Outcome**: The MVP delivery flow keeps human publication approval, generated output, preview/readiness, release authorization, and eventual publication distinct.

**Acceptance criteria**:

- Successful generation/preview does not authorize publication.
- Human semantic/publication approval occurs before generation.
- Release authorization remains a separate later gate.
- Traceability records are sufficient to connect approved content to generated output and any later publication outcome.
- DEC-006 trigger/release policy remains unresolved.

**Dependencies**: PBW-T003/T009/T010; DEC-005/DEC-006; BLK-001.

### PBW-T012 — Prepare eventual public-delivery decision gate

**Outcome**: The package identifies what must be decided before public production delivery without selecting an implementation.

**Acceptance criteria**:

- DEC-005 hosting/delivery operating model is explicitly required before production hosting selection.
- DEC-006 trigger/release policy is explicitly required before release automation or deployment mechanism selection.
- HTTPS remains mandatory for eventual public hosting.
- Rollback/recovery remains a capability requirement with no mechanism selected.
- DEC-007 measurement remains conditional.
- DEC-008A/DEC-008B and HF-002 dependencies remain carried forward.

**Dependencies**: Product Owner DEC-005/DEC-006 gates; BLK-001; Part C Risk Register acceptance recorded; accepted residual-risk set empty.

## Dependency and gate register

| Dependency/gate | Affected tasks | Treatment |
|---|---|---|
| DEC-005 hosting/delivery | PBW-T011/T012 | Decision dependency; do not select provider or topology |
| DEC-006 trigger/release | PBW-T011/T012 | Decision dependency; do not select release automation |
| DEC-007 measurement | PBW-T010/T012 | Conditional; no measurement implementation |
| DEC-008A breakpoints | PBW-T008 | Deferred/Open; validate responsive behavior without selecting breakpoints |
| DEC-008B conformance | PBW-T008 | Deferred/Open; qualitative accessibility remains mandatory |
| BLK-001 physical mapping | PBW-T009–T012 | SIGNIFICANT Deferred/Open; promote only if local/preview or later delivery cannot proceed coherently |
| Governed-file format/schema/tooling | PBW-T001/T002/T009 | Implementation decision dependency; do not infer |
| Frontend/build stack | PBW-T005/T006/T007/T008/T009/T010 | Implementation-entry decision prerequisite; do not infer |
| Contact/CV readiness | PBW-T001/T007/T010 | Governed content dependency |
| HF-002 provisional dependencies | PBW-T001/T007/T009–T012 | Track individually; none automatically a blocker |
| Part C Risk Register acceptance | Cross-epic | Part C risk acceptance recorded; accepted residual-risk set empty |

## Human task-generation checkpoint

No implementation tasks have been moved into Govern or assigned technology-specific task IDs. This task plan is ready for Product Owner review before Govern transition.
