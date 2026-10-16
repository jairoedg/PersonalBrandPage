# Domain Analysis: Personal Brand Website

**Project**: `personal-brand-website`  
**Created**: 2026-09-21  
**Last Updated**: 2026-09-22  
**Status**: Approved — Activity 3 (Domain Analysis) complete  

---

## 1. Domain Glossary

**Purpose**: Define domain-specific terms that must be used consistently across all artifacts.

### Core Domain Terms

| Term | Definition | Synonyms (Avoid) | Context | Examples |
|------|------------|------------------|---------|----------|
| **Professional Profile** | The overall professional identity and positioning of Jairo Enrique Diaz. | Brand, personal brand | Strategic positioning, About page | Professional vision, mission, value proposition |
| **Career Experience** | A period of employment or engagement in Jairo's career. | Job, employment, work history | Career Journey page, timeline | Comverse, TCS, Endava periods |
| **Project** | The underlying professional engagement — the factual record of what was delivered, for whom, and with what outcomes. | Case study, engagement | Context Warehouse, evidence base | Entel Chile recovery, GSK O2C stream |
| **Project Story** | The curated narrative representation of a Project for the website — how it is told, its prominence, and its narrative role. | Case study, project, experience | Projects page, individual project pages | Entel Chile flagship story |
| **Employer / Delivery Organization** | The organization that employed Jairo and was responsible for the delivery capability. | Employer, company | Project facts, career experience | Comverse/Mavenir, TCS, Endava |
| **Client / Customer Organization** | The organization that received the project deliverables and business outcomes. | Customer, client company | Project facts, business context | Claro, Digicel, Entel, GT&T, DFA, Avianca, GSK, Tigo |
| **Industry** | Broad sector classification. | Vertical, domain | Project context, capability relevance | Telecommunications, Pharmaceutical, Aviation, Capital Markets |
| **Market / Geography** | Geographic scope of the engagement. | Region, location, country | Project context, scale evidence | Peru, Chile, Jamaica, Guyana, Colombia, United States |
| **Role** | Role Jairo performed on the engagement. | Position, job title | Project facts, responsibilities | Senior Project Lead, Agile Project Manager, Order-to-Cash Stream Lead |
| **Business Problem** | The organizational problem the project addressed. | Challenge, issue, pain point | Project stories, business context | VAS platform relocation, ERP migration, SOX compliance automation |
| **Responsibility** | What Jairo actually owned on the project. | Duty, task, accountability | Project facts, attribution | Stakeholder management, team coordination, delivery recovery |
| **Leadership Challenge** | A people, stakeholder, delivery, or organizational difficulty. | Obstacle, difficulty | Project stories, leadership narrative | Rebuilding customer confidence, managing distributed teams |
| **Leadership Decision** | A decision, action, or influence Jairo personally changed. | Choice, intervention | Project stories, leadership evidence | Abandoning obsolete baseline, escalating missing architect, introducing missing expertise |
| **Achievement** | What Jairo or the project accomplished. | Success, result | Project facts, evidence | Production go-live, customer recognition, satisfaction improvement |
| **Business Outcome** | What changed for the client organization or its users. | Result, impact, benefit | Project stories, value proposition | Confidence restored, multi-country delivery, process refactoring |
| **Evidence** | Supporting material for publishable claims. | Proof, data, metric | Evidence strategy, claim traceability | KPI, business outcome, client recognition, team size, geographic scope |
| **Capability** | A business-problem-focused capability demonstrated across projects. | Skill, competency | How I Can Help, capability pages | Recovering complex delivery under pressure, aligning business and technology |
| **Technology** | Technology landscape at useful business-level depth. | Stack, tool | Project context, technical fluency | Azure, SAP, VAS, gRPC, Big Data |
| **Leadership Principle** | A core leadership belief demonstrated through projects. | Value, belief | Leadership page, project stories | People first, predictable delivery, continuous evolution |
| **Lesson Learned** | What changed in leadership/delivery thinking after the experience. | Takeaway, insight | Project stories, professional evolution | Data readiness, governance, delegation, escalation |
| **Page / Experience** | A page or interactive experience on the website. | Screen, section | Information architecture, wireframes | Home, Projects, Leadership, Contact |
| **Audience Segment** | A group of visitors with shared goals. | User type, persona | Personas, experience design | Recruiter, Hiring Manager, CTO, Consulting Client |

### Domain Actions (Verbs)

| Action | Definition | When Used | Examples |
|--------|------------|-----------|----------|
| **Progressive Disclosure** | Presenting minimal information initially, with deeper detail available on demand. | Information architecture, UX design | Summary cards → expandable sections → project pages |
| **Information Hierarchy** | The order and depth in which content is presented. | Homepage, page layouts, scanning | Hero claim → featured evidence → supporting details |
| **Normalize** | Structuring raw project knowledge into canonical domain entities. | A3, content production | Extracting client, role, outcomes, evidence from source documents |
| **Validate** | Confirming that material publishable claims have traceable, attributable, sufficiently strong evidence. | Project lifecycle, before story creation | Checking evidence completeness and defensibility |
| **Curate** | Selecting and shaping validated Project facts into a public Project Story. | Project Story lifecycle | Choosing prominence, narrative role, and presentation emphasis |
| **Surface** | Presenting a demonstrated capability or principle to visitors through a Project Story. | Project Story → Capability relationship | Entel Chile story surfaces **Recovering complex delivery under pressure** and **Leading complex stakeholder environments** |
| **Classify** | Assigning publication sensitivity or prominence/role values. | Publication decisions, story setup | `named`/`anonymised`/`restricted`; `flagship`/`supporting`/`contextual` |

### States and Statuses

| State | Definition | Applies To | Next States |
|-------|------------|------------|-------------|
| **draft** | Raw notes, initial capture, or content being edited | Project, Project Story, Career Experience, Page/Experience, Capability | normalized, review, wireframed, validated |
| **normalized** | Structured into the canonical domain entities with the currently available fields captured | Project | validated |
| **validated** | Evidence checked; stable factual record or approved public-ready content | Project, Career Experience, Capability | published (for public-content entities); stable state (Project) |
| **review** | Under steering-team review | Project Story | approved, draft |
| **approved** | Jairo confirmed accurate and publishable | Project Story | published |
| **published** | Live on website | Project Story, Career Experience, Page/Experience, Capability | retired, draft/wireframed (revision) |
| **retired** | Removed from public site — terminal publication state | Project Story, Page/Experience | — |
| **collected** | Evidence gathered from project sources | Evidence | assessed |
| **assessed** | Traceability, attribution, strength evaluated; sensitivity classified | Evidence | verified |
| **verified** | Sufficient to support publishable claims | Evidence | — |

### Roles and Actors

| Role | Definition | Responsibilities | Not To Be Confused With |
|------|------------|------------------|-------------------------|
| **Content Owner** | The person whose professional experience is the domain content and who holds final authority over all publication decisions (Jairo Enrique Diaz) | Approve/reject all public content; assign publication classifications; resolve strategic conflicts | Product Owner (organizational title) — same person, different lens |
| **Content Curator** | The actor who normalizes Projects, drafts Project Stories, proposes capabilities, and maintains the domain model (Devin / agent) | Normalize Projects; draft narratives; propose taxonomy; validate evidence traceability | Architect or Lead Engineer — those are implementation roles, not content roles |
| **Visitor** | Any person accessing the public website. All Visitors have the same access to published public content. | Navigate Recruiter Journey; read stories; evaluate evidence; initiate contact | Audience Segment — segments prioritize UX, they do not change access permissions |
| **Build System** | Automated system that transforms curated content into the static website | Read deployment-eligible content; generate pages; deploy assets | CMS or backend — this is a static build pipeline |
| **Analytics Collector** | System role that measures visitor behavior and outcomes | Collect defined events; aggregate metrics | Tracking pixel or cookie banner — implementation details TBD |

---

## 2. Domain Model

**Purpose**: Map core entities, their attributes, and relationships to support product and architecture decisions.

### Core Entities

**Professional Profile**

- **Description**: The overall professional identity and positioning of Jairo Enrique Diaz.
- **Category**: Core
- **Key Attributes**:
  - `name`: string — Full professional name
  - `tagline`: string — Positioning statement
  - `vision`: string — Professional vision
  - `mission`: string — Professional mission
  - `value_proposition`: string — What Jairo offers
  - `leadership_philosophy`: string — Core leadership belief summary
- **Lifecycle States**: `active`
- **Relationships**:
  - Has many `Career Experiences` (one-to-many)
  - Has many `Leadership Principles` (one-to-many)
- **Business Rules**: Must remain aligned with approved foundation documents (BR-10)

---

**Career Experience**

- **Description**: A period of employment or engagement in Jairo's career.
- **Category**: Core
- **Key Attributes**:
  - `employer`: string — Employer / Delivery Organization
  - `role_title`: string — Position held
  - `start_date`: date — Period start
  - `end_date`: date — Period end
  - `summary`: string — Experience overview
  - `key_themes`: list — Major themes of the period
- **Lifecycle States**: `draft → validated → published`
- **Relationships**:
  - Belongs to `Professional Profile` (many-to-one)
  - Has many `Projects` (one-to-many)
  - References `Employer / Delivery Organization` (many-to-one)
- **Business Rules**: Public claims about employer, title, dates, progression, and themes must be validated before publication

---

**Project**

- **Description**: The underlying professional engagement — the factual record of what was delivered, for whom, and with what outcomes. This is the knowledge/evidence layer.
- **Category**: Core
- **Key Attributes**:
  - `title`: string — Project name
  - `period`: string — Engagement period
  - `status`: string — Outcome status
  - `geographic_scope`: enum — `single_country`, `multi_country`, `regional`, `international`
  - `publication_class`: enum — `named`, `anonymised`, `restricted` (required before any derived Project Story is approved)
- **Lifecycle States**: `draft → normalized → validated`
- **Relationships**:
  - Belongs to `Employer / Delivery Organization` (many-to-one)
  - Belongs to `Client / Customer Organization` (many-to-one)
  - Belongs to `Industry` (many-to-one)
  - Has many `Markets / Geographies` (many-to-many)
  - Has many `Roles` (many-to-many)
  - Addresses many `Business Problems` (many-to-many)
  - Has many `Responsibilities` (one-to-many)
  - Has many `Leadership Challenges` (one-to-many)
  - Has many `Leadership Decisions` (one-to-many)
  - Has many `Achievements` (one-to-many)
  - Has many `Business Outcomes` (one-to-many)
  - Has many `Technologies` (many-to-many)
  - Has many `Lessons Learned` (one-to-many)
  - Demonstrates many `Capabilities` (many-to-many)
  - Supports many `Project Stories` (one-to-many)
- **Business Rules**: Must be validated before any governed Project Story is created; material publishable claims must have traceable, attributable, sufficiently strong evidence (BR-01)

---

**Project Story**

- **Description**: The curated narrative representation of a Project for the website — how it is told, its prominence, and its narrative role. This is the public content layer.
- **Category**: Core
- **Key Attributes**:
  - `project_id`: reference — Source Project
  - `title`: string — Public story title
  - `visitor_prominence`: enum — `flagship`, `supporting`, `contextual`
  - `narrative_role`: enum — `project_recovery`, `adaptive_delivery`, `cross_domain_leadership`, `business_technology_alignment`, `delivery_governance`, `professional_evolution`
  - `summary`: string — Story summary
  - `leadership_takeaway`: string — Key leadership insight
  - `publication_class`: enum — `named`, `anonymised`, `restricted`
  - `evidence_level`: string — Depth of evidence presented
- **Lifecycle States**: `draft → review → approved → published → retired`
- **Relationships**:
  - Derived from one `Project` (many-to-one)
  - Surfaces many `Capabilities` (many-to-many)
  - Illustrates many `Leadership Principles` (many-to-many)
  - Presented by many `Pages / Experiences` (many-to-many)
- **Business Rules**: Must derive only from validated Projects; prominence and narrative role are independent; publication class controls disclosure

---

**Employer / Delivery Organization**

- **Description**: The organization that employed Jairo and was responsible for the delivery capability.
- **Category**: Core
- **Key Attributes**:
  - `name`: string — Organization name
  - `sector`: string — Industry sector
  - `delivery_model`: string — How delivery was organized
