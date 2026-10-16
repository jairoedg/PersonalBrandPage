# Part C — Risk, Validation & Decisions: Personal Brand Website

**Generated:** 2026-09-30  
**Status:** APPROVED / COMPLETE — Product Owner risk-acceptance gate recorded 2026-09-30; accepted residual-risk set remains empty  
**Explore Type:** ERC  
**Risk documentation mode:** Warned inline fallback; `explore.proc.risk-documentation` is not installed

## Authority and Method Boundaries

This Part C record consumes existing risks from the canonical Explore Bundle, A5 Technical Feasibility, and A9 Architecture Context without reconstructing or arbitrarily rescoring them. Existing source ratings, statuses, and mitigations are preserved as recorded. A new or changed risk is included only when attributable to a specific Step 4 finding and is separately identified.

A8 Hypothesis remains intentionally excluded. No replacement hypothesis artifact has been created or inferred. Simulated validation uses only approved evaluation references:

- approved Signal/context outcomes;
- approved PRD success criteria and measures;
- approved A10 flows and experience principles;
- approved feasibility constraints;
- active assumptions AS-01, AS-02, AS-03, AS-04, AS-05, and AS-07.

These references retain distinct meanings: outcomes and criteria are evaluation targets; A10 flows/principles are experience constraints; feasibility constraints are boundaries; assumptions remain assumptions. Simulated results are analytical evidence only and are not empirical user, stakeholder, production, analytics, or usability validation.

## 1. Edge Cases from Approved A10 Flows

- No eligible Project Stories: publication/build-readiness issue, not a normal public runtime state.
- Incomplete Project Story: must not be treated as publication-ready.
- Restricted Evidence or unsupported claims entering deployable content: publication/build failure condition.
- Missing relationship to a validated Project: publication/build failure condition.
- Missing CV or contact destination: publication/readiness failure; do not deploy incomplete content.
- Broken internal link: provide usable navigation fallback where A10 defines one.
- External contact destination unavailable: keep other approved visible contact methods available; no automated destination-health detection.
- Visitor skips directly to Contact or supporting P1 context: valid non-linear path; no mandatory funnel is introduced.
- P3-specific evidence need: unresolved; no P3-specific navigation or behavior is inferred.

## 2. Simulated Validation Scenarios

| ID | Approved evaluation target / constraint | Scenario | Simulated result | Limitation |
|---|---|---|---|---|
| SV-01 | PRD overall success criterion; five-minute objective; A10 Flow 1 | A P1 visitor enters Home, scans identity/positioning, reviews Project Story summaries, opens Story Detail, and reaches Contact. | **Analytically aligned:** A10 provides the intended orientation → evidence → deeper evaluation → Contact sequence and permits shorter paths. | Does not establish that a real P1 visitor can answer the six strategy questions within five minutes. AS-01, AS-02, and AS-07 remain assumptions. |
| SV-02 | PRD R-005; A10 Flow 2 | A visitor opens Contact directly and chooses Email, LinkedIn, Phone, or CV. One external destination is unavailable. | **Constrained path is covered:** alternate approved contact methods remain visible; no destination-health mechanism is required. | No production destination or behavioral availability test was performed. |
| SV-03 | PRD R-004; A10 Flow 3; Evidence Paths, Not Funnel | A visitor explores How I Can Help, Leadership, Career Journey, or About before returning to Projects or Contact. | **Experience constraint is satisfied analytically:** P1 screens act as supporting context and do not create a mandatory sequence. | No empirical navigation or comprehension evidence exists. AS-07 remains active. |
| SV-04 | PRD R-002/R-003; A10 Flow 4; A3 publication rules | A visitor evaluates one Project Story from orientation through challenge, responsibilities, decisions, outcomes, capabilities, lessons, and optional public references. | **Content boundary is coherent:** Project Story remains distinct from Project; internal Evidence and governance are not exposed; restricted/unapproved claims are excluded from public content. | Specific story completeness and defensibility remain per-story content work. AS-03 remains partially validated, not resolved globally. |
| SV-05 | A3 evidence/publication criterion; PRD NFR-003 | A claim has internal/restricted Evidence but no publication-eligible public representation. | **Governance boundary holds:** Evidence may support a claim without becoming public; the claim must not be treated as publication-ready without appropriate evidence/publication treatment. | No implementation enforcement mechanism has been selected. |
| SV-06 | A10 accessibility principles; PRD NFR-002 | A visitor navigates headings, links, focus order, and any future disclosure control using the approved qualitative principles. | **Design baseline is represented:** meaningful headings/link purposes, keyboard navigation, visible focus, logical focus order, descriptive labels, and semantic links are preserved. | No usability test, assistive-technology test, conformance assessment, or formal WCAG level was performed. |
| SV-07 | A5/A9 frontend-only and proportional-complexity constraints; AS-04 | The MVP is evaluated against the approved eight-screen scope without backend, authentication, runtime personalization, or real-time behavior. | **Scope is compatible analytically:** PRD/A10 do not require those excluded capabilities; architecture and content/build decisions remain deferred. | No running implementation exists. AS-04 remains an assumption. |
| SV-08 | A3/A10 professional evolution; approved narrative context | A visitor encounters the Tigo → Avianca → DFA professional-evolution narrative. | **Narrative boundary holds:** the arc remains ordered and qualified; Tigo is learning contrast, Avianca is project-definition experience, and DFA is later applied learning. | No final copy or visitor route is selected; the arc is not a mandatory path. |

