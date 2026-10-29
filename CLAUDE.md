# CLAUDE.md — Personal Brand Page

Read this file first. It explains which documents are authoritative, what is still open, and how to work in this repo.

## Project

A personal portfolio website for Jairo Enrique Diaz, a Project Manager. It presents professional evidence (Project Stories), leadership, and contact paths. The site is a static frontend MVP, meant for production as soon as possible.

## Current status

- Signal: complete.
- Explore: complete (PRD, HLD, ADRs, epics, design, and architecture approved).
- Govern (implementation): started by this repo. Implementation work happens here.
- First draft: complete. Home, Projects, ten Project Story pages, About, Career Journey, How I Can Help (placeholders), Leadership (placeholders), Contact, and the 404 page are built in `site/`.
- Checks: `scripts/check_site.py` passes with 0 errors. The 15 warnings are the expected placeholders: the ten story summaries (D-025), the page introductions, Home's "Explore more" lines, and Leadership and How I Can Help content. `--strict` (the deploy gate) fails until every one is replaced.
- Impeccable detector (`.claude/skills/impeccable/scripts/impeccable detect --json site`): 0 findings. Measured false positives are recorded as scoped exceptions in `.impeccable/config.json`.
- Repository: public. GitHub Pages source is GitHub Actions. Nothing is deployed yet.
- Git: PRs #1 to #3 and #5 to #12 are merged into `main`. They hold the Impeccable skill, the deploy workflow and placeholder gate, expandable story sections, the monochrome Home with the photo hero, the Projects page (D-028), Leadership (D-030), How I Can Help (D-031), and Career Journey (D-032) with its follow-up fixes, About (D-033), and Contact (D-034).
- Look (2026-10-29): Home is fully monochrome (`.theme-mono` on its `<body>`). Every other page uses the monochrome base with one blue accent (D-027 as amended). About (D-033) opens with a light gray band (stone-200) and a credential card grid. Projects, Leadership (D-030), How I Can Help (D-031), Career Journey (D-032), and Contact (D-034) open with a dark band; on Contact the band holds the whole page and meets the footer. The shared light page header is retired. Project Stories (D-035) open with the header and "The story in 60 seconds" chapter buttons, then the selected chapter as numbered white cards.
- Next, in order:
  1. Jairo completes the missing story text: Tigo (leadership sections), GT&T (decisions section), and Digicel (decisions section).
  2. Text pass: the chapter-button texts (D-035) where Jairo edits them, story summaries (D-025), shorter card summaries, and page introductions, each approved by Jairo.
  3. Leadership and How I Can Help content, when Jairo approves it. The leadership draft is in Obsidian at `docs/explore/drafts/leadership-principles-draft.md` and is not approved.
  4. Deploy only after design, text, and final review are approved, and with no placeholders left on the site (D-017).

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
- **D-020 (Q-09 closed; partly revoked by D-025; the "On this page" list is superseded by D-035):** an "On this page" list of jump links moves between sections. Previous and Next follow the Projects page order; related stories come from each source file. The rule that every section stays visible is revoked.
- **D-022 (Q-07 closed):** Home profile wording approved: the third-person positioning statement, the vision line, and the profile summary paragraphs on the Home page. Wording can be revisited later.
- **D-021 (Q-10 closed):** the contact values (email, LinkedIn, phone) on `site/contact/index.html` are approved. The CV download is `site/assets/cv/CV_JairoDiaz - Project Manager.pdf`, kept under its existing name (spaces encoded as `%20` in links) and replaced when a final version is approved. Don't copy the phone number into docs or this file; the repository is public.
- **D-023:** decorative icons on section and project titles, not in the top navigation. Hand-drawn inline SVG: outlined, 24px grid, 1.75px stroke, `aria-hidden`, never the only label. No icon library.
- **D-024 (superseded in form by D-032):** the Career Journey timeline (the visual form of D-004): one continuous line, a marker per role, bold years, newest first, and projects as dated links inside their role. Its accent follows D-027 (blue; black on Home).
- **D-025 (the accordion is superseded by D-035; the summary rule stays):** story pages use expandable sections, one open at a time. Opening a section closes the one that was open. A short summary above the sections is always visible; it is first person, and Jairo approves each one. Each section heading has a disclosure triangle (right when closed, down when open). The first section of each story is open on load, and printed pages expand all sections. "Expand all" on screen is not part of this decision.
- **D-026:** option C teal look. Superseded by D-027.
- **D-027 (amended 2026-10-28):** monochrome base after devin.ai: stone-50 page, white cards, coal-black (stone-900) text and buttons, stone-600 secondary text, stone-200 borders. Home stays fully monochrome, with a two-column hero (name, positioning, vision, "Let's talk" and "Download CV" buttons; the portrait on the right, below the buttons on mobile). The Primary nav shows "Contact" as a black pill. Other pages add one blue accent: blue-700 for links, icons, and focus; blue-50 or blue-100 for tinted surfaces; blue sector labels on Project cards. Other hues only where they carry a meaning that is also written as text. Placeholder and warning colors are unchanged. Inter stays (D-019). H1 and H2 use weight 400; H3 and smaller headings use 600.
- **D-028:** Projects page (Option B), colors per D-027: dark band with "Projects", the intro line ("I love making projects succeed, using both Agile and Waterfall across different markets."), and three key figures; Featured projects (DFA, GSK, Entel Peru; three columns from 1024px, two from 768px); More projects (seven cards, newest first); a closing call-to-action band ("Let's talk about your next delivery challenge." with "Contact me"). Card anatomy per D-014 as amended; no uppercase line above the title. Still open: card summary wording and the Tigo card status.
- **D-029:** Project card labels, icons, and logos. Sector pill, tags, the method label (Agile or Waterfall, in gray, last in the row), and the year sit on one top row. Each sector pill has a small decorative outlined icon. Each card shows a logo with the company line: Endava (DCTX, DFA), TCS (Avianca, Tigo), "Comverse (now Mavenir)" with the Mavenir logo for the telecom projects, and GSK's own logo on the GSK card (D-029 as fixed 2026-10-28). Logos come only from official brand files, never traced copies. In the build (`site/assets/img/logos/`) they are symbol only, at Jairo's request: the Endava symbol from its brand pack, the TCS "tcs" mark taken from the official black logo file, and the GSK mark from its official PNG. Mavenir has no separate symbol, so its wordmark is used. Logos sit above the company line with empty alt text.
- **D-030 (built on branch `leadership-d030`):** Leadership layout "LeadershipLedger": a dark band with the title, the lead line, and the philosophy (with a visually hidden "Leadership philosophy" H2 for the outline); seven numbered principles (`.ledger`) with an evidence slot (right of the principle from 768px); then "How I lead" and a "Continue exploring" closing band. Evidence and "How I lead" stay placeholders.
- **D-031 (built on branch `help-d031`):** How I Can Help layout "HelpIndexRows": a dark band with title and intro; five numbered capability rows (`.capability`), each with a proof panel (`.proof`, heading "Proof in Project Stories" plus the story count) listing related stories in two columns (an odd last story spans both; one column below 768px). Intro and explanations stay placeholders.
- **D-032 (built on branch `journey-d032`):** Career Journey layout "JourneyOverview", amending D-024: a dark band; a "Roles at a glance, 2011–2026" span chart (`.span-chart`; one accent color, bar positions from the role months, text beside each bar); "Roles by company" panels (Endava, TCS, Comverse / Mavenir) as native `<details>`, several open at once, Endava and DCTX open on load. Each role keeps all highlights and achievements; each Project Story item shows the approved card summary. `site/assets/js/print-details.js` opens every panel for printing.
- **D-033 (built on branch `about-d033`):** About layout "AboutGray": a light gray header band (stone-200) on About only (Contact keeps the shared `.page-header`), with the title and "Based in Cali, Colombia." plus a decorative pin on the left and the professional summary on the right (below on mobile), approved by Jairo 2026-10-29. Then a card grid: Education and Languages (level as text plus a decorative five-dot meter) on the left, Certifications in a blue-tinted card on the right, and Courses and professional development full width (two columns from 768px). Then "Continue exploring". No photo; all credential content unchanged.
- **D-034 (built on branch `contact-d034`):** Contact layout "ContactSplit": a dark band (the Projects `page-band`) replaces the shared light page header, split in two from 1024px. Left: the `<h1>` "Contact", visually hidden at Jairo's request (2026-10-29), the D-028 closing line "Let's talk about your next delivery challenge." at display size, and the intro placeholder. Right: a white "Ways to reach me" panel with one clickable row each for Email, LinkedIn (external icon and "opens the LinkedIn website") and Phone, and the CV with a "Download CV (PDF)" button at the bottom. No "Continue exploring" on Contact; the footer keeps the navigation. Contact values and the CV file are unchanged (D-021).
- **D-035 (built on branch `stories-d035`):** Project Story layout "StoryChaptersBrief", for all ten stories. Sections are grouped into four chapters (01 The situation, 02 What I did, 03 The outcome, 04 What I learned; mapping by section name, each story's order kept inside a chapter). "The story in 60 seconds" shows the chapters as large buttons (number, reading time at 200 words a minute, title, a verbatim summary, "Read this part ↓"); the selected one is coal black and only its chapter shows. Sections are numbered cards (two per row from 1024px); numbered sub-headings become one card per item. The existing intro paragraphs become the "Overview" card; the Outcome line moves into button 03. `site/assets/js/story-chapters.js` makes real tabs; without JavaScript and in print every chapter shows. The button texts are in Obsidian at `docs/explore/drafts/story-chapter-summaries-draft.md`. `check_site.py` keeps each story's word count in `STORY_WORDS`; update it only when Jairo changes story text.
- Reference for D-030 to D-035: the Design System artifact "Jairo Diaz — Subpage Designs" (https://claude.ai/artifact/AiTJdhwH6v1YXAJVmYN6Ke). Where it differs from the log, the log governs.

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
