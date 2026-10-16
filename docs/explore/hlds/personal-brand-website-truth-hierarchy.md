# Truth Hierarchy: Personal Brand Website

**Status**: Validated — B.1 PASS
**Created**: 2026-10-01
**Last Validated**: 2026-10-01
**Validated By**: Jairo Enrique Diaz — Product Owner, B.1 PASS
**Domain**: Personal Brand Website — references the approved B.0 domain profile for authority-pattern guidance
**Evidence discipline**: `[OBS]` observed from approved artifacts; `[INF]` bounded interpretation; `[ASM]` unresolved assumption or open question.

---

## Authority Map

Authority patterns suggested by the approved domain profile:

- A3 Domain Analysis owns domain vocabulary, entities, relationships, rules, Evidence/publication terminology, mappings, prominence, narrative roles/themes, and lifecycles.
- Product and experience authorities are scoped to approved PRD and A10 responsibilities.
- B4, B5, B6, Part C, Architecture Context, and Technical Feasibility govern their approved respective scopes.
- Authority is scope-based; no artifact has universal precedence outside its approved scope.

| # | Authority | Scope | Consumers | Constraints | Evidence |
|---:|---|---|---|---|---|
| 1 | A3 Domain Analysis | Domain vocabulary, entities, relationships, business rules, Evidence/publication terminology, Capability mappings, narrative roles/themes, prominence, and lifecycles. | Content model, curation, architecture, experience mapping, implementation. | Do not add or reinterpret entities, relationships, mappings, rules, or lifecycle states by inference. | `[OBS]` |
| 2 | Approved PRD | Product requirements, NFRs, constraints, exclusions, success criterion, and deferred product/architecture questions. | Architecture, experience, implementation planning, validation. | Architecture must preserve requirements and must not turn deferred choices into approved decisions. | `[OBS]` |
| 3 | A10 Experience Design | Eight-screen inventory, screen hierarchy, responsibilities, flows, progressive disclosure, accessibility principles, and non-linear journey. | Public Website Experience, UX, frontend implementation. | Navigation and CTAs remain experience-level; they do not become A3 domain relationships. | `[OBS]` |
| 4 | B4 OOUX Mapping | 5 Core / 15 Supporting / 0 Boundary classification, CTA mappings, state distinctions, and preservation boundaries. | Semantic and experience design. | A3 remains canonical for domain relationships; internal Project/Evidence governance is not visitor-facing. | `[OBS]` |
| 5 | B5 Design Language | Approved visual and motion tokens, reserved-token boundaries, and `type/code` rule. | Design and implementation styling. | Reserved tokens do not authorize product behavior, screens, components, or interaction mechanisms. | `[OBS]` |
| 6 | B6 Design System | Approved six-page Figma infrastructure, layout grids, token verification, and `type/code` accounting exception. | Design-system implementation. | Preserve 10 physical Text Styles plus one approved documented exception; no substitute font or placeholder style. | `[OBS]` |
| 7 | Part C / Risk Decisions | Risks, dispositions, simulated-validation limitations, assumptions, SD-1/SD-2, and accepted-risk set. | Architecture trade-offs, hardening, later validation. | Simulated validation is not empirical; accepted residual-risk set remains empty. | `[OBS]` |
| 8 | Architecture Context | Primary Step 5 architecture baseline, drivers, constraints, bounded-context sketch, open questions, and carried-forward risks. | B.1 solutioning and later HLD work. | It identifies open questions; it does not resolve frontend, content, publication, hosting, deployment, or analytics choices. | `[OBS]` |
| 9 | Approved B.0 Domain Profile | Approved onboarding vocabulary/index, bounded contexts, constraints, authority guidance, quality prioritization, patterns, and derived hardening checks. | B.1 architecture context and trade-off framing. | Does not override A3 or select deferred architecture options. | `[OBS]` |
| 10 | Technical Feasibility | Feasibility constraints, data realities, dependencies, operational concerns, and validation candidates. | Architecture and delivery planning. | Feasibility candidates remain candidates until a later approved decision. | `[OBS]` |
| 11 | Context | Problem baseline, stakeholders, governance, system boundary, and assumptions. | Engagement scope, architecture, stakeholder alignment. | Stakeholder roles are preserved only as directly supported by canonical artifacts. | `[OBS]` |
| 12 | Explore Bundle | Approved Explore scope, ERC type, assumptions, strategic constraints, source context, and initial risks. | Engagement setup and lifecycle traceability. | Later approved artifacts govern where they refine or supersede earlier scope detail. | `[OBS]` |
| 13 | Approved Ideation Concepts | Credible Story Layers, Evidence Paths, Not Funnel, and Capability and Growth Threads as approved direction seeds. | Design direction and later concept mapping. | Concepts do not create new entities, relationships, services, APIs, databases, or runtime recommendation behavior. | `[OBS]` |
| 14 | Derived Domain Routing Input | Locked routing/index reference to approved A3 domain content. | Step 4 design-pipeline routing. | Not an independent domain authority; A3 governs conflicts. | `[OBS]` |
| 15 | Approved Foundation Documents | Brand identity, product vision, Recruiter Journey, website strategy, roadmap, and strategic decisions. | Strategic context and consistency checks. | Directional/supporting for Step 5; cannot override later approved canonical artifacts. | `[OBS]` |
| 16 | Project Knowledge Base and converted CV | Source material for factual professional knowledge and future content preparation. | Content curation and Evidence assessment. | Source material is not automatically website-ready or publication-eligible. | `[OBS]` |
| 17 | HLD Template Utility | Required architecture-document structure, evidence-labeling rules, and diagram conventions. | HLD artifact production. | Process/template authority only; does not decide product or architecture content. | `[OBS]` |

