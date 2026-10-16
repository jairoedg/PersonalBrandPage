# Wireframe Blueprint: Personal Brand Website

**Project**: `personal-brand-website`  
**Created**: 2026-09-27  
**Last Updated**: 2026-09-27  
**Status**: Approved

---

## 1. Snapshot

### Objective

Produce low-fidelity wireframe specifications that define screen structure, content hierarchy, navigation, key flows, interaction intent, meaningful states, and accessibility considerations before visual design or implementation.

### Inputs

**Required**:

- `explore/explore-personal-brand-website/context.md`
- `explore/explore-personal-brand-website/domain-analysis.md`
- `explore/explore-personal-brand-website/technical-feasibility.md`
- `explore/domain/personas-personal-brand-website.md`
- Approved A10 Step 1 scope, Step 2 inventory, Step 3 conventions, Step 4 P0 specifications, Step 5 flows, Step 6 cross-screen patterns, and Step 7 open questions

**Optional / not present as separate artifacts**:

- Dedicated IA document
- Dedicated journey-map document
- Dedicated user-flow document

The approved A10 scope permits deriving and validating information hierarchy and navigation from the approved sitemap concepts, Recruiter Journey, A3 domain model, A6 personas, and A10 checkpoints.

### Output

- This document: `explore/design/wireframes-personal-brand-website.md`

### Fidelity rules

- Layout, hierarchy, content types, and interaction intent only.
- Use boxes, labels, simple component names, and placeholder intent—not final marketing copy.
- Preserve approved domain and content terminology.
- Document behavior and states in notes rather than high-fidelity visuals.
- Component names are low-fidelity wireframe labels; they do not prescribe frontend components, implementation boundaries, or design-system architecture.

### Governing experience principle

The overall experience should support the five-minute relevance/confidence objective, while every screen remains scannable and progressively discloses deeper information according to its purpose.

The approved Recruiter Journey defines a confidence-building progression, not a mandatory linear funnel. Visitors may enter, skip, revisit, or move directly between approved screens according to their evaluation needs.

---

## 2. Users and Top Tasks

### Primary users

**P1 — Technical Recruiter / Talent Acquisition**

- Goal: quickly assess relevance, profile fit, evidence, and whether to continue screening.
- Constraints: device behavior and usage context are not specified; do not invent ATS-specific requirements.

**P2 — Hiring Manager**

- Goal: inspect deeper Project and Project Story evidence, decisions, outcomes, communication, and delivery knowledge.
- Constraints: deeper evaluation should be available progressively rather than required in the initial view.

**P3 — grouped Delivery and Technology Leader context**

- Goal and detailed evidence priorities remain intentionally unspecified by the approved persona artifact.
- Constraint: A10 must not invent P3-specific evidence priorities, navigation, or calls to action.

### Top tasks

1. Determine professional identity, positioning, and relevance from Home.
2. Browse Project Story summaries and select a relevant story.
3. Evaluate a Project Story progressively from orientation through deeper public detail.
4. Explore approved capability, leadership, career, or profile context as needed.
5. Contact Jairo or access the supporting CV.

---

## 3. Scope and Constraints

### In scope

- Four P0 screen specifications: Home, Projects, Project Story Detail, Contact.
- Four P1 MVP supporting screens in the approved inventory: How I Can Help, Leadership, Career Journey, About.
- Approved confidence-building flows and legitimate shorter/exploratory paths.
- Progressive disclosure as a MUST experience requirement.
- Public presentation of publication-eligible content and appropriate public evidence/reference information.
- Contact ownership of Email, LinkedIn, Phone, and secondary CV download.
- Responsive desktop/mobile structure without device priority or numeric breakpoint assumptions.
- Accessibility and meaningful public/static experience states.

### Out of scope

- High-fidelity visual styling, final marketing copy, and final content writing.
- New product capabilities or screens.
- Runtime personalization, recommendations, chatbot, real-time behavior, or backend-dependent features.
- Search, filtering, sorting, pagination, authentication, permissions, or runtime governance UI.
- Internal Evidence lifecycle, classification, verification, approval, or restricted source material in visitor-facing UI.
- Detailed internal interactions and state specifications for P1 screens beyond their approved information hierarchies and entry points.

