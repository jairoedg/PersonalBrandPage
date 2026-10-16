# Personal Brand Website — Explore Step 5 to Govern Handoff

**Purpose:** Start a new chat focused only on the **Govern** stage, with the approved Explore Step 5 package carried forward without reopening already-approved decisions.

**Current lifecycle position:** Explore Step 5 — **Architecture, Strategy & Backlog: COMPLETE / APPROVED**. Govern Readiness: **READY**. Govern Step 1 has started; implementation has **not** started yet.

---

## 1. Executive Summary

Explore Step 5 is complete across all required parts:

- Architecture / HLD / ADRs — complete and approved.
- Test Strategy — complete and approved.
- DevOps Strategy — complete and approved.
- Epic Forming — complete and approved.
- Task Generation — complete and approved.
- Govern Readiness — complete and READY.

The approved delivery posture is a **Lean MVP / experimental** approach focused on reaching a locally generated and validated eight-screen website as quickly as possible while preserving non-negotiable publication integrity, qualitative accessibility, and the approved visitor journeys.

The project has now entered **Govern**. The first Govern work item must resolve the minimum implementation-entry decisions before implementation-dependent tasks can execute:

1. Frontend/build stack.
2. Governed-file production representation.

These two decisions must be resolved through the applicable Govern decision process; they must not be inferred silently.

---

## 2. Product / Architecture Context Carried Into Govern

### 2.1 Product boundary

The approved MVP is a **frontend-only public experience** with governed content preparation and generated public delivery.

The approved logical responsibility boundaries are:

1. Context Warehouse / Professional Knowledge.
2. Project Story Curation / Publication Governance.
3. Public Website Experience.

(Source: HLD, Architecture Approach / Component Breakdown; ADR-001)

### 2.2 Eight approved screens

The MVP contains exactly eight screens:

1. Home
2. Projects
3. Project Story Detail
4. Contact
5. How I Can Help
6. Leadership
7. Career Journey
8. About

(Source: PRD R-001/R-006; A10 Wireframing; EPIC-002)

### 2.3 Critical visitor journeys

The approved selective E2E journeys are:

1. Home → Projects → Project Story Detail → Contact
2. Direct Contact / CV access
3. Supporting-context exploration
4. Project Story deep evaluation

(Source: Test Strategy, E2E Testing; EPIC-002)

---

## 3. Approved Architecture Decisions

### DEC-001 — Logical responsibility boundaries

**Status:** Active / approved.

Preserve the three logical responsibility boundaries listed above. Physical topology remains unresolved.

(Source: Decision Log DEC-001; ADR-001)

### DEC-002 — Governed-file MVP content direction

**Status:** Active / approved.

Use a governed-file approach for the MVP rather than a managed CMS.

Still unresolved:
- production file representation;
- Markdown/structured metadata vs JSON/YAML;
- schema;
- repository/content structure;
- validation tooling;
- build mechanism.

(Source: Decision Log DEC-002; ADR-002)

### DEC-003 — Publication-safety control direction

**Status:** Active / approved.

Publication safety combines:

- human semantic governance; and
- deterministic structural eligibility validation before public generation.

Human semantic governance remains responsible for:
- Evidence adequacy;
- attribution;
- truthful wording;
- narrative qualification;
- disclosure judgment;
- semantic publication suitability;
- final Content Owner approval.

Deterministic validation remains responsible for machine-checkable structural eligibility.

(Source: Decision Log DEC-003; ADR-003)

### DEC-004 — Combined delivery responsibility

**Status:** Active / approved.

Curation / Publication Governance remains the logical governance authority.

A **combined delivery responsibility** owns:
- approved-content preparation;
- public generation.

Public Website Experience remains the visitor-facing presentation/navigation responsibility.

Physical realization remains unresolved.

(Source: Decision Log DEC-004; ADR-004)

---

## 4. Deferred / Open Architecture Decisions

The following remain intentionally unresolved and must not be inferred in Govern:

### DEC-005 — Hosting / delivery operating model
Unresolved:
- provider;
- operating model;
- production hosting;
- preview/deployment responsibility;
- rollback/reliability model.

### DEC-006 — Build/publication trigger and release policy
Unresolved:
- stage composition;
- trigger policy;
- release authorization mechanics;
- release automation.

### DEC-007 — Measurement
Unresolved / conditional:
- whether MVP measurement events are required;
- event set;
- analytics mechanism;
- privacy/consent;
- retention/deletion;
- ownership.

### DEC-008A — Responsive implementation breakpoints
Unresolved.
B6 widths remain design references only.

### DEC-008B — Formal accessibility conformance level
Unresolved.
Qualitative accessibility remains mandatory.

