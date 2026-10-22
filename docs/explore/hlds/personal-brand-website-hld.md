---
domain: Personal Brand Website
source: explore/explore-personal-brand-website/domain-analysis.md
glossary_version: 2026-09-22
validated_by: Jairo Enrique Diaz — Product Owner, B.1 PASS
explore_type: ERC
evidence_label: OBS
prd_source: explore/prds/personal-brand-website-prd.md
prd_requirements_mapped: R-001 through R-006
prd_nfrs_mapped: NFR-001 through NFR-007
architecture_context_source: explore/explore-personal-brand-website/architecture-context.md
status: Part 1 Architecture Complete — Part 2 Test & DevOps Strategy pending
---

# HLD · Personal Brand Website

**Version**: 0.1
**Date**: 2026-10-01
**Author**: Devin
**B.2 status**: Sections 1–14 validated; ADR-001 through ADR-004 Accepted; ARCH-B2 PASS recorded; B.3/B.4 complete; Part 1 Architecture complete; Part 2 pending.

---

## 1. System Overview

### 1.1 Purpose

The Personal Brand Website is an evidence-based professional portfolio that complements Jairo Enrique Diaz's CV. It enables recruiters, hiring managers, and other approved visitors to assess professional relevance, project evidence, leadership, business outcomes, and career evolution progressively, then contact Jairo or access the supporting CV. `[OBS]` PRD; A10; approved foundations

The MVP contains exactly eight approved screens:

- Home
- Projects
- Project Story Detail
- Contact
- How I Can Help
- Leadership
- Career Journey
- About

This section formalizes the approved product and logical architecture direction. It does not select implementation technology, production content format, hosting, deployment, analytics architecture, or physical topology.

### 1.2 Logical responsibility flow

```text
Context Warehouse / Professional Knowledge
    → validated factual knowledge and Evidence
Project Story Curation / Publication Governance
    → approved, publication-eligible public content
Public Website Experience
    → public pages, navigation, external links/downloads
Visitor browser
```

The minimum physical-realization envelope approved at B.1 is:

```text
Governed source/context
    → curated and publication-eligible content
    → public generation
    → public hosting/runtime
    → visitor browser

Adjacent:
    → External Destinations
    → conditional Measurement
```

This is a responsibility and data-flow envelope, not a selection of services, modules, repositories, production schema, CMS/file format, build tooling, hosting provider, deployment tooling, or runtime topology. `[OBS]` validated Boundary Map; approved Design Sketch

### 1.3 Approved logical boundaries

#### Context Warehouse / Professional Knowledge

Maintains governed professional knowledge and factual Evidence, including Career Experience, factual Projects, source facts, references, and sensitivity metadata. It is not the public website runtime source. `[OBS]` A3; Architecture Context; Boundary Map

#### Project Story Curation / Publication Governance

Transforms validated Projects into approved public Project Stories and controls publication eligibility, publication classification, narrative role, prominence, approval state, and disclosure. Human semantic governance remains authoritative for Evidence adequacy, attribution, truthful wording, narrative qualification, disclosure judgment, and final Content Owner approval. `[OBS]` A3; PRD; DEC-003

#### Public Website Experience

Presents approved public Project Stories and related eligible public entities through the eight-screen A10 experience, including progressive disclosure, non-linear exploration, Contact paths, and approved external links/downloads. It is a consumer/presenter of approved public content, not the authority for Project, Evidence, or Project Story governance state. `[OBS]` A10; PRD; Boundary Map

### 1.4 Design goals and constraints

The direction must:

- preserve Project versus Project Story separation and the complete A3 relationship model; `[OBS]` A3; B4
- preserve Evidence/publication boundaries and prevent restricted or ineligible content from public generation; `[OBS]` A3; PRD NFR-003; DEC-003
- preserve the frontend-only MVP boundary and avoid unsupported backend-dependent behavior; `[OBS]` PRD; Architecture Context
- preserve accessible, responsive, scannable, progressive, and non-linear experience behavior; `[OBS]` A10; PRD NFR-002
- preserve HTTPS as a production-hosting requirement without selecting a provider; `[OBS]` PRD NFR-004
- keep added complexity justified by an approved requirement or identified risk; `[OBS]` PRD NFR-006
- preserve measurement readiness while keeping whether MVP measurement events are required unresolved; `[OBS]` / `[ASM]` PRD NFR-007; DEC-007
- preserve the approved B.0 quality-priority ordering for later trade-offs: truth/publication safety, boundary integrity, accessibility/responsive usability/scannability, maintainability/proportional simplicity, and secure/reliable delivery. `[OBS]` Product Owner B.0 prioritization

### 1.5 Approved directional decisions

- **DEC-001:** Option A logical-boundary direction is approved. Physical topology remains unresolved.
- **DEC-002:** Governed files are the approved MVP content-representation direction; Markdown/structured metadata versus JSON/YAML, production schema, repository/content structure, content contract, validation tooling, and build mechanism remain unresolved.
- **DEC-003:** Human semantic governance plus deterministic structural eligibility validation before public generation is approved as the publication-safety direction; exact enforcement stage/mechanism remains unresolved.
- **DEC-004:** Combined delivery responsibility is approved: Project Story Curation / Publication Governance remains the governance authority; the combined delivery responsibility owns approved-content preparation and public generation; Public Website Experience remains visitor-facing presentation/navigation. Remaining physical/implementation mapping remains unresolved.

These are bounded directional decisions, not implementation-level selections. `[OBS]` Product Owner B.1 decisions

### 1.6 Explicit exclusions and unresolved boundaries

This Section 1 intentionally does not select or resolve:

- DEC-004 combined delivery responsibility is approved; physical/implementation mapping remains Deferred/Open;
- hosting/delivery operating model — DEC-005 remains Deferred/Open;
- build/publication trigger and release policy — DEC-006 remains Deferred/Open;
- measurement requirement/mechanism — DEC-007 remains Deferred/Open;
- responsive implementation breakpoints — DEC-008A closed by D-013 (768px and 1024px); %%Updated 2026-10-20.%%
- formal accessibility conformance level — DEC-008B remains Deferred/Open;
- frontend stack/language;
- production schema, content contract, repository structure, or file format;
- publication-control implementation stage or tooling;
- API/event architecture;
- physical service, module, repository, deployment, or runtime topology.