### Constraints

**Technical**:

- Frontend-only MVP complexity boundary; backend-dependent functionality requires a later approved requirement or identified risk.
- Context Warehouse is a governed source, not the website runtime content source.
- Markdown/file-based and static/build-time delivery remain preferred directions, not locked architecture decisions.
- Added complexity requires a concrete approved requirement or identified risk.

**Content**:

- Public claims must be truthful, traceable, attributable, and defensible.
- Project Stories derive from validated Projects.
- Public evidence/reference information is optional and must be publication-eligible and materially useful.
- CV supports recruitment but does not replace Project Story storytelling.

**Compliance and safety**:

- Publication/content-readiness failures are authoring/build concerns, not normal public runtime states.
- Restricted Evidence must not enter the deployable public content set.
- Accessibility and responsive usability remain applicable; no specific numeric conformance level is assumed here.

**Business and delivery**:

- Approved MVP surfaces are eight screens: four P0 and four P1.
- The mid-October 2026 date is a Product Owner delivery target, not a committed public release date.
- Email → LinkedIn → Phone is the current working contact order and may be revisited only with later evidence.

---

## 4. Information Architecture Alignment

### Navigation model

**Selected model**: Hub-and-spoke responsive web navigation with contextual links and legitimate shorter paths.

**Rationale**: Home establishes identity and relevance; Projects and Project Story Detail provide the primary evidence path; P1 screens provide supporting context; Contact is a distinct terminal action screen. The Recruiter Journey guides hierarchy but is not a mandatory funnel.

### Primary sections

- **Home**: identity, approved positioning, profile summary, initial evidence entry, and supporting entry points.
- **Projects**: selection-oriented collection of public Project Stories.
- **Project Story Detail**: deeper evaluation of one validated Project’s curated public narrative.
- **How I Can Help**: approved business-problem-focused capabilities.
- **Leadership**: approved leadership principles and related public evidence.
- **Career Journey**: professional experience and progression; credentials appear when relevant to a role or period.
- **About**: broader professional profile, including education, certifications, courses, and credentials.
- **Contact**: Email, LinkedIn, Phone, and secondary CV action.

### Key entities

- **Project**: canonical factual engagement and evidence record; not the public narrative by itself.
- **Project Story**: curated public narrative derived from one validated Project.
- **Evidence**: source support for claims; internal lifecycle and governance are not visitor-facing.
- **Capability**: business-problem-focused capability demonstrated across Projects.
- **Leadership Principle**: evidenced leadership belief demonstrated through Projects.
- **Career Experience**: employment or engagement period in the professional history.
- **Page / Experience**: public website screen or experience.

### Labeling assumptions

**Preferred terms**:

- Project Story: curated public narrative derived from a validated Project.
- Public evidence/reference information: optional public support that materially improves understanding or confidence.
- Contact: screen owning Email, LinkedIn, Phone, and CV download.
- Progressive disclosure: clear orientation first, deeper information available according to screen purpose.

Internal A3 prominence and narrative-role values may influence ordering and hierarchy but are not automatically exposed as raw visitor-facing governance labels.

### Risks if IA is not confirmed

- Navigation could drift from the approved sitemap concepts and Recruiter Journey.
- Screen labels or content hierarchy could become inconsistent across P0 and P1 surfaces.
- Project Story ordering could be invented rather than derived from canonical A3 decisions and approved public content.

---

## 5. Key Flows

### Flow 1: Primary relevance-to-contact journey

**Purpose**: Move from initial identity and relevance to evidence, deeper experience, confidence, and contact.

**Entry points**:

- Home.
- Approved global navigation or a direct approved link to Projects.

**Steps**:

1. Home → identity, approved positioning, profile summary, and evidence entry.
2. Home → Projects → scan Project Story summaries.
3. Projects → Project Story Detail → orientation and deeper evaluation.
4. Project Story Detail → Contact → choose Email, LinkedIn, or Phone, or access the supporting CV download.

**Progressive disclosure**:

- Home provides identity and concise orientation.
- Projects provides selection-level summaries.
- Project Story Detail provides deeper evaluation.
- Contact provides immediate action.

