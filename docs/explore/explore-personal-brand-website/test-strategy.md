# Test Strategy: Personal Brand Website

**Status**: Approved / Complete — Product Owner approval, 2026-10-01

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-10-01 | Devin | Initial test strategy from approved PRD, HLD, ADRs, and Part 2 decisions. |

---

## 1. Overview

### Purpose

Define the smallest useful automated and exploratory testing approach that safely validates the Personal Brand Website MVP. The strategy protects publication integrity, mandatory qualitative accessibility, critical visitor journeys, and Contact/CV behavior without creating a test or CI architecture more elaborate than the product.

### Scope

**In scope:**

- Structural governed-file/content validation.
- Project / Project Story separation and traceability.
- Evidence/publication eligibility and negative cases.
- Critical visitor journeys.
- Qualitative accessibility and responsive/compatibility behavior.
- Contact/CV and external destination behavior.
- Frontend-only architecture-conformance checks.
- HF-001 operational failure-mode coverage.
- HF-002 provisional dependency/readiness checks.
- Security checks proportionate to the public frontend-only MVP.

**Out of scope or conditional:**

- Application API/event contract testing unless a later approved boundary is introduced.
- Backend/database/authentication testing under the current MVP boundary.
- CMS-specific testing.
- Provider/deployment-specific testing until DEC-005/DEC-006 are resolved.
- Measurement testing until DEC-007 determines whether MVP events are required.
- Framework-specific tooling until the frontend/build stack is selected.
- Formal accessibility conformance testing against an unapproved level.

### Guiding Principles

1. Use broad, fast lower-layer validation and focused higher-layer validation.
2. Push deterministic checks down to structural/unit layers.
3. Keep human semantic publication review separate from automated structural validation.
4. Use E2E selectively for the four approved critical journeys.
5. Treat accessibility as mandatory and validate it through automation plus targeted manual/exploratory checks.
6. Use isolated, version-controlled, synthetic or appropriately anonymized test data.
7. Keep quality gates proportionate to the MVP; deferred implementation choices remain deferred.
8. Treat all targets as qualitative unless an approved source establishes a numeric target.

### Risk Posture

MVP / experimental overall posture, with non-negotiable protection of publication integrity, accessibility requirements, critical visitor/contact journeys, and Contact/CV behavior.

### Source Documents

- PRD: `explore/prds/personal-brand-website-prd.md`
- HLD: `explore/hlds/personal-brand-website-hld.md`
- ADRs: `explore/decisions/personal-brand-website-adr-001-*` through `adr-004-*`
- Risk register: `explore/explore-personal-brand-website/risks.md`
- Architecture Context: `explore/explore-personal-brand-website/architecture-context.md`
- Technical Feasibility: `explore/explore-personal-brand-website/technical-feasibility.md`

---

## 2. Testing Pyramid

```text
              /\
             /  \       Selective E2E: four approved journeys
            / E2E\      Accessibility/compatibility at critical paths
           /------\
          /        \    Focused integration: content/build/link boundaries
         /----------\
        /            \  Broad structural/unit validation
       /--------------\
```

### Layer Distribution Guidance

| Layer | Guidance | Status |
|---|---|---|
| Structural/unit | Broad and fast coverage of deterministic rules, validators, transformations, and component behavior once implementation exists. | Required |
| Integration | Focused coverage of governed content, public generation, assets/links, and applicable presentation boundaries. | Required where boundaries exist |
| Contract | No application API/event/service boundary currently exists. | Not applicable unless scope changes |
| E2E | Small selective set covering all four approved journeys. | Required |

No percentage distribution, suite-duration target, or coverage percentage is selected.

---

## 3. Unit and Structural Testing

### Definition

A unit/structural test validates one deterministic rule, transformation, validator, or presentation behavior without external services or uncontrolled data.

### Scope

- A3 relationship/reference validation.
- Project / Project Story separation.
- Validated-Project traceability.
- Lifecycle and publication classification validation.
- Evidence sensitivity and claim-reference validation.
- Negative publication cases.
- Public-content filtering and transformations.
- Link/asset validation logic.
- Frontend component behavior once the frontend stack is selected.
- Structural accessibility semantics where automation can establish them.

### Exclusions

- No database, network, application API, message queue, or external service dependency under the current MVP.
- No human semantic judgment is automated by assertion.

### Framework and Tooling