### Simulated-validation conclusion

The approved PRD/A10/A3 design is **analytically coherent against the listed scenarios**, with unresolved implementation, content-readiness, measurement, and empirical-validation limitations. This is not empirical validation and does not close AS-01, AS-02, AS-03, AS-04, AS-05, or AS-07.

## 3. Feasibility Assessment

### Technical feasibility — **CONCERNS, not blocked**

- The approved frontend-only, static/lightweight direction is compatible with the current PRD boundary, but frontend stack, content representation, publication enforcement, hosting, and deployment remain deferred.
- File-based governed-content feasibility remains an open A5 risk: the A3 model, relationships, lifecycle metadata, and publication controls need representative content validation.
- Publication safety is feasible as a governance requirement, but its enforcement point is not selected.
- Responsive/accessibility/performance baselines are stated qualitatively; no implementation or formal conformance target exists yet.
- Figma infrastructure is now structurally set up and B6-approved. The `type/code` representation exception is explicitly accounted for. The remote TextStyle mutation limitation required manual fidelity verification.

### Operational feasibility — **CONCERNS, not blocked**

- Content Owner and Content Curator responsibilities are defined, but the curated-content/build boundary remains unresolved.
- Publication classification and Evidence governance remain human-governed; no runtime governance UI is approved.
- Hosting, deployment, rollback, domain/DNS, and operating model remain unresolved.
- Contact/CV destinations are external/static dependencies whose final values and availability remain open.

### Resource feasibility — **FEASIBLE WITH OPEN DECISIONS**

- The MVP scope is intentionally small and limited to eight approved screens.
- No high-throughput API, distributed system, or enterprise-scale availability requirement is present.
- Additional complexity must be justified by an approved requirement or a new reviewed risk.
- Figma access is available; the manual typography exception consumed Product Owner verification effort and remains an explicitly bounded tooling accommodation.

No architecture, stack, host, CMS, analytics mechanism, or implementation approach is selected by this assessment.

## 4. Preserved Existing Risks

The following are reproduced from canonical sources. No source score, status, or mitigation has been changed here.

### Explore Bundle risks

| Code | Risk | Source impact | Source likelihood | Source status | Source mitigation |
|---|---|---|---|---|---|
| R-01 | Claims exceed available evidence or fail to distinguish Jairo’s contribution. | Medium | Low | Not recorded in source table | A3 evidence mapping; traceable, attributable, defensible claims. |
| R-02 | Rich knowledge base overwhelms the easy-to-scan strategy. | High | Medium | Not recorded in source table | Progressive disclosure, hierarchy, A3/A6/A10 story roles, business-problem capability labels. |
| R-03 | Explore recreates, contradicts, or dilutes approved strategy. | Medium | Low | Not recorded in source table | Approved foundations constrain Explore; no strategic reopening without explicit approval. |
| R-04 | Technology or preferred stack dictates product requirements. | Medium | Low | Not recorded in source table | Keep product/content decisions ahead of stack/hosting decisions. |
| R-05 | Cost preference is treated as a Dava.Flow requirement. | Low | Low | Not recorded in source table | Preserve low-cost/simple/reliable preference as project constraint only. |
| R-06 | Client names, figures, or details are published too specifically. | Medium | Low | Not recorded in source table | A3 named/anonymised/restricted classification; default to safer specificity. |