**Success outcome**: Visitor understands relevance and either contacts Jairo, accesses the CV, or returns to explore.

**Valid alternate paths**:

- Home → Contact.
- Project Story Detail → Projects.
- Project Story Detail → Related / Next Exploration.
- Any approved screen → global navigation.

**Edge cases**:

- No eligible Project Stories: build/publication validation issue, not a normal public runtime state.
- Incomplete Project Story: prevent publication.
- External contact destination unavailable: keep other visible approved contact methods available.
- Permission denied: not applicable to the public experience.

**P1 participation**: About, Career Journey, How I Can Help, or Leadership may be visited before Projects or Contact without defining their internal behavior.

### Flow 2: Direct contact journey

**Purpose**: Allow visitors to act without consuming the full evidence journey.

**Entry points**:

- Home, Projects, Project Story Detail, or global navigation.

**Steps**:

1. Open Contact.
2. Choose Email, LinkedIn, or Phone, or access the supporting CV download.

**Progressive disclosure**: Essential contact methods are immediately available; the CV is secondary and does not compete with direct contact.

**Success outcome**: Visitor initiates contact or obtains the CV.

**Valid alternate paths**:

- Contact → Projects.
- Contact → global navigation.
- Use another visible approved contact method if one destination is unavailable.

**Edge cases**:

- Missing CV artifact: build/publication validation failure; do not deploy a broken download.
- Missing contact destination: prevent incomplete public publication.
- No runtime destination-health detection or automated fallback.

**P1 participation**: Not required.

### Flow 3: Exploratory supporting-context journey

**Purpose**: Allow visitors to understand broader professional context before or after reviewing Project Stories.

**Entry points**:

- Home.
- Global navigation.

**Steps**:

1. Home → one or more approved P1 screens.
2. P1 screen → Projects or Project Story Detail.
3. Project Story Detail → Contact if ready.

**Progressive disclosure**: Home establishes identity; P1 screens provide supporting context; Projects and Project Story Detail provide evidence; Contact provides action.

**Success outcome**: Visitor builds confidence through an exploratory path and can continue to evidence or contact.

**Valid alternate paths**:

- P1 screen → Home.
- P1 screen → Projects.
- P1 screen → Contact.

**Edge cases**:

- Missing supporting content: prevent incomplete mandatory content from public publication.
- Broken internal link: provide usable navigation fallback.
- Permission denied: not applicable.

**P1 participation**: P1 screens participate only as approved supporting surfaces; their detailed internal behavior is not defined here.

### Flow 4: Project Story deep-evaluation and return journey

**Purpose**: Let visitors evaluate one Project Story in depth and decide what to explore next.

**Entry points**:

- Projects.
- An approved Related / Next Exploration link.

**Steps**:

1. Projects → Project Story Detail orientation layer.
2. Project Story Detail → challenge, responsibilities, decisions/actions, and outcomes.
3. Project Story Detail → leadership takeaway, approved capabilities, lessons, and appropriate public evidence/reference information.
4. Project Story Detail → Related / Next Exploration or Contact.

**Progressive disclosure**: Orientation comes first; deeper information is available according to story purpose; public evidence/reference information is optional.

**Success outcome**: Visitor understands the engagement and explores a related path or contacts Jairo.

**Valid alternate paths**:

- Project Story Detail → Projects.
- Project Story Detail → approved related Project Story.
- Project Story Detail → How I Can Help or Leadership context where supported by canonical relationships.
- Project Story Detail → Contact.

**Edge cases**:

- Missing relationship to a validated Project: publication/build failure.
- Restricted Evidence or unapproved content in deployable content: publication/build failure.
- Unsupported material claim: publication/build failure.
- Broken asset or external reference: clear fallback where meaningful.

**P1 participation**: How I Can Help and Leadership may participate through approved related exploration; no runtime recommendation logic is introduced.

---

## 6. Screen Inventory

### P0 — Must Have / Critical Path

- **Home**: primary identity, relevance, and evidence entry point.
- **Projects**: selection-oriented collection of public Project Stories.
- **Project Story Detail**: deeper evaluation of one validated Project’s curated public narrative.
- **Contact**: Email, LinkedIn, Phone, and secondary CV action.

