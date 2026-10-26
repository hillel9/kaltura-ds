# Kaltura Design System

Buttons, inputs, selects, tabs, modals, icons and more, as plain HTML, CSS and JS. No install, no build. Open a file in the browser and it works.

Open `index.html` in this repo to see everything: colors, spacing, type, every component, and all icons with their names.

## Add it to a prototype

A prototype does not link the DS from a URL. Each prototype repo keeps its own copy of **one release** in a `ds/` folder, so the prototype never changes under you. Run this once in the prototype repo (it downloads the newest release; to pin another one, set `V=v1.0` instead):

```sh
V=$(curl -fsSL https://raw.githubusercontent.com/hillel9/kaltura-ds/main/releases/latest.txt)
mkdir -p ds
for f in styles.css ds.js ds-icons.js DS-GUIDE.md; do
  curl -fsSL "https://raw.githubusercontent.com/hillel9/kaltura-ds/main/releases/$V/$f" -o "ds/$f"
done
```

You get:

- `ds/styles.css` - the look (colors, spacing, components)
- `ds/ds-icons.js` - all icons
- `ds/ds.js` - the behavior (dropdowns, tabs, modals, toasts, dark mode, `<ds-icon>`)
- `ds/DS-GUIDE.md` - the guide for Claude: exact markup for every component, events, the `window.DS` API, all tokens and icon names

Commit the `ds/` folder with the prototype. Never edit files inside it; to change the DS, change this repo and release a new version.

Then add three tags to your page (paths are relative to the page, so adjust them for pages in subfolders):

```html
<link rel="stylesheet" href="ds/styles.css">
<script src="ds/ds-icons.js"></script>
<script src="ds/ds.js"></script>
```

Put `ds-icons.js` before `ds.js`. Both can go at the end of `<body>` or in the `<head>`. It works straight from your disk, no server needed. (The Lato font loads from Google Fonts, so it needs a network connection; offline it falls back to a system font.)

### Telling Claude about it

Add this to the prototype repo's `CLAUDE.md`:

```md
## Design system
This repo uses the Kaltura DS, copied into `ds/`. Before writing any UI, read `ds/DS-GUIDE.md`.
Use only the components, `--ds-*` tokens and `<ds-icon>` names listed there. Never edit anything in `ds/`.
```

### Which version do I have?

The top of `ds/DS-GUIDE.md` says `DS version: **1.0.0**`. In the browser console, `DS.version` shows the same.

### Upgrading

Run the fetch commands again with the version you want. Read `CHANGELOG.md` first: a new major version (v2.0) can change markup or behavior, and a new minor version (v1.1) only adds or fixes things. After upgrading, open the prototype and check the console is clean.

## A small example page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My prototype</title>
  <link rel="stylesheet" href="ds/styles.css">
  <script src="ds/ds-icons.js"></script>
  <script src="ds/ds.js"></script>
</head>
<body style="padding: var(--ds-space-8);">

  <h1>Projects</h1>

  <!-- Button with an icon -->
  <button class="ds-btn ds-btn-md ds-btn-primary">
    <ds-icon name="plus" size="16"></ds-icon> New project
  </button>

  <!-- Dropdown -->
  <div class="ds-select-wrapper">
    <button class="ds-select" aria-haspopup="listbox">
      <span>Sort by</span>
      <ds-icon class="ds-select-chevron" name="chevron-down" size="16"></ds-icon>
    </button>
    <div class="ds-select-menu" role="listbox">
      <button class="ds-select-item" role="option"><span class="ds-select-item-label">Name</span></button>
      <button class="ds-select-item" role="option"><span class="ds-select-item-label">Date</span></button>
    </div>
  </div>

  <!-- Modal: the first button opens it, any data-ds-close element inside it closes it -->
  <button class="ds-btn ds-btn-md ds-btn-secondary" data-ds-open="delete-modal">Delete</button>

  <div class="ds-modal ds-modal-sm" id="delete-modal" hidden>
    <div class="ds-modal-backdrop"></div>
    <div class="ds-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="delete-title">
      <div class="ds-modal-header">
        <h2 class="ds-modal-title" id="delete-title">Delete project?</h2>
      </div>
      <div class="ds-modal-body">This can't be undone.</div>
      <div class="ds-modal-footer">
        <button class="ds-btn ds-btn-md ds-btn-secondary ds-btn-borderless" data-ds-close>Cancel</button>
        <button class="ds-btn ds-btn-md ds-btn-danger" data-ds-close>Delete</button>
      </div>
    </div>
  </div>

</body>
</html>
```

Modal behavior depends on the version (v1.0 also closes on Escape and a backdrop click; newer versions only close from a `data-ds-close` button). The Cancel button above works in every version. For the exact modal markup of your copy, see `ds/DS-GUIDE.md`.

## Icons

```html
<ds-icon name="settings"></ds-icon>            <!-- 24px (default) -->
<ds-icon name="settings" size="16"></ds-icon>  <!-- 16px -->
```

- Find names in the Icons section of `ds/DS-GUIDE.md`, or on the Icons page of `index.html`. Names are lowercase with dashes (`chevron-left`).
- The icon takes the text color around it. To make it blue: `<ds-icon name="info" style="color: var(--ds-primary)">`.
- Not every icon has a 16px version; if it doesn't, the 24px one is shown smaller. A few icons exist only at 16px (for example `plus` and `close`): always write `size="16"` for those. `DS-GUIDE.md` lists them.
- Never paste SVG into a page; use `<ds-icon>`.

## Colors, spacing and type

Use the variables instead of typing numbers, so your prototype matches the DS and follows dark mode:

```css
.card {
  background: var(--ds-paper);
  color: var(--ds-tone-1);
  padding: var(--ds-space-4);          /* 16px */
  border-radius: var(--ds-roundness-2);
  box-shadow: var(--ds-shadow-floating);
  font-size: var(--ds-font-size-4);    /* 14px */
}
```

Spacing steps are multiples of 4px (`--ds-space-1` = 4px ... `--ds-space-8` = 32px). All tokens with their values are in `ds/DS-GUIDE.md` and in the Tokens sections of `index.html`.

## Dark mode

```html
<button data-ds-theme-toggle>Toggle dark</button>
<script> DS.setTheme('dark'); </script>   <!-- or 'light' -->
```

## Reacting to what people do

Selects, tabs, segmented controls, switches and pagination send a `ds-change` event:

```html
<script>
  document.addEventListener('ds-change', function (e) {
    console.log(e.detail.value, e.detail.label);
  });
</script>
```

For a select item, `value` is the item's `data-value` if it has one, otherwise its text. A switch gives `true` or `false`.

Toasts: `DS.showToast({ type: 'success', message: 'Saved' })` (types: `info`, `success`, `warning`, `error`).

## Versions and releases

Each release is a frozen folder `releases/vX.Y/` in this repo with exactly four files: `styles.css`, `ds.js`, `ds-icons.js` and `DS-GUIDE.md`. New versions never change old ones. `releases/latest.txt` holds the newest version name. `CHANGELOG.md` says what changed and what could break a prototype.

The files at the top of this repo (`styles.css`, `ds.js`, `DS-GUIDE.md`, ...) are the working copy and may contain changes that are not released yet; prototypes should only use files from `releases/`.

Working on the DS itself? Read `CLAUDE.md`. To ship a new version, ask Claude to "release the DS" (see `.claude/skills/release/SKILL.md`).
