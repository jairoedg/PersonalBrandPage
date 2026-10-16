# Personal Brand Website — Discovery → Ideation / PRD Handoff

**Purpose:** Preserve the approved Explore Step 2 — Discovery context so a fresh session can begin Explore Step 3 — Ideation without reconstructing decisions from conversation history.

**Current lifecycle state**
- **Explore Step 2 — Discovery: COMPLETE / APPROVED**
- **Explore Step 3 — Ideation: NEXT but NOT STARTED**
- **Exact next action:** **Step 3 — Ideation, Phase A — Frame, Action 1 — Problem Classification**
- **Explore Type:** Explore Readiness Check (ERC)

**Source:** `discovery.md` — Current lifecycle status, Discovery Completion Checkpoint.  
**Dava.Flow source:** `kb-explore-agent-steps.md` — Explore sequence; `explore.proc.wireframing@0.1.2`; `explore.proc.architecture-context@1.0.1`.

---

## 1. Canonical artifact authority

Use the latest approved artifacts below as the source of truth. Do **not** reconstruct approved decisions from prior conversation history.

| Authority | Canonical artifact | What it owns |
|---|---|---|
| Explore scope / selected activities | `explore-bundle.md` | ERC scope, selected/excluded Explore activities, approved foundation constraints |
| A1 | `context.md` | Problem/context baseline, scope, system boundary, stakeholders, governance, initial assumptions/gaps |
| A3 | `domain-analysis.md` | Canonical domain model, Project vs Project Story, Evidence model, capabilities, narrative roles, prominence, lifecycle/rules |
| A5 | `technical-feasibility.md` | Technical feasibility baseline, constraints, guardrails, risks, unresolved engineering questions |
| A6 | `personas-personal-brand-website.md` | Canonical persona set and evidence provenance |
| A9 | `architecture-context.md` | Architecture landscape, drivers, constraints, risks, bounded-context view, downstream architecture questions |
| A10 | `wireframes-personal-brand-website.md` | Approved low-fidelity experience baseline, screen hierarchy, flows, cross-screen patterns, open questions |
| Control record | `discovery.md` | Lifecycle status and completion checkpoint |

**Source:** `discovery.md` — Artifact Index.  
**Dava.Flow source:** `explore.proc.architecture-context@1.0.1` — final architecture-context artifact role; `explore.proc.wireframing@0.1.2` — durable wireframe artifact and final validation.

---

## 2. Discovery completion state

All selected Discovery activities are complete:

- **A1 — Context Documentation:** Complete / Approved
- **A3 — Domain Analysis:** Complete / Approved
- **A5 — Technical Feasibility:** Complete / Approved
- **A6 — Personas:** Complete / Approved
- **A9 — Architecture Context:** Complete / Validated / Approved
- **A10 — Wireframing / Experience Design:** Complete / Approved

No Discovery closure blocker remains. Remaining questions are intentionally deferred downstream.

**Source:** `discovery.md` — Discovery Completion Checkpoint; Artifact Index.

---

## 3. Decisions that are frozen and must not be reopened during Ideation

### 3.1 Domain and content model

- **Project and Project Story are distinct.**
  - `Project` = factual/governed engagement record.
  - `Project Story` = curated public narrative derived from a validated Project.
- A3 remains canonical for:
  - Layer 1 evidence-derived signals
  - Layer 2 canonical capabilities
  - Capability-to-Project mappings
  - Narrative themes
  - Narrative roles
  - Project prominence
  - Tigo → Avianca → DFA evolution arc
  - domain lifecycles and rules
- Public claims must remain evidence-grounded, traceable, attributable, and defensible.
- Internal/restricted Evidence is not automatically public content.

**Source:** `domain-analysis.md` — canonical A3 sections on entities/relationships, capabilities, narrative mappings, lifecycle, rules, evidence/publication.  
**Dava.Flow source:** `explore.proc.architecture-context@1.0.1` — Step 4 consolidates with approved A3 rather than creating a competing domain model.

### 3.2 Persona model

Exactly **3 personas** are approved:

1. P1 — Technical Recruiter / Talent Acquisition
2. P2 — Hiring Manager
3. P3 — grouped Delivery and Technology Leader

Do not recreate P4 as a standalone persona. Consulting clients / other professional visitors remain secondary audience contexts, not a fourth persona.

Do not invent:
- P3-specific navigation
- P3-specific calls to action
- unsupported P3 evaluation criteria
- device assumptions
- ATS behavior
- unsupported demographic characteristics

**Source:** `personas-personal-brand-website.md` — approved persona set and validation summary.

### 3.3 Experience model

Exactly **8 MVP screens** are approved:

**P0**
1. Home
2. Projects
3. Project Story Detail
4. Contact

