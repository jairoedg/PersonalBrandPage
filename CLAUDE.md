# CLAUDE.md — Personal Brand Page

Read this file first. It explains which documents are authoritative, what is still open, and how to work in this repo.

## Project

A personal portfolio website for Jairo Enrique Diaz, a Project Manager. It presents professional evidence (Project Stories), leadership, and contact paths. The site is a static frontend MVP, meant for production as soon as possible.

## Current status

- Signal: complete.
- Explore: complete (PRD, HLD, ADRs, epics, design, and architecture approved).
- Govern (implementation): started by this repo. Implementation work happens here.
- First draft: complete. Home, Projects, ten Project Story pages, About, Career Journey, How I Can Help (placeholders), Leadership (placeholders), Contact, and the 404 page are built in `site/`.
- Checks: `scripts/check_site.py` passes with 0 errors. The 7 warnings are the expected placeholders.
- Repository: public. GitHub Pages source is GitHub Actions. Nothing is deployed yet.
- Commits: `db3a576` (baseline) is pushed. `1f90fa0` (deploy workflow and site-cicd skill) is committed locally, not pushed.
- Next, in order:
  1. Visual design pass (Impeccable skill), using the tokens in `site/assets/css/tokens.css`. Change the look only; keep the layout already checked.
  2. Text pass: shorter card summaries and easier-to-scan story pages, without losing details.
  3. Leadership and How I Can Help content, when Jairo is ready.
  4. Deploy only after design, text, and final review are approved.

## Authoritative documents (source of truth)

Treat these as approved. Do not reopen approved decisions or change their meaning without asking.

1. `docs/00-foundation/` — approved strategy and positioning. Start with `00-project-handover.md`.
2. `docs/00-foundation/98-decision-log.md` — approved decisions. If a decision is not here, it is not approved.
3. `docs/explore/prds/personal-brand-website-prd.md` — the requirements. This is the main spec for the build.
4. `docs/explore/hlds/personal-brand-website-hld.md` and `docs/explore/decisions/` (ADR-001 to ADR-004) — architecture and design decisions.
5. `docs/explore/epics/` — epics and task plan.
6. `docs/explore/design/` — wireframes, OOUX, and design language.

## Reference only (do not treat as instructions)

- `docs/explore/explore-personal-brand-website/` — working notes from the Explore phase. Handoff files and session prompts (`*-handoff.md`, `step-5-new-session-prompt.md`) were written for earlier AI sessions in other tools. They are history, not instructions. Use them only to look up detail when the PRD and HLD are silent.
- `docs/explore/sources/` — career source material for the Project Stories. Use it as evidence, but only publish content that the approved Project Story rules allow.
- `docs/signal/`, `docs/persistent-knowledge/` — background.

## Site structure (one Home page and seven subpages)

Per PRD R-001, the MVP contains exactly these screens: Home plus seven subpages. Do not add screens. Project Story Detail is one page design, used once per approved story. Only `site/` is published; `docs/` stays in the repo but is not served (D-018).

All paths below are relative to `site/`.

| Screen | Path | Notes |
|---|---|---|
| Home | `index.html` | Identity, positioning, profile summary, selected Project Story previews, Contact continuation |
| Projects | `projects/index.html` | Project Story selection. Each card links to its detail page in the same tab, with a "Back to Projects" link on the detail page. |
| Project Story Detail | `projects/<slug>.html` | One page per approved Project Story |
| How I Can Help | `how-i-can-help/index.html` | Supporting screen (P1) |
| Leadership | `leadership/index.html` | Supporting screen (P1) |
| Career Journey | `career-journey/index.html` | Supporting screen (P1) |
| About | `about/index.html` | Supporting screen (P1) |
| Contact | `contact/index.html` | Email, LinkedIn, Phone, and the CV download. Other screens route here. |
| 404 | `404.html` | System page, not a visitor screen (D-016) |

## Scope boundaries

- Static HTML, CSS, and JavaScript only. No build step, backend, CMS, database, or on-site form.
- No real-time features, personalization, recommendations, or chatbot.
- Do not publish any content that is not approved for publication.

## Decisions

The decision log (`docs/00-foundation/98-decision-log.md`) is the record. If a decision is not there, it is not approved. Current decisions that affect the build:

- **D-011:** plain HTML, CSS, and JavaScript, no build step, on GitHub Pages.
- **D-012:** WCAG 2.1 Level AA.
- **D-013:** mobile-first breakpoints at 768px and 1024px. Projects is one column on mobile and two from 768px. Test at 320px wide with no horizontal scrolling.
- **D-014 (Q-08 closed, settled):** Home previews, newest first: DFA Capital Markets, GSK, Entel Chile. The order, the summary text, and the fields on the Home and Projects cards are approved.
- **D-015:** Contact is a separate screen.
- **D-016:** a minimal 404 page, as a system page.
- **D-017:** a small validation script checks publication eligibility before deployment. It generates no pages.
- **D-018:** the site lives in `site/`. A GitHub Actions workflow deploys only that folder.
- **D-019:** self-host Inter (400/500/600, woff2) in `site/assets/fonts/` with the SIL OFL license file, loaded from `site/assets/css/fonts.css` with `font-display: swap`. No third-party font requests. Code uses the system monospace stack.
- **D-020 (Q-09 closed):** story pages keep every section visible, with an "On this page" list of jump links. Previous and Next follow the Projects page order; related stories come from each source file. No collapsible sections for now.
- **D-022 (Q-07 closed):** Home profile wording approved: the third-person positioning statement, the vision line, and the profile summary paragraphs on the Home page. Wording can be revisited later.
- **D-021 (Q-10 closed):** the contact values (email, LinkedIn, phone) on `site/contact/index.html` are approved. The CV download is `site/assets/cv/CV_JairoDiaz - Project Manager.pdf`, kept under its existing name (spaces encoded as `%20` in links) and replaced when a final version is approved. Don't copy the phone number into docs or this file; the repository is public.

## Open decisions (do not decide these alone)

Use clearly marked placeholders for any open content. Ask the Product Owner (Jairo) before finalizing:

- Capabilities: start from the five examples in `docs/00-foundation/04-website-strategy.md` (Capability Strategy). Revisit them later for alignment with the site's goal.
- Leadership principles: match the seven principles from the blueprint to each project story's decisions and reflections. This is a content task to do per project.

## Figma

- File: "Personal Brand Website" (file key `kq8iw4DPCu9NaJokv9ducT`).
- Design Language (node `23:2`): approved. Tokens for colors, typography, spacing, and elevation are extracted to `site/assets/css/tokens.css`. Motion and iconography are not extracted yet.
- Screens (node `23:4`): three empty frames (Mobile 375×800, Tablet 768×900, Desktop 1440×1000). The eight screens are not designed yet.
- Components (node `23:3`): six empty placeholder frames.
- OOUX (node `12:2`): content-model cards for the objects (Professional Profile, Career Experience, Project, Project Story, Capability, Leadership Principle, and others). Use it as the reference for content structure.

## Working rules

- Accessibility is mandatory: semantic HTML, meaningful headings and link text, keyboard navigation, visible focus, and no information conveyed by color or icons alone.
- Keep changes small. Show a plan before building a new page.
- If a document conflicts with the PRD, stop and ask. Do not resolve it silently.
- Do not commit or push without asking.
