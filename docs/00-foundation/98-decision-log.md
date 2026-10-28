# Decision Log

Version: 1.0

---

# Purpose

Track all important strategic decisions taken during the engagement.

This document prevents future sessions from revisiting already approved decisions.

---

## D-001

Professional Vision approved.

"Helping organizations transform business ideas into successful technology solutions by connecting strategy, people, and execution."

Status

Approved

---

## D-002

The website is NOT a digital CV.

It is the authoritative professional reference.

Status

Approved

---

## D-003

Projects are the primary storytelling mechanism.

The website will present experience through business stories instead of job descriptions.

Status

Approved

---

## D-004

Timeline is part of the MVP.

However, it is secondary navigation.

Projects remain the primary exploration model.

Status

Approved

---

## D-005

Evidence precedes claims.

Every important statement should be supported by project experience, KPIs, leadership examples or measurable outcomes.

Status

Approved

---

## D-006

Leadership is one of the primary differentiators.

Leadership should be demonstrated through philosophy, principles and project stories.

Status

Approved

---

## D-007

The website focuses on recruiters and hiring managers.

Secondary audiences include Delivery Managers, Program Managers, CTOs, Technology Directors, consulting clients and internal Endava opportunities.

Status

Approved

---

## D-008

Explore Type selected:

Explore Readiness Check (ERC)

Status

Approved

---

## D-009

Signal completed before Explore.

No implementation work starts before Signal approval.

Status

Approved

---

## D-010

Foundation documents become the authoritative strategic context.

Future phases should extend these documents rather than replacing them.

Status

Approved


---

## D-011

Stack and hosting: plain HTML, CSS, and JavaScript with no build step, hosted on GitHub Pages. Revisit after the first draft is deployed; Astro or Next.js are options then.

Source: Q-13

Status

Approved

---

## D-012

Accessibility target: WCAG 2.1 Level AA.

Source: Q-15

Status

Approved

---

## D-013

Breakpoints: mobile-first. Tablet at 768px and desktop at 1024px. Projects shows one column on mobile and two from 768px. Test at 320px wide with no horizontal scrolling.

DEC-008A (breakpoints): closed by D-013.

Source: Q-15

Status

Approved

---

## D-014

Home Project Story previews: Entel Chile, GSK, and DFA Capital Markets, all confirmed as approved for publication.

Order, newest first: DFA Capital Markets (Endava, 2021–2025), GSK (TCS, 2017–2018), Entel Chile (Comverse, 2015).

Card fields, as approved on the new Projects design (Jairo, 2026-10-24): a sector pill and tags on the top row, with the year on the right; a short headline linked to the story page (the whole card is clickable); a "Client:" line; the company and role line; and one sentence on the main responsibility. The metric line and the Result block are removed from cards; the Result stays on the story pages. The card summary wording can be revisited later.

Source: Q-08 (closed); amended 2026-10-24 by Jairo's approval of the new card fields

Status

Approved

---

## D-015

Contact is a separate screen. Other screens route to it.

Status

Approved

---

## D-016

A minimal 404 page is included for GitHub Pages. It is a system page, not one of the eight visitor screens.

Status

Approved

---

## D-017

Publication eligibility is checked by a small validation script before deployment. The script checks that each Project Story has publication status "approved", that required sections are present, and that no placeholder markers (such as [UNKNOWN] or TBD) remain. It generates no pages, so the no-build-step rule still holds. Each story file needs a publication-status field.

Source: ADR-003

Status

Approved

---

## D-018

Repository layout: the public website lives in site/. docs/ stays in the repository but is not published. A GitHub Actions workflow deploys only site/ to GitHub Pages.

Status

Approved

---

## D-019

Website fonts: self-host Inter as woff2 files in site/assets/fonts/, with weights 400, 500, and 600. Keep the SIL Open Font License file next to the fonts. Load them with @font-face in site/assets/css/fonts.css using font-display: swap. Make no third-party font requests. Code text uses the system monospace stack and needs no font file.

