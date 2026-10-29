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

Headings use Inter. H1 and H2 use regular weight (400); H3 and smaller headings stay at 600, so they still stand apart from body text. This supersedes the heading weight of 600 in the design language specification (B5) for H1 and H2 only; the typeface stays Inter under D-019.

Home has a two-column hero on desktop: name, positioning, vision, and two buttons on the left; Jairo's portrait on the right. On mobile the photo sits below the buttons. Hero buttons: "Let's talk" (black, to Contact) and "Download CV" (outlined, the D-021 file). The primary navigation keeps the link text "Contact" and shows it as a black pill. The footer keeps "Contact". All approved Home wording (D-022) is unchanged. The monochrome palette applies to Home.

Amended 2026-10-28 (Jairo in chat): the other pages may use color. Each page keeps the monochrome base, and adds one accent from the design-language blue scale: blue-700 for text, links, and focus, and blue-50 or blue-100 for tinted surfaces. Sector labels on Project cards keep their blue colors. Other palette hues may be used only where they carry meaning, such as a category or a status, and that meaning is always also written as text, so color is never the only cue. Text contrast meets WCAG 2.1 AA on every surface. Heading weight (400), the coal-black action color for buttons, and the placeholder and warning colors are unchanged.

Source: Jairo in chat, 2026-10-23 (reference images: devin.ai and two other examples; layout only, no content or photos from them).

Status

Approved (2026-10-23)

%%Updated 2026-10-23: monochrome direction recorded; supersedes D-026's teal accent and D-024's teal timeline; heading weight changed to 400 for this site.%%
%%Updated 2026-10-24: the Projects page colors are still open. Jairo will compare a monochrome option with the blue Option B using Artifacts. D-027 governs the rest of the site until he decides.%%
%%Amended 2026-10-28: Jairo decided to allow color on pages other than Home. Home stays monochrome. The Projects page may use the blue accent, pending the Artifacts comparison.%%
%%Updated 2026-10-28: the Projects page colors are decided. Projects follows the amended rule: monochrome base with the blue accent, like every page except Home. This closes the 2026-10-24 note. Heading weight clarified: H1 and H2 at 400, H3 and smaller at 600, as built.%%

---

## D-028

Projects page layout (Option B, approved by Jairo, 2026-10-24). The page has a dark hero band with the title "Projects", an intro line, and three figures (KPIs): "15+ years leading software and infrastructure delivery", "5 industries", and "10+ projects, from on-site rollouts to cloud migrations". The "10+ projects" figure will grow as projects are added. Below the hero: Featured projects (three larger cards: DFA, GSK, Entel Peru), then More projects (seven cards, newest first), then a closing call-to-action band. Featured cards: three columns from 1024px, two columns from 768px to 1023px, one column below 768px. Cards are not all the same size; no equal-size rule is recorded in the decisions. Card anatomy is set by D-014 (amended 2026-10-24). The small uppercase line above the title is removed. The intro line reads "I love making projects succeed, using both Agile and Waterfall across different markets." The closing band reads "Let’s talk about your next delivery challenge." with a "Contact me" button to Contact.

Not decided: card summary wording (revisit later). Tigo card status (revisit later).

Reference: the approved Option B canvas is saved at `docs/explore/design/references/projects-option-b.dc.html`. Where its text or layout differs from this entry, this entry governs. Known differences to fix in the build: the featured row is one column from 768–1023px in the canvas (D-028 says two columns); the summaries say "about 60" and "about 25" where the sources say "approximately".

Source: Jairo in chat on 2026-10-24 (layout approved; featured row answer accepted; Artifacts used for the design comparison).

Status

Approved (2026-10-24), except the items listed as not decided

%%Updated 2026-10-24: Projects layout recorded as D-028. The featured row uses two columns from 768px, which is consistent with D-013 (two columns from 768px).%%
%%Updated 2026-10-28: Projects colors decided (D-027 amendment). Closing band wording approved ("Let’s talk about your next delivery challenge." with "Contact me"), and intro line recorded. Remaining open items: card summary wording and Tigo card status.%%

---

## D-029

Project card labels, icons, and logos (Projects page, Option B; Jairo in chat, 2026-10-28). Extends D-014 and D-023.

Labels: each card shows a sector pill, tags, and the year on one top row, aligned together. The method label (Agile or Waterfall) sits in the same row, in a gray tone. No label sits on the card edge. Tags stay outlined, in the current style. Labels use the Inter typeface only; no handwritten or script font is used (D-019).

Sector icons: each sector pill carries a small outlined icon, hand-drawn inline SVG on the 24px grid, decorative and hidden from screen readers (D-023).

