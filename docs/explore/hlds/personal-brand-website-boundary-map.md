# Boundary Map: HLD · Personal Brand Website

**Date**: 2026-10-01
**Status**: Validated — B.1 PASS
**Architect**: Devin
**Slug**: `personal-brand-website`
**Evidence discipline**: `[OBS]` observed from approved artifacts; `[INF]` bounded interpretation; `[ASM]` unresolved assumption or open question.

---

## 1. Truth Hierarchy

The full authority map and document classification are maintained in [`personal-brand-website-truth-hierarchy.md`](personal-brand-website-truth-hierarchy.md). The governing rule is scope-based authority: no artifact has universal precedence outside its approved scope, and directional/source inputs cannot override later canonical decisions.

Key authority boundaries:

- A3 governs domain vocabulary, entities, relationships, rules, Evidence/publication terminology, mappings, prominence, narrative roles/themes, and lifecycles.
- The PRD governs requirements, NFRs, constraints, exclusions, success criterion, and deferred decisions.
- A10 governs the approved eight-screen experience, flows, progressive disclosure, accessibility principles, and non-linear journey.
- B4, B5, B6, Part C, Architecture Context, Technical Feasibility, and the approved B.0 profile govern their respective scopes.

Evidence: `[OBS]` approved handoff, A3, PRD, A10, B4, B5, B6, Part C, Architecture Context, Technical Feasibility, B.0 profile.

---

## 2. Ownership Matrix

| # | Domain | Owns (authoritative) | Consumes (depends on) | Produces (hands off to) | Evidence |
|---:|---|---|---|---|---|
| 1 | Context Warehouse / Professional Knowledge | Governed source knowledge; Career Experience; factual Projects; Evidence; source facts; references; sensitivity metadata. | Foundation documents, CV, Project Knowledge Base, approved A3 model, and governed content inputs. | Validated factual knowledge and Evidence to Project Story Curation / Publication Governance. | `[OBS]` A3, Context, Architecture Context |
| 2 | Project Story Curation / Publication Governance | Project Story; narrative role; visitor prominence; publication class; approval state; public-content eligibility. | Validated Projects, Evidence, source facts, publication rules, and Content Owner decisions. | Approved public content to Public Website Experience through a logical handoff only. | `[OBS]` A3, PRD, Architecture Context |
| 3 | Public Website Experience | Page / Experience presentation structure; approved navigation; progressive-disclosure presentation; public visitor journey. | Approved public Project Stories and eligible public entities; A10 experience rules; B4/B5/B6 design inputs. | Visitor-facing pages and approved external links/downloads; measurement output is conditional on a future approved decision and remains unresolved. | `[OBS]` A10, PRD, B4, B5, B6, Architecture Context; `[ASM]` measurement |
| 4 | External Destinations — adjacent boundary | External LinkedIn, email, phone, and CV destination availability and behavior. Application ownership or API contract is not established. | Visitor actions originating from the Public Website Experience. | External navigation or download outcomes; no application contract is required by the approved scope. | `[OBS]` A10, Technical Feasibility, Architecture Context |
| 5 | Analytics / Measurement — adjacent boundary | **UNRESOLVED** — mechanism, event set, privacy, consent, retention, baseline, and operational ownership are not selected. | **UNRESOLVED** — any future approved measurement events from the Public Website Experience. | **UNRESOLVED** — future measurement data and post-launch validation inputs. | `[ASM]` PRD NFR-007, Architecture Context, Part C |

### Ownership gaps preserved as unresolved

1. Curated-content/build/runtime boundary ownership.
2. Publication-control enforcement ownership and stage.
3. Analytics/measurement ownership and runtime boundary.
4. Hosting/deployment/preview/rollback/release operational ownership.

These responsibilities are not assigned by inference.

The Curation → Public Website handoff is logical only. It does not select the physical content representation, CMS/file approach, schema, build mechanism, runtime boundary, or ownership.

---

## 3. Upstream Dependencies