### Precedence rules

1. No artifact has universal precedence outside its approved scope.
2. A3 remains authoritative for the domain model even when another artifact presents a design or architecture interpretation.
3. The PRD governs product requirements and deferred decisions.
4. A10 governs the visitor experience; navigation and CTAs do not become domain relationships.
5. Directional or source inputs cannot override later canonical decisions.
6. The approved Curation → Public Website handoff is logical only; physical content representation, CMS/file approach, schema, build mechanism, runtime boundary, and ownership remain unresolved.

---

## Document Classification

| # | Document | Type | Classification | Rationale |
|---:|---|---|---|---|
| 1 | A3 Domain Analysis | Domain analysis | Canonical | Product Owner-approved authority for the domain model and rules. |
| 2 | Approved PRD | PRD | Canonical | Product Owner-approved product definition and deferred decisions. |
| 3 | A10 Wireframes and Flows | Experience design | Canonical | Approved experience inventory, flows, hierarchy, and accessibility principles. |
| 4 | B4 OOUX | Semantic mapping | Canonical within B4 scope | Approved object mapping and preservation boundaries; A3 remains domain authority. |
| 5 | B5 Design Language | Design specification | Canonical within B5 scope | Approved token specification and reserved-token boundaries. |
| 6 | B6 Design System | Design-system infrastructure | Canonical within B6 scope | Product Owner-approved Figma infrastructure and token accounting. |
| 7 | Part C Risks | Risk/validation decisions | Canonical within risk scope | Approved lifecycle dispositions and empty accepted-risk set. |
| 8 | Architecture Context | Architecture context | Canonical primary Step 5 input | Approved baseline, drivers, constraints, and open questions. |
| 9 | B.0 Domain Profile | Persistent onboarding profile | Canonical within onboarding scope | Product Owner-approved B.0 domain framing and guidance. |
| 10 | Technical Feasibility | Feasibility analysis | Canonical within feasibility scope | Approved feasibility findings and validation candidates. |
| 11 | Context | Context baseline | Canonical within context scope | Approved problem, stakeholder, governance, and system-boundary baseline. |
| 12 | Explore Bundle | Scope statement | Canonical within engagement scope | Approved ERC scope, assumptions, and initial risks. |
| 13 | Approved Ideation Concepts | Direction seeds | Directional/approved | Approved creative and product direction; no architecture selection. |
| 14 | Derived Domain Routing Input | Domain index | Locked routing/index | Useful routing reference; not independent authority. |
| 15 | Foundation Documents | Strategic context | Directional/supporting | Approved strategic context, but later canonical artifacts govern Step 5 specifics. |
| 16 | Project Knowledge Base / CV | Source corpus | Directional/source | Factual source material requiring later normalization and Evidence/publication review. |
| 17 | HLD Template Utility | Process/template | Canonical process authority | Governs document structure, not product or architecture decisions. |
| 18 | Adjacent HLDs | Adjacent architecture | Not available | No adjacent HLD exists for convention inheritance or deviation. |

---

## Authority Conflicts

| # | Conflict | Domain A Claims | Domain B Claims | Resolution | Status |
|---:|---|---|---|---|---|
| — | None identified | — | — | Scope-based authority model applies; no conflict requires escalation at B.1.2. | Closed for current mapping |

Known stale administrative wording in upstream artifacts is governed by the approved handoff and later approved lifecycle status; it is not treated as a substantive authority conflict.

---

## Re-validation History

| Date | Trigger | Changes | Approved By |
|---|---|---|---|
| 2026-10-01 | ARCH-B1a engagement-scope review | Architecture engagement scope approved; no universal precedence introduced. | Jairo Enrique Diaz — Product Owner |
| 2026-10-01 | B.1.2 / ARCH-B1b review | Truth hierarchy and classifications approved; scope-based authority model preserved. | Jairo Enrique Diaz — Product Owner |

---

## Enrichment Log

| Date | Change | Source | Updated By |
|---|---|---|---|
| 2026-10-01 | Compiled truth hierarchy from approved B.0 Steps 1–4, B.1.1 scope, and B.1.2 artifact inventory. | Approved canonical artifacts and Product Owner checkpoint responses | Devin |

---

## Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-10-01 | Devin | Initial B.1.2 truth hierarchy draft for ARCH-B1b review. |