- **Lifecycle States**: `active`
- **Relationships**:
  - Has many `Career Experiences` (one-to-many)
  - Has many `Projects` (one-to-many)
- **Business Rules**: Distinct from Client; may be anonymised in public content if required

---

**Client / Customer Organization**

- **Description**: The organization that received the project deliverables and business outcomes.
- **Category**: Core
- **Key Attributes**:
  - `name_public`: string — Publicly displayable name
  - `name_internal`: string — Internal reference name
  - `industry`: reference — Sector classification
  - `publication_class`: enum — `named`, `anonymised`, `restricted`
- **Lifecycle States**: `active`
- **Relationships**:
  - Has many `Projects` (one-to-many)
  - Belongs to `Industry` (many-to-one)
- **Business Rules**: Publication classification determines whether name is shown, anonymised, or restricted

---

**Industry**

- **Description**: Broad sector classification.
- **Category**: Reference
- **Key Attributes**:
  - `name`: string — Industry name
  - `description`: string — Sector description
- **Lifecycle States**: `active`
- **Relationships**:
  - Contains many `Clients / Customers` (one-to-many)
  - Classifies many `Projects` (one-to-many)
- **Business Rules**: Project industry is the visitor-relevant classification

---

**Capability**

- **Description**: A business-problem-focused capability demonstrated across projects.
- **Category**: Core
- **Key Attributes**:
  - `name`: string — Capability name (business-problem framed)
  - `description`: string — What the capability means
  - `business_problem_framing`: string — The business problem it solves
- **Lifecycle States**: `draft → validated → published`
- **Relationships**:
  - Demonstrated by many `Projects` (many-to-many)
  - Surfaced by many `Project Stories` (many-to-many)
  - Presented by many `Pages / Experiences` (many-to-many)
- **Business Rules**: Must describe a business problem or outcome, not a technology skill (BR-02); evidence may be positive, developmental, or learning-based (BR-06)

---

**Leadership Principle**

- **Description**: A core leadership belief demonstrated through projects.
- **Category**: Core
- **Key Attributes**:
  - `name`: string — Principle name
  - `description`: string — What the principle means
- **Lifecycle States**: `active`
- **Relationships**:
  - Illustrated by many `Project Stories` (many-to-many)
  - Illustrated by many `Leadership Decisions` (many-to-many)
- **Business Rules**: Must be evidenced through projects, not stated as unsupported claim

---

**Page / Experience**

- **Description**: A page or interactive experience on the website.
- **Category**: Core
- **Key Attributes**:
  - `name`: string — Page name
  - `purpose`: string — Page objective
  - `audience`: list — Target Audience Segments
  - `content_entities`: list — Content types presented
  - `navigation_paths`: list — How visitors move through the page
- **Lifecycle States**: `draft → wireframed → specified → published`; `published → draft/wireframed` (revision); `published → retired`
- **Relationships**:
  - Presents selective `Project Stories`, `Capabilities`, `Leadership Principles` (many-to-many)
  - Designed for `Audience Segments` (many-to-many)
- **Business Rules**: Must support the Recruiter Journey and five-minute success criteria

---

**Audience Segment**

- **Description**: A group of visitors with shared goals.
- **Category**: Reference
- **Key Attributes**:
  - `name`: string — Segment name
  - `role`: string — Visitor role type
  - `primary_questions`: list — What they want to know
  - `success_criteria`: list — What success looks like for them
- **Lifecycle States**: `active`
- **Relationships**:
  - Served by many `Pages / Experiences` (many-to-many)
- **Business Rules**: Primary segments are Recruiters and Hiring Managers; secondary segments are Delivery/Program Managers, CTOs, Consulting Clients, Internal Endava Managers

---

### Supporting Entities

**Role**

- **Description**: Role Jairo performed on the engagement.
- **Purpose**: Captures the function performed, not just the organizational title.
- **Key Attributes**: `title`, `level`, `scope`
- **Relationships**: Belongs to many `Projects`

**Business Problem**

- **Description**: The organizational problem the project addressed.
- **Purpose**: Frames the project in business terms, not technology terms.
- **Key Attributes**: `description`, `context`, `severity`
- **Relationships**: Addressed by many `Projects`

**Responsibility**

- **Description**: What Jairo actually owned on the project.
- **Purpose**: Distinguishes individual contribution from team achievement.
- **Key Attributes**: `description`, `scope`
- **Relationships**: Belongs to a `Project`

**Leadership Challenge**

- **Description**: A people, stakeholder, delivery, or organizational difficulty.
- **Purpose**: Captures the leadership dimension of the project.
- **Key Attributes**: `description`, `impact`
- **Relationships**: Belongs to a `Project`

**Leadership Decision**

- **Description**: A decision, action, or influence Jairo personally changed.
- **Purpose**: Provides concrete leadership evidence.
- **Key Attributes**: `description`, `outcome`, `evidence_ref`
- **Relationships**: Belongs to a `Project`; illustrates `Leadership Principles`

**Achievement**

- **Description**: What Jairo or the project accomplished.
- **Purpose**: The positive action, deliverable, or result attributable to the engagement.
- **Key Attributes**: `description`, `evidence_ref`
- **Relationships**: Belongs to a `Project`; supported by `Evidence`; may contribute to `Business Outcomes`

**Business Outcome**

- **Description**: What changed for the client organization or its users.
- **Purpose**: The impact, benefit, or observable improvement.
- **Key Attributes**: `description`, `quantitative_value`, `evidence_ref`
- **Relationships**: Belongs to a `Project`; supported by `Evidence`

**Evidence**

- **Description**: Supporting material for publishable claims.
- **Purpose**: Makes claims traceable, attributable, and defensible.
- **Key Attributes**: `type`, `value`, `source`, `publication_sensitivity`, `verification_level`
- **Relationships**: Supports `Publishable Claims` (Achievements, Business Outcomes, Leadership Decisions, Responsibilities, Capabilities, and other assertions)

**Lesson Learned**

- **Description**: What changed in leadership/delivery thinking after the experience.
- **Purpose**: Captures professional evolution.
- **Key Attributes**: `description`, `context`
- **Relationships**: Belongs to a `Project`

**Technology**

- **Description**: Technology landscape at useful business-level depth.
- **Purpose**: Provides technical context without dominating the narrative.
- **Key Attributes**: `category`, `platforms`, `tools`, `purpose`
- **Relationships**: Used in many `Projects`

**Market / Geography**

- **Description**: Geographic scope of the engagement.
- **Purpose**: Captures location and scale.
- **Key Attributes**: `country_region`, `region`
- **Relationships**: Associated with many `Projects`

---

### Reference Data

| Reference Type | Description | Examples | Source |
|----------------|-------------|----------|--------|
| **Publication Classification** | Controls public presentation of client/project identity and details | `named`, `anonymised`, `restricted` | Jairo decision per project |
| **Evidence Publication Sensitivity** | Controls whether supporting evidence itself may be exposed publicly, anonymised, or retained internally | `public`, `anonymised`, `restricted` | Jairo/Devin assessment per evidence item |
| **Visitor Prominence** | How strongly a Project Story is surfaced to visitors | `flagship`, `supporting`, `contextual` | Derived from evidence depth and visitor value |
| **Narrative Role** | What a Project Story demonstrates about leadership and delivery capability | `project_recovery`, `adaptive_delivery`, `cross_domain_leadership`, `business_technology_alignment`, `delivery_governance`, `professional_evolution` | Derived from evidence and narrative themes |
| **Industry Taxonomy** | Sector classification for visitor relevance | `telecommunications`, `pharmaceutical`, `aviation`, `capital_markets`, `consulting`, `other` | Project Knowledge Base |
| **Market / Geography Taxonomy** | Geographic scope for visitor relevance | `peru`, `chile`, `jamaica`, `guyana`, `colombia`, `united_states`, `andean`, `caribbean`, `other` | Project Knowledge Base |
| **Geographic Scope** | Scale of the engagement | `single_country`, `multi_country`, `regional`, `international` | Project attribute |

---

### Entity Relationship Diagram (Text-Based)

```
Professional Profile
        │ 1
        │
        └──< Career Experiences
                    │
                    ├──> Employer / Delivery Organization
                    │
                    └──< Projects
                            │
                            ├──> Employer / Delivery Organization
                            ├──> Client / Customer Organization
                            │        └──> Industry
                            ├──> Industry
                            ├──<> Markets / Geographies
                            ├──<> Roles
                            ├──<> Business Problems
                            ├──< Responsibilities
                            ├──< Leadership Challenges
                            ├──< Leadership Decisions
                            │       └──<> Leadership Principles
                            │
                            ├──< Achievements
                            │       └──<> Evidence
                            │
                            ├──< Business Outcomes
                            │       └──<> Evidence
                            │
                            ├──<> Technologies
                            ├──<> Capabilities
                            ├──< Lessons Learned
                            │
                            └──< Project Stories
                                    │
                                    ├──<> Capabilities
                                    ├──<> Leadership Principles
                                    └──<> Pages / Experiences

Pages / Experiences
        │
        └──<> Audience Segments
```

**Conceptual overlay**: `Evidence ──supports──> Publishable Claims` — not restricted to Achievements and Business Outcomes only.

---

### Approved Domain Taxonomies and Mappings

The following taxonomies were approved during the A3 working sessions. They are restored here so the canonical model is preserved in the durable artifact rather than only in the conversation transcript.

#### Layer 1 — Evidence-Derived Delivery Signals

**Purpose**

Layer 1 records the project-specific observations used to derive the canonical professional capabilities in Layer 2. It separates delivery signals, business context, technology/domain information, and supporting practices or reported outcomes.

These entries summarize the source documents. They do not, by themselves, mark individual Evidence items as `verified`, authorize publication, or establish successful mastery of a capability. Evidence assessment and publication approval remain governed by the existing lifecycles and BR-01, BR-05, and BR-06.

