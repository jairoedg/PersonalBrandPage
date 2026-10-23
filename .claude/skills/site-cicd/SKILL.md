---
name: site-cicd
description: Use for any change to the static site in site/, before committing or pushing, and for anything about deploying it to GitHub Pages (the check script, the deploy workflow, git rules for this repo).
---

# Site CI/CD

This repo publishes the static site in `site/` to GitHub Pages. Decisions that drive this skill: D-011, D-017, D-018 (see `docs/00-foundation/98-decision-log.md`, read-only). Read-only means never edit that file.

## Before every push

1. Run the check script from the repo root:

   ```bash
   python3 scripts/check_site.py
   ```

2. **Stop** if it reports any ERROR.
3. **Stop** if it reports a placeholder or draft marker that is meant to be removed. Warnings about placeholders are expected while the open decisions (Q-07, Q-08 and the others in `CLAUDE.md`) remain. Report them, do not hide them. Do not remove or fill a placeholder to make the check pass.
4. Show the result to Jairo before pushing.

## Git rules

- Commit in small steps with clear messages. Each commit does one thing.
- **Never push without Jairo's approval.** Approval for one push does not carry to the next.
- **Never commit `docs/` edits from this folder.** The Obsidian vault owns `docs/`. Only `site/`, `scripts/`, `.github/`, and `.claude/skills/` are in scope for this project.
- Do not commit `CLAUDE.md` or `.claude/settings.local.json` unless Jairo asks.
- Identity for this repo is set locally: `Jairo Enrique Diaz <63517475+jairoedg@users.noreply.github.com>`. Do not change it.
- Commit trailer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Deployment

- Workflow: `.github/workflows/deploy-pages.yml`. It publishes only `site/` (D-018).
- **Manual trigger only** (`workflow_dispatch`). A push to `main` never deploys. This is deliberate: a public site with "Placeholder" labels must not go out by accident.
- Two jobs:
  - `validate` runs `scripts/check_site.py --strict`. Any error fails the run and blocks the deploy. With `--strict`, every placeholder or draft marker is an error (D-017), so the deploy is blocked until each one is replaced with approved content.
  - `deploy` uploads `site/` and publishes it to Pages. It runs only after `validate` passes.
- To run it, Jairo starts it from the GitHub Actions tab ("Run workflow"). Do not start it yourself unless Jairo asks in this chat for that specific run.
- Going live requires all three: every placeholder replaced, `scripts/check_site.py --strict` reporting 0 errors, and Jairo's explicit approval for that run.
- Local runs without `--strict` keep reporting placeholders as warnings. Run `python3 scripts/check_site.py --strict` to preview the deploy gate.

## One-time setup (Jairo does this, not Claude)

- Repo settings → Pages → Build and deployment → Source: **GitHub Actions**.
- The repo stays public. Pages is free on a public repo with the free GitHub plan, which is why the repo is public for the MVP.

## Testing the pipeline

- Pushing the workflow does not deploy.
- A manual run fails at the placeholder gate while any placeholder remains. That failure is the expected result until the content is approved, and it proves the gate works. Start a run only when Jairo asks for that specific run.