### A5 Technical Feasibility risks

| ID | Risk | Source likelihood | Source impact | Source status | Source mitigation |
|---|---|---|---|---|---|
| TR-01 / TR-04 / TR-09 | File-based governed-content feasibility and schema/relationship drift. | Medium | High | Open | Representative structured sample, canonical schema/template, proportionate validation. |
| TR-02 | Ineligible content reaches generated deployment assets. | Medium | High | Open | Evaluate publication-control enforcement and negative cases. |
| TR-03 | Evidence references fail claim adequacy, attribution, or wording. | Medium | High | Open | Automate existence/resolution only; adequacy/attribution/wording remain human-governed. |
| TR-05 | Build/hosting/deployment adds unnecessary MVP complexity. | Medium | Medium to High | Open | Evaluate simplicity, HTTPS, review, rollback, maintainability, deployment effort. |
| TR-06 | Minimal measurement cannot evaluate the Recruiter Journey. | Medium | Medium | Open | Define smallest useful A11 event set; baseline after launch. |
| TR-07 | Responsive, accessible, or performant behavior regresses. | Medium | Medium | Open | Preserve qualitative MVP baselines; validate in later work. |
| TR-08 | External contact destinations change or become unavailable. | Low to Medium | Medium | Open | Visible external links and sensible fallbacks; avoid API dependence. |
| TI-01 | Warehouse content/build preparation is confused with deployable runtime content. | Medium | High | Not separately recorded in A5 risk table | Preserve governed warehouse → curated content → generated/runtime boundary. |

### A9 Architecture Context carried-forward risks

These risks have no independent impact/likelihood/status fields in the A9 carried-forward list; they remain unscored and unchanged:

- File-based content may not safely represent required relationships and governance metadata.
- Publication-control stage and build-boundary ownership remain undefined.
- Hosting/deployment may not meet the delivery target without added complexity.
- Analytics/privacy decisions may later affect the build/runtime boundary.

### Current lifecycle interpretation for TR-06

The canonical A5 TR-06 wording and mitigation remain unchanged in the preserved-risk table above. For the current lifecycle only: A11/PRD Generation is complete and no A11 rerun is implied; measurement definitions remain unresolved downstream; architecture/privacy implications belong to the appropriate later architecture/solutioning work; and empirical behavioral validation and baseline require the launched product and occur post-launch in Evolve.

### Responsive breakpoint interpretation

The B6 Mobile/Tablet/Desktop values (375px, 768px, and 1440px) are approved Figma base-frame/grid references. They do not select implementation responsive breakpoints, which remain unresolved downstream.

## 5. New Step 4 Finding / Risk

| Code | Finding-based risk | Impact | Likelihood | Status | Step 4 rationale | Containment / control |
|---|---|---|---|---|---|---|
| STEP4-R-01 | Remote Figma MCP TextStyle mutation failed with `TypeError: object is not extensible`, requiring a manual typography push and fidelity audit; the approved `type/code` system-stack exception remains non-physical in Figma. | Medium | High | **Contained / resolved Step 4 finding** | Directly observed during Activity 9/B5 execution; the approved manual-push exception and fidelity audit completed successfully, and B6 explicitly accepted the accounting treatment. | Preserve the audit trail and documented `type/code` exception; do not retry the failed MCP mutation or infer a substitute font. |

This finding is retained historically and is not erased. It is not carried as an open Step 5/product-readiness risk because no future approved activity currently depends on MCP TextStyle mutation. The underlying tool limitation remains documented, but the approved workaround contained its engagement impact.

## 6. Mitigation Tracking