| Project | Evidence-Derived Delivery Signals | Context | Technology / Domain Evidence | Supporting Practices / Reported Outcomes |
|---------|-----------------------------------|---------|------------------------------|------------------------------------------|
| **Claro Peru** | Managing complex delivery dependencies; aligning customer, supplier, and third-party teams; maintaining constructive customer communication under schedule pressure. | International telecommunications modernization supporting a 4G rollout; infrastructure, facility, hardware, software, and network-integration dependencies. | Comverse VAS platform; Linux; 4G integration; Huawei network infrastructure. | Separate tracking of customer-owned and supplier-owned delays; risk/issue and dependency tracking; weekly status reporting; using external delays to improve internal readiness; production deployment and support handover. Source: `Claro-Peru.md`. |
| **Digicel Jamaica** | Customer-facing implementation leadership; coordinating dependencies and managing expectations under uncertainty; learning the importance of earlier prerequisite validation, realistic planning, and proactive risk identification. | Post-earthquake VAS platform relocation from Haiti to Jamaica; business-continuity requirements and service support for both markets. | Telecommunications VAS; proprietary Comverse hardware/software; Linux; mobile-network integrations. | Infrastructure validation and installation coordination; hardware and access-blocker escalation; customer status communication; testing and production deployment. The account records schedule extension and lessons about preparation—it does not establish that those lessons had already been applied successfully at the start of this engagement. Source: `Digicel-Jamaica.md`. |
| **Entel Chile** | Recovering a troubled engagement through objective assessment, credible replanning, and visible corrective action; restoring customer participation; mobilizing stronger internal technical support. | Recovery of a delayed transformation engagement at an established telecommunications operator, with deteriorated customer confidence and reduced testing participation. | Linux; mobile networking; proprietary Comverse telecommunications software; VAS. | Assessment of actual progress and remaining issues; revised delivery plan; escalation to development, architecture, and Tier 4 support; quick wins; milestone tracking; renewed customer participation; initial contractual scope entering production. Source: `Entel-Chile.md`. |
| **Entel Peru** | Adapting delivery strategy to maintain momentum when the original plan is disrupted; maintaining customer collaboration; connecting presales scope/timeline definition with implementation coordination. | Telecommunications market-entry and 4G transformation; customer, supplier, offshore-development, and third-party dependencies. | VAS services including VMS, USSD, and SMS; Linux; Cisco networking; proprietary Comverse software; 4G integrations. | Scope and timeline discussions; advancing available work during software delays; negotiating incremental releases; increasing customer testing capacity; production deployment and support handover; customer LinkedIn recommendation reported in the source. Source: `Entel-Peru.md`. |
| **GT&T Guyana** | Disciplined implementation coordination; consistent customer communication; dependency, risk, and blocker management. | Greenfield VAS implementation for a telecommunications operator in Guyana. | VAS platform; integration with existing telecommunications platforms, including prepaid charging systems. | Weekly status reporting; implementation-team coordination; risk/blocker management; production deployment following a moderate schedule extension. The source provides a concise account and does not establish a more extensive governance or adaptation narrative. Source: `GTT-Guyana.md`. |
| **DFA** | Adaptive Agile delivery; aligning technical, business, and delivery stakeholders; escalating missing business support; introducing specialist expertise; protecting team continuity; coordinating continuous releases. | Capital markets and investment-management integration; adapting existing business processes to a cloud-hosted IMS connectivity model. | C#; Azure; gRPC; REST; API Gateway; SSRS; SQL Server; automated and performance testing. | Team setup; RACI, roadmap, Definition of Ready/Done, and cost-baseline preparation; stakeholder reviews every two weeks; team-health monitoring; expertise introduced for gRPC; release coordination; production support and reported client-satisfaction improvement. Source: `DFA-CapitalMarket.md`. |
| **Avianca** | Shaping a technology initiative through business-case and TCO work, initial roadmapping, and expert coordination; identifying and escalating missing technical ownership rather than absorbing architectural accountability. | Aviation analytics modernization; participation limited to inception, due diligence, and project definition—not migration implementation. | Azure; Oracle Exadata; Databricks; Synapse; Spark; MySQL; cloud-data modernization. | Business Case and TCO completed; funding documentation prepared; initial roadmap and delivery planning; Microsoft collaboration; expert decision forum; escalation of the missing Data Architect; leadership of small ML/AI proofs of concept. Final architecture, scope, cost, and complete migration strategy remained outstanding when Jairo left. Source: `Avianca-DWH-migration-to-Azure.md`. |
| **GSK** | Business–technology translation; cross-functional stakeholder coordination; regulatory-change management; multi-country workstream delivery; learning an unfamiliar business domain sufficiently to connect specialists. | Pharmaceutical ERP transformation from JD Edwards to SAP; Order-to-Cash and electronic-invoicing workstream across Colombia, Peru, Ecuador, and Chile. | SAP; JD Edwards; electronic-invoicing interfaces; third-party provider integrations. | Business-process learning; requirements gathering; supplier selection/procurement involvement; country-interface planning; cross-stream dependency management; workstream readiness for the wider SAP go-live; provider-contract closure within available budget; client recognition reported in the source. Source: `GSK-O2CStreamLead.md`. |
| **Tigo** | Leading and coordinating a large multi-team distributed delivery environment; identifying architecture, data-readiness, team-capability, ownership, and escalation problems; recognizing shortcomings in Jairo’s own response and drawing lessons for later engagements. | SOX-control automation using a Big Data platform; product work in Colombia and development teams in India. The original delivery model failed to achieve its intended objectives and was stopped and restructured. | Big Data; Spark; Hive; MySQL; Data Warehouse; ingestion/transformation pipelines; Tableau reporting. | Product-definition and architecture-coordination responsibilities; risk reporting; acknowledged weaknesses in delegation, escalation, architectural consistency, and program structure; participation in restructuring reported in the source. These observations provide developmental and learning-based evidence, not proof of successful delivery or governance mastery. Source: `Tigo-sox-big-data-program.md`. |

**Layer 1 interpretation boundaries**

- Layer 1 is not the public capability catalogue. Technology, delivery context, practices, and reported outcomes remain distinct from the eight canonical capabilities. The approved Capability-to-Project Matrix determines which relationships are selected; the presence of an observation in Layer 1 does not automatically add another relationship.
- Lessons must remain distinguishable from actions already demonstrated. Digicel’s account includes retrospective lessons about preparation and earlier dependency identification; Tigo explicitly records inadequate responses and later learning. Neither should be rewritten as unqualified evidence of successful mastery.
- Contribution boundaries remain intact. Avianca supports project-definition experience, not completed migration delivery. GSK supports leadership of the Order-to-Cash workstream, not ownership of the entire global ERP program.
- Source references are not verification results. A project document reporting recognition, satisfaction improvement, or production completion establishes where the statement came from. Individual claims still require the agreed assessment of attribution, evidence strength, and publication suitability.
- The Layer 1 wording includes the source-accuracy clarification that Digicel uses “status communication,” not “weekly reporting,” because its source does not specify that cadence. Weekly reporting is explicitly documented for Claro and GT&T.

#### Layer 2 — Canonical Professional Capabilities

These are the approved capability names and definitions. Project assignments belong in the capability-to-project matrix and are intentionally not duplicated here.

| # | Canonical Capability | Definition |
|---|----------------------|------------|
| 1 | **Recovering complex delivery under pressure** | Re-establishing credible plans, mobilizing support, and restoring execution when delivery is off track. |
| 2 | **Aligning business and technology** | Translating business needs, technical realities, and delivery implications so stakeholders can make decisions. |
| 3 | **Leading complex stakeholder environments** | Creating alignment across clients, suppliers, specialists, distributed teams, and leadership. |
| 4 | **Improving delivery predictability** | Reducing uncertainty through planning, dependency management, risk management, and transparent communication. |
| 5 | **Leading distributed and multi-organization delivery** | Coordinating teams across organizations, countries, and specialist disciplines. |
| 6 | **Adapting delivery when conditions change** | Changing plans, sequencing, resources, or delivery approaches when evidence invalidates original assumptions. |
| 7 | **Turning technology initiatives into executable delivery plans** | Establishing scope, roadmaps, business cases, TCO, ownership, dependencies and delivery readiness before implementation. |
| 8 | **Leading effectively across unfamiliar domains** | Learning enough of a new business/technology environment to connect specialists and lead delivery without pretending to be the deepest SME. |

**Naming changes preserved**: Capability #5 replaces “Leading distributed and multi-party delivery”; capability #7 replaces “Shaping technology initiatives before execution.” Definition #7 includes dependencies, as approved in the A3 review.

#### Capability-to-Project Matrix

The matrix records approved capability relationships. A marked relationship means the Project contains meaningful evidence of the Capability; it does not by itself imply successful mastery. Evidence nature and strength remain traceable to the underlying Project. `†` marks learning-based evidence rather than positive mastery evidence.

| Canonical Capability | Claro Peru | Digicel Jamaica | Entel Chile | Entel Peru | GT&T Guyana | DFA | Avianca | GSK | Tigo |
|----------------------|:----------:|:---------------:|:-----------:|:----------:|:----------:|:---:|:-------:|:---:|:----:|
| **Recovering complex delivery under pressure** | — | — | ● | — | — | — | — | — | — |
| **Aligning business and technology** | — | — | — | — | — | ● | ● | ● | — |
| **Leading complex stakeholder environments** | ● | — | ● | ● | — | ● | — | ● | ●† |
| **Improving delivery predictability** | ● | ● | — | — | ● | ● | — | — | — |
| **Leading distributed and multi-organization delivery** | ● | — | ● | ● | — | ● | — | ● | ●† |
| **Adapting delivery when conditions change** | — | — | ● | ● | — | ● | — | — | — |
| **Turning technology initiatives into executable delivery plans** | — | — | — | ● | — | — | ● | — | — |
| **Leading effectively across unfamiliar domains** | — | — | — | — | — | — | ● | ● | — |

**Matrix legend**: `●` = relationship included in the reviewed matrix; `—` = no relationship selected in this matrix, not proof that the Project contains no relevant experience. `●†` preserves the Tigo qualification: the relationship provides developmental or learning-based evidence, not a claim of successful mastery. This matches BR-06.

**Corrections incorporated from matrix review**:

- **Removed**: Entel Peru → `Recovering complex delivery under pressure`. Entel Chile remains the clear recovery example; Entel Peru remains linked to `Adapting delivery when conditions change`.
- **Added**: Claro Peru → `Leading distributed and multi-organization delivery`, recognizing coordination across Claro, Comverse, and external technology stakeholders.
- **Final row confirmed**: `Leading effectively across unfamiliar domains` → Avianca and GSK.
- All other marked relationships remain as shown in the reviewed matrix.

**Matrix interpretation notes**:

- The matrix is not a success score or a prominence ranking. Tigo’s two marked relationships retain their developmental/learning qualification because the source states that the original delivery model did not achieve its intended objectives and should be represented as a learning experience rather than a successful case study.
- Avianca’s relationship to `Turning technology initiatives into executable delivery plans` records relevant project-definition experience. It must not be used to claim that Jairo completed or delivered the migration: his participation was limited to project definition, and the final architecture, scope, cost, and complete migration strategy remained outstanding when he left.
- `Professional evolution through applied learning` remains a narrative theme and the Tigo → Avianca → DFA arc, not a ninth canonical Capability. The separate professional-evolution section below preserves that arc.

#### Narrative Role Taxonomy (final)

| Narrative Role | Definition | Primary Projects | Supporting Projects | Learning Contrast / Cross-Project |
|----------------|------------|------------------|---------------------|-----------------------------------|
| `project_recovery` | Restoring a troubled engagement to credible delivery | Entel Chile | — | — |
| `adaptive_delivery` | Delivering despite changing conditions, uncertainty, or disrupted assumptions | Entel Peru, DFA | Claro Peru, Digicel Jamaica | — |
| `cross_domain_leadership` | Leading successfully in an unfamiliar industry, technology, or business domain | GSK, Avianca | DFA | — |
| `business_technology_alignment` | Connecting business problems with technical solutions and translating across stakeholders | GSK, Avianca, DFA | — | — |
| `delivery_governance` | Establishing structure, governance, and disciplined execution for complex delivery | DFA | GT&T | Tigo = learning contrast |
| `professional_evolution` | Demonstrating growth, learning, and career progression through experience | — | — | Tigo → Avianca → DFA = primary cross-project arc |

**Role semantics**:
- **Primary** = strong evidence; narrative is central to the story.
- **Supporting** = meaningful evidence; narrative is not the defining story.
- **Learning Contrast** = demonstrates why the capability/narrative became important through an acknowledged shortcoming or unsuccessful approach.

#### Project Story Prominence (final)

Prominence describes how strongly a story is surfaced to visitors. It is **independent** of narrative role.

| Project | Prominence | Rationale |
|---------|------------|-----------|
| **Entel Chile** | `flagship` | Strong recovery evidence; rebuilding confidence through credible replanning and visible corrective action |
| **GSK** | `flagship` | Strong cross-domain and multi-country leadership; business/technology translation; regulatory complexity; direct recognition |
| **DFA** | `flagship` | Mature modern delivery leadership; complex Agile/cloud integration; measurable satisfaction improvement |
| **Entel Peru** | `supporting` | Strong adaptive delivery; presales-to-delivery experience; client recognition |
| **Digicel Jamaica** | `supporting` | Early customer-facing leadership and delivery under substantial operational constraints |
| **Tigo** | `supporting` | Critical learning experience and essential foundation of the professional-evolution narrative |
| **Avianca** | `contextual` | Valuable business-case/cloud-definition and leadership-evolution evidence, but participation ended before execution |
| **Claro Peru** | `contextual` | Solid dependency, stakeholder and multi-organization delivery evidence reinforcing telecom depth |
| **GT&T Guyana** | `contextual` | Supports early-career delivery discipline; evidence currently less developed |

#### Professional Evolution Arc (first-class narrative)

The Tigo → Avianca → DFA sequence must be preserved as a connected narrative across Career Journey and Leadership pages, not flattened into three independent capability lists.

| Project | What Happened | What Changed in Jairo's Leadership |
|---------|---------------|-----------------------------------|
| **Tigo** | Original delivery model failed; insufficient architecture governance, delegation, escalation, and program structure | Learned consequences of absorbing accountability and not standing ground on structural problems |
| **Avianca** | First cloud/Azure, first aviation engagement, missing Data Architect | Applied lesson: assembled expert table, escalated missing Data Architect instead of absorbing technical accountability |
| **DFA** | Complex Agile delivery, gRPC complexity, stakeholder availability constraints | Demonstrated maturity: brought in right expertise, escalated missing business support, kept decision-makers aligned, adapted delivery pragmatically |