Stack-native framework, assertion, mocking, and coverage tooling: **TBD** until the frontend/build stack is selected.

### Patterns

- Arrange-Act-Assert or Given-When-Then.
- Isolated test data factories/builders.
- Version-controlled fixtures.
- No shared mutable state.
- Explicit evidence labels for test assumptions.

### Coverage expectations

Strong coverage is required for publication-integrity rules and negative cases. No arbitrary percentage is established.

---

## 4. Integration Testing

### Definition

Focused tests crossing an approved content, generation, presentation, asset, or external-destination boundary.

### Boundaries

| Boundary | Type | Approach | Tool |
|---|---|---|---|
| Governed content → structural validator | Content validation | Representative fixtures and negative cases | TBD with stack |
| Approved content → public generation | Publication/build boundary | Eligibility and generated-output checks | TBD; mechanism unresolved |
| Generated assets → Public Website Experience | Presentation/output | Render and link/asset checks | TBD with stack |
| Public Website → external destinations | External boundary | Controlled link/download behavior checks | TBD; no application API |
| Public Website → Measurement | Conditional | Only if DEC-007 approves events | TBD |

### Required scenarios

- Happy path for eligible content.
- Restricted/unclassified/incomplete/incorrectly related/invalid-lifecycle content.
- Missing or broken CV/contact assets.
- External destination unavailable while alternate approved methods remain visible.
- Public-generation failure without treating failure as successful eligibility.

No database, API, queue, or service contract integration layer is introduced.

---

## 5. Contract Testing

### Applicability

**Not applicable to the current approved MVP architecture.** No application API, event, service, database, or message-queue boundary exists.

### Process

If a later approved requirement or material risk introduces an API/event/service boundary, reassess contract testing through the applicable architecture gate. No contract-testing tool is selected now.

---

## 6. E2E Testing

### Definition

Full visitor-experience tests limited to the highest-value approved journeys.

### Critical User Journeys

| # | Journey | Coverage intent | Risk | Automated |
|---:|---|---|---|---|
| 1 | Home → Projects → Project Story Detail → Contact | Relevance, eligible Story presentation, progressive disclosure, Contact. | High | Yes, once stack exists |
| 2 | Direct Contact / CV access | Contact methods, CV asset, link/download behavior. | High | Yes, once stack exists |
| 3 | Supporting-context exploration | P1 context, non-linear movement, return to evidence/Contact. | High | Yes, once stack exists |
| 4 | Project Story deep evaluation | Orientation, deeper evidence, related/return path, Contact. | High | Yes, once stack exists |

### Tooling and stability

Browser automation product, visual-regression tool, retry policy, and execution environment: **TBD** until frontend/build and environment choices exist.

No exhaustive browser combinations or provider-specific flows are required.

---

## 7. Non-Functional Testing

### Performance

- Proportional page and asset performance validation.
- No numeric response-time, throughput, concurrency, or load target is approved.
- No load-testing programme or tool is selected.

### Security

- HTTPS and public-surface security checks.
- Publication boundary and restricted-content exclusion checks.
- Dependency/public-asset checks when implementation exists.
- No backend/authentication security architecture is assumed.

### Accessibility

- Automated structural/accessibility checks where implementation permits.
- Manual/exploratory keyboard, focus, semantic, disclosure, and comprehension validation.
- No formal conformance level is selected under DEC-008B.

### Compatibility

- Representative browser/device and responsive validation.
- B6 widths remain design references, not implementation breakpoints.
- No compatibility platform/tool is selected.

---

## 8. Test Data and Environments

### Test Data Strategy

| Layer | Approach | Details |
|---|---|---|
| Structural/unit | Isolated factories/builders and fixtures | Synthetic, version-controlled, no shared mutable state |
| Integration | Representative governed content | Tigo/Avianca/DFA scenarios plus negative publication cases; not production content |
| E2E | Synthetic or appropriately anonymized data | No restricted Evidence or client-sensitive material; no unapproved public records treated as approved production content |
| External destinations | Controlled fixtures/stubs | Validate links/downloads and fallback visibility without controlling third-party systems |

### Environment Topology

| Environment | Purpose | Status |
|---|---|---|
| Local/developer | Structural/unit and narrow integration validation | Generic capability; implementation TBD |
| CI | Automated checks once platform exists | Platform TBD |
| Preview/staging | Selective E2E, accessibility, compatibility, and security checks | Environment TBD under DEC-005/DEC-006 |
| Production | Future smoke/health checks only if approved | Hosting/release model TBD |

