
Branch: visual-design-pass. Read CLAUDE.md first. The decision log in Obsidian (docs/00-foundation/98-decision-log.md) is the record, and the full brief is at docs/explore/drafts/code-brief-2026-10-22.md in the vault. Do not change decisions. If something conflicts with the log, stop and ask. Do not commit or push without approval.

1. Look, option C (D-026)
- Apply the overrides in site/assets/css/base.css, not in tokens.css:
  page background blue-50; white cards (#ffffff) with radius 12px and elevation-floating; teal-700 for actions, links, icons, and timeline markers and years; border-default blue-100.
- Check text contrast against WCAG 2.1 AA.

2. Expandable story sections (D-025)
- Each h2 section on a Project Story page becomes an accordion section. The heading is the control (button with aria-expanded and aria-controls).
- A disclosure triangle sits on the left of each heading: right when closed, down when open. It is decorative (aria-hidden).
- Only one section is open at a time. Opening one closes the others.
- On load, open the first section of each story: Business Problem or Business Challenge for most stories, Business Context for GT&T, Scope of Responsibility for Tigo.
- The "On this page" jump links open their section, close the others, and move focus to the heading.
- Previous and Next stay as they are.
- Printing expands all sections.
- No on-screen "expand all" control.
- Keyboard: Enter and Space toggle a section; focus stays visible. Propose a fallback for users without JavaScript and report it.
- Summary block above the sections: always visible. Until Jairo approves the text, show a clearly marked slot such as "[Summary pending approval]". Do not publish unapproved text. Drafts: docs/explore/drafts/story-summaries-draft.md.

3. Accents (D-023, D-024 amended by D-026)
- Section icons and the Career Journey timeline use teal. Change the accent only; keep the layout.

4. Deploy gate (D-017)
- scripts/check_site.py must fail on placeholder markers when it runs for deployment. Add a --strict flag that the deploy workflow uses. Keep local runs warning-only.
- Remove the placeholder allowance from .github/workflows/deploy-pages.yml (added in e868b11), and update .claude/skills/site-cicd/SKILL.md to match.
- The deploy will fail until the placeholders are replaced with approved content. That is intended.

5. Checks and report back
- python3 scripts/check_site.py; the Impeccable detector on site/.
- Screenshots at 320, 375, 768, and 1280px: Home, Projects, one story with its first section open, and Career Journey. Confirm no sideways scrolling.
- Keyboard pass on a story: one section open at a time; jump links open their section; focus is visible.
- Report results per item, and list anything still open.

Not for code: the Tigo, GT&T, and Digicel story text; approval of the summaries; the Leadership and How I Can Help content; the text pass.