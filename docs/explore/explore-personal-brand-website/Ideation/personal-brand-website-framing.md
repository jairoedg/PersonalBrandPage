# Ideation Framing — Personal Brand Website

**Explore Type:** Explore Readiness Check (ERC)  
**Lifecycle:** Step 3 — Ideation, Phase A — Frame  
**Status:** Actions 1–2 reviewed; ID-1 classification approved; ID-2 framing direction approved  
**Scope:** Product/concept alternatives inside the approved Discovery envelope. This artifact does not reopen Discovery or decide downstream solutioning.

## Problem Statement

Jairo Enrique Diaz has accumulated more than 15 years of delivery leadership experience across telecommunications, aviation, pharmaceuticals, financial services, and capital markets. The traditional two-page CV cannot convey the depth of project complexity, business outcomes, leadership decisions, or professional evolution that differentiates him. Recruiters and hiring managers see only a partial professional profile, while Jairo lacks a single authoritative reference that complements the CV with evidence-based project stories, leadership philosophy, and a confidence-building path to contact. The desired outcome is a professional, evidence-based, story-driven digital portfolio that supports recruiters' key questions within five minutes and becomes the authoritative reference for Jairo's career.

Source: [context.md](context.md), Problem Statement.

## Problem Classification — ID-1 Approved

| Dimension | Value | Description (Why) | Evidence |
|-----------|-------|-------------------|----------|
| **Definition level** | **Semi-defined** | The approved product goal is clear. Product/concept questions remain open within the approved Discovery envelope: how progressive disclosure is realized; how Project Story previews are selected, ordered, and presented; how navigation and cross-linking support the non-linear Recruiter Journey; and how the experience supports the five-minute relevance/confidence objective. | `context.md`, Desired outcome; `explore-bundle.md`, Q1, Q-IA-1, Q-UX-1; `wireframes-personal-brand-website.md`, Governing experience principle and Open Questions. |
| **Solution space** | **Wide** | Multiple product/concept alternatives remain within the frozen 8-screen experience, 3-persona model, Project/Project Story distinction, evidence/publication rules, progressive-disclosure requirement, and non-linear Recruiter Journey. Alternatives include how Home routes visitors into evidence, how Projects presents story previews, how approved flows use contextual navigation, and how P1 screens support the P0 evidence journey. | `wireframes-personal-brand-website.md`, Screen Inventory, Key Flows, Cross-Screen Patterns; `personas-personal-brand-website.md`, approved persona set. |
| **Novelty needed** | **Adjacent** | The concept applies the approved evidence-based Project Story model, business-problem-focused Capability taxonomy, Leadership Principles, and Recruiter Journey to this specific professional portfolio experience. It uses an established portfolio category with a distinctive, governed professional-knowledge and storytelling context. | `explore-bundle.md`, Strategic Constraint and North Star; `domain-analysis.md`, canonical domain model and taxonomies; `wireframes-personal-brand-website.md`, Key Flows. |
| **Complexity** | **Complicated** | The problem combines bounded but interacting domain relationships, evidence and publication constraints, three persona contexts, progressive disclosure, P0/P1 screen responsibilities, and a non-linear journey with legitimate shorter and exploratory paths. These are knowable within approved Discovery artifacts, but require coordinated product decisions. | `domain-analysis.md`, Domain Model and Business Rules; `personas-personal-brand-website.md`; `wireframes-personal-brand-website.md`, Screen Inventory and Key Flows. |
| **User state** | **Informed** | P1 evaluates experience fit against job requirements first, then uses profile summary, years of experience, and certifications as subsequent screening signals. P2 examines relevant experience more deeply after initial screening and uses situational questions about comparable problems and responses. This classification uses only those validated evaluation behaviors; device behavior, usage context, ATS behavior, and portfolio familiarity remain unknown. | `personas-personal-brand-website.md`, P1 and P2 Goals, Behaviors, and Unsupported Characteristics. |
| **Prior context** | **Greenfield** | No website implementation, deployed runtime, inherited platform, or legacy architecture exists. The greenfield product has substantial approved strategic, domain, persona, experience, and feasibility foundations. | `architecture-context.md`, Existing Architecture Baseline; approved foundation documents; A3, A5, A6, and A10 artifacts. |

## Method Routing — Verified Against Skill Table

The Problem Classification skill's Method Routing Table maps **Semi-defined + Wide + Adjacent** to:

| Field | Selection |
|-------|-----------|
| **Primary method** | HMW + Synectics |
| **Supporting methods** | Round-Robin Perspectives |
| **Pathway** | Flexibility then Persistence |

Source: `skills/explore.util.problem-classification/SKILL.md`, Method Routing Table row “Semi-defined + Wide + Adjacent.” This routing is recorded as the skill's direct table result, not inferred from other method-selection guidance.