| # | Dependency | Source Domain | Type | Contract Status | Evidence |
|---:|---|---|---|---|---|
| 1 | Approved A3 domain vocabulary, entities, relationships, rules, Evidence/publication model, mappings, prominence, and lifecycles | A3 Domain Analysis | Data / authority | Exists | `[OBS]` |
| 2 | Validated Projects and Evidence supplied to Project Story Curation / Publication Governance | Context Warehouse / Professional Knowledge | Data | PROVISIONAL — logical source is defined, but the structured content contract and representation are unresolved | `[OBS]` / `[ASM]` |
| 3 | Approved public Project Stories and related eligible public content supplied to the Public Website Experience | Project Story Curation / Publication Governance | Data | PROVISIONAL — logical handoff is defined, but curated-content/build/runtime ownership and physical representation are unresolved | `[OBS]` / `[ASM]` |
| 4 | Approved PRD requirements, NFRs, constraints, exclusions, and deferred decisions | Approved PRD | Data / authority | Exists | `[OBS]` |
| 5 | Approved A10 screen hierarchy, flows, progressive disclosure, accessibility principles, and non-linear journey | A10 Experience Design | Data / experience contract | Exists as approved experience input; implementation contract is not selected | `[OBS]` |
| 6 | Approved B4 semantic mapping and B5/B6 design-system inputs | B4 OOUX, B5 Design Language, B6 Design System | Data / design contract | Exists as approved design input; code/component implementation mapping remains downstream | `[OBS]` |
| 7 | External Contact and CV destinations: LinkedIn, email, phone, and CV asset | External Destinations | Link / static asset | PROVISIONAL — approved mechanisms exist conceptually, but final values/assets and publication readiness remain open | `[OBS]` / `[ASM]` |
| 8 | Analytics and measurement events/data | Analytics / Measurement | Data | PROVISIONAL — measurement events, mechanism, privacy, consent, retention, baseline, and ownership remain unresolved | `[ASM]` |
| 9 | Hosting, deployment, preview, rollback, and release capability | Hosting / Operations | Operational dependency | PROVISIONAL — provider, operating model, deployment model, and ownership remain unresolved | `[ASM]` |

No dependency is classified as `Needs Creation`.

None has been promoted to a blocker because no specific dependency has yet been shown to prevent safe B.1.2 progression.

The five provisional dependency areas remain visible for later solutioning and implementation clarification. No API, event, or service contract has been created.

---

## 4. Platform Conventions

| # | Convention | Adjacent HLD Source | Pattern | Recommendation | Justification | Evidence |
|---:|---|---|---|---|---|---|
| — | None identified | None available | — | No inherit/deviate decision | No adjacent HLD exists; generic architecture patterns are not imported as project conventions. | `[OBS]` |

The approved B.0 engagement-specific patterns remain architecture context/guidance, not inherited platform standards:

- governed source-to-public-content pipeline;
- bounded-context separation;
- governed publication and human approval;
- static/build-time content delivery as preferred but unresolved;
- progressive disclosure / hub-and-spoke experience pattern.

---

## 5. Open Questions

All questions remain open. `Blocking?` describes whether the question blocks final B.1.2 mapping; several must still be resolved before implementation, publication, release, or measurement.