| Item | Source | Current status | Next action | Owner |
|---|---|---|---|---|
| Evidence/publication traceability | R-01, R-06, TR-02, TR-03 | Ongoing/open | Apply A3 lifecycle and publication classification per Project Story/content item. | Content Owner / Content Curator |
| Scanability and progressive disclosure | R-02, A10 | Design baseline approved; empirical validation open | Validate later with approved stakeholder/behavioral method; do not claim completion now. | Product Owner |
| File-based content/schema feasibility | TR-01/TR-04/TR-09, A9 ASM | Open | Test representative governed Project/Project Story content in later architecture/solutioning work. | Architect / Lead Engineer |
| Publication/build boundary | TR-02, A9 ASM | Open | Decide enforcement stage in downstream architecture work. | Product Owner / Architect |
| Contact/CV availability | TR-08 | Open | Confirm final destinations before publication. | Product Owner |
| Figma TextStyle tooling | STEP4-R-01 | Contained / resolved Step 4 finding; not carried as an open Step 5 risk | Preserve audit trail and exception; no future approved activity currently depends on MCP TextStyle mutation. | Design Lead / Product Owner |
| Measurement | TR-06, AS-01, AS-02, AS-07 | Open; monitor/validate later | Define measurement downstream; empirical baseline only after launch in Evolve. | Product Owner |

## 7. Targeted Risk Dispositions — Not Yet Accepted

These are proposed lifecycle dispositions, not Product Owner acceptance:

- **Mitigate / carry forward** — downstream work is required to reduce or control the exposure.
- **Monitor / validate later** — uncertainty remains and can only be meaningfully evaluated at a later lifecycle point.
- **Accept residual risk** — only if the Product Owner explicitly chooses to proceed despite a known remaining exposure.

| Risk/group | Disposition | Owner | Lifecycle point / next action | Product Owner acceptance required before Step 5? |
|---|---|---|---|---|
| R-01, R-06, TR-02, TR-03 | Mitigate / carry forward | Content Owner / Content Curator | Apply A3 evidence and publication controls per Project Story before publication. | No acceptance inferred; explicit acceptance only if residual exposure remains at SD-1. |
| R-02 and A10 scanability/progressive disclosure | Monitor / validate later | Product Owner | Later approved stakeholder/behavioral validation; no empirical closure claimed in Part C. | No. Monitoring is not acceptance. |
| R-03, R-04 | Mitigate / carry forward | Product Owner / Architect | Preserve approved foundations; make no strategy/stack inference; address architecture decisions later. | No acceptance inferred. |
| R-05 | Monitor / validate later | Product Owner | Continue treating cost as a project constraint, not a Dava.Flow requirement. | No. |
| TR-01/TR-04/TR-09 and A9 file-model ASM | Mitigate / carry forward | Architect / Lead Engineer | Test representative governed Project/Project Story content during later architecture/solutioning work. | No acceptance inferred. |
| TR-05 and A9 hosting/deployment ASM | Mitigate / carry forward | Product Owner / Architect | Evaluate proportional hosting/deployment, HTTPS, review, rollback, and maintainability later. | No acceptance inferred. |
| TR-06, AS-01, AS-02, AS-07 | Monitor / validate later | Product Owner | Define minimal measurement downstream; behavioral validation and baseline occur post-launch in Evolve. | No. Assumptions remain assumptions. |
| TR-07 | Mitigate / carry forward | Product Owner / Architect | Preserve qualitative accessibility/responsive/performance baselines in later implementation validation. | No acceptance inferred. |
| TR-08 | Mitigate / carry forward | Product Owner | Confirm contact/CV destinations before publication; preserve alternate approved contact methods. | No acceptance inferred. |
| TI-01 and A9 publication/build-boundary ASM | Mitigate / carry forward | Product Owner / Architect | Define warehouse → curated content → generated/runtime boundary and publication enforcement later. | No acceptance inferred. |
| A9 analytics/privacy ASM | Monitor / validate later | Product Owner / Architect | Resolve measurement/privacy and runtime-boundary implications in later architecture/solutioning work. | No. |
| STEP4-R-01 | Contained / resolved Step 4 finding | Design Lead / Product Owner | Preserve historical audit and approved exception; no future approved activity currently depends on MCP TextStyle mutation. | No residual Step 5 acceptance required. |