### P1 — Important MVP Supporting Screens

- **How I Can Help**: business-problem-focused capabilities.
- **Leadership**: leadership principles and related public evidence.
- **Career Journey**: experience and progression, with credentials where relevant.
- **About**: broader professional profile, education, certifications, courses, and credentials.

### P2 — Later

No P2 screens are approved.

**Total screens**: 4 P0, 4 P1, 0 P2.

CV download, LinkedIn, email, and phone are cross-screen/contact mechanisms owned by Contact, not standalone screens.

---

## 7. Wireframe Conventions

### Layout regions

- **Header**: identity/name and primary navigation.
- **Main**: primary screen content and hierarchy.
- **Optional contextual region**: related content or supporting navigation where justified.
- **Footer**: secondary navigation and supporting links where appropriate.

### Component naming

Component names are low-fidelity wireframe labels describing recurring experience/content patterns. They do not prescribe frontend components, implementation boundaries, or design-system architecture.

Approved examples include `PageShell`, `Header`, `PrimaryNav`, `SectionIntro`, `ProjectStorySummary`, `ContactInformationGroup`, `CVDownloadAction`, `RelatedExplorationGroup`, and `FooterNav`.

### Annotation style

- Number interactive elements sequentially: `[1]`, `[2]`, `[3]`.
- Add `Interaction:`, `State:`, `Responsive:`, `Accessibility:`, and `Question:` notes where relevant.
- Capture open questions at the end of each screen.

### Fidelity rules

- Layout and hierarchy only; no visual styling.
- Boxes, labels, simple component names, and placeholder intent.
- Behavior and states in notes, not high-fidelity visuals.
- Empty/error states are documented only where meaningful for the approved static/public experience.
- Publication/build controls should prevent invalid content states from reaching visitors.

---

## 8. Screen Specs

### Screen: Home

**Purpose**: Establish identity through approved positioning and profile summary, then guide visitors to evidence, supporting context, and Contact.

**Primary actions**:

- Navigate to relevant Project Stories.
- Continue through the evidence and experience journey.
- Open Contact.

**Secondary actions**:

- Navigate to How I Can Help, Leadership, Career Journey, or About.

**Layout**:

- **Header**: professional identity/name and primary navigation.
- **Main**: identity/name, approved positioning, concise approved professional profile summary, optional Value Proposition/North Star content candidate, selected Project Story previews, supporting entry points, and Contact continuation.
- **Side**: none required.
- **Footer**: secondary navigation.

**Content hierarchy**:

1. Professional identity/name.
2. Approved positioning.
3. Concise approved professional profile summary.
4. Value Proposition / North Star where appropriate; optional and may be integrated if separate presentation is redundant.
5. Selected Project Story evidence previews; selection remains open and must use A3 decisions, Recruiter Journey, and information hierarchy.
6. Capability / How I Can Help entry point.
7. Leadership entry point.
8. Career Journey entry point.
9. Contact continuation.

**Components**:

- `PageShell`: overall structure.
- `Header`: identity and navigation.
- `SectionIntro`: approved positioning and profile summary.
- `ProjectStorySummary`: public story preview.
- `CapabilityLink`: How I Can Help entry point.
- `LeadershipPrincipleLink`: Leadership entry point.
- `CareerJourneyLink`: Career Journey entry point.
- `ContactContinuation`: route to Contact.
- `FooterNav`: secondary navigation.

**Data needs**:

- `Page / Experience` Home structure.
- Approved professional identity, positioning, and profile-summary concepts.
- Public Project Story summaries.
- Public Capability and Leadership Principle references where appropriate.
- Approved Career Experience context.

**Interaction notes**:

1. Primary evidence route opens Projects or the approved primary evidence path.
2. Project Story preview opens the corresponding Project Story Detail.
3. Supporting navigation opens the approved P1 screen.
4. Contact continuation opens Contact.

**States**:

- **Default**: approved public content renders normally.
- **Incomplete content during local review**: show a content-readiness notice; prevent public publication.
- **Loading**: no custom loading state required for the static/public experience.
- **Error**: document only for meaningful asset failures.
- **No permission**: not applicable.
- **Offline**: no custom offline capability defined.

