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

Order, newest first: DFA Capital Markets (Endava, 2021–2025), GSK (TCS, 2017–2018), Entel Chile (Comverse, 2015). Summary text and fields on the Home and Projects cards are approved. The wording can be revisited later.

Source: Q-08 (closed)

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

Story page navigation (Q-09): every section of a Project Story page stays visible. An "On this page" list of jump links at the top moves between sections. Previous and Next links follow the Projects page order, and related stories come from each source file. Collapsible sections are not used for now and can be revisited later.

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