Status

Approved

---

## D-020

Story page navigation (Q-09): an "On this page" list of jump links at the top moves between sections. Previous and Next links follow the Projects page order, and related stories come from each source file. Revoked in part by D-025 (2026-10-22): the rule that every section stays visible, and that collapsible sections are not used, no longer applies. The jump links and the Previous / Next order still apply.

Status

Approved (2026-10-20)

---

## D-021

Contact values (Q-10) approved: the email address, LinkedIn profile, and phone number shown on the Contact page. The phone number is not repeated here because the repository is public. The CV download is the current version, kept under its existing file name, and will be replaced when a final version is approved.

Source: Q-10

Status

Approved (2026-10-20)

---

## D-022

Home profile wording (Q-07) approved: the third-person positioning statement, the vision line, and the three profile summary paragraphs as shown on the Home page. Wording can be revisited later.

Source: Q-07

Status

Approved (2026-10-20)

%%Updated 2026-10-20: closes Q-07. Also updated in the PRD, HLD, boundary map, design sketch, and wireframes (open items closed, with comments in each file). CLAUDE.md in the project repo updated to match.%%
%%Updated 2026-10-24: years of experience is 15+ years as a Project Manager (Jairo's correction). The profile paragraph and the CV source still say "10+ years" and must be updated to match: the Home profile text (site) by code, and the CV source by Jairo in Obsidian.%%

---

## D-023

Decorative icons support section titles and project titles. They are not used in the top navigation. Icons are outlined, on a 24px grid, with a 1.75px stroke and rounded caps and joins, as the design language defines. They are hand-drawn inline SVG, marked decorative (hidden from screen readers), and never carry meaning alone. No icon library is adopted.

Source: design language (Iconography), approved by Jairo in chat on 2026-10-22

Status

Approved (2026-10-22)

%%Updated 2026-10-22: icon decision recorded. Left-side navigation remains a parked roadmap idea (99-product-roadmap.md) and is not approved.%%

---

## D-024

Career Journey shows a connected timeline, which is the visual form of D-004 (timeline as secondary navigation; Projects stay primary). Each role has a marker on one continuous line, with the years in bold. The entries run newest first. Projects appear as dated links inside the role they belong to. One accent color (blue) marks the markers and years; the color does not encode anything else. Detailed learning stays in Project Stories.

Source: D-004; 04-website-strategy.md (Timeline Strategy); approved by Jairo in chat on 2026-10-22

Status

Approved (2026-10-22)

%%Updated 2026-10-22: timeline visual approved. The side-stripe rule on Career Journey is replaced by the connected timeline (site commit fd88153).%%

---

## D-025

Project Story pages use expandable sections, with one section open at a time. Each section heading opens its text. When a reader opens a section, any section that was open closes, so the reader moves through the story one section at a time. No content is removed; every section is one click away. The "On this page" jump links and the Previous / Next order from D-020 stay in place. A jump link opens the section it points to and closes the others.

A short summary sits above the sections and is always visible. It says what the project is about and what it shows, for example how the leader handled third-party issues, or how the project dealt with difficult clients. The summary is written in first person, like the story narratives, and each summary is approved by Jairo before publication.

Each section heading has a disclosure triangle on its left. It points right when the section is closed and down when it is open (Jairo's choice, 2026-10-22). The triangle is decorative; the heading text is the control.

When the page loads, the first section of the story is open (for most stories, Business Problem or Business Challenge; for GT&T, Business Context; for Tigo, Scope of Responsibility). When the page is printed, all sections print expanded.

Not decided yet: whether an "expand all" control exists on screen (it conflicts with one open section at a time, so it is not part of this decision).

Source: Jairo in chat on 2026-10-22. The reason: the page's text is long and dense, and sections are easier to read when they can be opened one at a time. Revokes the visible-sections rule in D-020. The PRD's progressive-disclosure principle (R-004) supports this.

Status

Approved (2026-10-22)

%%Updated 2026-10-22: one-open-at-a-time expandable sections approved, revoking the visible-sections rule in D-020. Short always-visible summary added above the sections. First section open on load; print expands all sections (answered by Jairo, 2026-10-22). Only the on-screen "expand all" control remains undecided.%%

---

## D-026

Visual direction: option C, "soft professional." Pale blue page background (blue-50), white floating cards with a soft shadow, and teal (teal-700) for actions, links, icons, and the timeline markers. This amends the timeline accent in D-024 from blue to teal. The palette and type tokens do not change.

Source: Jairo in chat on 2026-10-22, choosing option C from the three previews.

Status

Approved (2026-10-22)

%%Updated 2026-10-22: look approved as option C. Icon and timeline accents change from blue to teal (teal-700), amending D-024.%%

---

## D-027

Visual direction: monochrome, after the devin.ai reference. The page is off-white (stone-50), cards are white, text and buttons are coal black (stone-900), secondary text is stone-600, and borders are stone-200. Supersedes the teal accent of D-026, and its amendment of D-024: icons, timeline markers and years follow the black action color. Placeholder and warning colors are unchanged.

Headings use Inter at regular weight (400). This supersedes the heading weight of 600 in the design language specification (B5); the typeface stays Inter under D-019.

Home has a two-column hero on desktop: name, positioning, vision, and two buttons on the left; Jairo's portrait on the right. On mobile the photo sits below the buttons. Hero buttons: "Let's talk" (black, to Contact) and "Download CV" (outlined, the D-021 file). The primary navigation keeps the link text "Contact" and shows it as a black pill. The footer keeps "Contact". All approved Home wording (D-022) is unchanged. The monochrome palette applies to Home.

Source: Jairo in chat, 2026-10-23 (reference images: devin.ai and two other examples; layout only, no content or photos from them).

Status

Approved (2026-10-23)

%%Updated 2026-10-23: monochrome direction recorded; supersedes D-026's teal accent and D-024's teal timeline; heading weight changed to 400 for this site.%%
%%Updated 2026-10-24: the Projects page colors are still open. Jairo will compare a monochrome option with the blue Option B using Artifacts. D-027 governs the rest of the site until he decides.%%

---

## D-028

Projects page layout (Option B, approved by Jairo, 2026-10-24). The page has a dark hero band with the title "Projects", an intro line, and three figures (KPIs): "15+ years leading software and infrastructure delivery", "5 industries", and "10+ projects, from on-site rollouts to cloud migrations". The "10+ projects" figure will grow as projects are added. Below the hero: Featured projects (three larger cards: DFA, GSK, Entel Peru), then More projects (seven cards, newest first), then a closing call-to-action band. Featured cards: three columns from 1024px, two columns from 768px to 1023px, one column below 768px. Cards are not all the same size; no equal-size rule is recorded in the decisions. Card anatomy is set by D-014 (amended 2026-10-24). The small uppercase line above the title is removed.

Not decided: the Projects page colors (see D-027 note). Card summary wording (revisit later). Tigo card status (revisit later). The closing call-to-action wording is a placeholder until Jairo approves it.

Reference: the approved Option B canvas is saved at `docs/explore/design/references/projects-option-b.dc.html`. Where its text or layout differs from this entry, this entry governs. Known differences to fix in the build: the featured row is one column from 768–1023px in the canvas (D-028 says two columns); the summaries say "about 60" and "about 25" where the sources say "approximately".

Source: Jairo in chat on 2026-10-24 (layout approved; featured row answer accepted; Artifacts used for the design comparison).

Status

Approved (2026-10-24), except the items listed as not decided

%%Updated 2026-10-24: Projects layout recorded as D-028. The featured row uses two columns from 768px, which is consistent with D-013 (two columns from 768px).%%