**Accepted-risk set before Step 5:** Empty at this point. No material residual risk is being silently accepted merely to satisfy the gate. If the Product Owner chooses to accept a residual risk later, it must be recorded explicitly with rationale, owner, and conditions.

## 8. Unresolved Assumptions and Open Questions Affecting Readiness

The following remain assumptions/open questions, not requirements or validated findings:

- AS-01: portfolio improves recruiter engagement versus CV alone.
- AS-02: target audience reviews the portfolio during evaluation.
- AS-03: career material supports complete, defensible Project Stories.
- AS-04: frontend-only MVP boundary is sufficient.
- AS-05: approved foundations sufficiently constrain Explore.
- AS-07: Recruiter Journey translates effectively into the experience.
- Final Project Story content, copy, preview ordering, disclosure mechanics, Related/Next links, contact values/CV path.
- Content representation/CMS, publication-control implementation, build boundary.
- Frontend stack, hosting, deployment, rollback.
- Measurement events, privacy/retention/consent, baseline.
- Accessibility conformance level, responsive breakpoints, detailed P1 states.
- B6-approved `type/code` representation exception remains valid; no substitute font is selected.

## 9. Part C Human Review Gate

**Status:** APPROVED / COMPLETE — Product Owner 2026-09-30.

The Product Owner reviewed preserved risks, STEP4-R-01, simulated-scenario limitations, feasibility, lifecycle dispositions, the empty accepted-risk set, and unresolved assumptions/open questions. No residual risk acceptance was inferred.

## 10. SD-1 / SD-2 Readiness Dispositions

### SD-1 decision

**Decision:** All good — proceed toward Step 5, subject to completing the required SD-2 readiness disposition before Step 5 begins.

### SD-2 decision

**Disposition:** Accept as open questions.

This disposition does not constitute acceptance of the underlying residual risks, does not complete their mitigation, and does not close the open questions.

#### Success-measure testability

Carry forward the unresolved validation method, behavioral baseline, measurement mechanism, and any additional quantitative treatment as downstream validation/measurement questions. Preserve the approved overall five-minute/six-question criterion unchanged. Do not invent a usability method, analytics mechanism, baseline, participant model, or numeric threshold.

#### Feasibility

Preserve the Part C conclusions:

- Technical — concerns, not blocked.
- Operational — concerns, not blocked.
- Resource — feasible with open decisions.

Unresolved content representation, publication enforcement, build boundary, architecture, hosting, deployment, and related matters are legitimate Step 5/downstream inputs. Feasibility is not relabeled as unconditionally feasible.

#### Risk treatment

Preserve the approved `Mitigate / carry forward` and `Monitor / validate later` dispositions. The accepted residual-risk set remains empty. Carried-forward risks are not completed mitigation and are not Product Owner acceptance.

#### Hypothesis criterion

The readiness criterion is handled by the approved ERC adaptation: A8 remains intentionally excluded; no replacement hypothesis exists or is created; approved outcomes, criteria, flows, constraints, and assumptions were used for simulated analytical validation; and no empirical hypothesis validation is claimed. This is an adapted readiness treatment, not an unresolved product hypothesis requiring closure.

## 11. Final Step 4 Readiness State — COMPLETE / APPROVED

- PRD: approved and complete.
- Experience and B4–B6 design pipeline: approved and complete for ERC.
- Part C: approved and complete.
- SD-1 decision: recorded as proceed toward Step 5, subject to SD-2 disposition.
- SD-2 disposition: recorded as open questions.
- Accepted residual-risk set: empty.
- Remaining assumptions, open questions, feasibility concerns, and downstream architecture/measurement decisions: carried forward without invention or closure claims.
- Explore Step 4: **COMPLETE / APPROVED — Product Owner 2026-09-30**.
- Explore Step 5: **not started**.

The Step 4 completion state is recorded administratively. This does not resolve carried-forward architecture, implementation, measurement, content, publication, or empirical-validation questions.