#### Narrative Themes — Approved Analysis

| Narrative Theme | Meaning | Primary Evidence | Supporting Evidence / Learning Contrast |
|----------------|---------|------------------|----------------------------------------|
| **Restoring confidence through visible corrective action** | Rebuilding trust through credible replanning and observable delivery progress. | Entel Chile | Digicel Jamaica supports maintaining customer confidence during uncertainty, not recovering an already damaged relationship. |
| **Adapting delivery when assumptions fail** | Changing plans, sequencing, resources, or approaches when original assumptions no longer hold. | Entel Peru, DFA | Tigo provides a learning contrast about responding and escalating too late or insufficiently. |
| **Leading across unfamiliar domains** | Learning enough of a new business/technology environment to connect specialists and lead within the appropriate responsibility boundary. | GSK, Avianca | DFA provides reinforcement. |
| **Creating structure that makes complex delivery executable** | Establishing ownership, governance, and coordination appropriate to complex work. | DFA | Tigo provides a learning contrast through shortcomings in architecture governance, delegation, and program structure. |
| **Professional evolution through applied learning** | Showing how earlier experience informed changes in later leadership behavior. | Tigo → Avianca → DFA | Preserve the approved cross-project arc. Do not restore the unsupported GT&T → Digicel arc. |

The distinctions in this table follow the project accounts and the refinements agreed in the narrative review. These themes are separate from the approved Narrative Role Taxonomy and do not change role or prominence assignments.

---

## 3. Entity Lifecycle States

**Purpose**: Define how entities change over time and what actions are allowed in each state.

### Project Lifecycle

**States**:

**1. draft**
- **Description**: Raw project notes or initial capture
- **Entry conditions**: New project identified for ingestion
- **Exit conditions**: Structure and evidence extraction complete
- **Allowed actions**: Add/edit content, link evidence
- **Business rules**: Must be clearly marked as unverified
- **User permissions**: Content Curator, Content Owner

**2. normalized**
- **Description**: Structured into the canonical domain entities with the currently available fields captured
- **Entry conditions**: Domain entities (client, role, outcomes, evidence, decisions, lessons) extracted
- **Exit conditions**: Evidence completeness and defensibility confirmed
- **Allowed actions**: Edit entities; assess publication classification when available
- **Business rules**: Must have minimum required fields; publication classification is a separate governance checkpoint before each derived Project Story is approved
- **User permissions**: Content Curator, Content Owner

**3. validated**
- **Description**: Stable factual record; evidence checked. Publication classification may remain an open governance decision until the Project Story approval checkpoint.
- **Entry conditions**: All material publishable claims intended for Project Stories have traceable, attributable and sufficiently strong evidence
- **Exit conditions**: None — stable state; revalidation occurs when material facts/evidence change
- **Allowed actions**: Create Project Stories; update evidence only
- **Business rules**: Cannot create governed Project Stories until validated
- **User permissions**: Content Curator, Content Owner

**State Transitions**:
- `draft → normalized`: Structure and evidence extraction complete
- `normalized → validated`: Evidence completeness and defensibility confirmed
- `validated → validated`: Revalidation when material facts/evidence change

**Terminal States**: `validated` (stable factual record)

**Invalid Transitions**:
- `draft → validated`: Must normalize first
- `validated → draft`: Corrections create new version or evidence update, not regression

---

### Project Story Lifecycle

**States**:

**1. draft**
- **Description**: Initial narrative drafted from validated Project
- **Entry conditions**: Project validated; narrative outline created
- **Exit conditions**: Ready for steering-team review
- **Allowed actions**: Write, edit, restructure
- **Business rules**: Must derive only from validated Project
- **User permissions**: Content Curator, Content Owner

**2. review**
- **Description**: Under steering-team review for accuracy, tone, and publication compliance
- **Entry conditions**: Draft submitted
- **Exit conditions**: Approved or changes requested
- **Allowed actions**: Comment, revise, confirm publication classification, approve
- **Business rules**: Must respect publication classification; the separate publication review is completed before approval
- **User permissions**: Content Owner (approve/reject), Content Curator (revise)

**3. approved**
- **Description**: Jairo confirmed story is accurate and publishable
- **Entry conditions**: Review complete; explicit approval
- **Exit conditions**: Published to website
- **Allowed actions**: Publish
- **Business rules**: Cannot publish without approval
- **User permissions**: Content Owner

**4. published**
- **Description**: Live on website
- **Entry conditions**: Approved and deployed
- **Exit conditions**: Content retired or updated
- **Allowed actions**: Unpublish, update
- **Business rules**: Updates create new draft/review cycle
- **User permissions**: Content Owner, Build System (deploy)

**5. retired**
- **Description**: Removed from public site — terminal publication state
- **Entry conditions**: Strategic decision or content outdated
- **Exit conditions**: —
- **Allowed actions**: Archive
- **Business rules**: New story/version may be created later from the underlying Project; retirement of the public narrative never retires the factual Project
- **User permissions**: Content Owner

**State Transitions**:
- `draft → review`: Draft submitted
- `review → approved`: Jairo approves
- `review → draft`: Changes requested
- `approved → published`: Deployed
- `published → retired`: Strategic removal
- `published → draft`: Update/revision

**Terminal States**: `retired` (publication lifecycle ends; Project remains)

**Invalid Transitions**:
- `draft → published`: Must review and approve first
- `review → published`: Must approve first
- `published → draft` without version note

---

### Career Experience Lifecycle

**States**:

**1. draft**
- **Description**: Employment period being documented
- **Entry conditions**: New career period identified
- **Exit conditions**: Summary and key themes complete
- **Allowed actions**: Edit, link projects
- **User permissions**: Content Curator, Content Owner

**2. validated**
- **Description**: Public claims about employer, title, dates, progression, and themes verified
- **Entry conditions**: All material publishable claims have traceable, attributable evidence
- **Exit conditions**: Ready for publication
- **Allowed actions**: Prepare for publish
- **User permissions**: Content Owner

**3. published**
- **Description**: Part of public Career Journey
- **Entry conditions**: Validated and deployed
- **Exit conditions**: Retired or updated
- **Allowed actions**: Present on website
- **User permissions**: Content Owner, Build System

**State Transitions**:
- `draft → validated`: Claims verified
- `validated → published`: Deployed

**Stable active state**: `published` (can be updated or retired as needed; not technically terminal)

---

### Page / Experience Lifecycle

**States**:

**1. draft**
- **Description**: Page concept and purpose defined
- **Entry conditions**: Page identified in IA
- **Exit conditions**: Content outline and audience mapped
- **Allowed actions**: Outline, assign content
- **User permissions**: Content Curator

**2. wireframed**
- **Description**: Layout and information hierarchy designed
- **Entry conditions**: UX design complete
- **Exit conditions**: Wireframe approved
- **Allowed actions**: Prototype, test hierarchy
- **User permissions**: Content Curator, Content Owner

**3. specified**
- **Description**: Requirements, content entities, and navigation paths documented
- **Entry conditions**: PRD/spec complete
- **Exit conditions**: Build complete
- **Allowed actions**: Build, review
- **User permissions**: Content Curator, Content Owner

**4. published**
- **Description**: Live on website
- **Entry conditions**: Deployed
- **Exit conditions**: Redesign, revision, or retirement
- **Allowed actions**: Update, measure
- **User permissions**: Content Owner, Build System

**5. retired**
- **Description**: Removed from public site
- **Entry conditions**: Strategic decision
- **Exit conditions**: —
- **Allowed actions**: Archive
- **User permissions**: Content Owner

**State Transitions**:
- `draft → wireframed`: UX design complete
- `wireframed → specified`: Requirements documented
- `specified → published`: Deployed
- `published → draft/wireframed`: Redesign or substantial revision
- `published → retired`: Removed

**Terminal States**: `retired`

**Invalid Transitions**:
- `draft → published`: Must wireframe and specify first
- `wireframed → published` without spec

---

### Evidence Lifecycle

**States**:

**1. collected**
- **Description**: Evidence gathered from project sources
- **Entry conditions**: Source identified
- **Exit conditions**: Assessment complete
- **Allowed actions**: Tag, link to claims
- **Business rules**: May be incomplete or unverified
- **User permissions**: Content Curator, Content Owner

**2. assessed**
- **Description**: Traceability, attribution, and strength evaluated; publication sensitivity classified
- **Entry conditions**: Source, attribution, strength assessed
- **Exit conditions**: Sufficient to support claim wording
- **Allowed actions**: Assign `publication_sensitivity`
- **Business rules**: Classification: `public`, `anonymised`, `restricted`
- **User permissions**: Content Curator, Content Owner

**3. verified**
- **Description**: Stable state; sufficient to support publishable claims
- **Entry conditions**: Assessment complete; evidence adequate
- **Exit conditions**: —
- **Allowed actions**: Support claims
- **Business rules**: Verified evidence may remain private while supporting public claims
- **User permissions**: Content Curator, Content Owner

**State Transitions**:
- `collected → assessed`: Assessment complete
- `assessed → verified`: Evidence adequate

**Terminal States**: `verified`

**Key Principle**: Verified evidence can support a published claim **without itself being publicly exposed**. Internal documents, recognition emails, or project records may substantiate claims while remaining private or anonymised. This directly supports engagement risk **R-06** in the existing Explore risk register.

---

### Capability Lifecycle

**States**:

**1. draft**
- **Description**: Candidate derived from evidence signals
- **Entry conditions**: Capability proposed
- **Exit conditions**: Business-problem framing and Project evidence sufficient
- **Allowed actions**: Refine name/description
- **User permissions**: Content Curator

**2. validated**
- **Description**: Business-problem framing confirmed + sufficient Project evidence exists
- **Entry conditions**: Evidence signals normalized; framing approved
- **Exit conditions**: Approved for publication
- **Allowed actions**: Prepare for publish
- **User permissions**: Content Owner

**3. published**
- **Description**: Approved for public presentation
- **Entry conditions**: Validated and deployed
- **Exit conditions**: Retired or renamed
- **Allowed actions**: Present, link to stories
- **User permissions**: Content Owner, Build System

**State Transitions**:
- `draft → validated`: Framing and evidence confirmed
- `validated → published`: Approved and deployed

**Stable active state**: `published` (can be updated or retired as needed; not technically terminal)

---

### Lifecycle Principle

> **"Published" is a lifecycle state only for entities that are themselves public content.**

| Public content entities | Knowledge / evidence layer entities |
|-------------------------|-------------------------------------|
| Project Story | Project |
| Career Experience | Evidence |
| Page / Experience | |
| Capability | |

This preserves the boundary: **Context Warehouse knowledge → curated public content → website presentation**.

---

## 4. Domain Rules and Constraints

**Purpose**: Document what must be true in the domain to inform validation logic and business rules implementation.

### Business Rules

**BR-01: Material professional claims require verified evidence**
- **Description**: Every material professional claim derived from Jairo's experience must trace to at least one verified Evidence item.
- **Applies to**: Project, Project Story, Career Experience, Capability, Page/Experience
- **Validation**: Trace each material claim to ≥1 verified Evidence item
- **Exception handling**: Claim is removed, reworded to match evidence strength, or evidence is strengthened before publication
- **Example**: "Restored customer confidence" requires evidence of confidence restoration, not just project completion

**BR-02: Capability names describe business problems, not technology skills**
- **Description**: A Capability name must describe a business problem or outcome, not a technology skill.
- **Applies to**: Capability
- **Validation**: Capability name passes business-problem framing check
- **Exception handling**: Capability is renamed or rejected
- **Example**: "Recovering complex delivery under pressure" is valid; "Kubernetes" is not

**BR-03: Prominence and narrative role are independent**
- **Description**: A Project Story's `visitor_prominence` and `narrative_role` are set separately; one never derives from the other.
- **Applies to**: Project Story
- **Validation**: Both attributes populated independently
- **Exception handling**: Story cannot be approved until both are set
- **Example**: A contextual story can still have `project_recovery` as narrative role

**BR-04a: Project publication classification controls client/project identity disclosure**
- **Description**: Each Project and Project Story carries `publication_class = named | anonymised | restricted`, controlling public presentation of client/project identity and details.
- **Applies to**: Project, Project Story
- **Validation**: Content review against classification
- **Exception handling**: Content is anonymised, restricted to internal use, or claim is reworded
- **Example**: GSK may be `named`; a confidential client may be `anonymised`