**Accessibility notes**:

- Focus order follows identity, evidence route, Project Story previews, supporting navigation, and Contact.
- Disclosure controls must be keyboard accessible.
- Navigation-based disclosure may use semantic links.
- Headings and link purposes must be meaningful.

**Open questions**:

- Minimum approved profile summary for the first identity-to-evidence transition.
- Project Story preview selection and ordering.
- Whether the primary evidence route leads to Projects or a specific approved story.

### Screen: Projects

**Purpose**: Provide a scannable public collection of Project Stories for selection, not full evaluation.

**Primary actions**:

- Browse Project Story summaries.
- Open a relevant Project Story Detail.

**Secondary actions**:

- Use approved primary navigation.
- Open Contact.

**Layout**:

- **Header**: identity and primary navigation.
- **Main**: Projects title, approved section introduction, and Project Story summary collection.
- **Side**: none required; no filters are introduced.
- **Footer**: secondary navigation.

**Content blocks**:

- Page title and approved section framing.
- Project Story title and concise summary.
- Public business problem/context, role, or outcome only where useful and publication-eligible.
- Optional public evidence/reference information only where it materially improves relevance assessment; detailed evidence belongs primarily on Project Story Detail.
- Clear detail continuation.

**Components**:

- `PageShell`, `Header`, `PrimaryNav`, `SectionIntro`.
- `ProjectStoryList` or `ProjectStoryCollection`.
- `ProjectStorySummary`.
- `ContactContinuation`, `FooterNav`.

**Data needs**:

- Approved public Project Stories derived from validated Projects.
- Publication-eligible title, summary, context, role, outcome, and references where appropriate.

**Interaction notes**:

1. Selecting a Project Story summary opens Project Story Detail.
2. Primary navigation moves between approved MVP screens.
3. Contact continuation opens Contact.

**States**:

- **Default**: approved public Project Stories render as summaries.
- **No eligible stories during local review**: content-readiness notice; prevent invalid public publication where required.
- **Loading**: no custom loading state required.
- **Error**: meaningful asset/link fallback only.
- **No permission**: not applicable.
- **Offline**: no custom offline capability defined.

**Accessibility notes**:

- Meaningful page and Project Story headings.
- Clear accessible link purpose.
- Logical keyboard order.
- Semantic links for navigation-based disclosure.

**Open questions**:

- List, grid, or another collection pattern.
- Minimum summary fields for selection.
- Ordering based on A3 prominence/narrative decisions without exposing raw governance labels.

### Screen: Project Story Detail

**Purpose**: Present a curated public narrative of one validated Project for deeper evaluation.

**Primary actions**:

- Read orientation and deeper public story information.
- Explore approved related paths.
- Open Contact.

**Secondary actions**:

- Return to Projects.
- Use primary navigation.

**Layout**:

- **Header**: identity and primary navigation.
- **Main**: return link, story orientation, deeper evaluation, optional public reference information, Related / Next Exploration, and Contact continuation.
- **Side**: none required.
- **Footer**: secondary navigation.

**Content hierarchy**:

1. Title, concise story summary, role, relevant period/context, business problem, supported outcome/relevance signal.
2. Challenge, responsibilities, decisions/actions, and detailed outcomes.
3. Leadership takeaway, approved capabilities, lessons/professional evolution, and optional public evidence/reference information.
4. Related / Next Exploration followed by Contact.

**Components**:

- `BackToProjectsLink`, `StoryHeader`, `StorySummary`.
- `RoleAndContextBlock`, `BusinessProblemBlock`, `ChallengeAndResponsibilityBlock`.
- `DecisionAndActionBlock`, `OutcomeBlock`.
- `PublicReferenceBlock` — optional; use only where publication-eligible information materially improves understanding or confidence.
- `CapabilityLink`, `LeadershipPrincipleLink`.
- `RelatedExplorationGroup`, `ContactContinuation`, `FooterNav`.

**Data needs**:

- One approved public Project Story derived from one validated Project.
- Public title, summary, context, role, responsibilities, challenge, decisions, outcomes, and lessons where approved.
- Approved A3 capability, leadership-principle, and narrative relationships.
- Optional publication-eligible public evidence/reference information.

