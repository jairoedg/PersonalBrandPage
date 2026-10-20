# DCTX / Greenfield Web & Mobile development 

**Company:** Endava  
**Client:** DCTX  
**Period:** September 2025 – September 2026
**Industry:** Media
**Role:** Scrum Master
**Domain:** Web  & Mobile App  Development / Video Streaming / Data Migration / 
**Technology:** Java, Typescript, React Native, GCP Cloud, Postgres
**Delivery Model:** Scrum / Kanban / Agile Delivery  
**Outcome:** Greenfield Web / Mobile app. / Video Streaming / Video on Demand.

---

# Executive Summary

Dave Campbell’s Texas Sports (DCTX) is a premier sports media brand that has covered Texas football at all levels—primarily high school, along with college sports—since 1960. DCTX operates across multiple platforms to deliver its content.

However, DCTX’s legacy web and mobile applications had become outdated, creating a bottleneck that hindered the business's strategic vision. The main objective of this project was to deliver a modern, greenfield web application hosted on Google Cloud Platform (GCP). The new solution is powered by Kontent.ai—an AI-enhanced headless CMS used to manage all core company content, including news articles, live score updates, video on demand (VOD), video livestreams, podcasts, ad/sponsor integrations, and the online store.

---

# Business Context

DCTX has a dedicated fan base across Texas and the exclusive rights to Texas high school sports content (games, scores), which uniquely positions them to be the "ESPN+ for high school sports in the state of Texas."

Because its existing platform can no longer support this vision, DCTX is driving a digital transformation to modernize and unify its core experience. By bringing editorial content, video streaming, live scores, and community features into one seamless ecosystem, DCTX aims to maximize user engagement and unlock new revenue streams."



---

# Business Problem

Because its existing platform can no longer support this vision, DCTX is driving a digital transformation to modernize and unify its core experience. By bringing editorial content, video streaming, live scores, and community features into one seamless ecosystem, DCTX aims to maximize user engagement and unlock new revenue streams."
This new platform is intended to commit the following goals:

1. Launch a streamlined and stable platform​: Create a single brand experience across live streaming, content and mobile app. Enable reliable live streaming for weekly games to the state championship. Modernize the user experience and payments flow. ​
2. Make data-informed decisions​: Unified data strategy to enable reporting and visibility into business drivers and customer behavior. Segment and target customers based on geography and demographics.
3. Unlock new monetization opportunities​: Enable programmatic advertising to scale media sales. Automate customer service and renewals. Identify new data and content revenue opportunities.​
4. Increase customer awareness and acquisition​: Enable digital marketing tools and product growth strategies. Capture customers who are new to the brand.​
5. Scale content creation​: Utilize AI and other tools to create content and drive equal representation of teams, districts and sports.


---

# Scope of Responsibility

I was responsible for leading development team as Scrum Master for the FrontEnd (Web + Mobile app) &  Backend teams.  Also, I've led the Data Migration work plus DevOps team configuring GCP infrastructure, CI/CD pipeline.
 
## Project Setup

I participated in:

- Definition (along with the Technical leads and Solution architect) of the solutions per every feature defined in project scope.
- Maintain  project-status report documentation.
- Product roadmap definition alongside with the product owner.
- Scrum facilitation
- Team tracking
- Agile Delivery leadership
- Testing strategy definition (Along with QA team)
- Risk and issue management.
- Release coordination.
- Alignment between product, technical, and delivery stakeholders.

---

# Stakeholders

## Endava

- Project Manager & Delivery Manager.
- Client Partner.
- Engineering teams.
- Test teams.
- Technical leads.

---

# Team Structure

## Team 1

- 2 Frontend developers
- 4 Moblie developers.
- 3 Testers.

## Team 2

- 5 Backend Developers.
- 2 Testers.

## Team 3
- 2 Data Engineers

## Team 4
- 2 DevOps enginerr+


The engagement also involved solution architect and GCP architect support when needed.

---

# Technology Landscape

- Java.
- React / React Native.
- GCP.
- REST APIs.
- SQL Server / Cloud SQL.
- GitHub actions.
- Kontent.AI
- Braintree / Stripe

---

# Delivery Challenges

## 1. Product Requirements

The development team frequently reported that AI-generated user stories were misaligned, vague, and lacked necessary technical context for both backend and frontend execution. Stories often failed to accurately communicate the required work, containing excessive noise while lacking clear acceptance criteria. Additionally, Figma designs were frequently not ready in time for frontend development, leading to ongoing escalations to the Product team.

As a workaround, the team onboarded a bilingual Business Analyst to bridge the communication gap between US-based native English stakeholders and the LATAM development team. While this mitigated the impact, the underlying issue was never fully resolved. Figma design ready as a mandatory rule in the DoR.