DEC-004 ownership is approved as a combined delivery responsibility. B.2 must not silently infer the remaining physical mapping or implementation topology; if later HLD formalization cannot proceed coherently without those details, return to the appropriate Product Owner gate before HLD finalization. `[OBS]` approved B.1 governance

### 1.7 Section 1 traceability

- **R-001:** Exactly eight approved screens are preserved.
- **R-002:** Public Project Stories remain curated narratives derived from validated Projects.
- **R-003:** Evidence/publication governance remains mandatory and internal/restricted Evidence is not automatically public.
- **R-004:** Progressive, scannable, non-linear exploration is preserved.
- **R-005:** Contact owns Email, LinkedIn, Phone, and secondary CV download; no on-site form backend is introduced.
- **R-006:** Approved supporting screens and canonical Capabilities/Leadership Principles are preserved.
- **NFR-001:** Performance remains proportional; no numeric target is invented.
- **NFR-002:** Accessibility and responsiveness remain mandatory with qualitative requirements; formal conformance remains open; breakpoints are 768px and 1024px (D-013). %%Updated 2026-10-20.%%
- **NFR-003:** Publication and Evidence integrity remain mandatory.
- **NFR-004:** HTTPS remains mandatory for selected production hosting.
- **NFR-005:** Reliability remains proportional; no SLA or rollback target is invented.
- **NFR-006:** Maintainability and scope discipline remain mandatory.
- **NFR-007:** Measurement readiness is preserved conditionally; no analytics architecture is selected.

### 1.8 Section 1 review status

**Status:** Approved by Product Owner — B.2 Section 1 System Overview.

---

## 2. Architecture Approach

### 2.1 Approach statement

The HLD adopts the approved B.1 **logical responsibility and governed-publication approach**:

```text
Governed source/context
    → curated and publication-eligible content
    → public generation
    → public hosting/runtime
    → visitor browser
```

The approach preserves three logical responsibility boundaries:

1. **Context Warehouse / Professional Knowledge** — governed factual professional knowledge and Evidence.
2. **Project Story Curation / Publication Governance** — validated Projects, approved Project Stories, publication eligibility, and human semantic governance.
3. **Public Website Experience** — presentation of approved public content through the approved eight-screen experience.

External Destinations remain adjacent. Measurement remains conditional under DEC-007.

This is a logical responsibility/data-flow approach, not a physical topology selection. It does not select services, modules, repositories, production schema, file format, frontend technology, build tooling, hosting, deployment, runtime topology, APIs, events, or analytics architecture. `[OBS]` approved B.1 package

See ADR-001: logical-responsibility-boundaries; See ADR-002: governed-file-mvp-content-direction; See ADR-003: publication-safety-control-direction; See ADR-004: combined-delivery-responsibility-direction.

### 2.2 Approach principles

- Preserve A3 Project / Project Story separation and complete relationship model.
- Preserve Evidence/publication boundaries; restricted or ineligible content must not enter public generation.
- Use human semantic governance for Evidence adequacy, attribution, truthful wording, narrative qualification, disclosure judgment, and final Content Owner approval.
- Use deterministic structural eligibility validation for approved machine-readable lifecycle, classification, reference, and Evidence-sensitivity rules before public generation.
- Preserve the frontend-only MVP compatibility demonstrated at B.1 direction level.
- Preserve A10 progressive disclosure, accessibility, scannability, and non-linear exploration.
- Keep added complexity justified by an approved requirement or identified risk.
- Preserve measurement readiness conditionally without selecting events or analytics architecture.
- Preserve DEC-004 combined delivery ownership and keep remaining physical mapping/topology explicit; B.2 must not silently infer implementation details.

### 2.3 Pattern treatment

The following approved B.0 patterns inform the approach as contextual guidance only:

- governed source-to-public-content pipeline;
- bounded-context separation;
- governed publication and human approval;
- static/build-time content delivery as preferred but unresolved;
- progressive disclosure / hub-and-spoke experience pattern.

No adjacent platform convention is inherited. These patterns do not create a new service architecture, CMS, file format, schema, build mechanism, or deployment topology.

### 2.4 Deferred/Open decisions preserved

The following remain open and are not converted into architecture selections by this approach:

- DEC-004 combined delivery responsibility is approved; remaining physical mapping and implementation topology remain open;
- DEC-005 hosting/delivery operating model;
- DEC-006 build/publication trigger and release policy;
- DEC-007 measurement requirement and architecture;
- ~~DEC-008A responsive implementation breakpoints~~ closed by D-013;
- DEC-008B formal accessibility conformance level;
- Markdown/structured metadata versus JSON/YAML;
- production schema, repository/content structure, and content contract;
- deterministic validation tooling;
- exact publication-control enforcement stage/mechanism;
- frontend stack/language;
- implementation topology.

If formalization cannot proceed coherently without resolving remaining physical/implementation mapping, the HLD process must stop and return to the Product Owner gate.

### 2.5 Consistency check

- [x] Section 2 matches the validated Boundary Map and Truth Hierarchy.
- [x] Section 2 matches the approved Design Sketch direction.
- [x] Excluded systems, unresolved decisions, and negative boundaries are explicit.
- [x] No Deferred/Open decision was silently selected.
- [x] R-001 through R-006 and NFR-001 through NFR-007 remain binding from Section 1.

**Status:** Approved by Product Owner — B.2 Section 2 Architecture Approach.

---

## 3. Component Breakdown and Integration & Data Flows

### 3.1 Logical component breakdown

