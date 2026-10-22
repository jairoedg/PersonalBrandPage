---
domain: "Personal Brand Website"
slug: personal-brand-website
source: explore/explore-personal-brand-website/domain-analysis.md
glossary_version: 2026-09-22
validated_by: "Jairo Enrique Diaz — PRD-DOMAIN mapping"
explore_type: ERC
evidence_label: "A3 terms: OBS; domain mapping: Product Owner-approved"
---

# PRD · Personal Brand Website

**Status:** Approved — Product Owner sign-off recorded; Explore Step 4 COMPLETE / APPROVED  
**Priority:** High (Signal severity 4)  
**Stakeholder Appetite:** High (Signal resonance 4)  
**Created:** 2026-09-28  
**Last Updated:** 2026-09-28

**Domain mapping provenance:** “Personal Brand Website” is the Product Owner-approved Step 4 single-PRD mapping label. The A3 Domain Analysis artifact is titled “Domain Analysis: Personal Brand Website”; this mapping does not assert that A3 separately enumerated a formal PRD domain by that name.

**Related Documents:**
- Signal: [Personal Brand Page Website](20260908-personal-brand-website.md)
- Context: [context.md](context.md)
- Technical Feasibility: [technical-feasibility.md](technical-feasibility.md)
- Architecture Context: [architecture-context.md](architecture-context.md)
- Domain Analysis: [domain-analysis.md](domain-analysis.md)
- Personas: [personas-personal-brand-website.md](personas-personal-brand-website.md)
- Approved Recruiter Journey: [03-recruiter-journey.md](03-recruiter-journey.md)
- A10 Wireframes and Flows: [wireframes-personal-brand-website.md](wireframes-personal-brand-website.md)
- Approved Step 3 concepts: [personal-brand-website-refined-concepts.md](personal-brand-website-refined-concepts.md)
- Raw Ideation: [personal-brand-website-ideas-raw.md](personal-brand-website-ideas-raw.md)
- Explore Bundle and existing risks: [explore-bundle.md](explore-bundle.md)
- Discovery Index: [discovery.md](discovery.md) — not modified; the Step 3 approval is recorded in the refined-concepts artifact.
- No separate Hypothesis, Journey Map, Market Research, Regulatory Compliance, HLD, or `risks.md` artifact was produced; A8, A7, A2, and A4 were intentionally excluded, and HLD/`risks.md` remain pending.

---

## Problem Statement

**User Need:**

Recruiters and hiring managers have only a concise CV to assess Jairo’s delivery-leadership experience, project complexity, business outcomes, leadership decisions, and professional evolution. This leaves them with a partial profile when judging role fit and comparable problem-solving. Jairo needs an authoritative professional reference that complements—not replaces—the CV and helps visitors assess the evidence and value behind his career.

**Background:** The approved context baseline identifies the short-form CV as insufficient to communicate the depth of Jairo’s project work and leadership. The website is intended to complement the CV, not replace it, with an evidence-based professional reference.

---

## Goals

**What success looks like:**

1. **Support relevance and confidence across the overall experience.** Help visitors understand who Jairo is, what value he brings, whether he has solved similar problems, how he leads, whether they can trust him, and how to contact him.
2. **Make professional evidence understandable and defensible.** Present approved Project Stories and related context so P1 and P2 can assess relevant experience and deeper examples without unsupported claims or publication-ineligible content.
3. **Carry the three ID-9-approved concept inputs into product definition as distinct dimensions:** Credible Story Layers at the individual Project Story level; Evidence Paths, Not Funnel across approved relationships and visitor-selected exploration; and Capability and Growth Threads at the collective portfolio-evidence level. Their inclusion does not select a final product direction, combine them, or create three requirement sets.

---

## Success Measures and Product Success Criteria