**BR-04b: Evidence publication sensitivity controls evidence exposure**
- **Description**: Each Evidence item carries `publication_sensitivity = public | anonymised | restricted`, independently controlling whether supporting evidence itself may be exposed publicly, anonymised, or retained internally.
- **Applies to**: Evidence
- **Validation**: Sensitivity review during assessment
- **Exception handling**: Evidence may remain private while still supporting a public claim; only `public` evidence may be displayed verbatim
- **Example**: A client recognition email may verify a claim but remain `restricted` and not displayed

**BR-05: Evidence must be defensible**
- **Description**: Evidence must be traceable to a source, correctly attributed to Jairo's contribution, and strong enough to defend the claim's wording.
- **Applies to**: Evidence
- **Validation**: Assessment checklist: source identified, attribution clear, strength matches claim
- **Exception handling**: Claim wording is weakened, or claim is removed
- **Example**: "Improved satisfaction" requires satisfaction metrics or client recognition, not just completion

**BR-06: Capability evidence is not mastery proof**
- **Description**: A Project→Capability link means meaningful evidence exists; it may be positive, developmental, or learning-based.
- **Applies to**: Project, Capability
- **Validation**: Evidence nature recorded per relationship
- **Exception handling**: Website wording reflects evidence nature, not assumed mastery
- **Example**: Tigo provides a learning contrast for the narrative role `delivery_governance` through shortcomings in architecture governance, delegation, and program structure — not evidence of successful mastery

**BR-07: Project is factual layer; Project Story is curated layer**
- **Description**: A Project Story must derive from a `validated` Project and may not introduce facts absent from the Project.
- **Applies to**: Project, Project Story
- **Validation**: Diff story claims against Project facts
- **Exception handling**: Story is returned to draft; missing facts added to Project first
- **Example**: Cannot claim "managed 50-person team" if Project record says 12

**BR-08: "Published" is a lifecycle state only for public-content entities**
- **Description**: Project and Evidence never enter a `published` state.
- **Applies to**: All entities
- **Validation**: Lifecycle audit
- **Exception handling**: Model corrected
- **Example**: A Project is `validated`, not `published`; a Project Story is `published`

**BR-09: Retiring a Project Story never retires its Project**
- **Description**: The factual record persists; a new story/version may be created later.
- **Applies to**: Project, Project Story
- **Validation**: Retired stories retain link to validated Project
- **Exception handling**: —
- **Example**: Retiring an Entel Chile Project Story does not delete the underlying Entel Chile Project.

**BR-10: Foundation documents constrain all outputs**
- **Description**: Domain decisions must extend, not contradict, the approved strategic sources: `00-foundation/01-personal-brand-blueprint.md`, `00-foundation/02-website-product-vision.md`, `00-foundation/03-recruiter-journey.md`, and `00-foundation/04-website-strategy.md`. The approved Decision Log (`00-foundation/98-decision-log.md`) and Explore Bundle provide additional decision/governance context. The project handover remains a useful context document but is not an authoritative strategic source.
- **Applies to**: All
- **Validation**: Cross-check against the four authoritative foundation artifacts
- **Exception handling**: Conflict escalated to Jairo. Existing approved strategy remains authoritative unless the Product Owner explicitly approves a strategic change.
- **Example**: Cannot introduce Delivery Manager positioning because foundation documents defer it to V3

---

### Constraints

**C-1: Frontend-only MVP**
- **Description**: Frontend-only is the approved intended MVP boundary — no backend services, authentication, or database for MVP; content is static or lightweight managed. **This remains subject to A5/A9 feasibility validation under AS-04.**
- **Type**: Technical
- **Impact**: Constrains architecture, hosting, and content maintenance approach
- **Rationale**: Approved MVP scope; cost/simplicity preference
- **Workaround**: Static site generation, headless CMS, or managed content platforms

**C-2: Publication sensitivity per project**
- **Description**: Client identity and details must be classified before publication.
- **Type**: Business/Confidentiality
- **Impact**: Affects what can be published and how prominently
- **Rationale**: Confidentiality obligations; R-06 mitigation
- **Workaround**: Anonymised storytelling, aggregated evidence, or internal-only stories

**C-3: Evidence-before-claims ordering**
- **Description**: Content production must validate Projects before writing stories.
- **Type**: Business
- **Impact**: Build order and content workflow
- **Rationale**: Approved Evidence Strategy; R-01 mitigation
- **Workaround**: Exploratory sketching allowed, but formal stories require validated Projects

**C-4: Progressive disclosure required**
- **Description**: Rich knowledge must become scannable, not overwhelming.
- **Type**: Business/UX
- **Impact**: Information architecture, page design, content hierarchy
- **Rationale**: Approved Experience Strategy; R-02 mitigation
- **Workaround**: Summary cards, expandable sections, progressive depth

**C-5: Analytics required, implementation TBD**
- **Description**: Measurement capability must exist; tool, events, and privacy approach undecided.
- **Type**: Technical
- **Impact**: Architecture must accommodate measurement without locking implementation
- **Rationale**: Needed to validate AS-01/AS-02 in Evolve
- **Workaround**: Design for measurement hooks; defer tool selection to A5/A9/A11

---

### Invariants (Always True)

1. **INV-1**: Every `published` Project Story derives from exactly one `validated` Project.
   - Enforced by: Lifecycle gate + BR-07
   - Validation: Check story source reference

2. **INV-2**: Every material professional claim on the website traces to ≥1 `verified` Evidence item.
   - Enforced by: BR-01 + evidence lifecycle
   - Validation: Claim-to-evidence traceability audit

3. **INV-3**: Client identity presentation always matches the current `publication_class`.
   - Enforced by: BR-04a + content review
   - Validation: Review against classification before approval

4. **INV-4**: A Project's factual record is never deleted or regressed by publication-state changes.
   - Enforced by: BR-09 + lifecycle rules
   - Validation: Project record persists independently of story state

5. **INV-5**: `visitor_prominence` and `narrative_role` are always populated independently on every Project Story.
   - Enforced by: BR-03 + story approval checklist
   - Validation: Both fields present and set independently

6. **INV-6**: Evidence `publication_sensitivity` is independent of Project `publication_class`.
   - Enforced by: BR-04b + evidence assessment
   - Validation: Separate classification fields maintained

---

### Calculations and Formulas

No calculations/formulas apply to this domain — it is content, not transactional.

---

### Validation Rules

| Entity/Field | Rule | Error Message | Severity |
|--------------|------|---------------|----------|
| `Project → validated` | All material publishable claims intended for Project Stories have traceable, attributable, sufficiently strong Evidence | "Project cannot be validated — insufficient evidence for intended claims" | Critical |
| `Project Story.publication_class` | Must be one of `named`, `anonymised`, `restricted` | "Invalid publication class" | Critical |
| `Project Story.visitor_prominence` | Must be one of `flagship`, `supporting`, `contextual` | "Invalid prominence level" | Critical |
| `Project Story.narrative_role` | Must be one of `project_recovery`, `adaptive_delivery`, `cross_domain_leadership`, `business_technology_alignment`, `delivery_governance`, `professional_evolution`. `professional_evolution` may apply to an individual Project Story only when that story explicitly relates the project to evidence of change across earlier/later experiences; the canonical professional-evolution narrative may span multiple Project Stories. | "Invalid narrative role or professional_evolution applied without cross-project evidence" | Critical |
| `Project.geographic_scope` | Must be one of `single_country`, `multi_country`, `regional`, `international` | "Invalid geographic scope" | Warning |
| `Evidence → verified` | Source identified, attribution confirmed, strength assessed, `publication_sensitivity` assigned (`public`/`anonymised`/`restricted`) | "Evidence cannot be verified — missing source, attribution, or sensitivity classification" | Critical |
| `Capability → validated` | Business-problem framing confirmed + sufficient Project evidence exists | "Capability cannot be validated — framing or evidence insufficient" | Critical |
| `Page/Experience` | Must map to ≥1 Audience Segment and ≥1 content entity before `specified` | "Page cannot be specified — no audience or content mapped" | Warning |

---

## 5. User Roles and Responsibilities

**Purpose**: Define roles based on domain responsibilities (not organizational structure) to inform permissions and workflows.

### Role Definitions

**Content Owner**

- **Description**: The person whose professional experience is the domain content and who holds final authority over all publication decisions (Jairo Enrique Diaz).
- **Responsibilities**:
  - Approve/reject Project Stories, Career Experiences, Capabilities, and Page/Experience content
  - Assign publication classifications
  - Resolve strategic conflicts
  - Own final wording of public claims
- **Permissions**:
  - Create: All entities
  - Read: All entities
  - Update: All entities
  - Delete: None (retire instead)
  - Special actions: Approve, publish, retire, revalidate, assign publication class/sensitivity
- **Constraints**: Cannot delegate final approval; cannot publish without evidence validation (BR-01); cannot contradict foundation documents without explicit strategic change (BR-10)
- **Typical tasks**:
  1. Review drafted Project Story → approve or request changes
  2. Assign `named`/`anonymised`/`restricted` to a Project
  3. Decide prominence level for a story

---

**Content Curator**

- **Description**: The actor who normalizes Projects, drafts Project Stories, proposes capabilities, and maintains the domain model (Devin / agent).
- **Responsibilities**:
  - Normalize Projects into canonical entities
  - Draft Project Stories from validated Projects
  - Propose capability taxonomy and narrative roles
  - Validate evidence traceability
  - Maintain context and domain artifacts
- **Permissions**:
  - Create: Drafts of all entities
  - Read: All entities
  - Update: Draft/normalized entities
  - Delete: None
  - Special actions: Normalize, assess Evidence, draft, revise Project Stories under review, submit for review, flag rule violations
- **Constraints**: Cannot approve or publish; cannot introduce facts absent from validated Projects (BR-07); cannot contradict foundation documents (BR-10)
- **Typical tasks**:
  1. Extract evidence from project source → normalize into entities
  2. Draft Project Story → submit for Content Owner review
  3. Propose capability name → validate business-problem framing

---

**Visitor**

- **Description**: Any person accessing the public website. All Visitors have the same access to published public content. A Visitor may belong to an Audience Segment such as Recruiter, Hiring Manager, Internal Endava Manager, CTO, or Consulting Client. Audience Segments are used for product/UX prioritization and understanding different information needs; they do not provide different access permissions.
- **Responsibilities**:
  - Navigate Recruiter Journey
  - Read and evaluate Project Stories
  - Assess evidence and capabilities
  - Initiate contact through approved channels
- **Permissions**:
  - Create: None
  - Read: Published public content only
  - Update: None
  - Delete: None
  - Special actions: Download public assets, follow external links, submit contact
- **Constraints**: Cannot edit content; may read published named or approved anonymised content, but cannot access restricted source material, concealed identities, or unpublished drafts
- **Typical tasks**:
  1. Scan homepage → identify relevance
  2. Explore Projects → evaluate evidence
  3. Read Leadership → assess fit
  4. Download CV or click LinkedIn/email

---

**Build System**

- **Description**: Automated system that transforms curated content into the static website.
- **Responsibilities**:
  - Read deployment-eligible content
  - Generate static pages
  - Deploy assets to hosting
- **Permissions**:
  - Create: Static output files
  - Read: Deployment-eligible content
  - Update: Generated output
  - Delete: Old generated files
  - Special actions: Generate, deploy
- **Constraints**: **Consumes only content that is eligible for deployment according to the lifecycle rules of that entity type. Must not expose draft, under-review, internal-only, restricted, or otherwise non-publishable content.**
- **Typical tasks**:
  1. Read approved Project Stories → generate HTML
  2. Read curated content → build pages
  3. Deploy static assets to hosting

---

**Analytics Collector**

- **Description**: System role that measures visitor behavior and outcomes.
- **Responsibilities**:
  - Collect defined events
  - Aggregate metrics
  - Support AS-01/AS-02 validation
- **Permissions**:
  - Create: Measurement data
  - Read: Visitor interactions
  - Update: Aggregated metrics
  - Delete: None
  - Special actions: Measure, report