| Approved logical responsibility / boundary | Responsibility | Technology / realization status | Dependencies |
|---|---|---|---|
| Context Warehouse / Professional Knowledge | Maintain governed factual professional knowledge, validated Projects, Evidence, source facts, references, and sensitivity metadata. | Not selected; Context Warehouse is not public runtime. | A3 model, source corpus, Content Owner governance. `[OBS]` |
| Project Story Curation / Publication Governance | Transform validated Projects into approved Project Stories and apply human semantic governance plus structural eligibility rules. | Publication-control implementation unresolved. | Validated Projects, Evidence, publication classification, Content Owner approval. `[OBS]` / `[ASM]` |
| Public Website Experience | Present approved public content through the eight approved screens and A10 flows. | Frontend technology unresolved. | Approved public Project Stories, A10, B4/B5/B6. `[OBS]` / `[ASM]` |

### Realization stages — physical realization and implementation unresolved

| Realization stage / boundary | Responsibility in the envelope | Ownership / implementation status | Dependencies |
|---|---|---|---|
| Public generation | Combined delivery responsibility prepares approved eligible content and produces public assets. | Physical mapping/build mechanism unresolved under DEC-005/DEC-006. `[OBS]` / `[ASM]` | Approved content handoff and structural eligibility controls. |
| Public hosting/runtime | Serve generated public assets over HTTPS. | Hosting provider, deployment model, and operational ownership unresolved under DEC-005/DEC-006. `[ASM]` | Generated public assets, HTTPS, preview/rollback/release policy. |

### Adjacent boundaries

| Adjacent boundary | Responsibility | Status | Dependencies |
|---|---|---|---|
| External Destinations | Provide approved outbound LinkedIn, email, phone, and CV actions. | External links/downloads; final values/path unresolved. `[OBS]` / `[ASM]` | Public Website Experience and final governed Contact/CV content. |
| Measurement | Conditional future concern; no implementation boundary selected. | Events, mechanism, privacy, consent, retention, and ownership unresolved under DEC-007. `[ASM]` | Future Product Owner decision if measurement is required. |

These are logical responsibilities, not selected physical services, modules, repositories, or deployment units. DEC-004 combined delivery ownership is approved; B.2 must not infer remaining physical mapping silently. `[OBS]` / `[ASM]`

See ADR-001: logical-responsibility-boundaries; See ADR-003: publication-safety-control-direction; See ADR-004: combined-delivery-responsibility-direction.

### 3.2 Responsibility boundaries

- The Context Warehouse does not serve as the public runtime source.
- Curation owns neither visitor presentation nor runtime navigation.
- Public Website Experience does not own Project validation, Evidence assessment, publication approval, or internal governance state.
- Public generation is owned at the logical responsibility level by the approved combined delivery responsibility. Its physical realization, build mechanism, repository/process/deployment mapping, and implementation topology remain unresolved.
- Hosting/runtime consumes generated public assets but its provider and operational ownership remain unresolved.
- Measurement is conditional and does not create an application event architecture at this stage.

### 3.3 External integrations

| System / boundary | Integration type | Purpose | Protocol / mechanism |
|---|---|---|---|
| LinkedIn | External destination | Approved profile/contact action. | External hyperlink; final value unresolved. `[OBS]` / `[ASM]` |
| Email | External destination | Approved contact action. | Email-link mechanism/value unresolved. `[OBS]` / `[ASM]` |
| Phone | External destination | Approved contact action. | Phone-link mechanism/value unresolved. `[OBS]` / `[ASM]` |
| CV asset | Static/download destination | Supporting CV download owned by Contact. | Static asset path/delivery unresolved. `[OBS]` / `[ASM]` |
| Analytics / Measurement | Conditional future boundary | Measurement only if DEC-007 determines MVP events are required. | Mechanism, events, privacy, consent, and retention unresolved. `[ASM]` |

No application API or application-domain event contract is introduced. The logical Curation → Public Website handoff is not an API or event contract.

### 3.4 Internal data flows

```text
[Context Warehouse / Professional Knowledge]
        | validated Projects and Evidence
        v
[Project Story Curation / Publication Governance]
        | approved, publication-eligible public content
        v
[Public generation boundary]
        | generated public assets
        v
[Public hosting/runtime boundary]
        | HTTPS public delivery
        v
[Visitor browser]
        | renders
        v
[Public Website Experience]
        | approved external links/downloads
        v
[External Destinations]
```

Human semantic governance remains with Project Story Curation / Publication Governance and the Content Owner. The combined delivery responsibility owns approved-content preparation and public generation. Deterministic structural eligibility validation remains required before public generation, while its exact enforcement stage, mechanism, tooling, and physical implementation remain unresolved.

### 3.5 Key flows

1. **Governed content preparation and publication flow**
   - **Source:** Context Warehouse / Professional Knowledge.
   - **Destination:** Project Story Curation / Publication Governance → public generation → hosting/runtime.
   - **Trigger:** Content approval/build/publication stages remain unresolved under DEC-006.
   - **Data:** Validated Projects, Evidence, publication classification, approved Project Stories, eligible public content.
   - **Outcome:** Public assets may be generated only from eligible approved content.
   - **Status:** Logical combined-delivery ownership is approved under DEC-004; physical realization/mapping and trigger/release policy remain unresolved. `[OBS]` / `[ASM]`

2. **Visitor relevance-to-contact flow**
   - **Source:** Visitor browser.
   - **Destination:** Public Website Experience → Projects / Project Story Detail / supporting screens → Contact or approved external destination.
   - **Trigger:** Visitor requests an approved page or follows an approved link.
   - **Data:** Approved public Project Stories and related eligible public entities.
   - **Outcome:** Visitor explores non-linearly, contacts Jairo, or accesses the CV.
   - **Status:** Approved A10 experience flow; no application API/event architecture. `[OBS]`

3. **Conditional measurement flow**
   - **Source:** Public Website Experience, only if DEC-007 determines measurement events are required.
   - **Destination:** Unresolved Measurement boundary.
   - **Trigger:** Unresolved; no event architecture selected.
   - **Data:** Unresolved event set and privacy-governed measurement data.
   - **Outcome:** Future post-launch validation input, if approved.
   - **Status:** Conditional and unresolved. `[ASM]`

**Assumed contracts flagged for blocker register:** 0 new contracts. Existing provisional dependencies remain tracked in the Boundary Map and Blocker Register; no API, event, schema, or service contract is created here.

---

