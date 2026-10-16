# ADR-001: Logical Responsibility Boundaries

**Status**: Accepted
**Date**: 2026-10-01
**Accepted**: 2026-10-01 — Jairo Enrique Diaz, Product Owner
**Decision Maker**: Jairo Enrique Diaz — Product Owner
**Supersedes**: None

## Context

The approved architecture must preserve the distinction between governed professional knowledge, Project Story curation/publication governance, and visitor-facing presentation. The B.1 Boundary Map, Truth Hierarchy, and Design Sketch established these as logical responsibility boundaries.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows)

## Decision

Preserve the following three logical responsibility boundaries:

1. Context Warehouse / Professional Knowledge.
2. Project Story Curation / Publication Governance.
3. Public Website Experience.

This decision does not convert the boundaries into separate services, repositories, deployment units, or runtime components. Physical topology remains unresolved.

## Options Considered

### Option A: Preserve three logical responsibility boundaries

- **Description**: Keep the three approved contexts as logical ownership and responsibility boundaries while deferring physical topology.
- **Pros**: Preserves A3 ownership, Project/Project Story separation, publication governance, and proportionality; permits later physical mapping based on evidence.
- **Cons**: Physical realization remains open and must be formalized without silent inference.
- **Selected because**: It is the approved B.1 direction and preserves the validated domain and experience boundaries without unjustified infrastructure.

### Option B: Combine delivery responsibilities physically

- **Description**: Combine selected delivery concerns while retaining the logical boundaries.
- **Pros**: May reduce operational complexity and cost for the MVP.
- **Cons**: Could blur ownership or publication controls; requires evidence that governance remains intact.
- **Rejected because**: Not selected as a physical topology; retained only for later comparison if justified.

### Option C: Physically separate curation and website delivery

- **Description**: Realize curation/publication and website delivery as separate physical units.
- **Pros**: Could strengthen isolation and explicit handoff.
- **Cons**: Adds contract, deployment, and operational complexity.
- **Rejected because**: No approved requirement or material risk currently justifies the additional physical separation.

## Consequences

### Positive

- Logical ownership remains clear across all HLD sections.
- Future physical decisions can be evaluated without redefining the domain model or visitor experience.

### Negative

- Physical topology and implementation mapping remain unresolved.
- Later HLD/implementation work must explicitly preserve the logical boundaries.

### Risks

- Physical implementation could silently collapse boundaries — mitigate through the validated Boundary Map, Truth Hierarchy, negative boundary statements, and this ADR.

## Related Decisions

- DEC-001 in `personal-brand-website-decision-log.md`: approved logical-boundary direction.
- ADR-002: governed-file content direction depends on these boundaries.
- ADR-003: publication-safety controls depend on the curation/publication boundary.
- ADR-004: combined delivery ownership is bounded by these logical responsibilities.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows)