Company logos: each card shows the logo of the employer for that project, next to the company line. Endava (DCTX, DFA) and TCS (Avianca, Tigo) use their logos. Telecom projects delivered at Comverse are shown as "Comverse (now Mavenir)," with the Mavenir logo. GSK is a client, so logo is also important to be added. Logos must come from the company's official brand files, never from traced or approximated copies. Until the official files are supplied, the card shows a labeled placeholder.

Source: Jairo in chat, 2026-10-28 (label placement, icons, Comverse naming, GSK as client).

Status

Approved (2026-10-28)

---

## D-030

Leadership page layout (Jairo, 2026-10-29, option "LeadershipLedger", no changes). A dark band, in the same style as the Projects hero (D-028), holds the title "Leadership", the lead line "Projects succeed because people succeed.", and the leadership philosophy paragraphs. Below the band, the seven leadership principles form a numbered list: a large decorative numeral (01 to 07), the principle as a heading, and an evidence slot. The evidence slot sits to the right of the principle from 768px and below it on smaller screens. Then come "How I lead" and "Continue exploring".

The principle wording and the philosophy text are unchanged. The evidence slots and "How I lead" stay labeled placeholders until Jairo matches each principle to Project Stories (open decision: Leadership principles). Numerals are decorative; the list itself carries the order. Heading weights follow D-027 (H1 and H2 at 400; H3 and smaller at 600). The page uses the blue accent allowed by the D-027 amendment.

Reference: Design System artifact "Jairo Diaz — Subpage Designs", component LeadershipLedger ([Jairo Diaz — Subpage Designs](https://claude.ai/artifact/AiTJdhwH6v1YXAJVmYN6Ke)). Where the reference differs from this entry, this entry governs.

Source: Jairo, comment on the Design System artifact, 2026-10-29 ("I select this design for leadership (leadershipLedger). No changes needed.").

Status

Approved (2026-10-29)

---

## D-031

How I Can Help page layout (Jairo, 2026-10-29, option "HelpIndexRows"). A dark band holds the title "How I Can Help" and the page introduction. Below the band, the five capabilities are numbered rows. On the left: a large decorative numeral, the capability title, and its short explanation underneath. On the right: a proof panel with a tinted header "Proof in Project Stories" and the number of stories, followed by the related Project Stories in a two-column grid. Each story shows the company name, the story subtitle, and a decorative arrow, and links to its story page. With an odd number of stories, the last one spans both columns. Below 768px, the panel sits under the text and its stories run in one column.

The capability names and their related Project Stories are unchanged. The page introduction and the five explanations stay labeled placeholders until Jairo approves them (open decision: Capabilities). The story count is part of the panel heading text, so it is not conveyed by color. Heading weights follow D-027.

Reference: Design System artifact, component HelpIndexRows. Where the reference differs from this entry, this entry governs.

Source: Jairo, comment on the Design System artifact, 2026-10-29 (option selected; right side reworked to remove the empty space and balance the row).

Status

Approved (2026-10-29)

---

## D-032

Career Journey page layout (Jairo, 2026-10-29, option "JourneyOverview"). Amends D-024. A dark band holds the title "Career Journey" and the introduction. Below the band:

1. A span chart, "Roles at a glance, 2011–2026", with one bar per role, newest first. Every bar uses the one accent color; color encodes nothing. The company, role, and years are written beside each bar, so the chart does not rely on the bars. On mobile the text sits above each bar. The chart remains the timeline view that D-004 calls for.
2. "Roles by company": one expandable panel per employer (Endava, TCS, Comverse / Mavenir), newest first. Each panel heading shows the employer, the years, and the number of roles and Project Stories. When a panel opens, its roles are visible at once (there is no third level). Each role keeps its title, company line, dates, highlights, and achievements; Endava's achievements also appear as three figures (stakeholder satisfaction 5.0 to 8.7, gross margin above 30% in FY22 and FY23, recognized as a top performer). Inside each role, every Project Story is an expandable item with its dates, its approved card summary (D-014), and a "Read the Project Story" link.

Several panels can be open at the same time (confirmed by Jairo, 2026-10-29). When the page loads, Endava and its newest Project Story are open. The disclosure triangle follows D-025: it points right when closed and down when open; the heading text is the control. When the page is printed, all panels print expanded.

From D-024, the following still apply: entries run newest first, projects appear inside the role they belong to, and detailed learning stays in Project Stories. The connected timeline line and markers are replaced. The introduction stays a labeled placeholder until Jairo approves it. Heading weights follow D-027.

Reference: Design System artifact, component JourneyOverview. Where the reference differs from this entry, this entry governs.

Source: Jairo, comments on the Design System artifact, 2026-10-29 (one color for all bars; group by company with expandable projects; option selected; several panels open confirmed in chat).

Status

Approved (2026-10-29)

%%Updated 2026-10-29: Career Journey layout recorded. Supersedes the timeline form in D-024.%%