**Status:** Approved by Product Owner — B.2 Section 3 Component Breakdown and Integration & Data Flows.

---

## 4. Key Architectural Decisions and Technology Stack

### 4.1 Key architectural decisions

The following approved directional decisions are formalized here. ADR-001 through ADR-004 were accepted by the Product Owner on 2026-10-01 through the installed ADR lifecycle.

1. **DEC-001 — Logical responsibility boundaries**
   - **Decision:** Preserve Context Warehouse / Professional Knowledge, Project Story Curation / Publication Governance, and Public Website Experience as logical responsibility boundaries.
   - **Impact:** The minimum physical-realization envelope remains governed source/context → curated/publication-eligible content → public generation → public hosting/runtime → visitor browser. Physical topology and remaining implementation mapping remain unresolved; DEC-004 ownership is approved as combined delivery responsibility.
   - **Reference:** Approved Decision Log DEC-001; validated Boundary Map and Design Sketch. See ADR-001: logical-responsibility-boundaries.

2. **DEC-002 — Governed-file MVP direction**
   - **Decision:** Use a governed-file approach for the MVP rather than introducing a managed CMS.
   - **Impact:** Markdown/structured metadata versus JSON/YAML, production schema, content contract, repository structure, validation tooling, and build mechanism remain TBD.
   - **Reference:** Approved Decision Log DEC-002; representative validation evidence. See ADR-002: governed-file-mvp-content-direction.
   - **B.2 Product Owner clarification:** For MVP architecture trade-offs, public professional portfolio content is expected to be relatively low-change compared with a dynamically managed/high-frequency publishing product. This is a Product Owner architecture input, not a contractual content-update frequency. It supports proportionality context but is not the sole basis for DEC-002.

3. **DEC-003 — Publication-safety control direction**
   - **Decision:** Combine human semantic governance with deterministic structural eligibility validation before public generation.
   - **Impact:** Evidence adequacy, attribution, truthful wording, narrative qualification, disclosure judgment, and final Content Owner approval remain human-governed. Exact enforcement stage/mechanism and tooling remain TBD.
   - **Reference:** Approved Decision Log DEC-003; PRD NFR-003; Part C; representative validation evidence. See ADR-003: publication-safety-control-direction.

4. **DEC-004 — Combined delivery responsibility**
   - **Decision:** Project Story Curation / Publication Governance remains the governance authority; the combined delivery responsibility owns approved-content preparation and public generation; Public Website Experience remains visitor-facing presentation/navigation.
   - **Impact:** Provides proportional MVP simplicity without collapsing the approved logical boundaries. Remaining physical/implementation mapping remains unresolved.
   - **Reference:** Approved Decision Log DEC-004; ADR-004: combined-delivery-responsibility-direction.

5. **Deferred/Open decisions**
   - DEC-005 through DEC-008B remain Deferred/Open with their existing owners and escalation rules.
   - Remaining physical/implementation mapping after DEC-004 must not be inferred; if formalization cannot proceed coherently without those details, stop and return to the Product Owner gate.

### 4.2 Technology stack status

No production technology is committed by this section.

**Frontend:**

- Framework/language: **TBD** — any later selection must satisfy frontend-only MVP compatibility, PRD functional/NFR constraints, A10 accessibility/experience requirements, DEC-002 governed-content direction, DEC-003 publication-safety boundaries, and proportional-complexity constraints.
- State management: **Implementation-level; no dedicated state-management capability is currently established as necessary.** Revisit only if later implementation evidence requires one.
- UI library: **TBD / optional implementation choice**; not an architecture requirement.
- Responsive breakpoints: **768px and 1024px**, mobile-first, under DEC-008A (closed by D-013); B6 widths remain design references only.
- Formal accessibility conformance level: **TBD** under DEC-008B; qualitative accessibility remains mandatory.

**Backend:**

- Custom application backend: **Not applicable under the currently approved MVP direction** unless a later approved requirement or identified risk changes the frontend-only boundary.
- Application API requirement: **No application API requirement exists in the currently approved MVP scope.** A later approved requirement or identified risk may change this finding.
- Backend framework/language: **Not applicable under the currently approved MVP direction** unless the boundary changes through an approved gate.

**Data layer:**

- Primary database: **Not applicable under the currently approved MVP direction** unless later evidence establishes a requirement.
- Cache: **Not applicable under the currently approved MVP direction** unless later evidence establishes a requirement.
- Message queue/application-domain events: **No application-domain event requirement has been identified in the currently approved MVP scope. Measurement events remain conditional under DEC-007.**
- Production content format/schema: **TBD** within the approved governed-file direction; Markdown/structured metadata versus JSON/YAML remains unresolved.

**Infrastructure:**

- Hosting provider: **TBD** under DEC-005; HTTPS mandatory.
- Hosting/deployment operating model: **TBD** under DEC-005.
- Build/publication trigger and release policy: **TBD** under DEC-006.
- CI/CD/build tooling: **TBD / not selected**.
- Container orchestration: **Not applicable under the current architecture direction** unless later topology or operational evidence establishes a need.

### 4.3 Abstraction and governance checks

- [x] Approved directional decisions are stated as commitments without expanding their scope.
- [x] Deferred/Open decisions remain explicit and are not silently resolved.
- [x] Unresolved technology items are explicitly classified as TBD, not applicable under the current MVP direction, or conditional; none is silently assumed.
- [x] No infrastructure is inherited from adjacent systems; no adjacent conventions exist.
- [x] No API, event, schema, CMS, frontend technology, hosting provider, build mechanism, or physical topology is selected by inference.
- [x] DEC-004 stop/escalation rule is preserved.

**Active bounded directional decisions:** 4 — DEC-001 through DEC-004.
**Deferred/Open decisions:** DEC-005 through DEC-008B
**Technology selections:** 0
**ADR references:** ADR-001 through ADR-004 Accepted on 2026-10-01. Decision log remains authoritative for current decisions.

---

**Status:** Approved by Product Owner — B.2 Section 4 Key Architectural Decisions and Technology Stack.

---

## 5. Security, Scalability, Deployment, and Monitoring

### 5.1 Security considerations

