# CLAUDE.md — Personal Brand Page

Read this file first. It explains which documents are authoritative, what is still open, and how to work in this repo.

## Project

A personal portfolio website for Jairo Enrique Diaz, a Project Manager. It presents professional evidence (Project Stories), leadership, and contact paths. The site is a static frontend MVP, meant for production as soon as possible.

## Current status

- Signal: complete.
- Explore: complete (PRD, HLD, ADRs, epics, design, and architecture approved).
- Govern (implementation): started by this repo. Implementation work happens here.
- First draft: complete. Home, Projects, ten Project Story pages, About, Career Journey, How I Can Help (placeholders), Leadership (placeholders), Contact, and the 404 page are built in `site/`.
- Checks: `scripts/check_site.py` passes with 0 errors. The 16 warnings are the expected placeholders: the ten story summaries (D-025), the page introductions, Home's "Explore more" lines, and Leadership and How I Can Help content. `--strict` (the deploy gate) fails until every one is replaced.
- Impeccable detector (`.claude/skills/impeccable/scripts/impeccable detect --json site`): 0 findings. Measured false positives are recorded as scoped exceptions in `.impeccable/config.json`.
- Repository: public. GitHub Pages source is GitHub Actions. Nothing is deployed yet.
- Git: PRs #1, #2, #3, and #5 are merged into `main`. They hold the Impeccable skill, the deploy workflow and placeholder gate, expandable story sections, the monochrome Home with the photo hero, and the Projects page (D-028).
- Look (2026-10-28): Home is fully monochrome (`.theme-mono` on its `<body>`). Every other page uses the monochrome base with one blue accent (D-027 as amended). Content pages share one page header, a light blue-tinted band with the title and intro; the Projects page keeps its dark band. Jairo is drafting new designs for Career Journey, Contact, Leadership, and How I Can Help in Claude Artifacts, so those pages will likely change.
- Next, in order:
  1. Jairo completes the missing story text: Tigo (leadership sections), GT&T (decisions section), and Digicel (decisions section).
  2. Text pass: story summaries (D-025), shorter card summaries, and page introductions, each approved by Jairo.
  3. Leadership and How I Can Help content, when Jairo approves it. The leadership draft is in Obsidian at `docs/explore/drafts/leadership-principles-draft.md` and is not approved.
  4. Page redesigns from Jairo's Artifacts, once recorded in the decision log.
  5. Deploy only after design, text, and final review are approved, and with no placeholders left on the site (D-017).

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
- **D-020 (Q-09 closed; partly revoked by D-025):** an "On this page" list of jump links moves between sections. Previous and Next follow the Projects page order; related stories come from each source file. The rule that every section stays visible is revoked.
- **D-022 (Q-07 closed):** Home profile wording approved: the third-person positioning statement, the vision line, and the profile summary paragraphs on the Home page. Wording can be revisited later.
- **D-021 (Q-10 closed):** the contact values (email, LinkedIn, phone) on `site/contact/index.html` are approved. The CV download is `site/assets/cv/CV_JairoDiaz - Project Manager.pdf`, kept under its existing name (spaces encoded as `%20` in links) and replaced when a final version is approved. Don't copy the phone number into docs or this file; the repository is public.
- **D-023:** decorative icons on section and project titles, not in the top navigation. Hand-drawn inline SVG: outlined, 24px grid, 1.75px stroke, `aria-hidden`, never the only label. No icon library.
- **D-024:** the Career Journey timeline (the visual form of D-004): one continuous line, a marker per role, bold years, newest first, and projects as dated links inside their role. Its accent follows D-027 (blue; black on Home).
- **D-025:** story pages use expandable sections, one open at a time. Opening a section closes the one that was open. A short summary above the sections is always visible; it is first person, and Jairo approves each one. Each section heading has a disclosure triangle (right when closed, down when open). The first section of each story is open on load, and printed pages expand all sections. "Expand all" on screen is not part of this decision.
- **D-026:** option C teal look. Superseded by D-027.
- **D-027 (amended 2026-10-28):** monochrome base after devin.ai: stone-50 page, white cards, coal-black (stone-900) text and buttons, stone-600 secondary text, stone-200 borders. Home stays fully monochrome, with a two-column hero (name, positioning, vision, "Let's talk" and "Download CV" buttons; the portrait on the right, below the buttons on mobile). The Primary nav shows "Contact" as a black pill. Other pages add one blue accent: blue-700 for links, icons, and focus; blue-50 or blue-100 for tinted surfaces; blue sector labels on Project cards. Other hues only where they carry a meaning that is also written as text. Placeholder and warning colors are unchanged. Inter stays (D-019). H1 and H2 use weight 400; H3 and smaller headings use 600.
- **D-028:** Projects page (Option B), colors per D-027: dark band with "Projects", the intro line ("I love making projects succeed, using both Agile and Waterfall across different markets."), and three key figures; Featured projects (DFA, GSK, Entel Peru; three columns from 1024px, two from 768px); More projects (seven cards, newest first); a closing call-to-action band ("Let's talk about your next delivery challenge." with "Contact me"). Card anatomy per D-014 as amended; no uppercase line above the title. Still open: card summary wording and the Tigo card status.
- **D-029:** Project card labels, icons, and logos. Sector pill, tags, the method label (Agile or Waterfall, in gray, last in the row), and the year sit on one top row. Each sector pill has a small decorative outlined icon. Each card shows the employer's logo next to the company line: Endava (DCTX, DFA), TCS (Avianca, Tigo), and "Comverse (now Mavenir)" with the Mavenir logo for the telecom projects. GSK is a client, so its card has no logo. Logos come only from official brand files, never traced copies. In the build they are in `site/assets/img/logos/` (Endava and Mavenir in color, TCS in black, all from the companies' brand packs, with only the empty margins trimmed), shown above the company line with empty alt text.

## Open decisions (do not decide these alone)

Use clearly marked placeholders for any open content. Ask the Product Owner (Jairo) before finalizing:

- Capabilities: start from the five examples in `docs/00-foundation/04-website-strategy.md` (Capability Strategy). Revisit them later for alignment with the site's goal.
- Leadership principles: match the seven principles from the blueprint to each project story's decisions and reflections. A draft is in Obsidian (`docs/explore/drafts/leadership-principles-draft.md`); it is not approved.
- Story summaries (D-025): drafts are in Obsidian at `docs/explore/drafts/story-summaries-draft.md`; each needs Jairo's approval.
- Page redesigns: Career Journey, Contact, Leadership, and How I Can Help may change after Jairo's Artifacts designs. Build them only after the decision log records them.

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
- Do not commit or push without asking. Claude may keep this file up to date with the latest approved decisions and commit it (Jairo, 2026-10-28).
- The decision log and the rest of `docs/` belong to the Obsidian vault. Do not edit them from this repo.