---

## 2. Solution built as a whole, not feature-delivery driven

A major challenge was that the project was structured like a puzzle, non-incremental delivery model. Multiple features were built concurrently,  no clear milestones to complete in the sprints and sign off on individual epics or feature sets. This approach led to continuous discussions between Technical Leads and the Product team. Although Technical Leads reluctantly accepted the setup, it proved extremely difficult to pivot away from this way of working.

At the end, integration occurred late in the cycle, leaving insufficient time for User Acceptance Testing (UAT). The sudden discovery of numerous defects and scope changes right before release placed an unsustainable workload on Dev and QA teams to meet the deadline.

---

## 3. Unrealistic Mobile App Timeline

Development for the new mobile app kicked off in January 2026. This was an ill-timed management decision that severely impacted the broader project, as the overall release target of late July 2026 was kept intact despite adding the application to the scope—making on-time completion nearly impossible.

A detailed product roadmap was presented to executive sponsors and project leadership to demonstrate that delivering the full mobile scope within the existing timeframe without scope reduction was unrealistic. However, the deadline remained fixed with no room for negotiation.

To meet this constraint, project leadership and the Technical Lead executed a high-risk recovery plan:
- **Architecture Reuse:** Leveraged backend services previously built for the web platform.
- **Resource Augmentation & AI Tools:** Onboarded additional frontend developers and QA testers, leveraging AI development tools to accelerate output.
- **Capacity & Overtime:** Approved paid overtime for three consecutive months, which introduced team burnout risks.
- **Schedule Compression:** Severely compressed the User Acceptance Testing (UAT) window as an accepted project risk.

Ultimately, the mobile app launched two months past the initial target date, but was successfully delivered with minimal bugs reported in production.


---

# Leadership Decisions

## 1. Conflict Resolution:

This intervention enabled Business Analysts to refine their AI-assisted story workflows to better serve development needs with clearer scope and acceptance criteria. While the issue was not completely resolved, this alignment mitigated operational friction and improved cross-team collaboration.

---

## 2. Pragmatic Adaptation & Late-Stage Crisis Triage

Adapted technical delivery workflows to accommodate the Product team’s parallel feature model, while dynamically reallocating engineering and QA capacity to execute rapid defect triage and protect the target launch date, expanding automated testing across critical scenarios

---

## 3. Non-Negotiable Deadlines & Recovery Plan:

Presented a detailed product roadmap to project sponsors demonstrating that delivering the full mobile application without scope reduction within the fixed July 2026 deadline was unachievable.

Authorized paid overtime across a three-month crunch period and compressed the User Acceptance Testing (UAT) window—deliberately managing team fatigue as an explicit risk to protect delivery.

---

## 4. Keep Decision-Makers Closely Aligned

Maintaining real-time visibility into the various challenges identified throughout development enabled the leadership team to make swift, decisive choices. By closely monitoring risks, leadership took immediate action to protect project targets—including expanding team capacity and approving critical operational decisions, even when doing so created trade-offs with gross profit margins.


---

# Results

Although the initial July 30th launch target was shifted, the full scope defined during project inception was successfully deployed on September 18th.

- **Post-Launch Handover & Infrastructure Stabilization:** The solution was formally handed over to the Support team on October 2nd, following a critical performance bottleneck during peak Friday traffic. Because load testing had not fully covered this scenario, an unexpected backend overload caused a brief service disruption. After optimizing backend services and tuning the GCP infrastructure configuration, the platform has stabilized with no major service degradations to date.
- **Comprehensive Data Migration:** Successfully executed end-to-end data migration, including all digital content and core entity records (schools, players, coaches, venues, etc.).
- **Subscriber & Payment Gateway Migration:** Completed a seamless subscriber migration, securely transferring premium membership payment profiles from Stripe to Braintree.
 - **Client Retention & Expansion:** Based on the successful rollout, the client is currently evaluating phase-two mobile app enhancements, opening new strategic business opportunities for our team.


---

# Evidence

This project demonstrates:

- Negotiation skills.
- Agile project leadership.
- Scrum and Kanban delivery.
- Web / Mobile development understanding.
- GCP Cloud-integration delivery.
- Team setup and governance.
- Risk and issue management escalation.
- Continuous-release coordination.
- Technical dependency management.

---

# Leadership Reflection

It reinforced a fundamental truth: **the true value of Agile frameworks lies not in dogmatically following ceremonies, but in utilizing transparency, empirical data, and proactive risk management to enable swift decision-making and continuous delivery flow.**