(Source: Decision Log DEC-005–DEC-008B; HLD Open Questions / Risks; DevOps Strategy Risks & Open Questions)

---

## 5. Significant Dependency

### BLK-001 — Residual physical / implementation mapping

**Status:** SIGNIFICANT / Deferred/Open.

DEC-004 resolved logical ownership, but the physical realization remains unresolved.

Do not infer:
- repository layout;
- service/module layout;
- deployment units;
- build runtime mapping;
- physical topology.

Promote to a blocker only if implementation cannot proceed coherently without resolving it.

(Source: Blocker Register BLK-001; HLD / B.3 hardening)

---

## 6. Architecture Package Completion

The architecture package completed:

- HLD Sections 1–14
- Boundary Map
- Truth Hierarchy
- Design Sketch
- Decision Log
- Blocker Register
- ADR-001 through ADR-004
- B.3 hardening
- B.4 finalization / handoff

**ARCH-B4 PASS** was recorded.

The accepted ADRs are:

- ADR-001 — Logical Responsibility Boundaries
- ADR-002 — Governed-File MVP Content Direction
- ADR-003 — Publication-Safety Control Direction
- ADR-004 — Combined Delivery Responsibility Direction

(Source: HLD; ADR-001–ADR-004; B.4 package validation)

---

## 7. Test Strategy — Approved Baseline

**Status:** Approved / Complete.

**Quality posture:** MVP / experimental.

Non-negotiable protection areas:

- publication integrity;
- qualitative accessibility;
- critical visitor journeys;
- Contact/CV behavior.

### Testing pyramid

1. Broad / fast structural and unit validation
2. Focused integration validation
3. Contract testing — not applicable unless a future approved API/event/service boundary exists
4. Small selective E2E set — four approved journeys

### Publication integrity

Structural validation must reject:
- restricted content;
- unclassified content;
- incomplete content;
- incorrectly related content;
- invalid-lifecycle content.

Human semantic governance cannot be replaced by automation.

### Tooling posture

No test framework or browser automation product is selected yet.

Tool selection remains deferred until the frontend/build stack exists.

(Source: Test Strategy, Overview; Testing Pyramid; Unit/Structural Testing; E2E Testing; CI/CD Integration)

---

## 8. DevOps Strategy — Approved Baseline

**Status:** Approved / Complete.

**Strategy profile:** Lean.

The approved logical pipeline is:

Source/content change
→ deterministic structural validation
→ focused validation
→ human semantic/publication approval
→ generation/build readiness
→ preview/readiness validation
→ separate release authorization
→ eventual publication
→ conditional post-release confidence

Important invariant:

**Successful generation or preview does not authorize publication.**

### Environment posture

Logical capabilities only:

- local development/validation;
- automated validation;
- preview/readiness;
- production/public delivery;
- conditional measurement.

No mandatory staging environment.

### Tooling / infrastructure posture

No selection yet for:
- CI/CD platform;
- build tool;
- hosting provider;
- deployment platform;
- rollback mechanism;
- monitoring product;
- branch model;
- runtime topology.

### DORA

DORA concepts are future operational signals only:
- deployment frequency;
- lead time for changes;
- change failure rate;
- recovery time.

They are not current targets and are separate from DEC-007 product analytics.

(Source: DevOps Strategy, CI/CD Pipeline Design; Environment Strategy; Release & Deployment Strategy; DORA Metrics)

---

## 9. Epic Forming — Approved / Complete

Three approved epics:

### EPIC-001 — Governed Content and Publication Safety

Outcome:
Approved public Project Stories and supporting content can be prepared safely without exposing restricted or ineligible material.

Included Explore task definitions:
- PBW-T001
- PBW-T002
- PBW-T003
- PBW-T004

(Source: DFE-EPIC-001)

### EPIC-002 — Public Website Experience

Outcome:
Visitors can use the approved eight-screen accessible, non-linear portfolio experience.

Included Explore task definitions:
- PBW-T005
- PBW-T006
- PBW-T007
- PBW-T008

(Source: DFE-EPIC-002)

### EPIC-003 — MVP Generation, Preview, and Delivery Readiness

Outcome:
Approved content can be generated locally, preview-validated, and eventually published through controlled gates.

Included Explore task definitions:
- PBW-T009
- PBW-T010
- PBW-T011
- PBW-T012

(Source: DFE-EPIC-003)

### Delivery epochs

1. Governed content foundation
2. Experience assembly
3. MVP validation and delivery readiness

These are planning groupings, not mandatory serial implementation phases.

(Source: Epic Forming artifact / Epic Index)

---

