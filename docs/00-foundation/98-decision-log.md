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

Source: Q-15

Status

Approved

---

## D-014

Home Project Story previews: Entel Chile, GSK, and DFA Capital Markets, all confirmed as approved for publication.

Order, newest first: DFA Capital Markets (Endava, 2021–2025), GSK (TCS, 2017–2018), Entel Chile (Comverse, 2015). Summary fields remain open.

Source: Q-08 (partial)

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