Throughout this engagement, I learned critical lessons in cross-functional governance and adaptive leadership:

- **Making Bottlenecks Visible to Drive Real Alignment:** When faced with vague AI-generated user stories, incomplete designs, or non-incremental development models, enforcing rigid processes wasn't enough. The breakthrough came from exposing the downstream risks early, using data-backed roadmaps to facilitate tough conversations between US Product stakeholders and LATAM engineering teams.
    
- **Pragmatic Flexibility Over Dogmatic Planning:** When management introduced a non-negotiable mobile app deadline into an already tight schedule, the right response was not to defend the original baseline blindly, but to adapt pragmatically. By working closely with Solution Architects and Technical Leads, we engineered high-risk recovery plans—reusing backend infrastructure, leveraging AI development tools, scaling QA/Dev capacity, and making deliberate, transparent trade-offs regarding overtime and testing windows.
    

Ultimately, this project proved that **Agile leadership is about creating a bridge between business strategy and technical execution.** By maintaining real-time visibility, protecting the delivery flow, and fostering transparent stakeholder relationships, we successfully modernized a legacy brand into a unified digital ecosystem.

---

# What I Would Do Differently Today

Without hesitation I will challenge hardly several decisions taken in the management level, and inside my purview as Scrum master

- Set a non-negotiable **Definition of Ready (DoR)** gate immediately developers raised the hand several times.  No story enters a Sprint backlog without an approved Figma link and a mandatory technical breakdown review. Perhaps, training BAs to feed technical architecture constraints into their AI prompts before handing stories to developers.

- Push Back on the "Puzzle Approach" with Vertical Slice Deliveries. My main oversight was not pushing back harder on the fragmented product planning approach (the 'puzzle approach') and failing to drive delivery toward completing actionable features to close out epics incrementally. Accepting this structure ultimately led to significant extra rework, as a wave of bugs and change requests surfaced during User Acceptance Testing (UAT). While this approach was agreed upon by all stakeholders—including the technical leads—it created unnecessary late-stage risk, and I will not permit or repeat this delivery model on future projects."

- I would also establish stronger mechanisms for retaining business knowledge by product team, that ended up with additional features when tight schedule was an issue indeed

---

# How This Project Changed the Way I Lead

My experience on this project fundamentally changed how I view my role as a leader. Moving forward, I will no longer just advise on best practices—I will **actively advocate for and enforce core engineering standards** that protect the product's health and the team's capacity.

- **Standing Firm on Critical Decisions:** I learned that when I strongly believe a decision is beneficial—or necessary—for project health, I must step up, push back firmly against anti-patterns, and hold stakeholders accountable. Passive agreement creates late-stage risk; active leadership prevents it.
    
- **Non-Negotiable Automated Testing from Day One:** Test automation can no longer be treated as an afterthought or a late-stage triage effort. Important to ensure that automated regression testing is embedded into the Definition of Done (DoD) and the CI/CD pipeline from the very beginning of development to avoid late-stage integration bottlenecks.
    
- **Context-Aware AI Integration:** AI tools offer tremendous speed, but speed without alignment creates noise. AI-generated artifacts—such as user stories and requirements—are strictly governed and contextualized to match the specific system architecture and business context before entering sprint planning.

---

# Professional Evolution

Participating in this complex digital transformation was a pivotal milestone in my professional growth, pushing me outside my comfort zone and expanding my technical and delivery horizons:

- **Expanding Front-End & Mobile Domain Expertise:** Navigating my first enterprise-level web and mobile application delivery provided invaluable exposure to front-end architecture (React / React Native). Understanding the nuances of client-side performance, responsive design, and app store deployment models added a crucial technical dimension to my software project management background.
    
- **Navigating Pure Scrum Facilitation vs. Delivery Leadership:** Serving in a dedicated Scrum Master role challenged me to lead through influence rather than direct authority. Acting as a strategic advisor to the Project Manager required me to balance supporting leadership decisions with advocating for agile best practices. This experience sharpened my diplomacy, stakeholder management, and ability to navigate high-stakes decision-making even when aligned against my personal delivery preferences.
    
- **Hands-On GCP & Cloud Infrastructure Governance:** Leading a cloud-native initiative hosted on Google Cloud Platform (GCP) bridged the gap between software delivery and cloud infrastructure. Working directly with GCP Architects and DevOps engineers allowed me to actively contribute to technical decisions surrounding CI/CD pipeline automation, infrastructure scaling, and cost optimization.
    

While this engagement brought significant operational pressure and hard-learned lessons, I deeply value the experience. Managing multi-team dependencies across a top-notch technology stack provided me with the resilience and technical versatility needed to lead complex, cloud-native transformations in the future.