**Interaction notes**:

1. Return to Projects.
2. Use keyboard-accessible progressive-disclosure controls where used.
3. Open approved Related / Next Exploration links.
4. Open Contact.
5. Use primary navigation.

**States**:

- **Default**: approved public story renders normally.
- **Incomplete local content**: content-readiness notice; prevent publication.
- **Loading**: no custom loading state required.
- **Error**: meaningful asset/external-reference fallback only.
- **No permission**: not applicable.
- **Offline**: no custom offline capability defined.

**Accessibility notes**:

- Clear page and section headings.
- Logical focus from return link through story content, related exploration, and Contact.
- Disclosure controls keyboard accessible.
- Navigation-based movement uses semantic links.

**Open questions**:

- Exact progressive-disclosure mechanism.
- Exact Related / Next Exploration links.
- Which optional public references materially improve understanding or confidence.

### Screen: Contact

**Purpose**: Provide the final low-friction action path after a visitor has sufficient confidence.

**Primary actions**:

- Choose Email.
- Choose LinkedIn.
- Choose Phone.

**Secondary actions**:

- Access the supporting CV download.
- Continue to Projects where appropriate.

**Layout**:

- **Header**: identity and primary navigation.
- **Main**: Contact title, approved contact-purpose introduction, direct contact methods in Email → LinkedIn → Phone order, secondary CV download, and minimal Projects continuation.
- **Side**: none required.
- **Footer**: secondary navigation.

**Components**:

- `ContactInformationGroup`.
- `EmailAction`, `LinkedInAction`, `PhoneAction`.
- `CVDownloadAction`.
- `ContinueExploringLinks`, `Header`, `PrimaryNav`, `FooterNav`.

**Data needs**:

- Approved email, phone, LinkedIn, and CV destinations.
- Approved contact-purpose content.

**Interaction notes**:

1. Email action opens the approved email destination.
2. LinkedIn action opens the approved LinkedIn destination.
3. Phone action opens the approved phone destination where supported.
4. CV action downloads the approved CV artifact.
5. Projects continuation returns to Projects.

**States**:

- **Default**: approved contact information and CV render normally.
- **Missing contact destination during local review**: content-readiness failure; prevent incomplete publication.
- **Unavailable external destination**: keep alternative approved contact methods visibly available; no automated health detection.
- **Unavailable CV artifact during local review**: prevent publication of a broken download.
- **Loading**: no custom loading state required.
- **No permission**: not applicable.
- **Offline**: no custom offline capability defined.

**Accessibility notes**:

- Essential contact methods are immediately available and do not require progressive disclosure.
- Use descriptive labels for all contact methods.
- Preserve focus order: orientation, Email, LinkedIn, Phone, CV, Projects continuation.
- Do not rely on icons alone.
- Make external-destination behavior clear where applicable.

**Open questions**:

- Whether CV should be visually grouped separately from direct contact methods while remaining immediately available after them.
- Exact wording for contact-purpose introduction, to be supplied later without inventing claims.

### P1 Screen: How I Can Help

**Purpose**: Present the canonical A3 business-problem-focused capabilities that Jairo can demonstrate through approved professional experience.

**Information hierarchy**:

1. Page orientation.
2. Canonical Capability set.
3. Concise explanation of each Capability.
4. Supporting or related Project Stories derived from approved A3 relationships.
5. Projects and Contact continuation.

**Relationship to canonical A3 content**: Uses approved `Capability` concepts and their relationships to validated `Project` and `Project Story` content. No new capability names or mappings are introduced.

**Principal continuation paths**: Related Project Story, Projects, Contact, and approved global navigation.

**Approved content boundary**: Do not turn the page into a technology-skills catalogue or invent new capabilities. Public content must remain publication-eligible and evidence-grounded.

### P1 Screen: Leadership

**Purpose**: Present approved Leadership Principles through demonstrated professional evidence.

**Information hierarchy**:

1. Leadership orientation.
2. Approved Leadership Principles.
3. Relevant decision or Project context.
4. Related Project Stories.
5. Projects and Contact continuation.

