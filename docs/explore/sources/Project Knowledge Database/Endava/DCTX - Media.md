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


---



---

# Leadership Decisions

## 1. Treat Risks as Triggers for Delivery Improvement

I used identified risks as signals that the delivery model might need to change.

Rather than only tracking issues, the objective was to adapt the way the team worked whenever the original assumptions were no longer effective.

---

## 2. Bring in the Right Expertise

When the team struggled with gRPC, the response was not to continue pushing the same approach.

An experienced developer was brought in to bridge the gap between the architectural definition and practical implementation.

This accelerated the team's understanding and helped stabilize delivery.

---

## 3. Escalate Missing Business Support

The engineering team could not successfully refactor business processes without sufficient knowledge from DFA stakeholders.

When business participation became a blocker, I escalated the issue and worked with the client to improve availability and coordination.

---

## 4. Keep Decision-Makers Closely Aligned

Project reviews were scheduled every two weeks and included key technical and delivery decision-makers.

These reviews helped maintain alignment across:

- Technical leads.
- Client Project Management.
- Sponsors.
- Endava delivery leadership.

The objective was to reduce delays in decisions and keep roadmap changes visible.

---

## 5. Work Collaboratively With the Client

A major strength of the engagement was the close working relationship with DFA.

The client was generally supportive of changes required to improve delivery.

This made it possible to address issues with less bureaucracy and focus on solving problems collaboratively.

---

# Results

The API Gateway solution was successfully implemented using gRPC and REST-based integration patterns.

The solution supported the required production traffic and peak loads during go-live.

The refactored business processes required only limited adjustments for edge cases identified after release.

The project maintained a continuous delivery model across the approximately 60 business processes included in the broader program.

Customer satisfaction improved significantly during the engagement:

- First-year satisfaction score: approximately 5.6.
- Later satisfaction score: approximately 8.5.

The engagement continued with improved client confidence and delivery stability.

---

# Evidence

This project demonstrates:

- Agile project leadership.
- Scrum and Kanban delivery.
- Capital Markets experience.
- Cloud-integration delivery.
- API-platform delivery.
- Team setup and governance.
- Client relationship management.
- Risk and issue management.
- Business-process refactoring.
- Continuous-release coordination.
- Distributed technical-team leadership.
- Technical dependency management.
- Stakeholder escalation.
- Delivery adaptation.
- Client satisfaction improvement.

---

# Leadership Reflection

This project gave me the opportunity to apply Agile delivery practices in a much more mature and practical way than in my previous experiences.

I learned that the value of Scrum or Kanban does not come from following ceremonies mechanically.

The value comes from using the principles behind them to improve transparency, decision-making, team alignment, and delivery flow.

The project also reinforced the importance of adapting the delivery approach when initial assumptions no longer apply.

When technical complexity, stakeholder availability, or team changes affected delivery, the right response was not to protect the original plan at all costs.

It was to make the problem visible, involve the right decision-makers, agree on the required change, and keep the team aligned with the product vision and program milestones.

The strong working relationship with the client made this possible.

---

# What I Would Do Differently Today

Today I would formalize several areas earlier in the engagement:

- Business-process ownership for each refactored workflow.
- Knowledge-transfer expectations when team members change.
- Technical onboarding for complex frameworks such as gRPC.
- Explicit dependency mapping between business, technical, and release activities.
- Capacity buffers for team transitions.
- Clear escalation thresholds for missing business support.

I would also establish stronger mechanisms for retaining business and technical knowledge so that team changes had less impact on delivery continuity.

---

# How This Project Changed the Way I Lead

- I learned how to apply Agile principles pragmatically rather than mechanically.
- I became more confident adapting roadmaps and delivery plans when evidence showed that the original assumptions were no longer valid.
- I learned to use regular stakeholder reviews to accelerate decisions and keep technical and business leaders aligned.
- I became more deliberate about protecting team health and continuity.
- I learned how critical business participation is when technology teams are refactoring complex domain processes.
- I strengthened my ability to communicate risks and issues clearly to both client and internal stakeholders.
- I became more comfortable leading delivery in a highly regulated and technically complex Capital Markets environment.
- I gained more experience supporting presales, contract discussions, and new opportunity development.

---

# Professional Evolution

This engagement marked a significant step in my development as an Agile Project Manager.

Earlier in my career, I had learned delivery primarily through Waterfall projects and later through a difficult first experience with Agile.

This project gave me the opportunity to apply Agile delivery successfully in a complex real-world environment.

I learned how to combine:

- Agile practices.
- Project-management discipline.
- Technical understanding.
- Stakeholder management.
- Client partnership.
- Delivery adaptation.

It also strengthened my confidence in leading projects where technology, business processes, and delivery governance are tightly interconnected.