- **Authentication:** No public visitor authentication is required by the approved MVP. No runtime governance/authentication capability is selected or required by the currently approved public MVP scope, subject to a later approved scope change. `[OBS]` PRD / Technical Feasibility
- **Authorization:** Publication eligibility, Evidence sensitivity/classification, approval, and publication governance are pre-publication governance concerns. No runtime RBAC/ABAC or governance UI is selected or required by the currently approved public MVP scope. `[OBS]` A3 / PRD / Architecture Context
- **Data encryption:** HTTPS is mandatory for selected production hosting. At-rest encryption treatment is provider/operating-model dependent and remains TBD. `[OBS]` PRD NFR-004 / `[ASM]` DEC-005
- **Compliance:** No additional sector-specific regulatory regime was identified in the approved B.0 baseline. Basic privacy, secure delivery, accessibility, and publication-sensitivity controls remain applicable. `[OBS]` PRD / Architecture Context
- **Evidence/publication integrity:** Internal/restricted Evidence must not become public. Material public claims require traceability, attribution, defensibility, and publication eligibility. `[OBS]` A3 / PRD NFR-003
- **Governance traceability:** Content Owner approval, Evidence traceability, publication classification, and architecture-decision governance remain recorded through the approved governance model. No runtime audit-logging/access architecture is selected. `[OBS]`
- **Data retention:** No separate public-MVP application data-retention architecture is currently required or selected. Governed professional/content lifecycle concerns remain within the approved source/publication governance model and must not be reinterpreted as a new runtime retention requirement. If DEC-007 later introduces measurement/analytics data, privacy, minimization, retention, and deletion/purge treatment must be determined as part of that decision and the selected mechanism/provider. Provider policies must not be assumed to satisfy project governance/privacy obligations. `[OBS]` Product Owner B.2 clarification / `[ASM]` DEC-007
- **Provider/privacy obligations:** Provider-specific, privacy, or analytics obligations remain subject to later approved hosting/privacy decisions where applicable. No provider-specific retention or data-handling policy is assumed to satisfy project requirements. `[ASM]` DEC-005 / DEC-007

### 5.2 Scalability and performance

- **Expected load:** No numeric traffic, concurrency, data-volume, or high-volume scalability target is approved. `[OBS]` Architecture Context
- **Scaling posture:** The MVP is bounded to a frontend-only public experience with no required application API, database, runtime personalization, or real-time behavior. `[OBS]` PRD / Architecture Context
- **Performance target:** Reasonable page and asset performance is required on representative desktop/mobile conditions; no numeric response-time or throughput target is approved. `[OBS]` PRD NFR-001
- **Scaling strategy:** Static/build-time delivery remains preferred but unresolved. No scaling technology, cache, queue, or infrastructure topology is selected. `[OBS]` / `[ASM]`
- **Quality constraint:** Added infrastructure or complexity requires an approved requirement or identified risk. `[OBS]` PRD NFR-006

### 5.3 Deployment architecture

- **Environments:** Local/development and preview concepts are useful for validation, but exact environment structure remains TBD. Production hosting and operating model remain TBD under DEC-005.
- **Deployment strategy:** TBD under DEC-005/DEC-006. No provider, CI/CD system, build tool, preview mechanism, rollback mechanism, or release automation is selected.
- **Current posture:** Public deployment must consume only publication-eligible generated content, use HTTPS, preserve the frontend-only boundary, and avoid runtime Warehouse access. `[OBS]`
- **Release control:** Content approval, preparation/build or preview, production release authorization, and automation/scheduling remain composable unresolved stages under DEC-006.
- **DEC-004 dependency:** Combined delivery ownership is approved; remaining physical mapping and implementation topology remain Deferred/Open. B.2 must not silently infer them; stop at the Product Owner gate if formalization requires resolution.

### 5.4 Monitoring and observability

- **Logging:** No runtime logging architecture is selected. Human approval, Evidence/publication decisions, and architectural decisions remain governed through their approved records. `[OBS]` / `[ASM]`
- **Metrics:** No measurement events are selected. Determine first whether MVP measurement events are required under DEC-007; only then define any metrics.
- **Tracing:** No distributed application or API tracing requirement is identified because no application API/event architecture is approved. `[OBS]`
- **Alerting:** No operational alerting model is selected. Any later hosting/deployment model must define proportionate operational treatment if required. `[ASM]`
- **Audit access:** Access to governed decision and publication records remains a process/ownership concern; runtime audit-access implementation is not selected. `[OBS]` / `[ASM]`

### 5.5 Architecture-rule checks

- [x] Bounded-context ownership remains explicit; no ownership is blurred.
- [x] Human approval and correction flows remain core governance flows.
- [x] Each logical responsibility and realization stage has an explicit boundary.
- [x] No application API, event, schema, service, or monitoring implementation is invented.
- [x] Security, performance, deployment, and observability TBD items remain explicit.

---

**Status:** Approved by Product Owner — B.2 Section 5 Security, Scalability, Deployment, and Monitoring.

---

## 6. Future-State Experience Journey and Open Questions

### 6.1 Future-state experience journey

The future-state experience preserves the approved A10 journey without introducing a mandatory funnel:

1. A visitor enters Home or another approved entry point.
2. The visitor establishes identity, positioning, and relevance.
3. The visitor selects Projects or an approved supporting context.
4. Projects presents eligible Project Story summaries.
5. Project Story Detail presents orientation first, followed by deeper approved context, responsibilities, decisions, outcomes, capabilities, lessons, and eligible public references.
6. The visitor may continue to related approved context, return to Projects, visit supporting screens, or proceed directly to Contact.
7. Contact provides Email, LinkedIn, Phone, and the secondary CV action.
8. Measurement remains conditional under DEC-007 and is not represented as an implemented runtime flow.

This journey preserves entry, skip, revisit, direct Contact, progressive disclosure, accessibility principles, and non-linear exploration. It does not introduce runtime personalization, recommendation logic, search, filtering, authentication, chatbot behavior, or governance UI. `[OBS]` A10 / PRD

### 6.2 Open questions