**Relationship to canonical A3 content**: Uses approved `Leadership Principle`, `Leadership Decision`, `Project`, and `Project Story` relationships. No A3 mappings are reconstructed or re-ranked.

**Principal continuation paths**: Related Project Story, Projects, Contact, and approved global navigation.

**Approved content boundary**: Do not add unsupported leadership claims. Relationships remain grounded in approved public content and canonical A3 mappings.

### P1 Screen: Career Journey

**Purpose**: Communicate professional progression and evolution over time.

**Information hierarchy**:

1. Career Journey orientation.
2. Career Experiences in chronological context.
3. Role, organization, and period.
4. Relevant professional evolution or context.
5. Related Projects and Project Stories.
6. Credentials only when they clarify a role, career period, or progression.
7. Projects and Contact continuation.

**Relationship to canonical A3 content**: Uses approved `Career Experience`, `Role`, `Employer / Delivery Organization`, `Project`, and `Project Story` relationships.

**Principal continuation paths**: Related Project or Project Story, Projects, Contact, and approved global navigation.

**Approved content boundary**: Do not reproduce the CV as the page structure. Credentials remain contextual to professional progression.

### P1 Screen: About

**Purpose**: Provide the broader supporting professional profile.

**Information hierarchy**:

1. Concise professional biography/profile context.
2. Education.
3. Certifications.
4. Courses and professional development.
5. Other approved professional credentials.
6. Career Journey, Projects, and Contact continuation.

**Relationship to canonical A3 content**: Supports approved professional identity and `Career Experience` context without replacing Project and Project Story evidence.

**Principal continuation paths**: Career Journey, Projects, Contact, and approved global navigation.

**Approved content boundary**: About owns broader credentials. Career Journey includes credentials only when relevant to a role, period, or progression. Do not invent facts or final marketing copy.

---

## 9. Cross-Screen Patterns

### Navigation

- Consistent identity and primary navigation across screens.
- Semantic links for screen movement.
- Project Story Detail includes Return to Projects.
- Related / Next Exploration uses approved A3/content relationships only.
- Contact is reached through Contact continuation or global navigation.
- Visitors may enter, skip, revisit, or move directly between approved screens.
- No breadcrumbs are required by the current scope.

### Forms and validation

- No contact form, application form, or runtime validation workflow is introduced.
- Missing required public content, publication eligibility, or CV artifacts are build/publication validation failures.

### Feedback and messaging

- Avoid unnecessary toasts, modals, or transient messaging.
- Use clear inline/page-level fallback only for meaningful public failures such as unavailable assets or external destinations.
- Content-readiness failures remain authoring/build concerns.

### Lists and collections

- Projects uses a consistent Project Story summary collection.
- Summary content supports selection, not full evaluation.
- List/grid treatment, ordering, and detailed fields remain open for later refinement.
- No pagination, sorting, or filtering is introduced.

### Search

- Search is not introduced.

### Permissions

- The public experience has one visitor access model.
- No authentication, authorization, or visitor-specific permissions are introduced.
- Internal Evidence lifecycle and publication governance remain outside visitor-facing UI.

### Progressive disclosure

- Every screen remains scannable.
- Deeper information is disclosed according to screen purpose.
- Essential Contact methods are immediately available.
- Disclosure controls are keyboard accessible.
- Navigation-based disclosure may use semantic links.

### Contact

- Contact owns Email, LinkedIn, Phone, and the secondary CV action.
- Other screens route to Contact rather than duplicating direct contact mechanisms unless later explicitly approved.
- External fallback uses visibly available approved alternatives; no health detection or automated fallback.

### Responsive and accessibility behavior

- Support responsive desktop/mobile layouts.
- Do not assume device priority or numeric breakpoints.
- Preserve meaningful headings, focus order, accessible names, keyboard behavior, and non-visual relationship cues.

---

## 10. Validation Checklist

### Coverage

- [x] Four P0 screens have specifications.
- [x] P1 inventory includes lightweight information hierarchies without inventing detailed interactions or implementation behavior.
- [x] Approved P0 flows have start-to-finish coverage.
- [x] Screen inventory matches the approved scope.

### Clarity

