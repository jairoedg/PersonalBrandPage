# Decision Log: HLD · Personal Brand Website

**Engagement start**: 2026-10-01
**Last updated**: 2026-10-01
**Total decision entries**: 9 (4 active directional; 5 deferred/open)
**Architect**: Devin
**Slug**: `personal-brand-website`

This decision log is active for B.1–B.4. It records approved directional decisions, considered alternatives, and explicit deferrals so the full architecture decision landscape remains auditable. Deferred/open entries are not selections. Governed files are the approved MVP content-representation direction, and a managed CMS is not selected for the MVP. Markdown/structured metadata versus JSON/YAML remains unresolved. Production schema, repository/content structure, approved content contract, validation tooling, build mechanism, frontend technology, and physical topology remain unresolved. No publication-control enforcement stage/mechanism, hosting/deployment model, analytics architecture, responsive breakpoint set, or formal accessibility conformance level has been selected.

---

## Decision Index

| # | Date | Step | Decision | Driver | Status |
|---|---|---|---|---|---|
| DEC-001 | 2026-10-01 | B.1.3.1 | Option A — preserve three logical bounded contexts as the working boundary direction | Product Owner decision | Active |
| DEC-002 | 2026-10-01 | B.1.3.6 | Governed-file direction for MVP content representation | Product Owner decision | Active |
| DEC-003 | 2026-10-01 | B.1.3.6 | Human semantic governance plus deterministic structural eligibility validation | Product Owner decision | Active |
| DEC-004 | 2026-10-01 | B.2 formalization | Combined delivery responsibility direction | Product Owner decision | Active |
| DEC-005 | 2026-10-01 | B.1.3.6 | Hosting and delivery operating model | Product Owner decision | Deferred / Open |
| DEC-006 | 2026-10-01 | B.1.3.6 | Build/publication trigger and release policy | Product Owner decision | Deferred / Open |
| DEC-007 | 2026-10-01 | B.1.3.6 | MVP measurement requirement and mechanism | Product Owner decision | Deferred / Open |
| DEC-008A | 2026-10-01 | B.1.3.6 | Responsive implementation breakpoints | Product Owner decision | Deferred / Open |
| DEC-008B | 2026-10-01 | B.1.3.6 | Formal accessibility conformance level | Product Owner decision | Deferred / Open |

---

## Decision Details

### DEC-001: Working logical-boundary direction

- **Date**: 2026-10-01
- **Step**: B.1.3.1 — Propose Service Boundary
- **Driver**: Product Owner decision
- **Decision**: Use Option A as the working B.1.3 boundary direction: preserve Context Warehouse / Professional Knowledge, Project Story Curation / Publication Governance, and Public Website Experience as logical ownership/responsibility boundaries.
- **Rationale**: Preserves the approved boundary map while avoiding premature physical topology selection. B.1.3 must resolve the design direction to the extent required for an approved sketch; B.2 will formalize that approved direction rather than discover or silently select the architecture.
- **Alternatives not selected / retained for comparison**:
  - Option B — retained as a later topology candidate only if subsequent analysis demonstrates that combining delivery concerns preserves publication safety and ownership while reducing justified MVP complexity.
  - Option C — retained as a comparison/reference alternative; physical separation and contract/operational complexity require a concrete approved requirement or identified risk.
- **Evidence level**: [VALIDATED]
- **Impact**: Guides module mapping while preserving all physical architecture questions as open. Does not select separate services, modules, repositories, deployment units, CMS/file approach, build mechanism, or runtime topology.
- **Status**: Active

---

### DEC-002: Governed-file direction for MVP content representation

- **Date**: 2026-10-01
- **Step**: B.1.3.6 — Architectural Decision Points
- **Driver**: Product Owner decision
- **Decision**: Use a governed-file approach for the MVP rather than introducing a managed CMS.
- **Rationale**: Representative Tigo, Avianca, and DFA validation demonstrated that both governed-file candidates can preserve the required logical model and structural publication controls. No approved requirement or material risk currently justifies CMS complexity.
- **Alternatives rejected**:
  - Managed CMS — not justified by the current approved requirements or demonstrated feasibility risk; remains available only if later evidence shows governed files cannot satisfy an approved requirement or material risk.
  - Markdown/structured metadata versus JSON/YAML — not selected at this gate.
- **Evidence level**: [VALIDATED]
- **Impact**: Establishes only the governed-file direction. Production format, schema, repository structure, content contract, validation tooling, build mechanism, frontend technology, and physical topology remain unresolved.
- **Status**: Active

---

### DEC-003: Publication-safety control direction