| Category | Baseline | Target / criterion | Measurement method and timing |
|---|---|---|---|
| **Approved overall product success criterion** | No pre-launch website baseline exists. | Within the overall five-minute objective, a P1 visitor can obtain sufficient information from the experience to answer the six approved strategy questions. This is not a per-screen, per-transition, or forced-consumption target. | Validation method remains unresolved. No usability-testing method, sample definition, completion percentage, analytics mechanism, or additional numeric threshold is proposed here. |
| **Mandatory evidence/publication quality criterion** | Final publishable content has not been assessed as a whole. | Material public claims must be traceable, attributable, defensible, and publication-eligible under A3; internal/restricted Evidence is not automatically public. | Apply the existing A3 evidence and publication rules; any implementation mechanism remains deferred. |
| **Desired post-launch business outcomes—not quantified KPIs** | No post-launch behavioral baseline exists. | Foundation-supported directions: more recruiter contacts, more interview invitations, better interview quality, greater visibility for senior delivery opportunities, and better consistency among Website, CV, and LinkedIn. Quantitative targets remain open. | Baselines, target values, measurement definitions, and analytics mechanisms remain TBD. The foundation specifies a twelve-month outcome horizon. |

The five-minute objective and six overall strategy questions are approved. Business outcomes are recorded only as directional outcomes; no numeric KPI target or measurement mechanism is invented.

---

## Target Users

### Primary Users

- **P1 — Technical Recruiter / Talent Acquisition:** assesses experience fit against job requirements first, then the profile summary, years of experience, and certifications.
- **P2 — Hiring Manager:** examines relevant experience more deeply and uses situational questions to understand comparable problems and responses.

### Secondary Users / Contexts

- **P3 — grouped Delivery and Technology Leader:** remains one grouped context; specific evidence priorities are unknown. No P3-specific requirement or navigation is added.
- Consulting clients and other professional visitors remain secondary audience contexts, not additional personas.

**User Segments:** Preserve the approved three-persona model. Device priority, usage context, ATS behavior, and unsupported P3 evaluation needs remain unknown.

---

## User Flows & Scenarios

**Reference:** Approved A10 flows in [wireframes-personal-brand-website.md](wireframes-personal-brand-website.md). The separate A7 Journey Map was intentionally excluded; the approved foundation Recruiter Journey and A10 flows are used.

### Primary Flow — F1: Primary Relevance-to-Contact

Home establishes identity, positioning, profile summary, and evidence entry; Projects supports Project Story selection; Project Story Detail supports orientation and deeper evaluation; Contact provides Email, LinkedIn, Phone, and the secondary CV download. Approved alternate paths include Home → Contact, Project Story Detail → Projects or Related / Next Exploration, and any approved screen → global navigation.

### Alternative Flows

- **F2 — Direct Contact:** Open Contact from an approved entry point and choose an approved contact method or the supporting CV download.
- **F3 — Exploratory Supporting Context:** Visit one or more approved P1 screens before or after Projects/Project Story Detail; proceed to Contact when ready.
- **F4 — Project Story Deep-Evaluation and Return:** Start from Projects or an approved related link, examine one Project Story progressively, and continue to related approved context, Projects, or Contact.

These flows preserve the Recruiter Journey as a confidence-building progression, not a mandatory linear funnel. No separate runtime recommendation logic is introduced.

### Edge Cases

- Incomplete or ineligible Project Stories are prevented from public publication; they are not normal visitor-facing runtime states.
- Restricted Evidence and unsupported material claims must not enter public content.
- If one external contact destination is unavailable, other approved contact methods remain available; no runtime destination-health detection is introduced.
- Missing CV/contact assets and broken links are publication/readiness concerns with fallbacks where A10 specifies them.

---

## Functional Requirements

These requirements preserve approved A3/A10 scope. The three concepts are distinct inputs, not three requirement sets.