| # | Question | Source | Impact | Blocking? | Proposed Resolution |
|---:|---|---|---|---|---|
| 1 | Which frontend stack and language should implement the approved frontend-only MVP? | `[ASM]` PRD / Architecture Context | Affects implementation structure, tooling, accessibility validation, and maintainability. | No for B.1.2; yes before implementation. | Present viable options and trade-offs at a later approved architecture gate. |
| 2 | Which content representation should be used, including governed files versus CMS? | `[ASM]` PRD / Architecture Context | Affects content maintenance, relationships, governance metadata, and build preparation. | No for B.1.2; yes before implementation. | Validate against representative Project and Project Story content; present options later. |
| 3 | At which stage and through which mechanism is publication eligibility enforced? | `[ASM]` PRD / Architecture Context / Part C | Restricted, unclassified, or ineligible content must not reach public deployment assets. | No for B.1.2; yes before safe publication. | Evaluate content-preparation, pre-build, build, deployment, or combined enforcement options. |
| 4 | Who owns the curated-content/build/runtime boundary? | `[ASM]` Architecture Context / Part C | Ambiguous ownership could weaken change control and publication safety. | No for B.1.2; yes before implementation. | Define ownership through an approved architecture decision. |
| 5 | How does approved public content move logically from Curation to the Public Website Experience? | `[OBS]` / `[ASM]` Architecture Context | Logical handoff is known, but physical representation, schema, build mechanism, and runtime boundary are not selected. | No for B.1.2; yes before implementation. | Resolve only through a later architecture option; do not infer a CMS, file model, API, or build contract. |
| 6 | Can a representative Project / Project Story sample safely represent the A3 model and governance metadata? | `[ASM]` Technical Feasibility / Architecture Context | File-based or other content feasibility remains unsubstantiated. | No for B.1.2; yes before implementation/publication. | Perform representative content validation during later solutioning. |
| 7 | Can contextual navigation be generated from approved relationships without backend functionality? | `[ASM]` Architecture Context | May affect content structure and build capability. | No for B.1.2; yes before implementation. | Validate against A3 relationships and A10 navigation without converting CTAs into domain relationships. |
| 8 | Which hosting provider and operating model meet HTTPS and proportional reliability needs? | `[ASM]` PRD / Technical Feasibility / Architecture Context | Affects public delivery, operational reliability, preview, and cost trade-offs. | No for B.1.2; yes before release. | Present hosting options and trade-offs; provider remains unselected. |
| 9 | What deployment, preview, rollback, and release model is appropriate? | `[ASM]` PRD / Technical Feasibility / Architecture Context | Affects operational readiness and the local-validation target. | No for B.1.2; yes before release. | Define through later architecture and DevOps strategy work. |
| 10 | Are measurement events required and, if so, what event set and mechanism are appropriate? | `[ASM]` PRD NFR-007 / Part C / Architecture Context | Affects measurement readiness and possible runtime-boundary changes. | No for B.1.2; yes before measurement implementation. | Determine later whether measurement events are required and, if so, define the minimum appropriate event set and mechanism. |
| 11 | What privacy, consent, retention, and minimization treatment applies to analytics? | `[ASM]` PRD / Part C / Architecture Context | May affect runtime, data boundaries, and future residency considerations. | No for B.1.2; yes before analytics implementation. | Resolve as part of the later analytics/privacy architecture decision. |
| 12 | What responsive implementation breakpoints should be used? | `[ASM]` PRD / Part C / Architecture Context | Affects implementation and responsive validation. | No for B.1.2; yes before implementation. | Closed by D-013 (768px and 1024px, mobile-first). B6 values of 375/768/1440 remain Figma reference frames only. %%Updated 2026-10-20.%% |
| 13 | What formal accessibility conformance level, if any, should be adopted? | `[ASM]` PRD / Part C / Architecture Context | Affects formal validation criteria; qualitative accessibility requirements already apply. | No for B.1.2; yes before formal conformance testing. | Product Owner decision during later architecture/implementation planning. |
| 14 | How will the frontend-only MVP satisfy all approved requirements, especially publication safety and measurement readiness? | `[ASM]` PRD / Technical Feasibility / Part C | Determines whether the intended MVP boundary is sufficient. | No for B.1.2; yes before architecture finalization. | Evaluate explicitly during B.1 design direction and later HLD solutioning. |
| 15 | What are the final public Contact values and CV asset path? | `[ASM]` PRD / A10 / Technical Feasibility | Publication readiness depends on complete and valid contact/download destinations. | No for B.1.2; later governed content/implementation readiness. | Closed by D-021 (2026-10-20). %%Updated 2026-10-20: contact values and CV path approved.%% |
| 16 | Which Project Story previews, ordering, summary fields, Related / Next links, and disclosure mechanism will be finalized? | `[ASM]` PRD / A10 | Affects content readiness and detailed presentation. | No for B.1.2; later content/implementation unless an architecture dependency is demonstrated. | Closed by D-014, D-020, and D-025 (2026-10-20 and 2026-10-22); A3 mappings unchanged. %%Updated 2026-10-22.%% |
| 17 | How should the qualified Tigo → Avianca → DFA evolution arc be presented in public content? | `[OBS]` A3 / PRD / A10; copy remains open | Final narrative treatment must preserve qualifications and must not become a mandatory visitor route. | No for B.1.2; later governed content/copy. | Governed content preparation and final copy approval, preserving the approved A3 arc and qualifications. |
| 18 | How should B5/B6 design tokens and the approved `type/code` exception map to implementation? | `[OBS]` B5 / B6; implementation mapping unresolved | Affects design-system implementation without changing approved tokens or Figma infrastructure. | No for B.1.2; later design-system/implementation unless an architecture dependency is demonstrated. | Resolve during design/implementation planning; no substitute font or placeholder style. |

### Ownership gaps carried forward

- Curated-content/build/runtime boundary ownership.
- Publication-control enforcement ownership and stage.
- Analytics/measurement ownership and runtime boundary.
- Hosting/deployment/preview/rollback/release operational ownership.

### Provisional dependency areas carried forward

- Structured Project / Evidence content contract.
- Approved public-content handoff contract.
- Final Contact/CV destination and asset readiness.
- Measurement/privacy contract.
- Hosting/deployment operational contract.

No dependency is promoted to a blocker at this stage.

---

## 6. Enrichment Log

| Date | Change | Source | Updated By |
|---|---|---|---|
| 2026-10-01 | Compiled final B.1.2 boundary map from approved truth hierarchy, ownership matrix, dependency mapping, platform-convention review, and open-question checkpoint. | Approved canonical artifacts and Product Owner checkpoint responses | Devin |
| 2026-10-01 | ARCH-B1b and overall B.1 PASS recorded; boundary map validated with DEC-004 preserved as Deferred/Open. | Product Owner B.1 PASS | Devin |

---

## 7. Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-10-01 | Devin | Initial B.1.2 boundary map draft for ARCH-B1b review. |
