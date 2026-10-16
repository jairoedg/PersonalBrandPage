# Architecture Engagement Brief · Personal Brand Website

**Status**: B.1 PASS — Architecture Direction Approved
**Engagement start**: 2026-10-01
**Slug**: `personal-brand-website`
**Explore type**: Explore Readiness Check (ERC)
**Architect / Lead Engineer**: Devin
**Product Owner / Content Owner**: Jairo Enrique Diaz
**Evidence discipline**: `[OBS]` observed from approved artifacts; `[INF]` bounded interpretation; `[ASM]` unresolved assumption or open question.

---

## 1. Engagement Scope

This engagement defines the architecture direction for an evidence-based professional portfolio website that complements Jairo Enrique Diaz's CV. It must preserve the approved product, domain, experience, design, risk, and architecture-context decisions while resolving architecture questions through explicit options, trade-offs, evidence, assumptions, and human gates.

The engagement covers B.1 Context & Design Direction only at this stage. B.2 HLD drafting, ADR finalization, test strategy, DevOps strategy, epic forming, and Govern Readiness remain downstream and gated.

## 2. Architecture Context

### Existing architecture state `[OBS]`

- Greenfield website runtime; no existing website runtime architecture is being inherited.
- Context Warehouse is governed source context, not the public website runtime source.
- Approved target-context flow: Context Warehouse → curated/publication-eligible content → build output → hosting/CDN → visitor browser.
- No final frontend framework, content representation, CMS, hosting provider, deployment pipeline, analytics mechanism, or runtime observability approach is selected.

### Explore and engagement direction `[OBS]`

- ERC engagement with approved PRD and approved Step 4 experience/design artifacts.
- MVP has exactly eight approved screens: Home, Projects, Project Story Detail, Contact, How I Can Help, Leadership, Career Journey, and About.
- Project and Project Story remain distinct.
- Evidence/publication boundaries remain A3-governed.
- A10 supports progressive disclosure, scannability, accessibility, and non-linear exploration.
- B4 remains 5 Core / 15 Supporting / 0 Boundary.
- B5 token boundaries and B6 Figma infrastructure remain preserved.
- Part C accepted residual-risk set remains empty.

## 3. Architecture Drivers

The approved Architecture Context ranks these drivers:

1. Publication eligibility and restricted-Evidence separation — hard constraint.
2. Context Warehouse/runtime boundary — hard constraint.
3. Evidence truthfulness and traceability — hard constraint.
4. Project/Project Story separation — hard constraint.
5. MVP complexity boundary — hard constraint.
6. Simple, maintainable delivery compatible with the local-validation target — delivery driver.
7. File-based governed-content feasibility — soft preference and open validation candidate.
8. Static/build-time delivery feasibility — soft preference and open validation candidate.
9. Progressive disclosure with accessible scanning — MUST functional/quality driver.
10. Hosting reliability, HTTPS, preview, and rollback — proportional operational driver.

The Product Owner's B.0 trade-off prioritization is recorded for option comparison, not as a pre-existing canonical fact:

1. Truthfulness and publication safety.
2. Boundary integrity and domain separation.
3. Accessibility, responsive usability, and scannability.
4. Maintainability and proportional simplicity.
5. Secure and reliable delivery.

Measurement readiness remains a cross-cutting concern outside the top-five ordering.

## 4. Constraints

- Frontend-only MVP boundary; no custom backend, database, authentication, runtime personalization, real-time behavior, or unsupported backend-dependent functionality absent an approved requirement or identified risk.
- Context Warehouse is not the public website runtime content source.
- Only publication-eligible content may become public; internal/restricted Evidence may support claims without becoming public.
- Public claims must be truthful, traceable, attributable, and defensible.
- Project and Project Story remain distinct; Project Stories derive from validated Projects.
- HTTPS is required of selected production hosting; provider and operating model remain unselected.
- Accessibility and responsive usability are mandatory; formal conformance target and implementation breakpoints remain unresolved.
- Preserve exactly eight approved screens, approved flows, progressive disclosure, scannability, Contact model, and non-linear exploration.
- Markdown/file-based governed content and static/build-time delivery remain preferred but unselected directions.
- Analytics measures/events, mechanism, privacy, consent, retention, baseline, and implementation remain unresolved.
- Mid-October 2026 is a local-validation target, not a committed production-release date.
- Simple/reliable/maintainable/low-cost remains a project trade-off preference, not a technology decision.
- Added complexity requires an approved requirement or identified risk.

## 5. Bounded Contexts `[OBS]`

1. **Context Warehouse / Professional Knowledge** — governed professional knowledge and factual Evidence.
2. **Project Story Curation / Publication Governance** — validated Projects, approved narratives, publication eligibility, prominence, and narrative role.
3. **Public Website Experience** — presentation of approved public content through the visitor journey and approved pages.

These are responsibility boundaries and do not select separate services, databases, APIs, or deployment units.

## 6. Open Architecture Questions `[ASM]`

The following remain intentionally unresolved and must be handled through later options/trade-off gates:

- frontend stack;
- content representation, including file-based content versus CMS;
- publication-control enforcement stage and mechanism;
- curated-content/build/runtime boundary and ownership;
- hosting provider and operating model;
- deployment, preview, rollback, and release model;
- analytics measures/events, mechanism, privacy, consent, retention, and baseline;
- responsive implementation breakpoints;
- formal accessibility conformance level;
- representative governed Project/Project Story validation;
- how the frontend-only boundary satisfies the approved requirements.

## 7. Quality and Hardening Scope

B.0-derived hardening checks remain checks, not new requirements. B.1 must preserve checks for A3 model integrity, Project/Project Story separation, Evidence traceability, publication safety, context boundaries, approved experience flows, accessibility/responsiveness, secure/proportional delivery, measurement/privacy boundaries, design-system preservation, and decision/regression discipline.

## 8. Required B.1 Outputs

- Engagement brief — this document.
- Decision log — initialized and maintained throughout B.1–B.4.
- Blocker register — initialized and maintained throughout B.1–B.4.
- Boundary map and truth hierarchy — B.1.2, after ARCH-B1a confirmation.
- Design sketch — B.1.3, after ARCH-B1b confirmation.

## 9. Source Authority

A3 remains authoritative for domain entities, relationships, rules, Evidence/publication terminology, mappings, prominence, narrative roles/themes, and lifecycles. The approved PRD governs requirements, NFRs, constraints, exclusions, success criterion, and deferred decisions. A10 governs experience and visitor-flow decisions. B4, B5, B6, Part C, Architecture Context, and Technical Feasibility govern their approved respective scopes.

## Decision Gate

**ARCH-B1a** — Product Owner approved the architecture engagement scope on 2026-10-01.

**Overall B.1 gate** — PASS; Product Owner approved the architecture direction on 2026-10-01. B.2 transition remains separately authorized.

---

## Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-10-01 | Devin | Initial B.1.1 engagement scope from approved Explore artifacts. |