| # | Question | Owner | Target resolution |
|---:|---|---|---|
| 1 | What minimum physical mapping realizes the approved combined delivery responsibility and the approved envelope? | Product Owner / Architect | If formalization requires it; otherwise carry DEC-004 explicitly and prohibit silent inference. |
| 2 | Which governed-file format should be used: Markdown/structured metadata or JSON/YAML? | Product Owner / Architect | Later architecture/content decision; governed-file direction already approved. |
| 3 | What production schema, repository/content structure, and approved content contract are needed? | Product Owner / Architect | Before implementation; do not infer during HLD drafting. |
| 4 | What validation tooling and publication-control enforcement stage/mechanism are appropriate? | Product Owner / Architect | Before public generation; exact stage remains Deferred/Open. |
| 5 | Which hosting/delivery operating model and deployment/preview/rollback/release implementation are appropriate? | Product Owner / Architect | Before release planning; DEC-005/006 remain Deferred/Open. |
| 6 | Are MVP measurement events required, and if so what event set, mechanism, privacy, consent, retention, and ownership apply? | Product Owner / Architect | Before measurement implementation; DEC-007 remains Deferred/Open. |
| 7 | Which frontend implementation stack/language should be used? | Architect / Lead Engineer analysis; Product Owner approval | Later implementation planning, subject to frontend-only, PRD/NFR, A10, DEC-002/003, and proportionality constraints. |
| 8 | What responsive implementation breakpoints should be used? | Architect / Lead Engineer analysis; Product Owner approval if scope changes | Closed by D-013 (768px and 1024px, mobile-first; test at 320px). DEC-008A closed. %%Updated 2026-10-20.%% |
| 9 | What formal accessibility conformance level should be adopted? | Product Owner / Content Owner; Architect / Lead Engineer advises | Later formal validation planning; DEC-008B remains Deferred/Open. |
| 10 | Can contextual navigation be generated from approved relationships without backend functionality? | Architect / Lead Engineer analysis; Product Owner approval if boundary changes | Before implementation if required; do not create navigation-domain relationships. |
| 11 | What final Contact values and CV asset path are publication-ready? | Product Owner / Content Owner | Closed by D-021 (2026-10-20). %%Updated 2026-10-20: contact values and CV path approved.%% |
| 12 | Which Project Story previews, ordering, summary fields, Related/Next links, and disclosure mechanism are final? | Product Owner / Content Owner | Closed by D-014 (previews, order, summary fields) D-020 (Related/Next links), 2026-10-20, and D-025 (disclosure: one section open at a time), 2026-10-22. %%Updated 2026-10-20.%% |
| 13 | How should the qualified Tigo → Avianca → DFA arc appear in final copy? | Product Owner / Content Owner | Later governed content/copy. |
| 14 | How should B5/B6 tokens and the `type/code` exception map to implementation? | Architect / Lead Engineer analysis; Product Owner approval if scope changes | Later design-system/implementation. |

### 6.3 B.2 closure disposition

| Question | Closure classification | Disposition / target resolution |
|---|---|---|
| DEC-004 — remaining physical mapping after approved combined delivery ownership | **May carry into B.3 Review & Hardening** | B.2 drafting completed coherently after resolving the bounded DEC-004 ownership direction. Remaining physical mapping and implementation topology are carried forward as open; B.2 has not inferred them. Promote the dependency and return to the Product Owner gate before HLD finalization if formalization later depends on those details. |
| Governed-file format | **May carry into B.3 Review & Hardening** | Governed-file direction is approved; Markdown/structured metadata versus JSON/YAML remains unresolved. |
| Production schema/content contract/repository structure | **May carry into B.4 Finalization & Handoff or applicable implementation activity** | Not required for current HLD coherence; no structure is silently invented. |
| Validation tooling/publication-control stage | **May carry into B.3 Review & Hardening** | Direction is coherent; exact tooling and enforcement stage remain Deferred/Open and are required before public generation. |
| Hosting/deployment model | **May carry into B.4 Finalization & Handoff and Part 2 DevOps Strategy** | Provider and operating model remain unselected. |
| Trigger/release policy | **May carry into B.4 Finalization & Handoff and Part 2 DevOps Strategy** | Stages remain composable; no policy selected. |
| Measurement | **Applicable later strategy/measurement activity** | First determine whether MVP events are required; no analytics architecture selected. |
| Contextual-navigation feasibility | **May carry into B.3 Review & Hardening or applicable implementation activity** | Validate against approved relationships without creating navigation-domain relationships. |
| Frontend stack/language | **Downstream implementation/strategy decision** | Must satisfy frontend-only, PRD/NFR, A10, DEC-002/003, and proportionality constraints. |
| Responsive breakpoints | **Closed** | DEC-008A closed by D-013 (768px and 1024px); B6 widths are references only. |
| Formal accessibility conformance | **Downstream implementation/validation decision** | DEC-008B remains Deferred/Open; qualitative accessibility remains mandatory. |
| Contact/CV values | **Downstream content/implementation** | Not an HLD decision unless a concrete architecture dependency emerges. |
| Project Story presentation details | **Downstream content/implementation** | Not an HLD decision unless a concrete architecture dependency emerges. |
| Tigo → Avianca → DFA final copy | **Downstream governed content/copy** | Preserve A3 qualifications. |
| B5/B6 token-to-implementation mapping | **Downstream design-system/implementation** | No architecture dependency demonstrated. |

**B.2 closure result:** No question currently must be resolved before ARCH-B2 approval/finalization. If B.3/B.4 review demonstrates that DEC-004 or another Deferred/Open question is required for coherent HLD formalization, stop and return to the Product Owner gate.

No open question is silently resolved by this section. DEC-004 combined delivery ownership is approved; remaining physical/implementation mapping is Deferred/Open. If the HLD cannot be formalized coherently without those details, stop and return to the Product Owner gate.

### 6.4 Enrichment and document status

