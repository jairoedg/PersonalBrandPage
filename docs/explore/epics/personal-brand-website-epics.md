# Epic Forming: Personal Brand Website

**Status**: Approved / Complete — Product Owner approval, 2026-10-02
**Date**: 2026-10-02
**Source package**: Approved PRD, ARCH-B4 Part 1 Architecture package, Accepted ADRs, approved Test Strategy, approved DevOps Strategy
**Slug**: `personal-brand-website`

## Epic-forming principles

- Preserve PRD R-001 through R-006 and NFR-001 through NFR-007.
- Preserve the eight-screen A10 experience and approved journeys.
- Preserve A3 domain, Evidence, and publication boundaries.
- Treat DEC-001 through DEC-004 and ADR-001 through ADR-004 as approved constraints.
- Carry DEC-005 through DEC-008B and BLK-001 as explicit dependencies; do not resolve them by inference.
- Integrate Test Strategy and DevOps Strategy gates into epic acceptance criteria rather than creating technology/test-stage epics.
- Prefer the smallest coherent MVP epic structure and avoid implementation-technology epics.

## Proposed epic structure

### EPIC-001 — Governed Content and Publication Safety

**Outcome**: Approved public Project Stories and supporting content can be prepared safely from validated professional knowledge without exposing restricted or ineligible material.

**Scope**:

- Governed Project, Project Story, Evidence, classification, lifecycle, and reference handling.
- Project / Project Story separation and A3 relationship preservation.
- Content preparation and Contact/CV readiness.
- Support and enforce the governed publication lifecycle, including deterministic structural eligibility and the required human semantic/Content Owner approval boundary.
- Human-governed responsibilities: Evidence adequacy, attribution, truthful wording, narrative qualification, disclosure judgment, publication eligibility, and final Content Owner approval.
- Negative publication cases and HF-001 publication-integrity controls.

**Acceptance boundaries**:

- Structural validation cannot waive or replace human semantic governance.
- Human disposition cannot waive mandatory publication-integrity requirements.
- Restricted/unclassified/ineligible content cannot enter public generated assets.
- Exact governed-file format/schema/tooling remains unresolved under DEC-002.

**Dependencies**:

- A3 canonical domain and Evidence model.
- DEC-002, DEC-003, DEC-004 and ADR-002/003/004.
- Governed Project/Evidence contract remains provisional under HF-002.
- Contact/CV final readiness remains a downstream dependency.

**Owners**: Product Owner / Content Owner / Curation-Publication Governance; implementation ownership to be assigned without changing approved boundaries.

### EPIC-002 — Public Website Experience

**Outcome**: Visitors can use the approved eight-screen, accessible, non-linear portfolio experience to understand Jairo’s profile, evaluate Project Stories, and reach Contact/CV actions.

**Scope**:

- Home, Projects, Project Story Detail, Contact, How I Can Help, Leadership, Career Journey, and About.
- A10 entry, skip, revisit, progressive disclosure, related-context, and direct Contact paths.
- Four critical journeys from the approved Test Strategy.
- Qualitative accessibility across structural, component/integration, E2E, and manual/exploratory validation.
- Proportionate responsive/compatibility validation.
- Contact/CV and external-destination behavior.

**Acceptance boundaries**:

- No additional screens, runtime personalization, search/filtering, authentication, chatbot, governance UI, backend-dependent behavior, or real-time content are introduced.
- Formal accessibility conformance remains Deferred/Open under DEC-008B.
- Responsive implementation breakpoints remain Deferred/Open under DEC-008A.
- Frontend/build stack remains unresolved.

**Dependencies**:

- EPIC-001 approved eligible public content.
- A10 wireframes/flows and B5/B6 design-system artifacts.
- Contact/CV asset readiness remains provisional under HF-002.

**Owners**: Product Owner / design-system and frontend implementation owners to be assigned later.

### EPIC-003 — MVP Generation, Preview, and Delivery Readiness

**Outcome**: Approved content can be transformed into validated public output and eventually published through a controlled, traceable, proportionate delivery flow.

**Scope**:

- Combined delivery preparation and public generation under DEC-004.
- Local MVP generation/build validation and generation/build readiness.
- Preview/readiness validation using the approved Test Strategy gates.
- Selective E2E, accessibility, compatibility, security, Contact/CV, and external-destination checks.
- Human publication approval before generation and separate release authorization after preview/readiness validation.
- Future HTTPS public delivery and proportional post-release confidence.
- DevOps capability-level traceability from source/content through validation, approval, generated output, release authorization, and publication outcome.

**Acceptance boundaries**:

- Successful generation or preview does not authorize publication.
- No CI/CD platform, build tool, hosting provider, deployment mechanism, branch model, release automation, rollback mechanism, artifact registry, environment topology, or runtime topology is selected.
- DEC-005 hosting/delivery and DEC-006 trigger/release policy remain Deferred/Open.
- BLK-001 remains the residual physical/implementation-mapping dependency after DEC-004.
- Measurement and related testing remain conditional under DEC-007.
- Local validation and preview/readiness are sufficient for the current MVP target; eventual HTTPS public delivery remains conditional on DEC-005/DEC-006 and must not select hosting, deployment, release automation, or rollback mechanisms during Epic Forming.