| ID | Requirement | User Story | Acceptance Criteria | Priority / scope |
|---|---|---|---|---|
| **R-001** | Provide the approved screen inventory. | As a visitor, I want the approved website screens available so I can understand Jairo’s profile, evidence, context, and contact paths. | - [ ] The MVP contains exactly Home, Projects, Project Story Detail, Contact, How I Can Help, Leadership, Career Journey, and About.<br>- [ ] Preserve P0/P1 as A10 experience-role classifications.<br>- [ ] Do not add screens. | **MUST — required MVP scope.** P0/P1 are not mapped to High/Medium. |
| **R-002** | Present credible public Project Stories. | As a visitor, I want public Project Stories to explain relevant business context, Jairo’s contribution, and outcomes so I can assess comparable experience and value. | - [ ] Public stories are curated narratives derived from validated Projects.<br>- [ ] Public evidence/reference material appears only when eligible and materially useful.<br>- [ ] Visitor-facing content does not expose internal Evidence, lifecycle state, or publication-classification machinery. | **MUST — approved public-story scope.** |
| **R-003** | Preserve evidence and publication governance. | As Content Owner, I want material claims and Project Stories checked against A3 evidence and publication rules before public release so public content remains defensible and ineligible content remains private. | - [ ] Claims are traceable, attributable, and defensible.<br>- [ ] Stories derive from validated Projects.<br>- [ ] Only publication-eligible content may become public; internal/restricted Evidence may support claims without itself becoming public.<br>- [ ] No enforcement stage or mechanism is prescribed here. | **MUST — A3/A5 publication and evidence guardrail.** |
| **R-004** | Support scannable, progressive, non-linear exploration. | As a visitor, I want to scan content and choose where to continue so I can assess relevance and explore deeper evidence as needed. | - [ ] Preserve scannability and progressive disclosure according to screen purpose.<br>- [ ] Support entry, skip, revisit, and direct Contact paths; impose no mandatory linear funnel.<br>- [ ] Retain the approved A10 flows.<br>- [ ] Exact link sets and disclosure mechanisms remain open. | **MUST — approved experience scope.** |
| **R-005** | Provide the approved Contact options. | As a visitor, I want Contact to provide the approved ways to reach Jairo or access the supporting CV. | - [ ] Contact owns Email, LinkedIn, Phone, and the secondary CV download.<br>- [ ] Other screens route to Contact unless later explicitly approved.<br>- [ ] No on-site form backend is introduced. | **MUST — approved Contact scope.** |
| **R-006** | Preserve the approved P1 screen responsibilities. | As a visitor, I want the approved P1 screens to provide their supporting professional context so I can explore capabilities, leadership, career progression, and broader profile information. | - [ ] How I Can Help uses canonical business-problem-focused Capabilities.<br>- [ ] Leadership, Career Journey, and About retain their approved responsibilities.<br>- [ ] P1 screens are required MVP scope; P1 does not mean optional.<br>- [ ] Do not invent P3-specific needs, navigation, or calls to action. | **MUST — required MVP scope.** P1 remains an experience-role label, not a Medium-priority mapping. |

---

## Non-Functional Requirements

| ID | Related requirements | Requirement / acceptance criterion |
|---|---|---|
| **NFR-001 — Performance** | R-001, R-004, R-005 | Expectations remain proportional to the MVP. No numeric response-time, throughput, availability, or equivalent performance target is approved. |
| **NFR-002 — Accessibility and responsiveness** | R-001, R-004, R-005, R-006 | Accessibility is mandatory despite the absence of a formal conformance level or numeric breakpoint. Preserve the approved A5/A10 qualitative requirements: semantic content structure; meaningful headings and link purposes; keyboard navigation, visible focus, and logical focus order; clear descriptive labels for links and controls; keyboard-accessible disclosure controls where used; semantic links for navigation-based disclosure; and do not rely on visual styling or icons alone. Responsive usability remains required; device priority and usage context remain unknown. Later work may refine acceptance detail without inventing an unapproved conformance standard. |
| **NFR-003 — Publication and evidence integrity** | R-002, R-003 | Only publication-eligible content may become public. Internal/restricted Evidence may support claims without itself becoming public. |
| **NFR-004 — Secure delivery** | R-001–R-006 | The selected production hosting must support HTTPS, as required by A5. Provider and operating model remain unselected. |
| **NFR-005 — Proportional reliability** | R-001, R-004, R-005 | Reliability expectations remain proportional to the MVP. No uptime SLA, disaster-recovery target, rollback target, or other quantitative service level is approved; hosting and operational requirements remain deferred. |
| **NFR-006 — Maintainability and scope** | R-001–R-006 | Keep the solution small and maintainable; added complexity requires an approved requirement or identified risk. The Context Warehouse is not a public runtime source. |
| **NFR-007 — Measurement readiness** | Group 1 business outcomes | The product must remain capable of supporting the measurement needed for approved post-launch validation. Exact measures/events, mechanism, privacy/retention/consent treatment, baseline, and implementation remain unresolved downstream decisions. |