- **Date**: 2026-10-01
- **Step**: B.1.3.6 — Architectural Decision Points
- **Driver**: Product Owner decision
- **Decision**: Publication safety must combine human semantic governance with deterministic structural eligibility validation before public generation.
- **Rationale**: Representative validation demonstrated that structural checks can reject restricted, unclassified, incomplete, incorrectly related, and invalid-lifecycle content, while Evidence adequacy, attribution, truthful wording, narrative qualification, disclosure judgment, and final Content Owner approval remain human responsibilities.
- **Alternatives rejected**:
  - Deterministic validation as a substitute for semantic governance — rejected because structural checks cannot independently judge semantic truthfulness or Evidence adequacy without a later approved machine-readable constraint that genuinely makes a check deterministic.
  - Human semantic governance without structural validation — rejected as incomplete for the demonstrated publication-safety risks.
- **Evidence level**: [VALIDATED]
- **Impact**: Establishes the control direction only. Content-preparation, pre-build, build, deployment/release, and combined enforcement stages/mechanisms remain unresolved. No schema, contract, tooling, service, event, or build mechanism is selected.
- **Status**: Active

---

### DEC-004: Combined delivery responsibility direction

- **Date**: 2026-10-01
- **Step**: B.2 formalization
- **Driver**: Product Owner decision
- **Decision**: Approve Option B — a combined delivery responsibility owns approved-content preparation and public generation, while Project Story Curation / Publication Governance remains the logical governance authority and Public Website Experience remains the visitor-facing presentation/navigation responsibility.
- **Rationale**: Provides proportionate MVP simplicity without weakening human semantic governance, publication eligibility, Evidence boundaries, or the approved logical bounded contexts.
- **Boundaries**:
  - Curation retains Project Story governance, Evidence adequacy and attribution judgment, publication classification, disclosure judgment, publication eligibility, and final Content Owner approval.
  - Combined delivery consumes only content that has passed the applicable governance/eligibility boundary and prepares it for generation and produces public website assets.
  - Public Website Experience does not acquire Project validation, Evidence assessment, publication approval, or internal governance responsibilities.
- **Alternatives not selected**:
  - Separate curation and build responsibilities — retained for reconsideration only if evidence demonstrates a concrete need.
  - Shared responsibility with an explicit ownership contract — not selected at this gate.
- **Evidence level**: [VALIDATED]
- **Impact**: Establishes bounded ownership direction only. It does not select one repository, deployment unit, process, physical service, production schema, content format, validation tooling, build tool, hosting provider, deployment platform, trigger/release policy, runtime topology, API/event architecture, or analytics architecture.
- **Disposition**: Active directional decision; remaining physical/implementation mapping is Deferred/Open.
- **Status**: Active

---

### DEC-005: Hosting and delivery operating model

- **Date**: 2026-10-01
- **Step**: B.1.3.6 — Architectural Decision Points
- **Driver**: Product Owner decision
- **Decision**: Deferred / open. HTTPS remains mandatory; provider, operating model, preview, rollback, release, and reliability treatment remain unselected.
- **Options considered**:
  - Managed static hosting/CDN category.
  - Managed web platform category with broader build/preview capabilities.
  - Self-managed or infrastructure-heavy hosting category.
- **Rationale for deferral**: Depends on content/publication boundaries, operational evidence, and proportional complexity analysis.
- **Disposition**: Deferred / Open — Product Owner confirmed
- **Evidence level**: [ASM] — underlying architecture question/options remain unresolved.
- **Impact**: Must be resolved before release planning; no provider or deployment model is selected.
- **Status**: Deferred / Open

---

### DEC-006: Build/publication trigger and release policy

- **Date**: 2026-10-01
- **Step**: B.1.3.6 — Architectural Decision Points
- **Driver**: Product Owner decision
- **Decision**: Deferred / open. Content approval/change, preparation/build or preview, production release authorization, and automation/scheduling remain composable stages; no combination is selected.
- **Options considered**:
  - Approved content change initiates preparation or preview.
  - Preview/build initiation is separate from production release authorization.
  - Automation or scheduling governs preparation, preview, or release timing.
- **Rationale for deferral**: Publication-control stage, build/runtime ownership, and release operations remain unresolved.
- **Disposition**: Deferred / Open — Product Owner confirmed
- **Evidence level**: [ASM] — underlying architecture question/options remain unresolved.
- **Impact**: Must be resolved before deployment and release design; no trigger, message flow, API, or event architecture is created.
- **Status**: Deferred / Open

---

### DEC-007: MVP measurement requirement and mechanism

- **Date**: 2026-10-01
- **Step**: B.1.3.6 — Architectural Decision Points
- **Driver**: Product Owner decision
- **Decision**: Deferred / open. First determine whether MVP measurement events are required; only if required should the minimum appropriate event set and mechanism be defined.
- **Options considered**:
  - Determine that no MVP measurement events are required.
  - Determine that a minimum approved event set is required and define it later.
  - Broader behavioral instrumentation, if an approved requirement or material risk justifies it.
- **Rationale for deferral**: Measurement readiness is required as a cross-cutting concern, but events, mechanism, privacy, consent, retention, baseline, and ownership remain unresolved.
- **Disposition**: Deferred / Open — Product Owner confirmed
- **Evidence level**: [ASM] — underlying architecture question/options remain unresolved.
- **Impact**: No analytics events, schema, endpoint, service, or runtime boundary is selected.
- **Status**: Deferred / Open

