# Kaltura Design System

Buttons, inputs, selects, tabs, modals, icons and more, as plain HTML, CSS and JS. No install, no build. Open a file in the browser and it works.

Open `index.html` to see everything: colors, spacing, type, every component, and all icons with their names.

## Use it in a prototype

Add these three tags to your page. Use the released version so your prototype doesn't change under you:

```html
<link rel="stylesheet" href="https://YOUR-HOST/ds/releases/v1.0/styles.css">
<script src="https://YOUR-HOST/ds/releases/v1.0/ds-icons.js"></script>
<script src="https://YOUR-HOST/ds/releases/v1.0/ds.js"></script>
```

- `styles.css` - the look (colors, spacing, components)
- `ds-icons.js` - all icons
- `ds.js` - the behavior (dropdowns, tabs, modals, toasts, dark mode, `<ds-icon>`)

Working locally? Use relative paths instead, for example `href="ds/releases/v1.0/styles.css"`. Works straight from your disk, no server needed.

Order: put `ds-icons.js` before `ds.js` as shown. Put both at the end of `<body>` or in the `<head>`; either works.

## A small example page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My prototype</title>
  <link rel="stylesheet" href="ds/releases/v1.0/styles.css">
  <script src="ds/releases/v1.0/ds-icons.js"></script>
  <script src="ds/releases/v1.0/ds.js"></script>
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

  <!-- Modal: the button opens it, any data-ds-close element closes it -->
  <button class="ds-btn ds-btn-md ds-btn-secondary" data-ds-open="delete-modal">Delete</button>

  <div class="ds-modal ds-modal-sm" id="delete-modal" hidden>
    <div class="ds-modal-backdrop" data-ds-close></div>
    <div class="ds-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="delete-title">
      <div class="ds-modal-header">
        <h2 class="ds-modal-title" id="delete-title">Delete project?</h2>
        <button class="ds-modal-close" data-ds-close aria-label="Close"><ds-icon name="clear"></ds-icon></button>
      </div>
      <div class="ds-modal-body">This can't be undone.</div>
      <div class="ds-modal-footer">
        <button class="ds-btn ds-btn-md ds-btn-secondary" data-ds-close>Cancel</button>
        <button class="ds-btn ds-btn-md ds-btn-danger" data-ds-close>Delete</button>
      </div>
    </div>
  </div>

</body>
</html>
```

## Icons

```html
<ds-icon name="settings"></ds-icon>            <!-- 24px (default) -->
<ds-icon name="settings" size="16"></ds-icon>  <!-- 16px -->
```

- Find the name on the Icons page of `index.html`. Names are lowercase with dashes (`chevron-left`).
- The icon takes the text color around it. To make it blue: `<ds-icon name="info" style="color: var(--ds-primary)">`.
- Not every icon has a 16px version; if it doesn't, the 24px one is shown smaller.

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

Spacing steps are multiples of 4px (`--ds-space-1` = 4px ... `--ds-space-8` = 32px). See the Tokens sections on `index.html` for all of them.

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

## Versions

Each release is a frozen folder under `releases/` (`v1.0`, later `v1.1`, ...). Pin your prototype to one. New versions never change old ones. See `CHANGELOG.md` for what changed.
