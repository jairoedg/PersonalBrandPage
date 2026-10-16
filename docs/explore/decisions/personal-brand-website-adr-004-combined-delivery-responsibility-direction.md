# ADR-004: Combined Delivery Responsibility Direction

**Status**: Accepted
**Date**: 2026-10-01
**Accepted**: 2026-10-01 — Jairo Enrique Diaz, Product Owner
**Decision Maker**: Jairo Enrique Diaz — Product Owner
**Supersedes**: None

## Context

DEC-004 resolves the logical ownership direction for approved-content preparation and public generation while preserving the three approved logical responsibility boundaries. The Product Owner selected the combined delivery direction for proportional MVP simplicity, without selecting one repository, service, process, deployment unit, or runtime topology.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows), Section 4 (Key Architectural Decisions and Technology Stack), Section 10 (Deployment Architecture)

## Decision

- Project Story Curation / Publication Governance remains the logical governance authority.
- Curation retains Project Story governance, human semantic governance, Evidence adequacy and attribution judgment, publication classification, disclosure judgment, publication eligibility, and final Content Owner approval.
- A combined delivery responsibility owns approved-content preparation and public generation.
- It may consume only content that has passed the applicable governance/eligibility boundary.
- Public Website Experience remains the visitor-facing presentation/navigation responsibility and does not acquire Project validation, Evidence assessment, publication approval, or internal governance responsibilities.

“Combined delivery responsibility” does not imply one repository, service, process, deployment unit, or runtime topology. Remaining physical and implementation mapping remains open.

## Options Considered

### Option A: Separate curation and build responsibilities

- **Description**: Curation owns approved content and a separate build responsibility consumes it.
- **Pros**: Strong separation of governance and generation responsibilities.
- **Cons**: Adds a responsibility handoff and operational coordination for the MVP.
- **Rejected because**: The Product Owner selected the simpler combined-delivery ownership direction for the MVP; reconsider only if evidence demonstrates a concrete need for separation.

### Option B: Combined delivery responsibility

- **Description**: A combined delivery responsibility prepares approved content and produces public website assets while Curation retains governance authority.
- **Pros**: Proportionate MVP simplicity; avoids an additional responsibility boundary; preserves governance ownership.
- **Cons**: Requires explicit controls so combined delivery cannot bypass eligibility or Content Owner approval; physical mapping remains unresolved.
- **Selected because**: It is the Product Owner-approved direction for simplicity without weakening publication governance or logical bounded contexts.

### Option C: Shared responsibility with explicit ownership contract

- **Description**: Curation and delivery share responsibilities through a separate ownership matrix and handoff contract.
- **Pros**: Could coordinate specialized responsibilities while preserving governance.
- **Cons**: Adds coordination and contract complexity without a demonstrated MVP requirement.
- **Rejected because**: Not selected at this gate; may be reconsidered only with concrete evidence.

## Consequences

### Positive

- Reduces unnecessary MVP responsibility-boundary overhead.
- Preserves Curation/Content Owner authority and the Public Website Experience boundary.

### Negative

- Combined delivery must be prevented from bypassing publication eligibility or semantic governance.
- Physical repository/process/deployment mapping remains unresolved.

### Risks

- Combined delivery could be interpreted as collapsing logical boundaries — mitigate through the Boundary Map, DEC-003 controls, explicit negative boundaries, and this ADR.
- Physical mapping may later require refinement — stop and return to the Product Owner gate if HLD formalization cannot proceed coherently.

## Related Decisions

- DEC-004 in `personal-brand-website-decision-log.md`: combined delivery responsibility direction.
- ADR-001: logical responsibility boundaries remain distinct.
- ADR-002: governed-file direction supplies approved content to delivery.
- ADR-003: publication-safety controls apply before public generation.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows), Section 4 (Key Architectural Decisions and Technology Stack), Section 10 (Deployment Architecture)