- **Constraints**: **Must not collect restricted professional content. Visitor-data collection, identification/anonymity, cookies or equivalent mechanisms, retention, and other privacy behavior remain TBD until the analytics/privacy requirements and implementation approach are defined.**
- **Typical tasks**:
  1. Measure permitted visitor interactions according to the analytics and privacy approach defined later in Explore
  2. Aggregate journey depth, content engagement, contact actions

---

### Role Categories

| Category | Roles |
|----------|-------|
| **Domain/content actors** | Content Owner, Content Curator |
| **Public access role** | Visitor |
| **Audience Segments** | Primary: Recruiters, Hiring Managers. Secondary: Delivery/Program Managers, CTOs/Technology Directors, Consulting Clients, Internal Endava Managers |
| **System actors** | Build System, Analytics Collector |

---

### Role Relationships

- **Content Owner → Content Curator**: delegates drafting, normalization, and artifact preparation; retains final approval
- **Content Curator → Content Owner**: escalates conflicts, rule violations, and publication classification questions
- **Visitor → Content Owner**: initiates contact through approved channels (email, LinkedIn, phone)
- **Build System → Content Curator**: consumes only deployment-eligible content per entity lifecycle; never touches drafts
- **Analytics Collector → Visitor**: measures permitted visitor interactions according to the analytics and privacy approach defined later in Explore

---

### Permission Matrix

**Permission matrix qualification**: The permissions below are general role permissions and are always subject to the lifecycle state, entity-specific transition rules, publication classification, and approval gates documented in Sections 3 and 4. In particular, the Content Curator may revise Project Stories under review and assess Evidence, but cannot grant final approval or publication authority.

| Role | Project | Project Story | Career Experience | Capability | Page/Experience | Evidence | Special Actions |
|------|---------|---------------|-------------------|------------|-----------------|----------|-----------------|
| **Content Owner** | Create, Read, Update | Create, Read, Update | Create, Read, Update | Create, Read, Update | Create, Read, Update | Create, Read, Update | Approve, publish, retire, revalidate, assign classifications |
| **Content Curator** | Create, Read, Update | Create, Read, Update | Create, Read, Update | Create, Read, Update | Create, Read, Update | Create, Read, Update | Normalize, assess Evidence, draft, revise under review, submit for review, flag violations |
| **Visitor** | — | Read (published) | Read (published) | Read (published) | Read (published) | — | Download public assets, contact |
| **Build System** | Read (deployment-eligible) | Read (deployment-eligible) | Read (deployment-eligible) | Read (deployment-eligible) | Read (deployment-eligible) | — | Generate, deploy |
| **Analytics Collector** | — | — | — | — | — | — | Measure permitted interactions (per TBD approach) |

**Legend**:
- Create: Can create new instances
- Read: Can view existing instances
- Update: Can modify existing instances
- Delete: Can remove instances (none granted — retire instead)
- Special Actions: Domain-specific actions beyond CRUD

---

## 6. Current State

**Purpose**: Document how the domain operates today to understand what to preserve vs what to change.

### Historical Baseline (pre-engagement)

Before the Context Warehouse and Dava.Flow work began:

**Process: Professional storytelling**
- **How it worked**: Career narrative was primarily communicated through CV and LinkedIn
- **Pain points**: CV and LinkedIn formats provide limited space and structure for full project depth, leadership decisions, and supporting evidence
- **Workarounds**: Interviews may fill gaps once recruiter interest exists

**Process: Recruiter evaluation**
- **How it worked**: The intended evaluation path treated CV and LinkedIn as initial screening inputs before possible further engagement
- **Pain points**: **Assumption, not universal fact** — actual recruiter behavior and the amount of project complexity or differentiation visible during screening remain unvalidated

**Process: Content maintenance**
- **How it worked**: CV updated sporadically; project knowledge lived in memory and scattered documents
- **Pain points**: Knowledge not normalized, reusable, or publication-classified; rich detail lost between updates

**Process: Evidence gathering**
- **How it worked**: Evidence existed implicitly in project documents, recognition, and recollection
- **Pain points**: Not traceable, attributable, or strength-assessed; publication sensitivity undefined

---

### Current State (after Signal, A1, A3)

**Process: Professional storytelling**
- **Current state**: Foundation documents, Project Knowledge Base, and Context Warehouse now exist; website does not yet exist
- **Remaining gaps**: No public professional reference — **the missing authoritative reference is specifically the public-facing website, not the internal Context Warehouse**

**Process: Recruiter evaluation**
- **Current state**: Recruiter Journey approved; audience segments defined; no live website yet
- **Remaining gaps**: Assumed recruiter behavior remains unvalidated until website and analytics exist

**Process: Content maintenance**
- **Current state**: Context Warehouse provides governed source; Project Knowledge Base contains nine structured narratives
- **Remaining gaps**: Individual evidence items still need normalization, verification, and publication-sensitivity classification per the A3 evidence model

**Process: Evidence gathering**
- **Current state**: Formal A3 evidence model now exists (`collected → assessed → verified`, publication_sensitivity, supports publishable claims)
- **Remaining gaps**: Individual evidence items within each project still need to be assessed, verified, and classified

**Process: Domain modeling**
- **Current state**: Canonical entities, relationships, capabilities, narrative roles, and prominence defined and grounded in the corpus
- **Remaining gaps**: Model must be applied to content production and validated against real website needs

---

### Current Systems

| System | Purpose | Limitations | Integration Points |
|--------|---------|-------------|-------------------|
| **CV (DOCX/PDF)** | Two-page executive summary of career | Cannot tell project stories, show leadership decisions, or provide evidence | Manual input to recruiters |
| **LinkedIn Profile** | Public professional profile | Generic format; not evidence-based; limited storytelling depth | External link from website |
| **Project Knowledge Base** | Nine structured project narratives in Markdown | Exists but is an **evolving corpus**, not a one-time ingestion; evidence within each project still needs normalization/verification/classification per the A3 evidence model | Context Warehouse ingestion |
| **Context Warehouse** | Governed repository of strategy, context, domain knowledge, and project evidence | Internal only — not a public professional reference; content not yet transformed for website consumption | Source for curated website content |

---

### Current Data Flows

| Source | Destination | Data | Frequency | Issues |
|--------|-------------|------|-----------|--------|
| Jairo's memory/documents | CV | Roles, dates, summaries | Sporadic | Lossy — drops project depth, evidence, leadership nuance |
| Jairo's memory/documents | LinkedIn | Profile fields | Sporadic | Platform format constrains evidence and storytelling |
| Project Knowledge Base | Context Warehouse | Structured narratives | **Evolving process** — projects added/updated as needed | Evidence within projects not yet normalized/verified/classified per A3 model |
| Context Warehouse | Website | — | — | Does not exist yet — this is the gap the project fills |

---

### Known Pain Points (Prioritized)

**High Priority**:

**1. No public professional reference consistently communicates project depth, leadership, or evidence**
- **Description**: CV and LinkedIn provide executive-summary formats with limited space and structure; the internal Context Warehouse is not public
- **Impact**: May limit differentiation and evidence visibility in some external evaluations; magnitude remains unvalidated
- **Frequency**: Varies by evaluation context; not yet measured
- **Current mitigation**: None — this is the core problem the website is intended to address
- **Cost**: Potentially missed engagement, weaker interview context, and limited differentiation

**2. Professional identity is fragmented across CV, LinkedIn, memory, and internal warehouse**
- **Description**: No single public authoritative source
- **Impact**: Inconsistent or incomplete professional presentation
- **Frequency**: Continuous
- **Current mitigation**: Context Warehouse unifies internally but is not public-facing
- **Cost**: Fragmented narrative, repeated explanation effort

**3. Individual evidence items not yet normalized, verified, or publication-classified**
- **Description**: A3 evidence model exists but application to individual items is next work
- **Impact**: Blocks evidence-based claims even though model exists
- **Frequency**: Every content decision
- **Current mitigation**: A3 evidence model defined; application pending
- **Cost**: Cannot yet produce fully defensible public stories

**Medium Priority**:

**4. No way to measure visitor engagement or content effectiveness**
- **Description**: Analytics approach is TBD
- **Impact**: Cannot validate AS-01/AS-02
- **Frequency**: Continuous
- **Current mitigation**: None — measurement capability required but not designed
- **Cost**: Cannot evaluate website success post-launch

**5. LinkedIn format is generic and not evidence-based**
- **Description**: Platform constraint limits storytelling
- **Impact**: Limits differentiation
- **Frequency**: Every profile view
- **Current mitigation**: None — platform constraint
- **Cost**: Lost opportunity to stand out

---

### What Works Well (Don't Break This)

1. **Foundation documents approved**
   - **What works**: Clear strategy, vision, journey, and evidence rules constrain all downstream work
   - **Preserve because**: Prevents strategic drift and rework

2. **Project Knowledge Base structure**
   - **What works**: Nine projects already in evidence-based narrative format — strong normalization starting point; corpus is evolving
   - **Preserve because**: Provides the factual foundation for all public storytelling

3. **Context Warehouse discipline**
   - **What works**: Single governed internal source prevents fragmentation; supports traceability
   - **Preserve because**: Enables evidence-before-claims and consistent content production

4. **A3 evidence model defined**
   - **What works**: Formal lifecycle, sensitivity classification, and claim-support rules now exist
   - **Preserve because**: Makes evidence handling systematic and defensible

5. **Evidence-before-claims rule**
   - **What works**: Already mitigates the biggest credibility risk
   - **Preserve because**: Core differentiator and trust builder

6. **Audience segmentation approved**
   - **What works**: Clear primary/secondary audiences guide content and UX decisions
   - **Preserve because**: Focuses design on real visitor needs

7. **Recruiter Journey approved**
   - **What works**: Gives the website a concrete narrative spine to implement
   - **Preserve because**: Translates strategy into experience structure

8. **Domain model validated**
   - **What works**: Canonical entities, capabilities, narrative roles, and prominence are defined and grounded in the corpus
   - **Preserve because**: Provides shared vocabulary and structure for all downstream work

---

## 7. Domain Risks and Unknowns

**Purpose**: Document what we don't know and what could go wrong to inform validation priorities.

### Unknowns (What We Need to Learn)

**U-1: Individual evidence verification status per project**
- **What we don't know**: Which specific evidence items within each project are verified, attributable, and strong enough to support public claims
- **Why it matters**: Cannot publish stories without verified evidence; evidence exists in sources but not yet assessed per A3 model
- **How to resolve**: Apply `collected → assessed → verified` lifecycle to each project's evidence items
- **Owner**: Jairo + Devin
- **Deadline**: Before each Project Story enters the governed `draft` lifecycle
- **Priority**: High

**U-2: Publication classification per project**
- **What we don't know**: Whether each project may be published as `named`, `anonymised`, or `restricted`
- **Why it matters**: Controls what client identity and details may be shown publicly
- **How to resolve**: Jairo reviews and assigns class per project
- **Owner**: Jairo
- **Deadline**: Before each Project Story is approved
- **Priority**: High
- **Jairo decision on timing**: Publication classification is decided per Project Story selected for publication, before that story is approved. It is not a requirement to classify every internal Project before any approved story can launch. A separate publication review remains part of Project Story approval.

**U-3: Whether assumed recruiter behavior is accurate**
- **What we don't know**: Whether recruiters and hiring managers actually explore portfolios during candidate evaluation, and how they navigate
- **Why it matters**: Validates AS-02; personas and journey are evidence-based but not directly validated with recruiters
- **How to resolve**: Post-launch analytics + optional recruiter feedback
- **Owner**: Jairo
- **Deadline**: Evolve phase
- **Priority**: Medium

**U-4: Analytics/privacy approach**
- **What we don't know**: Which tool, events, identification/anonymity model, retention, and privacy mechanisms to use
- **Why it matters**: Required capability but implementation/privacy approach undefined
- **How to resolve**: A5/A9/A11 decisions; ADR
- **Owner**: Devin recommends; Jairo approves
- **Deadline**: Before launch
- **Priority**: Medium

**U-5: Content storage and maintenance approach**
- **What we don't know**: How structured content should be stored and maintained (Markdown, JSON/YAML, headless CMS, SSG)
- **Why it matters**: Affects build workflow, contributor experience, and future evolution
- **How to resolve**: A3 → A5/A9 evaluation; ADR
- **Owner**: Devin recommends; Jairo approves
- **Deadline**: Architecture decision
- **Priority**: Medium