- [x] Each P0 screen has a clear primary purpose.
- [x] Labels align with A3 and approved A10 decisions.
- [x] Navigation is predictable and reversible where applicable.
- [x] Component naming is consistent and explicitly non-prescriptive.

### Feasibility

- [x] Data needs use approved domain/content concepts.
- [x] Publication and content-readiness constraints are captured.
- [x] No backend, authentication, personalization, or runtime governance capability was introduced.
- [x] Contact and CV behavior respects the approved static/public boundary.

### Test readiness

- [x] Open questions are explicit and prioritized by closure impact.
- [x] Flow review tasks can be derived from the documented journeys.
- [x] Meaningful public/static states are defined without manufacturing prevented runtime states.
- [x] Accessibility considerations are documented.
- [ ] Final Step 9 validation remains pending.

---

## 11. Open Questions and Decisions Needed

### Closure status

No questions currently block A10 wireframe document completion. The following may remain open for later Experience Design, PRD, or implementation:

1. Should Projects use a list, grid, or another collection pattern?
2. Which Project Stories appear first on Home and Projects, using canonical A3 decisions and the Recruiter Journey?
3. Which summary fields are sufficient for Projects selection?
4. What exact interaction mechanism supports progressive disclosure?
5. What exact Related / Next Exploration links are supported by approved content relationships?
6. What responsive breakpoints are selected during implementation?
7. What final contact destination values and CV artifact path are used?
8. What final wording is supplied for approved content concepts?

### Resolved and not to reopen

- Eight-screen inventory: four P0 and four P1.
- Contact ordering and Contact ownership of Email, LinkedIn, Phone, and CV.
- Recruiter Journey as progression, not mandatory funnel.
- Progressive disclosure as a MUST.
- Five-minute objective as an overall initial relevance/confidence objective.
- No search, filtering, sorting, pagination, authentication, personalization, or runtime governance UI without an approved requirement.
- A3 as canonical source for domain, relationships, prominence, narrative, capability, and lifecycle detail.

### Wireframe-specific risks

- IA derivation risk because no separate IA artifact exists.
- Content readiness risk if approved public Project Story material is incomplete.
- Publication-safety risk if restricted Evidence is represented as public content.
- P1 interaction/state detail remains intentionally deferred, while approved information hierarchies are now documented.
- Responsive-detail risk because device priority and breakpoints are not selected.
- Ordering risk if Project Stories are selected outside canonical A3 and Recruiter Journey decisions.

---

## 12. Next Steps

### Immediate

- Review this complete wireframe document against the approved A10 checkpoints.
- Run A10 Step 9 final validation.
- Resolve any validation findings without changing approved A9 or A10 decisions.

### Near-term

- Refine P1 screen specifications if PRD or implementation requires them.
- Resolve list/grid and responsive interaction details.
- Supply approved content concepts and publication-eligible Project Story examples.
- Prepare a low-fidelity clickable prototype if needed.

### Future

- Prepare usability-test tasks if user validation is commissioned.
- Feed approved wireframe requirements into PRD generation.
- Define detailed interaction and implementation specifications after structural validation.

---

## 13. Acceptance Criteria

- [x] IA alignment and navigation model are documented.
- [x] Approved end-to-end P0 flows and meaningful edge cases are documented.
- [x] All four P0 screens include purpose, content hierarchy, components, actions, interactions, states, accessibility, and open questions.
- [x] P1 screens are represented as approved MVP supporting surfaces without invented internal behavior.
- [x] Assumptions and open questions are explicit and prioritized.
- [x] Cross-screen patterns are consistent and documented.
- [x] Publication/build concerns are separated from visitor-facing states.
- [x] Progressive disclosure and the five-minute overall experience principle are preserved.
- [x] Accessibility and responsive considerations are included without device-priority assumptions.
- [ ] Final Step 9 validation and Product Owner approval remain pending.

---

## Related Artifacts

- [Context](context.md)
- [Domain Analysis](domain-analysis.md)
- [Technical Feasibility](technical-feasibility.md)
- [Personas](personas-personal-brand-website.md)
- [Architecture Context](architecture-context.md)
- [Discovery Control Record](discovery.md)

**Last Updated**: 2026-09-27  
**Status**: Approved