## 10. Task Generation — Approved / Complete

Twelve bounded Explore task definitions exist:

### EPIC-001
- PBW-T001 — Prepare representative governed content cases
- PBW-T002 — Implement deterministic structural eligibility validation
- PBW-T003 — Implement the human publication-governance handoff
- PBW-T004 — Verify publication-safety regression cases

### EPIC-002
- PBW-T005 — Assemble the approved eight-screen experience
- PBW-T006 — Implement approved navigation and critical journeys
- PBW-T007 — Implement Contact/CV and external-destination readiness
- PBW-T008 — Validate qualitative accessibility and responsive usability

### EPIC-003
- PBW-T009 — Implement local generation/build readiness
- PBW-T010 — Execute preview/readiness validation
- PBW-T011 — Record release/publication authorization boundary
- PBW-T012 — Prepare eventual public-delivery decision gate

(Source: Task Generation Plan)

---

## 11. Shared Task Definition of Ready / Definition of Done

### Shared DoR

A task is ready only when, where applicable:

- approved inputs/dependencies are available;
- required frontend/build or governed-file production decisions have been resolved;
- required human-governed content/input is available;
- no Deferred/Open decision needs to be inferred;
- acceptance criteria and relevant Test/DevOps gates are identifiable;
- unresolved dependencies have owner and escalation condition.

### Shared DoD

A task is done only when, where applicable:

- acceptance criteria pass;
- applicable Test Strategy and DevOps gates pass;
- required source/content/output traceability is preserved;
- mandatory publication integrity and qualitative accessibility remain satisfied;
- human semantic / Content Owner responsibilities remain human-governed;
- no unauthorized architecture/implementation decision was introduced;
- remaining dependencies are recorded with owner and lifecycle destination.

(Source: Task Generation Plan, Shared DoR / Shared DoD)

---

## 12. Implementation-Entry Decision Prerequisite

Before implementation-dependent tasks execute, Govern must resolve:

1. the minimum frontend/build stack;
2. the governed-file production representation.

This decision must preserve:

- frontend-only MVP boundary;
- DEC-002 governed-file direction;
- DEC-003 publication-safety boundaries;
- DEC-004 combined-delivery ownership;
- qualitative accessibility;
- maintainability / proportional simplicity;
- no backend/API/database architecture unless approved evidence changes the boundary.

(Source: Task Generation Plan, Implementation-entry decision prerequisite)

Affected implementation-dependent tasks include:

- PBW-T005
- PBW-T006
- PBW-T007
- PBW-T008
- PBW-T009
- PBW-T010

---

## 13. Product Owner Intent to Preserve in Govern

The Product Owner repeatedly established the following delivery intent:

- The immediate goal is to **see a working website**, not to continue expanding process unnecessarily.
- Quality posture is **MVP / experimental**.
- Simplicity is preferred over unnecessary architecture or tooling.
- Local generation/validation is the current MVP target.
- Production hosting and release decisions can remain later under DEC-005/DEC-006.
- No CMS is needed for the MVP unless future evidence materially changes the requirement.
- Content is expected to be relatively low-change; this is a Product Owner architecture input, not a contractual update-frequency requirement.
- No separate public-MVP runtime data-retention architecture is required.
- Measurement remains conditional under DEC-007.

(Source: Product Owner clarifications recorded in HLD / Decision Log / strategy artifacts)

---

## 14. Publication / Evidence Governance Rules to Preserve

Non-negotiable:

- restricted / ineligible content must never enter public generated assets;
- deterministic structural eligibility cannot replace human semantic governance;
- human semantic governance cannot waive mandatory structural eligibility;
- human publication approval occurs before generation;
- preview success is not publication authorization;
- release authorization is distinct;
- publication traceability must be preserved.

(Source: DEC-003 / ADR-003; Test Strategy; DevOps Strategy; Task Generation Plan)

---

## 15. Accessibility Rules to Preserve

Mandatory qualitative accessibility includes, where applicable:

- semantic structure;
- meaningful headings and link purposes;
- keyboard operation;
- visible focus;
- logical focus order;
- descriptive labels;
- accessible disclosure behavior;
- no essential meaning conveyed only through visual styling/icons.

Formal accessibility conformance level remains unresolved under DEC-008B.

Responsive implementation breakpoints remain unresolved under DEC-008A.

(Source: Test Strategy, Non-Functional Testing; PBW-T008)

---

## 16. Current Govern Entry State

Govern has started.

### Govern Step 1
**Complete.**

Govern configuration exists, but there are currently no stage-map bindings.

### Govern work discovery

Command executed:

`dft task next`

Result:

`No merge requests or tasks available.`