**U-6: Whether future evidence requires evolution of the canonical capability set**
- **What we don't know**: Whether new project evidence or content analysis will reveal gaps in the eight canonical capabilities
- **Why it matters**: Eight canonical capabilities validated against current nine-project corpus; reassess only when new evidence shows material gap. **Relevant because one professional experience remains to be added later.**
- **How to resolve**: Reassess when new projects are ingested or content analysis shows gap
- **Owner**: Devin proposes; Jairo approves
- **Deadline**: As needed
- **Priority**: Low

---

### Assumptions (What We're Assuming)

**Assumption history note**: The current canonical assumption table contains AS-01, AS-02, AS-03, AS-04, and AS-07. AS-05 remains recorded in `explore/explore-personal-brand-website/context.md` as the assumption that the foundation documents provide sufficient strategic guidance; it is not silently treated as closed by its omission here. AS-06 remains removed as an assumption; hosting is handled as an open technical decision. This preserves the history without reopening the latest five-assumption register.

**AS-01 — Portfolio measurably improves recruiter engagement vs CV/LinkedIn alone**
- **Assumption**: A dedicated portfolio website will materially improve recruiter engagement compared with the CV alone.
- **Risk if wrong**: Investment may not produce measurable career benefits
- **Validation method**: Post-launch analytics + feedback
- **Status**: Active / unvalidated
- **Owner**: Jairo
- **Priority**: Post-launch validation — strategically important, not a pre-build blocker

**AS-02 — Target users meaningfully explore the portfolio during candidate evaluation**
- **Assumption**: The target audience will spend time reviewing a portfolio website as part of their evaluation.
- **Risk if wrong**: Content investment may be ignored
- **Validation method**: **Pre-release directional feedback** (testers/reviewers) + **Evolve behavioral evidence** (actual visitor analytics). Measurement questions: How deeply do visitors navigate? Which Project Stories receive engagement? Do visitors move from summary → evidence? Which contact actions occur? How much of the intended Recruiter Journey is actually followed?
- **Status**: Active / unvalidated
- **Owner**: Jairo
- **Priority**: Post-launch validation — strategically important, not a pre-build blocker

**AS-03 — Evidence corpus supports sufficiently complete and defensible Project Stories**
- **Assumption**: Existing career material can be enriched into sufficiently evidence-backed project stories.
- **Risk if wrong**: Website cannot support evidence-before-claims strategy
- **Validation method**: Per-project evidence normalization and verification via `collected → assessed → verified` lifecycle
- **Status**: **PARTIALLY VALIDATED** — corpus supports viable Project Stories; per-project Evidence items still require normalization/verification
- **Owner**: Jairo + Devin
- **Priority**: Pre-design/build blocker — must complete before a Project Story enters the governed `draft` lifecycle

**AS-04 — Frontend-only implementation suffices for MVP**
- **Assumption**: A frontend-only implementation will be sufficient for the MVP because the site can use static or lightweight managed content without requiring backend services.
- **Risk if wrong**: MVP scope or feasibility underestimated
- **Validation method**: A5 Technical Feasibility + A9 Architecture Context
- **Status**: Active / unvalidated
- **Owner**: Devin recommends; Jairo approves
- **Priority**: Explore validation — resolve in later Explore activities

**AS-07 — Recruiter Journey translates effectively into product experience**
- **Assumption**: The approved Recruiter Journey can be translated effectively into concrete navigation and experience design.
- **Risk if wrong**: Website may fail to deliver the progressive confidence-building sequence the strategy requires
- **Validation method**: A6 Personas + A10 Wireframing + A11 PRD
- **Status**: Active / unvalidated
- **Owner**: Jairo
- **Priority**: Explore validation — resolve in later Explore activities

---

### Domain Risks

The `DR-01`–`DR-07` identifiers belong to this Domain Analysis register. They are distinct from the existing engagement-risk register `R-01`–`R-06` maintained in the Explore Bundle and Context artifacts; the underlying engagement-risk meanings and scores are not changed here.

**DR-01: Evidence depth varies across projects**
- **Description**: Some projects (e.g., GT&T) are thinner than flagship stories
- **Likelihood**: Medium
- **Impact**: High
- **Mitigation**: Prominence model assigns `contextual` to thin evidence; no forced claims
- **Owner**: Jairo + Devin
- **Status**: Open

**DR-02: Publication sensitivity violation**
- **Description**: Client details published beyond allowed class
- **Likelihood**: Low-Medium
- **Impact**: High
- **Mitigation**: BR-04a/04b; classification before publication; Jairo approval gate
- **Owner**: Jairo
- **Status**: Open

**DR-03: Overstated claims**
- **Description**: Wording stronger than evidence supports
- **Likelihood**: Medium
- **Impact**: High
- **Mitigation**: BR-01 evidence-before-claims; BR-05 defensibility check; claim rewording
- **Owner**: Jairo + Devin
- **Status**: Open

**DR-04: Tigo perceived as failure rather than evolution**
- **Description**: Visitors may interpret the learning story negatively
- **Likelihood**: Medium
- **Impact**: Medium
- **Mitigation**: `professional_evolution` narrative role; explicit "learning experience" framing; careful wording; later usability/content validation can test perception
- **Owner**: Jairo + Devin
- **Status**: Open

**DR-05: Avianca overstated as implementation**
- **Description**: It was definition-stage only, not implementation
- **Likelihood**: Medium
- **Impact**: Medium
- **Mitigation**: Explicit status in story; `contextual` prominence; scope note
- **Owner**: Jairo + Devin
- **Status**: Open

**DR-06: Information overload**
- **Description**: Rich corpus becomes overwhelming
- **Likelihood**: Medium
- **Impact**: High
- **Mitigation**: Progressive disclosure; prominence model; information hierarchy map (Q-IA-1)
- **Owner**: Jairo + Devin
- **Status**: Open

**DR-07: Domain model drift**
- **Description**: Content production diverges from canonical model
- **Likelihood**: Low
- **Impact**: Medium
- **Mitigation**: BR-07, BR-10; validation gates before publication
- **Owner**: Devin
- **Status**: Open

---

### Complexity Areas

1. **Evidence normalization across 9 projects**
   - **Why it's complex**: Each project has different evidence types, sources, and sensitivity levels
   - **Implications**: Requires per-project assessment; may reveal gaps requiring story re-scoping
   - **Approach**: Apply A3 evidence model project by project; track verification status

2. **Tigo narrative framing**
   - **Why it's complex**: Must balance honest acknowledgment of failure with positive professional positioning
   - **Implications**: Wording is critical; Jairo must approve tone; may need multiple drafts
   - **Approach**: Frame as `professional_evolution`; explicit "learning experience" positioning; test with reviewers

3. **Multi-project professional_evolution arc**
   - **Why it's complex**: Spans Tigo → Avianca → DFA; requires cross-story orchestration
   - **Implications**: Career Journey and Leadership pages must present the arc coherently, not as isolated stories
   - **Approach**: Design arc as connected narrative; use consistent visual/structural cues

4. **Publication classification decisions**
   - **Why it's complex**: Requires per-project **publication/confidentiality judgment**
   - **Implications**: Affects what flagship/supporting stories can actually be published; if a project later reveals actual legal/contractual restriction, that is handled separately
   - **Approach**: Jairo decides per project; document classification rationale

5. **Capability evidence nature tracking**
   - **Why it's complex**: Same capability may be positive evidence in one project, developmental in another
   - **Implications**: Website wording must reflect evidence nature, not just capability presence
   - **Approach**: Record evidence nature per Project→Capability relationship; review during story drafting

6. **Dual-layer model (Project vs Project Story)**
   - **Why it's complex**: Must maintain factual record separate from curated narrative
   - **Implications**: Prevents accidental fact invention; requires clear boundaries in content production
   - **Approach**: Project = what happened. Project Story = how we choose to communicate what happened. Enforce through BR-07 and lifecycle gates.

---

### Edge Cases to Consider

| Edge Case | Scenario | How to Handle | Priority |
|-----------|----------|---------------|----------|
| **Strong evidence, restricted publication** | Project has excellent evidence but client is `restricted` | Story may be written for internal use or anonymised; prominence adjusted; never publish restricted identity | High |
| **Verified evidence, private source** | Recognition email verifies claim but is itself `restricted` | Claim may be published; evidence supports it internally but is not displayed publicly | High |
| **Project spans multiple employers** | Hypothetical: project during career transition | The current Project model points to one Employer / Delivery Organization. If a real project requires multiple employers, reassess the relationship model rather than expanding it now | Medium |
| **Retired story needs republication** | Story retired for strategy reasons, later needed | New Project Story created from same `validated` Project; retirement does not retire Project | Medium |
| **Evidence strength mismatch** | Strong claim but only moderate evidence | Reword claim to match evidence strength; do not upgrade evidence artificially | High |
| **Learning-based capability evidence** | Tigo provides a learning contrast for the narrative role `delivery_governance` through shortcomings in architecture governance, delegation, and program structure | Capability relationship marked as learning-contrast; wording reflects lesson, not mastery | Medium |

---

## 8. Domain Model Summary

**Purpose**: Synthesize findings into actionable insights for product and architecture decisions.

### Core Entities (11 entities; supporting entities omitted for brevity)

1. **Professional Profile**: Overall identity and positioning
   - Key relationships: Career Experiences, Leadership Principles
   - Complexity: Must remain aligned with foundation documents

2. **Career Experience**: Employment period
   - Key relationships: Professional Profile, Projects, Employer
   - Complexity: Public claims require validation before publication

3. **Project**: Factual underlying engagement (knowledge layer)
   - Key relationships: Employer, Client, Industry, Markets, Roles, Business Problems, Responsibilities, Challenges, Decisions, Achievements, Outcomes, Evidence, Technologies, Lessons, Capabilities, Project Stories
   - Complexity: Most connected entity; must maintain factual integrity separate from narrative

4. **Project Story**: Curated public narrative (content layer)
   - Key relationships: Project, Capabilities, Leadership Principles, Pages/Experiences
   - Complexity: Independent prominence and narrative role; publication class controls disclosure

5. **Employer / Delivery Organization**: Who employed Jairo
   - Key relationships: Career Experiences, Projects
   - Complexity: Distinct from Client; may be anonymised

6. **Client / Customer Organization**: Who received deliverables
   - Key relationships: Projects, Industry
   - Complexity: Publication classification controls disclosure

7. **Industry**: Sector classification
   - Key relationships: Clients, Projects
   - Complexity: Project industry is visitor-relevant classification

8. **Capability**: Business-problem-focused capability
   - Key relationships: Projects (demonstrates), Project Stories (surfaces), Pages/Experiences
   - Complexity: Evidence may be positive, developmental, or learning-based

9. **Leadership Principle**: Core leadership belief
   - Key relationships: Project Stories, Leadership Decisions
   - Complexity: Must be evidenced, not just stated

10. **Page / Experience**: Website page or experience
    - Key relationships: Project Stories, Capabilities, Leadership Principles, Audience Segments
    - Complexity: Must support Recruiter Journey and five-minute success criteria

11. **Audience Segment**: Visitor group with shared goals
    - Key relationships: Pages/Experiences
    - Complexity: Segments prioritize UX but do not change access permissions

---

### Key Relationships

- **Project** → **Employer / Delivery Organization**: Aggregation (many → 1)
  - Business rule: Project must identify its delivery organization

- **Project** → **Client / Customer Organization**: Aggregation (many → 1)
  - Business rule: Client identity controlled by publication classification

- **Project** → **Industry**: Aggregation (many → 1)
  - Business rule: Project industry is visitor-relevant

- **Project** ↔ **Capabilities**: Association — demonstrates (many ↔ many)
  - Business rule: Evidence may be positive, developmental, or learning-based

- **Project Story** ↔ **Capabilities**: Association — surfaces (many ↔ many)
  - Business rule: Story chooses which demonstrated capabilities to present

- **Project Story** ↔ **Pages / Experiences**: Association — presented by (many ↔ many)
  - Business rule: Page presents selective stories per audience and journey stage

- **Achievements** → **Evidence**: Aggregation (many ↔ many)
  - Business rule: Every achievement claim requires verified evidence

- **Business Outcomes** → **Evidence**: Aggregation (many ↔ many)
  - Business rule: Every outcome claim requires verified evidence

---

### Critical Business Rules