---

## Constraints

### Technical Constraints

- **[CONFIRMED]** Frontend-only is the intended MVP boundary; do not add custom backend, database, visitor authentication, runtime personalization, real-time behavior, or unsupported backend-dependent functionality absent an approved requirement or identified risk.
- **[CONFIRMED]** The Context Warehouse is not the public website’s runtime content source.
- **[CONFIRMED]** HTTPS is required of the selected production hosting; the provider is not selected.
- **[SOFT]** Markdown/file-based governed content and static/build-time delivery are preferred directions, not locked decisions.
- **[SOFT]** Low-cost, simple, reliable, maintainable hosting is a preference, not a Dava.Flow requirement.

### Business / Product Constraints

- **[CONFIRMED]** Preserve the eight approved screens, three personas, Project/Project Story distinction, A3 mappings, evidence/publication rules, Contact model, scannability, progressive disclosure, and non-linear Recruiter Journey.
- **[CONFIRMED]** The five-minute relevance/confidence objective applies to the overall experience, not per-screen, per-transition, or forced consumption time.
- **[CONFIRMED]** Tigo → Avianca → DFA remains an ordered professional-evolution narrative, not a mandatory visitor route.
- **[SOFT DELIVERY TARGET]** Mid-October 2026 is a local-validation target, not a committed public production-release date.

### Regulatory / Resource Constraints

- No sector-specific regulatory regime is identified for the public MVP. Basic privacy, secure delivery, accessibility, and publication-sensitivity controls remain applicable; detailed standards remain open.
- No separate resource, budget, or public-launch commitment is introduced here.

---

## Out of Scope and Deferred Choices

### Explicit Product Exclusions

- AI product capabilities, runtime personalization, real-time capabilities, chatbot, on-site form backend, and unsupported backend-dependent functionality.
- Search, filtering, sorting, pagination, authentication, runtime governance UI, blog/newsletter, interactive architecture diagrams, public-speaking portfolio, and separate Delivery Manager / Program Manager positioning.
- Additional screens, P3-specific needs/navigation, runtime recommendations, or unsupported claims.

### Intentionally Deferred Decisions — Not Selected or Ruled Out

- **PRD / Experience Design:** none open. Final wording, the Home profile summary, Project Story previews, progressive disclosure, Related / Next Exploration links, and contact values are closed by D-014, D-020, D-021, and D-022. Wording can be revisited later.
- **Architecture / Solutioning:** frontend stack; content storage/maintenance representation, including whether a CMS is needed; hosting provider; deployment pipeline and rollback; build-boundary ownership; publication-control implementation stage.
- **Analytics / Measurement:** measures/events, mechanism, privacy/retention/consent, baseline, and implementation.
- **Implementation detail:** list/grid treatment, detailed P1 states/interactions, and formal accessibility conformance target. Responsive breakpoints are closed by D-013 (768px and 1024px).

---

## Open Questions

%%Updated 2026-10-20: Q-07 to Q-10 closed by D-014, D-020, D-021, and D-022 (see the decision log). The same items are closed in the HLD, boundary map, design sketch, and wireframes.%%

