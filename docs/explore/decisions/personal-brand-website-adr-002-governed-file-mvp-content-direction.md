# ADR-002: Governed-File MVP Content Direction

**Status**: Accepted
**Date**: 2026-10-01
**Accepted**: 2026-10-01 — Jairo Enrique Diaz, Product Owner
**Decision Maker**: Jairo Enrique Diaz — Product Owner
**Supersedes**: None

## Context

The MVP needs a governed way to represent factual Projects, Evidence, and curated Project Stories while preserving A3 relationships and publication controls. Representative Tigo, Avianca, and DFA validation showed that governed-file candidates can support the required logical model and structural checks. The website content is expected to be relatively stable rather than high-frequency or dynamically managed content. The approved governed-file direction therefore satisfies the current MVP architecture. No approved requirement or material risk currently justifies the additional CMS infrastructure, operating model, or maintenance complexity. `[OBS]` Technical Feasibility §2 Data Latency states that content changes are build/review dependent, no real-time content feed is required for the MVP, and the experience must not depend on live content feeds or runtime repository access.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows), Section 4 (Key Architectural Decisions and Technology Stack)

## Decision

Use a governed-file approach for the MVP rather than introducing a managed CMS.

This decision does not select Markdown/structured metadata versus JSON/YAML, production schema, repository/content structure, content contract, validation tooling, build mechanism, or frontend technology.

## Options Considered

### Option A: Governed files

- **Description**: Maintain governed content in versioned files with explicit metadata and relationships.
- **Pros**: Proportionate infrastructure; versionable; compatible with the Context Warehouse direction; supports reviewable content changes.
- **Cons**: Requires disciplined metadata, references, validation, and authoring conventions.
- **Selected because**: Representative feasibility checks passed for the candidate governed-file forms; content is expected to be relatively stable; and no approved requirement or material risk currently justifies additional CMS infrastructure, operating model, or maintenance complexity. A managed CMS is therefore not selected for the MVP. This does not prohibit reconsidering a CMS if later evidence demonstrates that governed files cannot satisfy an approved requirement or material risk.

### Option B: Managed CMS

- **Description**: Use a managed content platform for authoring, relationships, workflows, and delivery preparation.
- **Pros**: Could provide authoring workflows and structured content management.
- **Cons**: Adds vendor, operational, integration, privacy, and publication-boundary complexity.
- **Rejected because**: No approved requirement or material risk currently demonstrates that governed files are insufficient.

### Option C: Unstructured source prose as runtime content

- **Description**: Use the existing CV and Project Knowledge Base prose directly as public website source content.
- **Pros**: Minimal transformation effort.
- **Cons**: Cannot reliably preserve A3 relationships, Project/Project Story separation, Evidence sensitivity, publication classification, or eligibility checks.
- **Rejected because**: Violates approved content-governance and publication-safety boundaries.

## Consequences

### Positive

- Avoids unjustified CMS complexity for the MVP.
- Preserves a governed, reviewable content direction compatible with A3 and publication controls.

### Negative

- Production format and schema work remain necessary.
- Authoring and validation discipline must be designed before implementation.

### Risks

- A governed-file representation may fail to express the full A3 model or governance metadata — mitigate through representative content validation and deterministic structural checks before production selection.

## Related Decisions

- DEC-002 in `personal-brand-website-decision-log.md`: governed-file MVP direction.
- ADR-001: logical boundaries constrain content ownership and consumption.
- ADR-003: publication-safety controls apply to governed content before generation.
- ADR-004: combined delivery consumes only approved eligible content.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows), Section 4 (Key Architectural Decisions and Technology Stack)