1. **BR-01**: Every material professional claim must trace to ≥1 verified Evidence item.
   - Impact: Prevents unsupported claims; core of evidence-before-claims strategy

2. **BR-02**: Capability names describe business problems/outcomes, not technology skills.
   - Impact: Keeps How I Can Help business-focused, not résumé-like

3. **BR-03**: Prominence and narrative role are independent.
   - Impact: Allows flexible storytelling without conflating presentation and evidence

4. **BR-04a**: Project publication classification controls client/project identity disclosure.
   - Impact: Protects client confidentiality; gates what can be published

5. **BR-04b**: Evidence publication sensitivity independently controls evidence exposure.
   - Impact: Allows defensible public claims while keeping sources private

6. **BR-05**: Evidence must be traceable, attributable, and strong enough to defend claim wording.
   - Impact: Maintains credibility; prevents overstated claims

7. **BR-06**: Capability evidence is not mastery proof; evidence may be positive, developmental, or learning-based.
   - Impact: Enables honest learning narratives (e.g., Tigo) without overstating capability

8. **BR-07**: Project is factual layer; Project Story is curated layer; stories derive only from validated Projects.
   - Impact: Prevents fact invention; maintains boundary between knowledge and presentation

9. **BR-08**: "Published" is a lifecycle state only for public-content entities.
   - Impact: Preserves knowledge/evidence layer separation

10. **BR-09**: Retiring a Project Story never retires its Project; the factual record persists and can support future stories.
    - Impact: Protects evidence base; allows narrative refresh without losing facts

11. **BR-10**: Foundation documents constrain all outputs; conflicts escalate to Jairo.
    - Impact: Prevents strategic drift; maintains governance

---

### Domain Complexity Drivers

1. **Evidence normalization across 9 projects**
   - Why: Each project has different evidence types, sources, and sensitivity levels
   - Mitigation: Apply A3 evidence model project by project; track verification status

2. **Tigo narrative framing**
   - Why: Must balance honest acknowledgment of failure with positive professional positioning
   - Mitigation: Frame as `professional_evolution`; explicit "learning experience" positioning; test with reviewers

3. **Multi-project professional_evolution arc**
   - Why: Spans Tigo → Avianca → DFA; requires cross-story orchestration
   - Mitigation: Design arc as connected narrative; use consistent visual/structural cues

4. **Publication classification decisions**
   - Why: Requires per-project publication/confidentiality judgment
   - Mitigation: Jairo decides per project; document classification rationale

5. **Capability evidence nature tracking**
   - Why: Same capability may be positive evidence in one project, developmental in another
   - Mitigation: Record evidence nature per Project→Capability relationship; review during story drafting

6. **Dual-layer model (Project vs Project Story)**
   - Why: Must maintain factual record separate from curated narrative
   - Mitigation: Project = what happened. Project Story = how we choose to communicate what happened. Enforce through BR-07 and lifecycle gates.

---

### Implications for Product Design

1. **Progressive disclosure is mandatory**: The domain is rich (9 projects, 8 capabilities, multiple evidence types). Without prominence levels and information hierarchy, visitors will be overwhelmed. Product must surface flagship stories first, supporting/contextual on demand.
   - Recommendation: Use `flagship`/`supporting`/`contextual` prominence to drive homepage and Projects page hierarchy.

2. **Content publication is gated by evidence validation**: Formal Project Stories derive from validated Projects. Evidence normalization and validation therefore precede approval/publication of website stories and claims. This governs the formal lifecycle; it does not prohibit exploratory writing or narrative sketching during analysis.
   - Recommendation: Build content production workflow that validates Projects before drafting stories.

3. **Publication classification is a launch gate for each selected Project Story**: Until Jairo classifies the underlying Project as `named`/`anonymised`/`restricted`, that Project Story cannot be approved for publication. This does not require every internal Project to be classified before any approved story launches.
   - Recommendation: Schedule classification decisions before approval of each selected Project Story.

4. **Canonical capabilities inform How I Can Help**: The eight capabilities are business-problem-focused and provide the evidence-based input for that page. **Exact presentation — which appear, how many, and in what form — is a later Experience Design/PRD decision, not an A3 decision.**
   - Recommendation: Use capabilities as input to How I Can Help design, not as a fixed layout spec.

5. **Professional evolution arc needs cross-page orchestration**: Tigo → Avianca → DFA is a single narrative spanning three projects. Career Journey and Leadership pages must present this arc coherently, not as three separate stories.
   - Recommendation: Design arc as connected narrative with consistent visual/structural cues.

6. **Tigo requires careful framing**: As a learning experience, it must be framed as `professional_evolution` with explicit acknowledgment of what failed. Wording is critical and requires Jairo's approval.
   - Recommendation: Draft Tigo story early; test tone with reviewers.

7. **Defensible claims do not require public evidence exposure**: Internal documents, recognition emails, and project records can substantiate claims without being displayed. **This allows defensible public claims while respecting confidentiality.**
   - Recommendation: Use verified evidence to support claims; display only `public` evidence when available.

8. **Analytics must be designed but not yet decided**: Measurement is required, but tool, privacy approach, and events are TBD. Product design should plan for measurement hooks without locking the implementation.
   - Recommendation: Include analytics placeholders in architecture; defer tool selection to A5/A9/A11.

---

### Implications for Technical Architecture

1. **Content storage must support dual-layer model**: The architecture must store Projects (factual) and Project Stories (curated) separately, with clear derivation links.
   - Recommendation: Evaluate Markdown+frontmatter, JSON/YAML, or headless CMS options in A5/A9.

2. **Publication eligibility must be enforced**: The Build System must not deploy restricted or non-publishable content.
   - Requirement: Architecture must enforce publication eligibility so restricted or non-publishable content cannot be deployed. The exact enforcement mechanism is determined during A5/A9. Build-time validation is one candidate among others.

3. **Evidence traceability requires structured linking**: The content model must support explicit evidence-to-claim relationships.
   - Candidate approaches (A5/A9 to evaluate): frontmatter, structured data fields, JSON/YAML, CMS-managed references.

4. **Static/frontend-only architecture is assumed but not validated**: A5/A9 must confirm this approach satisfies all MVP requirements.
   - Recommendation: Evaluate static site generators, hosting options, and content workflows in A5/A9.

5. **Analytics integration must be loosely coupled**: The measurement tool is TBD; architecture should not hardcode a specific provider.
   - Requirement: Provide measurement hooks without committing to a specific analytics tool or mechanism. Candidate approaches (A5/A9 to evaluate): script-based injection, API-based integration, build-time event registration.

---

## 9. Assumptions to Validate

**Purpose**: Prioritize what needs validation before proceeding to design and development.

### High Priority — pre-design/build blockers

**1. AS-03 — Evidence corpus supports sufficiently complete and defensible Project Stories**
- **Statement**: Existing career material can be enriched into sufficiently evidence-backed project stories.
- **Risk if wrong**: Website cannot support evidence-before-claims strategy
- **Validation method**: Per-project evidence normalization and verification via `collected → assessed → verified` lifecycle
- **Owner**: Jairo + Devin
- **Deadline**: Before a Project Story enters the governed `draft` lifecycle
- **Status**: **PARTIALLY VALIDATED** — corpus supports viable Project Stories; per-project Evidence items still require normalization/verification

**2. AS-04 — Frontend-only implementation suffices for MVP**
- **Statement**: A frontend-only implementation will be sufficient for the MVP because the site can use static or lightweight managed content without requiring backend services.
- **Risk if wrong**: MVP scope or feasibility underestimated
- **Validation method**: A5 Technical Feasibility + A9 Architecture Context
- **Owner**: Devin recommends; Jairo approves
- **Deadline**: Before architecture decision
- **Status**: Active / unvalidated

---

### Explore Validation — resolve in later Explore activities

**3. AS-07 — Recruiter Journey translates effectively into product experience**
- **Statement**: The approved Recruiter Journey can be translated effectively into concrete navigation and experience design.
- **Risk if wrong**: Website may fail to deliver the progressive confidence-building sequence the strategy requires
- **Validation method**: A6 Personas + A10 Wireframing + A11 PRD
- **Owner**: Jairo
- **Deadline**: Before PRD approval
- **Status**: Active / unvalidated

---

### Post-launch Validation — strategically important, not a pre-build blocker

**4. AS-01 — Portfolio measurably improves recruiter engagement vs CV/LinkedIn alone**
- **Statement**: A dedicated portfolio website will materially improve recruiter engagement compared with the CV alone.
- **Risk if wrong**: Investment may not produce measurable career benefits
- **Validation method**: Post-launch analytics + feedback
- **Owner**: Jairo
- **Deadline**: Evolve phase
- **Status**: Active / unvalidated

**5. AS-02 — Target users meaningfully explore the portfolio during candidate evaluation**
- **Statement**: The target audience will spend time reviewing a portfolio website as part of their evaluation.
- **Risk if wrong**: Content investment may be ignored
- **Validation method**: **Pre-release directional feedback** (testers/reviewers) + **Evolve behavioral evidence** (actual visitor analytics). Measurement questions: How deeply do visitors navigate? Which Project Stories receive engagement? Do visitors move from summary → evidence? Which contact actions occur? How much of the intended Recruiter Journey is actually followed?
- **Owner**: Jairo
- **Deadline**: Evolve phase
- **Status**: Active / unvalidated

---

### Open Decisions (not assumptions)

| ID | Decision | Why It's Open | Resolution Path | Owner | Deadline |
|----|----------|---------------|-----------------|-------|----------|
| **OD-PUB-01** | Assign `named`, `anonymised`, or `restricted` to each Project before its Project Story can be approved | Required by BR-04a but value per project unknown | Jairo reviews and assigns class per project | Jairo | Before each Project Story approval |
| **OD-TECH-01** | Content storage and maintenance approach | Intentionally deferred until A3 established content model | A3 → A5/A9 evaluation; ADR | Devin recommends; Jairo approves | Architecture decision |
| **OD-TECH-02** | Analytics/privacy approach (tool, events, identification/anonymity, retention) | Measurement required but implementation/privacy approach TBD | A5/A9/A11 decisions; ADR | Devin recommends; Jairo approves | Before launch |

### Evolution Trigger

| Trigger | When It Activates | Response |
|---------|-------------------|----------|
| **Future evidence requires capability-taxonomy evolution** | New project evidence or content analysis reveals a material gap in the eight canonical capabilities | Devin proposes addition/removal/rename; Jairo approves. Relevant because one professional experience remains to be added later. |

---

### Validation Plan

| Activity | Method | Timeline | Owner | Dependencies |
|----------|--------|----------|-------|--------------|
| **Per-project evidence normalization** | Apply `collected → assessed → verified` lifecycle | Before each Project Story enters governed `draft` lifecycle | Jairo + Devin | A3 evidence model defined |
| **Publication classification** | Jairo reviews and assigns class per project | Before each story approval | Jairo | Evidence normalization complete |
| **Technical feasibility** | Evaluate frontend-only, content storage, hosting options | A5 | Devin | A3 complete |
| **Architecture context** | Define system context, constraints, candidate stack, hosting shortlist | A9 | Devin | A5 complete |
| **Personas + wireframing** | Validate Recruiter Journey translation and information hierarchy | A6, A10 | Devin + Jairo | Context baseline, domain model |
| **PRD** | Consolidate requirements including analytics definitions | A11 | Devin | A6, A9, A10 complete |
| **Pre-release directional feedback** | Testers/reviewers provide directional evidence on AS-02 | Before launch | Jairo | Website built |
| **Post-launch analytics** | Measure engagement, journey depth, CV downloads, contact actions | Evolve | Jairo + Devin | Website live, analytics implemented |

---

## Related Artifacts

- **Context**: `explore/explore-personal-brand-website/context.md`
- **Explore Bundle**: `explore/explore-personal-brand-website/explore-bundle.md`
- **Discovery Index**: `explore/explore-personal-brand-website/discovery.md`
- **Project Knowledge Base**: `explore/sources/Project-Knowledge-Base/`
- **Foundation Documents**: `00-foundation/01-personal-brand-blueprint.md`, `02-website-product-vision.md`, `03-recruiter-journey.md`, `04-website-strategy.md`, `98-decision-log.md`

---

**Last Updated**: 2026-09-22  
**Status**: Approved — Activity 3 (Domain Analysis) complete