**P1**
5. How I Can Help
6. Leadership
7. Career Journey
8. About

**Source:** `wireframes-personal-brand-website.md` — Screen Inventory.

### 3.4 Governing experience principles

Preserve both principles exactly in intent:

1. **The overall experience should support the five-minute relevance/confidence objective, while every screen remains scannable and progressively discloses deeper information according to its purpose.**
2. **The Recruiter Journey defines a confidence-building progression, not a mandatory linear funnel. Visitors may enter, skip, revisit, or move directly between approved screens according to their evaluation needs.**

The five-minute objective is **not** a per-page consumption limit.

**Source:** `wireframes-personal-brand-website.md` — Snapshot / Governing experience principle; Key Flows.

### 3.5 Screen responsibilities

- **Home:** establish identity, approved positioning, concise profile summary, initial evidence entry, supporting entry points, Contact continuation.
- **Projects:** support Project Story selection, not full evaluation.
- **Project Story Detail:** support deeper evaluation through progressive disclosure.
- **Contact:** final low-friction action screen.

**Source:** `wireframes-personal-brand-website.md` — Screen Specs.

### 3.6 Contact model

Contact owns:
1. Email
2. LinkedIn
3. Phone
4. CV download as a **secondary supporting recruitment artifact**

Other screens route to Contact rather than duplicating direct contact mechanisms unless later explicitly approved.

CV must not replace Project Story-based storytelling.

**Source:** `wireframes-personal-brand-website.md` — Contact Screen; Cross-Screen Patterns.

### 3.7 P1 information hierarchy

- **How I Can Help:** canonical A3 business-problem-focused capabilities + supporting Project Story relationships; not a technology-skills catalogue.
- **Leadership:** approved Leadership Principles + relevant decision/project context + related Project Stories; no unsupported leadership claims.
- **Career Journey:** professional progression + Career Experiences + related Projects/Stories; credentials only when they clarify a role, period, or progression.
- **About:** broader profile + education + certifications + courses/professional development + other approved credentials.

**Source:** `wireframes-personal-brand-website.md` — P1 Screen Specs.

---

## 4. Technical and architecture guardrails that remain in force

### 4.1 MVP complexity boundary

The approved intended MVP boundary is frontend-only. Do not introduce:
- custom backend
- database
- authentication
- runtime personalization
- real-time capability
- backend-dependent functionality

unless a concrete approved requirement or identified risk demonstrates the need.

**Source:** `architecture-context.md` — hard constraints / MVP complexity boundary; `technical-feasibility.md` — Design Guardrails.

### 4.2 Preferred directions, not immutable architecture decisions

These remain **preferences / validated directions**, not hard locks:
- Markdown/file-based governed content
- static/build-time delivery

Do not convert them into mandatory technology choices unless downstream architecture formally decides so.

**Source:** `technical-feasibility.md` — A5 design guardrails / preferences; `architecture-context.md` — soft constraints/preferences.

### 4.3 Context Warehouse boundary

The Context Warehouse is the governed source of engagement knowledge and must **not** become the public website runtime content source.

**Source:** `technical-feasibility.md` — system context / design guardrails; `architecture-context.md` — runtime boundary.

### 4.4 Publication safety

Publication eligibility must be enforced before public deployment. Restricted, unapproved, unclassified-when-required, incomplete, or otherwise ineligible content must not reach public deployment.

Publication-control implementation stage remains a downstream architecture/solutioning concern.

**Source:** `domain-analysis.md` — publication rules; `technical-feasibility.md` — publication safety guardrails; `architecture-context.md` — unresolved publication-control stage.

### 4.5 Proportional NFR posture

Do not introduce enterprise-grade scalability, availability, observability, disaster-recovery, compliance, or performance targets without an approved requirement or identified risk.

**Source:** `technical-feasibility.md` — NFR principle / Technical Constraints; `architecture-context.md` — project architecture posture.

---

## 5. Explicit MVP exclusions

Do not reintroduce without an approved product requirement:

- AI product capabilities
- runtime personalization
- real-time capabilities
- chatbot / public AI assistant
- on-site form backend
- other backend-dependent functionality
- CMS unless Markdown/file-based content proves inadequate for a concrete requirement
- search
- filtering
- sorting
- pagination
- authentication
- runtime governance UI
- blog/newsletter
- interactive architecture diagrams
- public-speaking portfolio
- separate Delivery Manager / Program Manager positioning

**Source:** `technical-feasibility.md` — Explicit MVP Exclusions; `wireframes-personal-brand-website.md` — Scope and Cross-Screen Patterns; `context.md` — MVP scope/out-of-scope.

---

## 6. Intentionally open / downstream questions

These are **not Discovery blockers** and should not be treated as missing Discovery work.