## Framing Exploration

The framings below were explored during Action 2. Only Framings 3 and 4 were selected at the ID-2 gate. All others remain exploratory probes and are not approved requirements, targets, or changes to Discovery.

| # | Framing | Type | Abstraction | Why it matters / what it opens |
|---|---------|------|-------------|--------------------------------|
| 1 | HMW help recruiters see relevant evidence within the first minute on the Home screen? | Narrow | Specific P1 evaluation need | Explores how Home might establish relevance and expose evidence efficiently. **Hypothetical provocation only:** “first minute” is not a time target, requirement, or acceptance criterion. |
| 2 | HMW make the Project Story Detail screen answer “has this person solved problems like mine?” before the visitor scrolls? | Narrow | Specific P2 evaluation need | Explores how story orientation could foreground comparable business problems and outcomes. **Hypothetical provocation only:** “before the visitor scrolls” is not a requirement or acceptance criterion. |
| 3 | HMW turn Jairo's delivery-leadership experience into an overall five-minute relevance/confidence experience? | Broad | Overall experience objective | Treats the five-minute objective as an overall relevance/confidence objective, not a per-screen, per-transition, or forced-consumption-time requirement. The experience remains scannable while allowing deeper exploration where needed. **Selected at ID-2.** |
| 4 | HMW make the website an authoritative reference grounded in evidence and defensible professional storytelling, rather than a self-promotional brochure? | Broad | Credibility and positioning | Centers concepts on credible, attributable, defensible stories and professional evidence rather than unsupported promotional presentation. **Selected at ID-2.** |
| 5 | HMW make the website so overwhelming that a recruiter abandons within 30 seconds? Then invert. | Inverted | Risk avoidance | Uses an exaggerated failure case to surface overload and navigation risks. **Hypothetical provocation only:** “30 seconds” is not a target, requirement, or acceptance criterion. |
| 6 | HMW design the experience so visitors never reach the Contact screen? Then invert. | Inverted | Contact friction | Probes what could obstruct confidence or make the Contact path difficult to find; inversion may expose useful principles for low-friction contact. |
| 7 | HMW make the Projects page feel like a curated exhibition where each piece invites closer inspection? | Analogical | Collection and selection | Borrows the idea of a curated exhibition to explore story selection and invitations to deeper detail; it does not prescribe a visual design or final layout. |
| 8 | HMW structure Career Journey like a documentary timeline where each era reveals the evolution of leadership philosophy? | Analogical | Professional evolution | Uses documentary progression as a probe for expressing career evolution. Any direction must remain grounded in approved Career Experiences and evidence. |

## Constraint Flip Probes — Not Constraint Changes

These counterfactual questions were exploratory probes only. None removes, weakens, or changes an approved Discovery constraint. Any insight considered later must be re-grounded against the canonical Discovery envelope before it can advance.

| # | Frozen constraint | Counterfactual probe if removed | Probe if intensified | Status |
|---|--------------------|-------------------------------|---------------------|--------|
| 1 | Frontend-only intended MVP boundary; backend-dependent functionality requires an approved need or identified risk. | What product experience might be imagined if this boundary did not apply? Such possibilities are outside the approved MVP unless separately justified and approved; this probe does not authorize them. | If every experience must remain within the approved frontend-only boundary, what product value can clear information hierarchy and progressive disclosure provide? | Probe only; boundary remains frozen. |
| 2 | Exactly eight approved MVP screens: four P0 and four P1. | What needs might suggest additional surfaces? The approved inventory remains eight; do not add screens from this counterfactual. | If every approved screen must earn its role, how can each fulfill its approved responsibility and connect clearly to the others? | Probe only; inventory remains frozen. |
| 3 | Project and Project Story are distinct; public claims must be evidence-grounded, traceable, attributable, and defensible. | What would become possible without these safeguards? Unsupported or unattributed public claims remain impermissible. | If every material public claim is scrutinized for evidence and attribution, how can the story remain clear and useful without exposing internal/restricted Evidence? | Probe only; domain and evidence rules remain frozen. |
| 4 | Publication classification controls disclosure; restricted or ineligible content must not become public. | What could be told if no publication restrictions existed? This does not authorize disclosure of restricted information. | If every public detail is checked against eligibility, how can concepts preserve useful context while respecting classification? | Probe only; publication rules remain frozen. |
| 5 | The Recruiter Journey builds confidence but is not a mandatory linear funnel; visitors may enter, skip, revisit, or move directly between approved screens. | What would a forced sequence look like? It is not an approved experience direction. | If visitors may enter at any approved screen and take shorter paths, how can each screen provide orientation and meaningful onward routes? | Probe only; non-linear journey remains frozen. |
| 6 | Progressive disclosure is required; screens remain scannable and reveal deeper information according to purpose. | What would an undifferentiated full-detail presentation look like? It conflicts with the approved experience principles. | If scanning and detail-on-demand are consistently required, what content layers make each screen useful at its approved depth? | Probe only; progressive-disclosure principle remains frozen. |