---

### DEC-008A: Responsive implementation breakpoints

- **Date**: 2026-10-01
- **Step**: B.1.3.6 — Architectural Decision Points
- **Driver**: Product Owner decision
- **Decision**: Deferred / open. B6 widths of 375/768/1440 remain Figma reference frames only; implementation breakpoints are not selected.
- **Options considered**:
  - Define implementation breakpoints after representative responsive validation.
  - Use B6 reference widths as implementation breakpoints — not approved.
- **Rationale for deferral**: Device priority and implementation breakpoints remain unresolved; selecting them would exceed approved design infrastructure scope.
- **Disposition**: Deferred / Open — Product Owner confirmed
- **Evidence level**: [ASM] — underlying architecture question/options remain unresolved.
- **Impact**: Affects implementation and validation only; does not select a frontend technology.
- **Status**: Deferred / Open

---

### DEC-008B: Formal accessibility conformance level

- **Date**: 2026-10-01
- **Step**: B.1.3.6 — Architectural Decision Points
- **Driver**: Product Owner decision
- **Decision**: Deferred / open. Qualitative accessibility requirements remain mandatory; no formal conformance level is approved.
- **Options considered**:
  - Define a formal conformance level later.
  - Continue with approved qualitative requirements until a formal target is selected.
- **Rationale for deferral**: The PRD and A10 establish mandatory qualitative accessibility requirements but do not approve a formal level.
- **Disposition**: Deferred / Open — Product Owner confirmed
- **Evidence level**: [ASM] — underlying architecture question/options remain unresolved.
- **Impact**: Must not weaken current accessibility requirements; formal testing target remains open.
- **Status**: Deferred / Open

---

## Reversals

None.

---

## Enrichment Log

| Date | Change | Source | Updated By |
|---|---|---|---|
| 2026-10-01 | Initialized for B.1.1; no architecture selections recorded. | Approved PRD, A3, A10, B4, B5, B6, Part C, Architecture Context, Technical Feasibility, approved B.0 profile | Devin |
| 2026-10-01 | Recorded DEC-001 as the Product Owner-approved working logical-boundary direction; physical topology remains open. | ARCH-B1c predecessor review / Product Owner boundary-direction approval | Devin |
| 2026-10-01 | Recorded DEC-002 and DEC-003 as directional decisions; format, schema, tooling, enforcement stage, and physical topology remain open. | Approved representative-content feasibility evidence and Product Owner Step 6 disposition | Devin |
| 2026-10-01 | Recorded DEC-004 through DEC-008A/B as explicit deferred/open decision entries with options and rationale. | Product Owner Step 6 dispositions | Devin |
| 2026-10-01 | DEC-004 approved as a combined delivery responsibility direction; physical/implementation mapping remains open. | Product Owner B.2 DEC-004 decision | Devin |
| 2026-10-01 | Created ADR-001 through ADR-004 with status Proposed; no ADR accepted. | Product Owner ADR-gate authorization; installed ADR lifecycle | Devin |
| 2026-10-01 | Transitioned ADR-001 through ADR-004 from Proposed to Accepted after Product Owner approval. | Product Owner ADR review gate; installed ADR lifecycle | Devin |
| 2026-10-01 | Recorded Product Owner B.2 clarification: portfolio content is expected to be relatively low-change for proportionality context; no separate public-MVP retention architecture is required; future measurement retention/privacy remains conditional under DEC-007. | Product Owner clarification during B.2 HLD elaboration | Devin |
| 2026-10-01 | Recorded ADR-002 provenance as a non-substantive historical/documentation limitation; Accepted ADR-002 was not edited or superseded. | Product Owner ADR-002 provenance disposition | Devin |
| 2026-10-01 | ARCH-B2 PASS recorded; Part 1 Architecture complete and B.3 Review & Hardening is the next prescribed gate. | Product Owner ARCH-B2 approval | Devin |
| 2026-10-01 | Applied B.3.4 HF-001 operational failure-mode tracking and HF-002 provisional dependency tracking; no architecture decision or blocker promotion added. | B.3.4 Canonical Hardening | Devin |
| 2026-10-01 | Part 1 Architecture complete after ARCH-B4 PASS; Part 2 Test & DevOps Strategy is the next lifecycle activity. | Product Owner Part 1 approval | Devin |

---

## Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-10-01 | Devin | Initialized at B.1.1 engagement start. |
| 0.2 | 2026-10-01 | Devin | Recorded DEC-001 working boundary direction. |
| 0.3 | 2026-10-01 | Devin | Recorded DEC-002 and DEC-003 directional architecture decisions. |
| 0.4 | 2026-10-01 | Devin | Added explicit deferred/open decision entries for remaining Step 6 decisions. |
| 0.5 | 2026-10-01 | Devin | Recorded DEC-004 combined delivery responsibility direction; retained physical/implementation questions as open. |