- Sections 1–5: approved.
- Sections 6–14: drafted as bounded formalization; final ARCH-B2 Product Owner review pending.
- ADRs: ADR-001 through ADR-004 Accepted on 2026-10-01; no ADR remains Proposed.
- B.1 artifacts remain authoritative for the approved B.1 state at that gate. Subsequent Product Owner-approved Decision Log entries and Accepted ADRs govern later architecture decisions within their approved decision scope. DEC-004 was Deferred/Open at B.1 approval and was subsequently resolved directionally during B.2; remaining physical/implementation mapping remains Deferred/Open.

---

## 7. Security Considerations

Section 5 contains the approved consolidated Security, Scalability, Deployment, and Monitoring baseline. Sections 7–11 provide the prescribed detailed HLD treatment of those same concerns; they are expansions of the approved baseline, not new or contradictory architecture decisions. This section records the HLD treatment without introducing a runtime security subsystem.

- Public visitor authentication: not required by the approved MVP.
- Runtime governance/authentication capability: not selected or required by the approved public MVP scope.
- Authorization: publication eligibility, Evidence sensitivity/classification, approval, and publication governance remain pre-publication concerns.
- Runtime RBAC/ABAC and governance UI: not selected or required by the approved public MVP scope.
- HTTPS: mandatory for selected production hosting; provider remains TBD under DEC-005.
- Restricted/ineligible Evidence: must not enter public generated assets.
- Governance traceability: Content Owner approval, Evidence traceability, publication classification, and architecture-decision governance remain recorded through the approved governance model; no runtime audit subsystem is selected.
- Regulatory baseline: no additional sector-specific regime was identified in the approved B.0 baseline; provider/privacy/analytics obligations remain subject to later approved choices.
- Data retention: no separate public-MVP application data-retention architecture is required or selected. Governed content lifecycle remains within source/publication governance. Measurement retention/minimization/deletion treatment is conditional under DEC-007.

PRD traceability: R-002, R-003, NFR-003, NFR-004, NFR-006, NFR-007.

## 8. Quality Attributes and Operational Requirements

| Attribute / requirement | HLD treatment | Status |
|---|---|---|
| NFR-001 Performance | Reasonable page/asset performance on representative desktop/mobile conditions; no numeric target. | Approved qualitative constraint |
| NFR-002 Accessibility/responsiveness | Semantic structure, meaningful headings/links, keyboard navigation, visible focus, logical focus order, descriptive labels, accessible disclosure, responsive usability. | Mandatory; formal level/breakpoints Deferred/Open |
| NFR-003 Publication/evidence integrity | Human semantic governance plus deterministic structural eligibility validation before public generation. | Direction approved; stage/tooling TBD |
| NFR-004 Secure delivery | HTTPS required for selected hosting. | Provider/model TBD |
| NFR-005 Proportional reliability | Review/preview, rollback, reliable delivery, and release treatment proportional to MVP. | DEC-005/006 TBD |
| NFR-006 Maintainability/scope | Added complexity requires approved requirement or identified risk. | Binding constraint |
| NFR-007 Measurement readiness | Preserve future measurement capability; first determine whether MVP events are required. | Conditional under DEC-007 |

No numeric SLA, latency, throughput, availability, accessibility, retention, or rollback target is invented.

## 9. Scalability and Performance

- No high-volume traffic, concurrency, data-volume, or seasonal-load target is approved.
- The frontend-only MVP has no required application API, database, runtime personalization, or real-time behavior.
- Static/build-time delivery remains preferred but unresolved.
- No cache, queue, scaling service, CDN/provider, or infrastructure topology is selected.
- Performance validation remains proportional to the approved MVP and representative desktop/mobile conditions.
- Added scaling infrastructure requires an approved requirement or identified risk.

Traceability: NFR-001, NFR-005, NFR-006; Architecture Context drivers 5, 7, 8, and 10.

## 10. Deployment Architecture

- Local/development and preview concepts may support validation, but environment structure is TBD.
- Production hosting/provider and operating model remain TBD under DEC-005.
- Deployment, preview, rollback, and release policy remain TBD under DEC-005/DEC-006.
- HTTPS is mandatory for selected production hosting.
- Public deployment must consume only publication-eligible generated content.
- The Context Warehouse is not a public runtime source.
- No CI/CD system, build tool, deployment mechanism, rollback mechanism, release automation, container orchestration, or physical topology is selected.
- If DEC-004 physical mapping becomes necessary for coherent HLD formalization, stop at the Product Owner gate rather than infer it.

## 11. Monitoring and Observability

- Runtime logging architecture: not selected.
- Measurement events and metrics: conditional under DEC-007; first determine whether MVP events are required.
- Distributed tracing: no requirement identified under the frontend-only/no-application-API direction.
- Operational alerting: not selected; future treatment must be proportional to the eventual hosting/delivery model and approved requirements/risks.
- Audit access: governed decision/publication records remain process-governed; no runtime audit-access architecture is selected.
- No monitoring, metrics, tracing, alerting, or analytics infrastructure is introduced by inference.

## 12. Future-State Experience Journey

The future-state journey is defined in Section 6.1 and remains the approved A10 experience:

- non-linear visitor entry, skipping, revisiting, and direct Contact;
- Home orientation → Projects/Supporting Context → Project Story Detail → Contact or continued exploration;
- progressive disclosure from orientation to deeper eligible public content;
- External Destinations through approved links/downloads;
- conditional measurement only if DEC-007 determines events are required;
- no runtime personalization, recommendation engine, search/filtering, authentication, chatbot, or governance UI.

## 13. Open Questions

The complete owner-attributed open-question and closure-disposition register is maintained in Section 6.2–6.3. B.2 carries forward:

- DEC-005 hosting/delivery operating model;
- DEC-006 trigger/release policy;
- DEC-007 measurement requirement/architecture;
- DEC-008A responsive breakpoints;
- DEC-008B formal accessibility conformance;
- governed-file format/schema/content contract/tooling;
- residual physical/implementation mapping after DEC-004.

No open question is silently resolved. If a B.3/B.4 review demonstrates that any Deferred/Open item is required for coherent HLD formalization, stop and return to the appropriate Product Owner gate.

### B.3 Hardening finding HF-001 — Operational failure-mode coverage

**Severity:** SIGNIFICANT — tracking correction applied; downstream resolution retained.