## Approved Discovery Envelope for Further Ideation

- Preserve the approved eight-screen inventory: Home, Projects, Project Story Detail, Contact (P0); How I Can Help, Leadership, Career Journey, About (P1).
- Preserve exactly three personas: P1 Technical Recruiter / Talent Acquisition, P2 Hiring Manager, and P3 grouped Delivery and Technology Leader. Do not invent P3-specific evidence priorities or split P3.
- Preserve the A3 Project / Project Story boundary, approved capability and narrative mappings, evidence rules, and publication classifications.
- Preserve the overall five-minute relevance/confidence objective, scannability, progressive disclosure, and non-linear Recruiter Journey. Do not turn the objective into per-screen timing, forced consumption, or a linear funnel.
- Preserve screen responsibilities and Contact ownership, including CV as a secondary supporting recruitment artifact.
- Keep public claims truthful, traceable, attributable, and defensible; internal/restricted Evidence is not automatically public content.
- Do not introduce excluded product capabilities or backend-dependent functionality absent an approved requirement or identified risk.
- Do not decide frontend stack, content representation, hosting, deployment, publication-control implementation stage, analytics mechanism, or other deferred solutioning questions in Ideation.

## Hard and Soft Constraints

| Type | Constraint | Source |
|------|------------|--------|
| **Hard** | The overall experience supports the five-minute relevance/confidence objective; each screen remains scannable and progressively discloses detail according to its purpose. | `wireframes-personal-brand-website.md`, Governing experience principle. |
| **Hard** | The Recruiter Journey is not a mandatory linear funnel; visitors may enter, skip, revisit, or move directly among approved screens. | `wireframes-personal-brand-website.md`, Governing experience principle and Key Flows. |
| **Hard** | Preserve the eight approved MVP screens and their P0/P1 responsibilities; do not create additional screens. | `wireframes-personal-brand-website.md`, Screen Inventory. |
| **Hard** | Preserve the three approved personas without unsupported P3-specific needs or assumptions. | `personas-personal-brand-website.md`; `personal-brand-discovery-to-ideation-handoff.md`. |
| **Hard** | Project and Project Story remain distinct; public claims require traceable, attributable, defensible Evidence; publication eligibility controls what can be public. | `domain-analysis.md`, Business Rules; `technical-feasibility.md`, Design Guardrails. |
| **Hard** | Maintain the approved frontend-only MVP complexity boundary; do not add backend-dependent functionality without a concrete approved requirement or identified risk. This is a guardrail, not an invitation to select architecture. | `architecture-context.md`, Constraints Register; `technical-feasibility.md`, Design Guardrails. |
| **Soft** | Prefer evidence-based, story-driven professional storytelling that communicates business value and leadership rather than reproducing a traditional CV. | `explore-bundle.md`, Strategic Constraint; `context.md`, Problem Statement. |
| **Soft** | Prefer concise orientation and relevant supporting links while allowing deeper evaluation where the screen's purpose calls for it. | `wireframes-personal-brand-website.md`, Key Flows and Screen Specs. |

## Success Criteria for Ideation

Product concepts should:

1. Support the overall five-minute relevance/confidence objective without a per-screen timer, forced consumption time, or mandatory linear journey.
2. Preserve scannability and progressive disclosure while supporting deeper evaluation when needed.
3. Express an authoritative professional reference through evidence-based, attributable, defensible Project Stories and relevant approved context.
4. Fit the approved personas, screen inventory, A3 domain model, Contact model, and publication rules without reopening them.
5. Explore product/concept alternatives only; leave downstream architecture, technology, hosting, deployment, analytics, and implementation decisions unresolved.

## ID-2 Decision Record

- **Decision:** Framings 3 and 4 selected as the framing direction.
- **Clarification for Framing 3:** The five-minute objective applies to overall relevance/confidence, not per-screen, per-transition, or forced consumption time; the experience remains scannable and permits deeper exploration where needed.
- **Clarification for Framing 4:** Preserve the authoritative-reference framing, grounded in evidence, credibility, and defensible professional storytelling rather than self-promotional presentation.
- **Other framings and Constraint Flips:** Valid exploratory probes only; they do not modify frozen Discovery constraints. Any insight carried forward must be re-grounded against the canonical Discovery envelope.
- **Explicit non-requirements:** The “first minute,” “before the visitor scrolls,” and “30 seconds” phrases are hypothetical provocations only, not product requirements, UX targets, or acceptance criteria.
- **Gate:** ID-2 approved by the Product Owner on 2026-09-28. No approval of generated concepts is implied by this decision.