No provider, database, CI system, environment implementation, or deployment tooling is selected.

---

## 9. CI/CD Integration

### Capability stages

1. Structural/unit validation before public generation.
2. Focused integration and content/publication checks.
3. Build/preview readiness checks.
4. Critical journey, accessibility, compatibility, and security readiness.
5. Conditional post-release confidence checks after DEC-005/DEC-006.

### Quality gates

- **Gate A:** publication eligibility and negative-case validation pass.
- **Gate B:** preview/build output contains only eligible content; Contact/CV/assets are ready.
- **Gate C:** four critical E2E journeys, qualitative accessibility, compatibility, and proportionate security checks pass.
- **Gate D:** measurement checks only if DEC-007 approves events.
- **Gate E:** hosting/release/rollback checks only after DEC-005/DEC-006.

### Failure policies

- Failed structural validation blocks public generation.
- Failed preview/build readiness blocks promotion.
- Failed critical journey/accessibility/security/compatibility checks block release readiness until corrected or explicitly dispositioned at the applicable human gate. Such disposition must not silently weaken mandatory publication-integrity or accessibility requirements.
- Hosting/release failure handling remains subject to later approved DEC-005/DEC-006 choices.

No pipeline platform, branch model, command, CI stage implementation, or numeric threshold is selected.

---

## 10. Metrics and Success Criteria

### Coverage indicators

- Publication negative cases have corresponding structural checks.
- All four critical journeys have E2E coverage once implementation exists.
- Applicable integration boundaries have happy/error/edge coverage.
- Qualitative accessibility requirements are checked through automation plus targeted manual validation.

### Quality indicators

- Publication-validation failures and rejected negative cases.
- Unresolved structural references.
- Critical-journey pass/fail results.
- Accessibility and compatibility findings.
- Contact/CV/link failures.
- Test instability and maintenance burden.

These are observational signals, not numeric release thresholds.

### Deferred metrics

- Framework-specific coverage metrics: deferred with frontend/build stack.
- Pipeline duration: deferred with CI/CD selection.
- Hosting/release metrics: deferred under DEC-005/DEC-006.
- Measurement/business metrics: deferred under DEC-007.
- Formal accessibility score: deferred under DEC-008B.

---

## 11. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Publication negative cases are incomplete | High | Maintain structural eligibility cases and human semantic review. |
| Semantic validation is mistaken for automation | High | Keep Evidence adequacy, attribution, wording, qualification, disclosure, and final approval human-governed. |
| E2E scope expands beyond MVP value | Medium | Limit E2E to the four approved journeys. |
| Accessibility automation creates false confidence | High | Pair automated checks with manual/exploratory validation. |
| Frontend/build stack remains unresolved | Medium | Keep tooling and organization deferred; select only after stack approval. |
| Provisional dependencies remain unresolved | Medium | Track individually in the Blocker Register; promote only if implementation is blocked. |
| Measurement is introduced prematurely | Medium | Keep all measurement testing conditional under DEC-007. |
| Provider/release assumptions enter testing | Medium | Defer environment/provider-specific checks to DEC-005/DEC-006. |

---

## 12. References

| Document | Path |
|---|---|
| PRD | `explore/prds/personal-brand-website-prd.md` |
| HLD | `explore/hlds/personal-brand-website-hld.md` |
| ADRs | `explore/decisions/personal-brand-website-adr-001-*` through `adr-004-*` |
| Risk register | `explore/explore-personal-brand-website/risks.md` |
| Architecture Context | `explore/explore-personal-brand-website/architecture-context.md` |
| Technical Feasibility | `explore/explore-personal-brand-website/technical-feasibility.md` |
| Approved experience | `explore/design/wireframes-personal-brand-website.md` |
| Approved domain model | `explore/explore-personal-brand-website/domain-analysis.md` |

This strategy preserves the MVP objective: enough testing to safely reach and validate a working website, without creating a testing architecture more elaborate than the product.

## Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-10-01 | Devin | Initial Test Strategy from approved PRD, HLD, ADRs, and Part 2 decisions. |
| 0.2 | 2026-10-01 | Devin | Product Owner approved Test Strategy; deferred implementation-specific tooling and thresholds preserved. | 
