# ADR-003: Publication-Safety Control Direction

**Status**: Accepted
**Date**: 2026-10-01
**Accepted**: 2026-10-01 — Jairo Enrique Diaz, Product Owner
**Decision Maker**: Jairo Enrique Diaz — Product Owner
**Supersedes**: None

## Context

The MVP must prevent restricted, unclassified, incomplete, unsupported, or otherwise ineligible content from public generation while preserving human judgment for semantic truthfulness and Evidence adequacy. Representative validation demonstrated that structural checks can reject machine-detectable negative cases, but cannot independently judge attribution, truthful wording, narrative qualification, or Evidence adequacy.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows), Section 7 (Security Considerations), Section 10 (Deployment Architecture)

## Decision

Publication safety must combine:

1. human semantic governance for Evidence adequacy, attribution, truthful wording, narrative qualification, disclosure judgment, and final Content Owner approval; and
2. deterministic structural eligibility validation before public generation for approved machine-readable lifecycle, classification, reference, Evidence-sensitivity, and related structural rules.

Deterministic validation must not be represented as proof of semantic truthfulness or Evidence adequacy unless a later approved machine-readable constraint genuinely makes such a check deterministic.

The exact enforcement stage, mechanism, tooling, and physical implementation remain unresolved.

## Options Considered

### Option A: Human semantic governance plus deterministic structural validation

- **Description**: Human Content Owner governance handles semantic and disclosure judgment; structural validation rejects machine-detectable eligibility failures before public generation.
- **Pros**: Preserves truthfulness and attribution judgment while preventing structural publication failures.
- **Cons**: Requires coordinated governance and validation; exact enforcement stage remains open.
- **Selected because**: It is the approved control direction supported by representative validation and the publication-safety risks.

### Option B: Deterministic validation as the primary publication authority

- **Description**: Automated validation determines whether content is truthful, adequate, attributable, and eligible.
- **Pros**: Potentially repeatable and fast.
- **Cons**: Cannot independently determine semantic truthfulness, Evidence adequacy, attribution, narrative qualification, or disclosure judgment without approved machine-readable constraints.
- **Rejected because**: It would weaken the approved human governance boundary.

### Option C: Human approval without deterministic structural validation

- **Description**: Rely on Content Owner review without machine-readable eligibility checks.
- **Pros**: Low tooling complexity.
- **Cons**: Does not reliably reject missing references, invalid lifecycle, restricted sensitivity, unclassified content, or incorrect relationships.
- **Rejected because**: It is incomplete against publication-safety risks TR-02 and TR-03.

## Consequences

### Positive

- Preserves human authority over semantic truth and disclosure.
- Provides repeatable structural protection before public generation.

### Negative

- Requires both governance workflow and structural validation capability.
- Exact stage and tooling remain open and may affect build/release complexity.

### Risks

- Structural checks may create false confidence — mitigate by explicitly keeping semantic review and Content Owner approval mandatory.
- Enforcement may be placed too late — mitigate through later stage analysis and negative-case testing.

## Related Decisions

- DEC-003 in `personal-brand-website-decision-log.md`: publication-safety control direction.
- ADR-001: logical boundaries define governance and presentation ownership.
- ADR-002: governed-file direction supplies the candidate representation for structural checks.
- ADR-004: combined delivery may prepare/generate content only after the applicable governance boundary.

**Affects**: HLD Section 2 (Architecture Approach), Section 3 (Component Breakdown and Integration & Data Flows), Section 7 (Security Considerations), Section 10 (Deployment Architecture)