The approved Explore task definitions exist, but they have not yet transitioned into the Govern task workflow.

### Current blocker

Govern task creation is currently blocked by Context Warehouse configuration:

`dft task create` requires:

```toml
[project]
task_id_prefix = "..."
```

The current `config.toml` does not yet contain the required project task prefix.

### Product Owner prefix decision

Use:

```toml
[project]
task_id_prefix = "PBW"
```

Govern task IDs should therefore use:

- `PBW-0001`
- `PBW-0002`
- etc.

These are **Govern work-item IDs**.

The approved Explore task-definition IDs remain:

- `PBW-T001`
- ...
- `PBW-T012`

They must be cross-referenced rather than replaced.

(Source: Govern Step 1 work discovery; Product Owner decision in current chat)

---

## 17. Immediate Next Govern Action

Do **not** start implementation yet.

The next Govern action is:

1. update the required project task-ID prefix configuration to `PBW`;
2. run the prescribed config check;
3. create/import the first Govern planning work item;
4. use that work item to resolve the implementation-entry decisions;
5. stop at the applicable human gate before implementation.

The first Govern planning work item should resolve:

- frontend/build stack;
- governed-file production representation.

These two decisions should be evaluated together for compatibility but remain separately traceable.

Decision criteria:

- frontend-only;
- eight approved screens;
- A10 journeys;
- DEC-002;
- DEC-003;
- DEC-004;
- local generation/validation;
- qualitative accessibility;
- approved Test Strategy;
- approved DevOps Strategy;
- maintainability;
- proportional simplicity;
- no backend/API/database unless approved evidence requires it.

Do not resolve:
- DEC-005;
- DEC-006;
- DEC-007;
- DEC-008A;
- DEC-008B;
- production hosting/deployment.

---

## 18. Recommended Govern Working Principle

**Developers no longer write code manually.**

Developers orchestrate, review, and validate AI-generated code.

The Agentic IDE operates in Govern and should use the approved Explore context to implement bounded work rather than rediscovering product intent.

Preferred Agentic IDEs:
- Devin Desktop
- Codex

Do not use Devin Cloud.

(Source: Dava.Flow role guidance / Agentic IDE guidance)

---

## 19. What Govern Must Not Reopen Without New Evidence

Do not reopen by default:

- eight-screen MVP scope;
- R-001 through R-006;
- NFR-001 through NFR-007;
- DEC-001 through DEC-004;
- ADR-001 through ADR-004;
- Test Strategy;
- DevOps Strategy;
- three-epic decomposition;
- twelve Explore task definitions;
- frontend-only MVP boundary;
- publication governance model;
- qualitative accessibility requirement.

Reopen only if Govern produces new material evidence or a concrete blocker requiring the appropriate human gate.

---

## 20. Govern Chat Kickoff Prompt

Use the following as the opening instruction in the new Govern-focused chat:

> We are now in the **Govern** phase for the Personal Brand Website.
>
> Explore Step 5 is complete and Govern Readiness passed.
>
> The approved package includes the PRD, HLD, ADR-001 through ADR-004, Test Strategy, DevOps Strategy, EPIC-001 through EPIC-003, and PBW-T001 through PBW-T012.
>
> Preserve all approved Explore decisions and boundaries. Do not rediscover or redesign approved product intent unless new evidence requires the appropriate human gate.
>
> The immediate goal is to reach a locally running and validated eight-screen MVP as quickly as the approved Govern workflow permits.
>
> The first Govern planning work must resolve the implementation-entry prerequisite:
>
> 1. frontend/build stack;
> 2. governed-file production representation.
>
> Use proportional simplicity as the primary selection principle.
>
> Do not silently resolve DEC-005 through DEC-008B, BLK-001, hosting, deployment, analytics, breakpoints, or formal accessibility conformance.
>
> Govern task IDs use the `PBW-0001` style. Explore task definitions retain `PBW-T001` through `PBW-T012` and must remain traceable.
>
> Before implementation begins, create/claim the first Govern planning work item through the prescribed task workflow and stop at the required human gate before making the implementation-entry decision.
>
> Developers no longer write code manually. They orchestrate, review, and validate AI-generated code.

---

## 21. Final Handoff State

**Explore:** COMPLETE for the approved ERC scope.

**Step 5 — Architecture, Strategy & Backlog:** COMPLETE.

**Govern Readiness:** READY / PASS.

**Govern:** STARTED.

**Govern Step 1:** COMPLETE.

**Implementation:** NOT STARTED.

**Next action:** Configure `task_id_prefix = "PBW"` and establish the first Govern planning work item for the implementation-entry decision gate.