| Scenario | Affected boundary/stage | Known invariant or safe behavior | Mechanism status | Owner | Target lifecycle/activity | Promotion condition |
|---|---|---|---|---|---|---|
| Publication validation failure | Curation / Publication Governance → public generation | Restricted/ineligible content must not enter generated public assets; failed validation is not successful eligibility. | Enforcement/failure mechanism unresolved. | Product Owner / Architect | B.4 hardening and applicable implementation/publication work | Promote if safe public generation cannot be demonstrated. |
| Public-generation failure | Public generation → hosting/runtime | Failed generation must not be treated as successful public publication. No further fallback is asserted. | Failure detection, artifact handling, and release behavior unresolved. | Architect / Lead Engineer | B.4 and Part 2 DevOps Strategy | Promote if safe release cannot be formalized. |
| Preview/release failure | Build/preview/release stages | Approval and release authority remain governed; no specific recovery behavior is canonically selected. | Preview, release, and failure-handling mechanism unresolved under DEC-006. | Product Owner / Architect | B.4 and Part 2 DevOps Strategy | Promote if release safety cannot be maintained. |
| Hosting unavailability | Hosting/runtime → visitor browser | HTTPS is mandatory; no availability fallback or SLA is approved. | Hosting resilience/fallback mechanism unresolved under DEC-005. | Product Owner / Architect | B.4 and Part 2 DevOps Strategy | Promote if approved reliability requirements cannot be met. |
| Rollback requirement | Deployment/release boundary | Reliability and rollback remain proportional concerns; no rollback target or mechanism is approved. | Rollback mechanism unresolved under DEC-005/DEC-006. | Product Owner / Architect | B.4 and Part 2 DevOps Strategy | Promote if release safety cannot be formalized. |
| External destination failure/unavailability | Public Website Experience → External Destinations | A10 preserves alternate visible approved contact methods; no runtime destination-health detection is introduced. | Destination availability and fallback implementation remain unresolved. | Product Owner / Content Owner | Later governed content/implementation | Promote only if an approved requirement or material risk requires runtime handling. |

### B.3 Hardening finding HF-002 — Provisional dependency/contract tracking

**Severity:** SIGNIFICANT — tracking correction applied; dependencies remain provisional.

| Provisional dependency | Current status | Owner | Required by | Currently blocking? | Promotion condition |
|---|---|---|---|---|---|
| Governed Project/Evidence content contract | PROVISIONAL; A3 fidelity and publication metadata must be preserved. | Product Owner / Architect | Before implementation/content preparation. | No | Promote if the A3/publication model cannot be safely represented. |
| Approved public-content handoff contract | PROVISIONAL; logical Curation → Public Website handoff exists, physical representation remains open. | Product Owner / Architect | Before implementation/public generation. | No | Promote if HLD/implementation cannot proceed without an unprovided contract. |
| Contact/CV asset readiness | PROVISIONAL; final values/path and publication readiness remain open. | Product Owner / Content Owner | Before public publication. | No | Promote if required public Contact/CV behavior cannot be safely delivered. |
| Measurement/privacy contract | PROVISIONAL and conditional on DEC-007; no events are selected. | Product Owner / Architect | Before measurement implementation, if events are approved. | No | Promote only if DEC-007 establishes a required mechanism that cannot be safely defined. |
| Hosting/deployment operational contract | PROVISIONAL under DEC-005/DEC-006; provider, preview, rollback, release, and ownership remain open. | Product Owner / Architect | Before release/DevOps planning. | No | Promote if approved HTTPS/reliability/release needs cannot be met. |

These corrections do not create APIs, schemas, event contracts, hosting contracts, or implementation mechanisms. They do not alter DEC-001 through DEC-008B or BLK-001.

## 14. Enrichment Log

| Date | Change | Source | Updated By |
|---|---|---|---|
| 2026-10-01 | Completed Sections 7–14 as bounded formalization of approved direction; retained all Deferred/Open decisions and TBD implementation choices. | Approved B.1 package, PRD, A3, A10, B4, B5, B6, Part C, Architecture Context, Technical Feasibility | Devin |
| 2026-10-01 | Recorded ADR-002 provenance as a non-substantive historical/documentation limitation without editing the Accepted ADR or changing DEC-002. | Product Owner ADR-002 provenance disposition | Devin |
| 2026-10-01 | ARCH-B2 PASS recorded; Part 1 Architecture complete and B.3 is the next prescribed gate. | Product Owner ARCH-B2 approval | Devin |

**Status:** Sections 1–14 validated; ADR-001 through ADR-004 Accepted; ARCH-B2 PASS recorded.

---

## Document History

| Version | Date | Author | Changes | Reviewed By |
|---|---|---|---|---|
| 0.1 | 2026-10-01 | Devin | Initial B.2 Section 1 draft from approved B.1 package. | Jairo Enrique Diaz |
| 0.2 | 2026-10-01 | Devin | Drafted B.2 Section 2 Architecture Approach without selecting Deferred/Open options. | Jairo Enrique Diaz |
| 0.3 | 2026-10-01 | Devin | Drafted B.2 Section 3 logical components and flows without selecting physical implementation. | Jairo Enrique Diaz |
| 0.4 | 2026-10-01 | Devin | Drafted B.2 Section 4 decisions and technology status with all unresolved choices marked TBD. | Jairo Enrique Diaz |
| 0.5 | 2026-10-01 | Devin | Drafted B.2 Section 5 security, scalability, deployment, and monitoring status without selecting operational technologies. | Jairo Enrique Diaz |
| 0.6 | 2026-10-01 | Devin | Drafted B.2 Section 6 future-state journey and open questions without resolving Deferred/Open decisions. | Jairo Enrique Diaz |
| 0.7 | 2026-10-01 | Devin | Added explicit B.2 closure disposition for remaining architecture questions; no Deferred/Open decision resolved. | Jairo Enrique Diaz |
| 0.8 | 2026-10-01 | Devin | Drafted Sections 7–14 with bounded security, quality, deployment, monitoring, journey, questions, enrichment, and history treatment. | — |