**Owners**: Product Owner / Architect; later delivery and implementation owners to be assigned through approved downstream work.

## Cross-epic dependency order

```text
EPIC-001 Governed Content and Publication Safety
    → EPIC-002 Public Website Experience
    → EPIC-003 MVP Generation, Preview, and Delivery Readiness
```

The dependency order is logical, not a mandatory serial implementation plan. Work may proceed in parallel where approved content, design, or environment dependencies permit.

## Carried dependencies and decision points

| Item | Epic impact | Lifecycle treatment |
|---|---|---|
| DEC-005 hosting/delivery operating model | EPIC-003 eventual public delivery | Deferred/Open; Product Owner gate before provider/operating-model selection |
| DEC-006 trigger/release policy | EPIC-003 stage composition and release authorization | Deferred/Open; Product Owner gate before release-policy selection |
| DEC-007 measurement | EPIC-003 optional measurement readiness | Conditional; no analytics mechanism or test scope selected |
| DEC-008A breakpoints | EPIC-002 responsive implementation | Deferred/Open; downstream design/implementation |
| DEC-008B formal accessibility conformance | EPIC-002 formal validation | Deferred/Open; qualitative accessibility remains mandatory |
| BLK-001 physical/implementation mapping | EPIC-003 delivery realization | SIGNIFICANT Deferred/Open; do not infer topology |
| Governed-file format/schema/tooling | EPIC-001/003 content and generation | Deferred implementation decision under DEC-002 |
| Frontend/build stack | EPIC-002/003 implementation and tooling | Deferred implementation decision |
| Risk Register acceptance | Cross-epic delivery risk | Part C risk acceptance recorded; accepted residual-risk set empty |

## Proposed delivery epochs

| Epoch | Capability focus | Epics | Exit condition |
|---|---|---|---|
| Epoch 1 — Governed content foundation | Prepare governed content and publication-safety boundaries. | EPIC-001 | Eligible public content can be prepared and human-approved without exposing restricted/ineligible material. |
| Epoch 2 — Experience assembly | Assemble the approved eight-screen experience and critical journeys. | EPIC-002 | Approved experience behavior, qualitative accessibility, Contact/CV, and responsive expectations are ready for validation. |
| Epoch 3 — MVP validation and delivery readiness | Generate locally, validate preview/readiness, and preserve eventual publication gates. | EPIC-003 | Local MVP validation and preview/readiness pass; public delivery remains gated by DEC-005/DEC-006. |

Epochs are planning groupings, not implementation phases that select technology or require serial execution.

## Boundary validation

| Check | Result |
|---|---|
| Product/content governance versus visitor experience | PASS — EPIC-001 and EPIC-002 remain distinct. |
| Logical ownership versus physical realization | PASS — EPIC-003 carries physical mapping as open under BLK-001. |
| Publication approval versus generation/release | PASS — human approval precedes generation; release authorization remains separate. |
| Test/DevOps scope versus product epics | PASS — test and delivery gates are acceptance constraints, not technology epics. |
| PRD requirement coverage | PASS — R-001–R-006 map across EPIC-001–003. |
| NFR coverage | PASS — NFR-001–NFR-007 are carried as acceptance constraints or explicit downstream dependencies. |
| Deferred/Open transfer | PASS — DEC-005–DEC-008B, BLK-001, HF-002, and Part C risk acceptance recorded; accepted residual-risk set empty are explicit. |
| Technology inference | PASS — no framework, provider, CI/CD, schema, tooling, breakpoint, analytics, or topology is selected. |

## Epic index and links

- Epic proposal: [`personal-brand-website-epics.md`](personal-brand-website-epics.md)
- PRD: [`../prds/personal-brand-website-prd.md`](personal-brand-website-prd.md)
- HLD: [`../hlds/personal-brand-website-hld.md`](personal-brand-website-hld.md)
- Decision Log: [`../hlds/personal-brand-website-decision-log.md`](personal-brand-website-decision-log.md)
- Blocker Register: [`../hlds/personal-brand-website-blocker-register.md`](personal-brand-website-blocker-register.md)
- Test Strategy: [`../explore-personal-brand-website/test-strategy.md`](test-strategy.md)
- DevOps Strategy: [`../explore-personal-brand-website/devops-strategy.md`](devops-strategy.md)
- ADRs: [`../decisions/`](../decisions/)

## Exclusions from epic formation

The following are not separate epics because they are capabilities or constraints integrated into the three epics above:

- individual screens;
- individual NFRs;
- unit/integration/E2E test layers;
- CI/CD stages;
- hosting or provider setup;
- frontend framework selection;
- CMS/file-format selection;
- analytics implementation;
- accessibility conformance selection.

## Human checkpoint

No task breakdown, implementation plan, technology selection, or Part 3 execution has started. This proposed epic structure is ready for Product Owner review.