### PRD / Experience Design
- final approved wording/copy
- minimum Home profile summary content
- exact Project Story preview selection/ordering
- exact Project Story summary fields
- exact progressive-disclosure interaction mechanism
- exact Related / Next Exploration links
- final contact values and CV artifact path

### Architecture / solutioning
- final frontend stack
- hosting provider
- deployment pipeline
- rollback approach
- build-boundary ownership
- publication-control implementation stage
- final file/content representation details

### Analytics / later measurement
- final event definitions
- analytics mechanism
- privacy/retention/consent details as applicable
- post-launch behavioral baseline

### Implementation detail
- responsive breakpoints
- final list/grid treatment
- detailed P1 interactions/states

**Source:** `wireframes-personal-brand-website.md` — Open Questions and Decisions Needed; `architecture-context.md` — Open Questions; `technical-feasibility.md` — Engineering Questions.

---

## 7. Historical-record warning

`discovery.md` contains historical intermediate sections from earlier A9 work. Some of those entries describe the state **at that earlier checkpoint** and are not the current lifecycle authority.

For current state:
1. use the **Discovery Completion Checkpoint** and **Artifact Index** in `discovery.md`;
2. use the final canonical A9 `architecture-context.md`;
3. do not infer current lifecycle status from historical Enrichment Log wording.

**Source:** `discovery.md` — current lifecycle status / Discovery Completion Checkpoint / Artifact Index.

---

## 8. Ideation-specific guardrails

### Explore Step 3 sequence

For this ERC, use the compressed Ideation path:

- Phase A — Frame
- Phase C — Generate and Evaluate
- Top 3 concepts

The exact next action is:

**Phase A — Frame, Action 1 — Problem Classification**

Do not execute later phases before the required human review gate.

**Source:** `kb-explore-agent-steps.md` — Step 3 Ideation ERC adaptation.

### Ideation must not reopen Discovery

Ideation may explore alternatives **within** the approved:
- problem
- MVP scope
- domain model
- persona model
- technical guardrails
- experience boundaries

It must not use “ideation” as justification to reopen approved Discovery decisions.

If an idea conflicts with an approved Discovery constraint, the conflict must be raised explicitly rather than silently changing the baseline.

**Source:** `kb-explore-agent-steps.md` — Step 3 Ideation; canonical A3/A5/A6/A9/A10 artifacts.

---

## 9. PRD & Experience Design handoff rules

The canonical Explore sequence after Ideation is:

**Step 4 — PRD & Experience Design**

A10 already established substantial approved Experience Design. Step 4 must consume that work rather than regenerate it from scratch.

Preserve:
- 8-screen inventory
- approved P0 hierarchies
- approved P1 hierarchies
- 4 approved flows
- cross-screen patterns
- accessibility/responsive rules
- progressive disclosure
- non-linear Recruiter Journey
- Contact model
- publication/public-evidence boundaries

**Source:** `kb-explore-agent-steps.md` — Explore sequence; `wireframes-personal-brand-website.md` — complete A10 artifact.

---

## 10. Recommended first message in the new chat

Use this before allowing the new session to execute Ideation:

> You are taking over a Dava.Flow Explore engagement at a formal lifecycle boundary.
>
> Load the attached canonical artifacts and this handoff document.
>
> Do **not** execute Ideation yet.
>
> First report:
> 1. current Explore lifecycle state;
> 2. exact next action;
> 3. canonical artifact authority/order;
> 4. frozen decisions that must not be reopened;
> 5. intentionally deferred/open decisions;
> 6. Ideation-specific guardrails;
> 7. any conflict or ambiguity you detect across the canonical artifacts.
>
> Treat the canonical artifacts as authoritative and do not reconstruct approved Discovery decisions from prior conversation history.
>
> After I approve your context summary, proceed only with:
> **Explore Step 3 — Ideation, Phase A — Frame, Action 1 — Problem Classification.**

---

## 11. Recommended files to attach to the new chat

Attach the latest canonical versions of:

1. `explore-bundle.md`
2. `context.md`
3. `domain-analysis.md`
4. `technical-feasibility.md`
5. `personas-personal-brand-website.md`
6. `architecture-context.md`
7. `wireframes-personal-brand-website.md`
8. `discovery.md`
9. this handoff document

Add approved foundation documents only if the new session needs exact product/brand/strategy wording during Ideation or PRD.

**Source:** `discovery.md` — Artifact Index; `wireframes-personal-brand-website.md` — Inputs.

---

## 12. One-line handoff state

**Discovery is complete and approved. Start a fresh session at Explore Step 3 — Ideation, Phase A — Frame, Action 1 — Problem Classification, using the canonical Discovery artifacts as frozen upstream inputs.**

**Source:** `discovery.md` — Discovery Completion Checkpoint; `kb-explore-agent-steps.md` — Step 3 Ideation.
