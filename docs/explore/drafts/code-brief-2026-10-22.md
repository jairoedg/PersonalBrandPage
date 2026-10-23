# Code brief — apply decisions D-023 to D-026 (2026-10-22)

**From:** Jairo's planning chat. **To:** the code session working on `visual-design-pass`.
**Authority:** the decision log (`docs/00-foundation/98-decision-log.md`) is the record. Read D-017, D-020, D-023, D-024, D-025, and D-026 before you start. Do not change decisions; if something here conflicts with the log, stop and ask.

**Rules:** do not commit or push without Jairo's approval. Do not edit the token values in `site/assets/css/tokens.css`; put overrides in `base.css`. Keep the layout already checked; change the look only, except where D-025 asks for the expandable sections.

## 1. Look: option C, soft professional (D-026)

Apply these overrides in `site/assets/css/base.css`, after the token file is loaded. Values come from the option C preview.

```css
:root {
  --color-surface-background: var(--blue-50);
  --color-surface-card: #ffffff;
  --color-action-primary: var(--teal-700);
  --color-text-link: var(--teal-700);
  --color-border-default: var(--blue-100);
}
.story-card { border-color: transparent; border-radius: 12px; box-shadow: var(--elevation-floating); }
.heading-icon { color: var(--teal-700); }
```

- Timeline markers and years (D-024, amended by D-026) use teal-700, not blue.
- Check text contrast on blue-50 and on the teal links (WCAG 2.1 AA, D-012).
- Preview: option C was previewed at `http://localhost:8766/opt-c/index.html` while the preview server was running. It is not kept; use the CSS above.

## 2. Expandable story sections (D-025)

- On Project Story pages, each main section (the `h2` headings from Business Context to Professional Evolution) becomes an expandable section.
- Each section heading has a disclosure triangle on its left: right when closed, down when open. The triangle is decorative; the heading text is the control.
- **One open at a time.** Opening a section closes the one that was open. Use one shared group name (for example native `<details name="…">`, or equivalent script). Do not allow two open at once.
- A short summary sits above the sections and is always visible. It is written in first person and approved by Jairo; use the drafts in `docs/explore/drafts/story-summaries-draft.md` once approved. Until then, show no summary text that is not approved.
- Keep the "On this page" jump links. A jump link must open its section, close the others, and move focus to the section heading. A browser does not open a closed section by itself.
- Keep Previous and Next exactly as they are (Projects order).
- Keyboard: Enter and Space toggle a section; the heading shows its state; visible focus stays (D-012).
- **Decided on open state (answered by Jairo, 2026-10-22):**
  - The first section of each story is open on load. It is Business Problem or Business Challenge for most stories, Business Context for GT&T, and Scope of Responsibility for Tigo. Use the first `h2` section after "On this page".
  - Printing expands all sections.
- **Not decided:** an on-screen "expand all" control. Do not add it. It conflicts with one-open-at-a-time.

## 3. Icons and timeline

- Icons (D-023) stay on section and project titles, not in the top navigation. Only the color changes, to teal (section 1).
- The timeline (D-024) keeps its current layout. Only the accent changes.

## 4. Documentation and project file

- `CLAUDE.md` has been updated in the project folder (uncommitted). Review it with the code change, and keep it in sync with the decision log.
- The `CLAUDE.md` Next list had a broken line break; it is fixed in the working copy.

## 5. Deploy gate (D-017)

- Commit `e868b11` lets placeholder warnings pass on a manual deploy. D-017 says no placeholder markers may remain before publication.
- Proposed change, for Jairo to approve before it is made: make `scripts/check_site.py` fail on placeholder markers (for example a `--strict` flag), remove the allowance from `.github/workflows/deploy-pages.yml`, and update `.claude/skills/site-cicd/SKILL.md` to match.
- The site will not deploy until the placeholders are replaced with approved content. That is intended.

## 6. Checks to run and report back

- `python3 scripts/check_site.py` (expect 0 errors and the placeholder warnings until the content is filled).
- The Impeccable detector on `site/`.
- Screenshots at 320, 375, 768, and 1280px for Home, Projects, one Project Story, and Career Journey. Confirm no sideways scrolling.
- Keyboard pass on a Project Story: one section open at a time, jump links open their section, focus is visible.
- Report which open questions in section 2 are still waiting for Jairo.

## Content still needed from Jairo (not for code to write)

- Story text for Tigo (leadership sections), GT&T (decisions section), and Digicel (decisions section).
- The leadership principles and the How I Can Help content, when approved. The draft is in `docs/explore/drafts/leadership-principles-draft.md`.
