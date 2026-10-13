---
name: release
description: Release a new version of the Kaltura design system (vX.Y). Use when the user asks to release the DS, cut a release, ship a new version, or publish the unreleased changes. Not for editing components.
---

# Release the DS

Follow the steps in order. Stop and tell the user as soon as a step fails; never skip a check to keep going. The rules in `CLAUDE.md` ("Releasing") are the source of truth; this skill is the procedure.

Hard rules: never modify an existing `releases/vX.Y/` folder, never reuse a version number, never use `--no-verify` or force-push, and never push before the check in step 6 passes.

## 1. Preflight
Run `git branch --show-current`, `git status --porcelain`, and `git fetch origin && git status -sb`.
- Must be on `main`, with an empty `git status --porcelain` (clean tree, no untracked files other than ignored ones). Otherwise stop and tell the user what is dirty; do not stash, reset or commit for them.
- If `main` is behind `origin/main`, stop and tell the user. (Ahead is fine.)
- Read `releases/latest.txt` (current version, e.g. `v1.0`) and confirm that folder exists.

## 2. Summarize what is unreleased
Read the `## Unreleased` section of `CHANGELOG.md`.
- If it is missing or empty, stop: there is nothing to release.
- Show the user a short summary grouped as: Changed (behavior), Added, Fixed, Removed. Call out anything a prototype could notice.
- Sanity-check it against reality: `diff` the working `styles.css` / `ds.js` against `releases/<latest>/`. If the code changed in a way the changelog does not mention, say so and ask whether to add it before releasing.

## 3. Propose a version and wait
Compare with the latest version `vA.B`:
- **Minor** (`vA.(B+1)`): additions and fixes only. Existing markup, classes and behavior keep working.
- **Major** (`v(A+1).0`): any renamed or removed class, removed or renamed icon, changed markup, or changed behavior that could break a prototype (for example a modal no longer closing on Escape).
- When unsure, pick major and say why.

Tell the user the proposed version and the reason in one or two sentences, then **stop and wait for an explicit confirmation** (or a different version). Do not touch any file before they answer. Use their answer as `vX.Y` below. Refuse a version whose folder already exists.

## 4. Do every release step (all in the working tree, one commit later)
Replace `X.Y` with the confirmed version.
1. `python3 tools/bundle-icons.py`
2. In `ds.js`, set `version: 'X.Y.0'` in `window.DS` (a minor release `v1.1` is `'1.1.0'`). Update the version mention in any file header comment if there is one.
3. `python3 tools/build-guide.py` to refresh the guide's version, tokens and icon lists. Then read the hand-written sections of `DS-GUIDE.md` against what the Unreleased changelog says changed (markup, variants, states, events, `window.DS`, modal behavior, new components) and fix anything stale. A component that is new or changed must be correct in the guide. Check that every `ds-` class named in the guide exists in `styles.css`.
4. `mkdir releases/vX.Y` and copy `styles.css`, `ds.js`, `ds-icons.js`, `DS-GUIDE.md` into it, unchanged, with `cp`. The folder contains exactly those four files. Then `cmp` each file against the working copy; they must be identical.
5. `CHANGELOG.md`: rename the `## Unreleased ...` heading to `## vX.Y (YYYY-MM-DD)` using today's date, keep the entries as they are (add a "could break a prototype" note for a major version), and put a new empty `## Unreleased` heading above it.
6. `echo vX.Y > releases/latest.txt`

## 5. Point the test page at the new release
In `test-prototype.html`, change the three tag paths and the `<title>` from the old `releases/vA.B/` to `releases/vX.Y/` so it links ONLY the new release (check with `grep -n "releases/" test-prototype.html`: every hit must be `vX.Y`). If the release changed markup that the test page uses (for example the modal), update the test page's markup to match the new `DS-GUIDE.md`; it should be a faithful example of a prototype built from that guide.

## 6. Verify in a browser
Open `test-prototype.html` straight from disk (`open test-prototype.html`; it must work over `file://`) and check:
- the browser console shows **no errors and no warnings** from `[DS]` (for example an unknown icon);
- the button, the `ds-icon`s, the select (open, pick an item, arrow keys, Escape), the tabs (click and arrow keys), and the modal (opens, focus trapped, closes the way the new `DS-GUIDE.md` says; for a static modal check that the backdrop click and Escape do NOT close it, and Cancel does) all work;
- `DS.version` in the console equals `X.Y.0`.

Also open `index.html` and check the console is clean and the theme toggle works in both themes.

You can only claim a check passed if you actually ran it. A headless browser is fine if one is available (for example `npx playwright` installed outside the repo, in `/tmp`; never add npm files to this repo): load `file:///.../test-prototype.html`, collect `console` and `pageerror` events, and drive the components. If you cannot run a browser, say so plainly, open the page for the user, list exactly what to click, and wait for their confirmation before step 7.

If any check fails, stop. Report what failed. Do not commit or push; leave the working tree for the user to inspect.

## 7. Commit and push
- `git status` should show only: the new `releases/vX.Y/`, `releases/latest.txt`, `CHANGELOG.md`, `ds.js` (version bump), `ds-icons.js` (only if the icons changed), `DS-GUIDE.md`, and `test-prototype.html`. The tree was clean at step 1, so anything else is unexpected: stop and ask.
- Confirm `git diff -- releases/` shows no change to any older release folder.
- Stage those files by name (not `git add -A`), then commit with exactly the message `Release vX.Y`:
  `git commit -m "Release vX.Y"`
- `git push origin main`. If the push is rejected, stop and report; do not force-push.
- Finish with: the version released, the commit hash, and one line on how a prototype repo fetches it (`releases/vX.Y/` from the GitHub repo into its `ds/` folder).