| ID | Question | Owner | Priority | Target resolution |
|---|---|---|---|---|
| **Q-01 / AS-01** | Will the portfolio materially improve recruiter engagement compared with the CV alone? | Jairo | Not assigned in source | Measurement definitions remain unresolved downstream; evaluate behavioral impact post-launch in Evolve. |
| **Q-02 / AS-02** | Will the target audience meaningfully review the portfolio during candidate evaluation? | Jairo | Not assigned in source | Measurement definitions remain unresolved downstream; evaluate behavior post-launch in Evolve. |
| **Q-03 / AS-03** | Does the available career material support sufficiently complete and defensible Project Stories, assessed individually? | Jairo | Not assigned in source; partially validated | Assess each Story under A3’s evidence and publication lifecycle. |
| **Q-04 / AS-04** | Is the intended frontend-only MVP boundary sufficient for the approved PRD requirements, and what architecture/strategy decisions follow? | Devin recommends; Jairo approves | High in A9 | A5/A9 are completed Discovery inputs and provide the feasibility/context baseline. Remaining requirement-fit and architecture/strategy decisions belong to Step 5; no future A5/A9 work is implied. |
| **Q-05 / AS-05** | Has a concrete contradiction with the approved foundations emerged that requires explicit Product Owner review? Absent such a contradiction, the approved foundations continue to govern. | Jairo | Not assigned in source | Review only if a concrete contradiction arises or the Product Owner explicitly approves a strategic change; this is not a routine strategy-reopening exercise. |
| **Q-06 / AS-07** | Does the approved Recruiter Journey translate effectively into the experience? | Jairo | Not assigned in source | A10 flows are approved; effectiveness remains an assumption for any later validation. |
| **Q-07** | What final wording and minimum Home profile summary content will be approved? | Jairo | Not assigned in source | Closed by D-022 (2026-10-20). |
| **Q-08** | Which Project Story previews should appear, in what order, and which summary fields are sufficient? | Jairo | Not assigned in source | Closed by D-014 (2026-10-20). |
| **Q-09** | What progressive-disclosure interaction and Related / Next Exploration links will be used? | Jairo; UX role not separately assigned | Not assigned in source | Closed by D-020 (2026-10-20). |
| **Q-10** | What final contact values and CV artifact path will be approved? | Jairo | Not assigned in source | Closed by D-021 (2026-10-20). |
| **Q-11** | Can the preferred file-based direction represent and govern A3 content; is a CMS needed for a concrete approved requirement? | Architect / Lead Engineer recommends; Jairo approves | High in A9 | Step 5 architecture/strategy work; neither a CMS nor another content representation is selected or ruled out here. |
| **Q-12** | Who owns the curated-content/build boundary, and at which stage is publication eligibility enforced? | Architect / Lead Engineer recommends; Jairo approves | High in A9 | Step 5 architecture/strategy work; implementation stage remains deferred. |
| **Q-13** | Which frontend stack, hosting, deployment, rollback, and release approach—if any—will be approved? | Architect / Lead Engineer recommends; Jairo approves | High for the approach in A9; public release date is separately Medium | Step 5 architecture/strategy work. A5/A9 remain completed inputs; the mid-October target is for local validation, not a committed public production date. |
| **Q-14** | What measurement events, mechanism, privacy/retention/consent treatment, and post-launch baseline are appropriate? Could later decisions create a data-residency requirement? | Jairo | Medium; data-residency question is conditional/Low in A9 | Measurement/privacy questions remain unresolved inputs to appropriate downstream architecture/measurement work; behavioral validation is post-launch in Evolve. |
| **Q-15** | What accessibility conformance level, responsive breakpoints, list/grid treatment, and detailed P1 states will be adopted? | Jairo | Accessibility conformance is Medium in A9; other details unprioritized in source | Breakpoints closed by D-013 (768px and 1024px). Conformance level, list/grid treatment, and P1 states remain open; do not infer an unapproved standard. |

---

## Risks & Mitigation

