# Design System (ds/) - rules for working on the DS

This folder is the design system itself. Prototypes link its files from a hosted URL.
(The parent folder's CLAUDE.md is about building pages *with* the DS; this one is about changing the DS.)

## Hard rules
- **Plain HTML, CSS and JS only.** No npm, no frameworks, no bundler, no build step.
- **Everything must work by opening a file directly in the browser (`file://`).** So: classic `<script>` tags (never `type="module"`), no `fetch()`, no `import`. Icons are bundled into `ds-icons.js` for this reason.
- **Components use tokens only, never raw values.** Colors, spacing, font sizes and weights, line heights, radius, shadows, durations and z-index all come from `--ds-*` variables defined in `:root` in `styles.css`. If a value has no token, add one first, then use it. Structural dimensions (a 32px button height, border widths, `50%` radius) may stay literal.
- **Do not change how existing components look.** Existing `ds-` class names and markup must keep working, because prototypes already use them.

## Where things go
| The component... | Put it in |
|---|---|
| has no behavior | CSS classes in `styles.css` plus documented markup on `index.html` |
| has behavior | logic in `ds.js` using **event delegation on `document`** (no per-element init, no inline `onclick`), or a web component |
| needs an icon | `<ds-icon name="..." size="16|24">`, never pasted SVG (one-off decorative shapes that are not in the icon set may stay inline) |

Behavior conventions in `ds.js`:
- Fire a bubbling `ds-change` `CustomEvent` with `detail: { value, label }` when a user changes a value.
- Keyboard support is part of the component: Escape closes, arrows move, Enter and Space select.
- Components added to the page later must work with no extra call.
- Expose public functions on `window.DS` only; keep everything else inside the IIFE.

## Every component must appear on `index.html`
Add a section with live examples (all variants and states) **and a usage snippet**. Update the Quick Reference too. `index.html` holds no component logic: it only links `styles.css`, `ds-icons.js` and `ds.js`. The `<style>` block in its `<head>` is preview-only (swatches, tables) and is not part of the DS.

## Files
- `styles.css` - tokens and component styles (working copy)
- `ds.js` - behavior and `<ds-icon>` (working copy)
- `ds-icons.js` - generated icon bundle (working copy). Regenerate with `python3 tools/bundle-icons.py`; do not hand-edit.
- `Icons/16`, `Icons/24` - source SVGs, kebab-case file names (`chevron-left.svg`)
- `Images/` - sample images used by the demo
- `index.html` - the demo and documentation page
- `test-prototype.html` - links ONLY `releases/v1.0/`; proves a prototype works against a frozen release
- `releases/` - frozen releases
- `CHANGELOG.md`, `README.md`

## Adding an icon
1. Drop a single-color SVG into `Icons/16/` or `Icons/24/`. Name it in kebab-case (`my-icon.svg`); use `-alt` for a variant of an existing name, not `-1`.
2. Run `python3 tools/bundle-icons.py`. It rewrites `ds-icons.js` (black fills become `currentColor`).
3. It shows up on the Icons page automatically only if you regenerate that grid; add the tile to `index.html` (copy an existing `icon-tile`).

## Releasing
- **Never edit anything inside `releases/`.** The files are read-only on purpose.
- To release: create `releases/vX.Y/` and copy `styles.css`, `ds.js` and `ds-icons.js` into it unchanged. Add an entry to `CHANGELOG.md` describing what changed (and anything that could break a prototype). Never reuse or overwrite a version folder.
- Bump `version` in `ds.js` before copying.
- Breaking changes (renamed class, removed icon, changed markup) mean a new major version.

## Checking your work
Open `index.html` and `test-prototype.html` straight from disk and check:
- the browser console shows no errors;
- select, tabs, segmented control, switch, toast, modal and the theme toggle all work (mouse and keyboard);
- the page looks the same in light and dark theme as before your change.