Step 4 Part C risk assessment has not been performed. This consolidated PRD adds no risk ratings, owners, or mitigation decisions. Existing risk sources remain canonical: [Explore Bundle risks](explore-bundle.md#risks), [A5 Technical Risks and Unknowns](technical-feasibility.md#5-technical-risks-and-unknowns), and [A9 carried-forward risks](architecture-context.md#7-solutioning-readiness-summary). Part C remains pending.

---

## Dependencies

### Upstream Dependencies

- Approved Signal, foundation documents, and the Product Owner-approved single-PRD mapping.
- Approved Discovery outputs A1, A3, A5, A6, A9, and A10; approved Ideation output; and approved PRD Groups 1–4.
- Project Knowledge Base and CV source material. Any specific public Project Story depends on its own evidence, validation, and classification.
- A2, A4, A7, and A8 remain intentionally excluded; no replacement artifacts are created here.

### Downstream Dependencies

- PRD preservation review and final PRD sign-off remain pending.
- Step 4 Part B experience-design and Part C risk-assessment work remain subject to their workflow gates; approved A10 work is consumed rather than regenerated.
- Step 5 Architecture, Strategy & Backlog follows completion of Step 4.

### External Dependencies

- LinkedIn, email, phone, and the CV artifact are approved external/static destinations; final values and availability are not established here.
- Domain/DNS and hosting remain unresolved; no provider is named.

---

## Epic Extraction

**Status:** Not Started.

After PRD approval and explicit Step 5 entry, map approved requirements to candidate epics. No epic files or implementation tasks are created here. Do not create one epic per concept or treat all three concepts as authorized for implementation; preserve them as distinct product/concept inputs at different conceptual levels. This does not select a final direction, combine them, or require all three to coexist in the eventual solution.

---

## Implementation Notes

- No implementation phasing, estimate, platform, stack, host, deployment, monitoring, rollback, CMS/content representation, or analytics design is selected.
- Retain the Product Owner’s mid-October local-validation target as a target only; no public release date is committed.
- Consume A10’s approved eight-screen experience baseline; do not recreate flows or wireframes in this Group.
- Content-dependent implementation must have evidence, validation, and classification information sufficient for that work. Final publication eligibility is mandatory before public deployment, not necessarily before unrelated implementation begins.
- Preserve the A3 Project Story lifecycle as `draft → review → approved → published`; do not collapse or skip states.

---

## Approval & Sign-Off

**PRD Group Gates:** Groups 1–4 approved. **Final consolidated PRD:** Approved by Product Owner Jairo Enrique Diaz on 2026-09-28. PRD approval does not complete Explore Step 4 or authorize Step 5.

| Role | Name / assignment | Date | Status |
|---|---|---|---|
| Product Manager / Product Owner | Jairo Enrique Diaz | 2026-09-28 | Approved |
| Architect / Lead Engineer | Devin is explicitly assigned these roles; RACI marks Jairo Accountable and Devin Responsible for PRD work. No separate “Tech Lead” title or individual final-signatory record is asserted. | Not recorded | No separate final sign-off recorded |
| UX Lead | Not separately assigned in the approved steering team | Not recorded | No sign-off asserted |
| Stakeholder / Content Owner | Jairo Enrique Diaz; same person as Product Owner for this personal project | 2026-09-28 | Covered by the same Product Owner sign-off; no separate signature recorded |

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-09-28 | Devin | Consolidated approved PRD Groups 1–4 for Product Owner preservation review; no later Step 4/Step 5 activity included. |
| 1.1 | 2026-09-28 | Devin | Applied the approved neutral concept-level wording correction and recorded Product Owner final PRD approval; no analytical changes. |

---

## Related Documentation

### Explore Phase Artifacts

- [Signal](20260908-personal-brand-website.md)
- [Context](context.md)
- [Approved refined concepts](personal-brand-website-refined-concepts.md)
- [Discovery Index](discovery.md) — unchanged; current Step 3 approval is recorded in the refined-concepts artifact.
- Hypothesis: no separate artifact; A8 was intentionally excluded.

### Discovery and Design Artifacts

- [Personas](personas-personal-brand-website.md)
- [Domain Analysis](domain-analysis.md)
- [Technical Feasibility](technical-feasibility.md)
- [Architecture Context](architecture-context.md)
- [A10 Wireframes and Flows](wireframes-personal-brand-website.md)
- [Approved Recruiter Journey](03-recruiter-journey.md)
- Separate Journey Map: none; A7 was intentionally excluded.
- [Explore Bundle](explore-bundle.md) — includes approved scope and existing risk source.

### Deferred / Not Yet Produced

- HLD and ADRs: Step 5, not produced.
- Separate risk register: not produced; Step 4 Part C risk assessment remains pending.
- Market Research and Regulatory Compliance artifacts: A2/A4 intentionally excluded.

---

**Slug:** `personal-brand-website`  
**Domain mapping label:** `Personal Brand Website` (Product Owner-approved; not asserted as a separate A3 glossary entry)  
**Last Updated:** 2026-09-28  
**Status:** Approved by Product Owner Jairo Enrique Diaz on 2026-09-28; Explore Step 4 COMPLETE / APPROVED on 2026-09-30
