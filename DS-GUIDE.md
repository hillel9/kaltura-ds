# Kaltura DS - guide for AI assistants

Read this before writing any UI in a prototype that has a `ds/` folder. It lists every component's exact markup, the JS API, all tokens and all icon names. Everything here is in `ds/styles.css`, `ds/ds.js`, `ds/ds-icons.js`.

<!-- BEGIN GENERATED: version -->
DS version: **x**
<!-- END GENERATED: version -->

## Rules

1. **Use tokens, never raw values.** Colors, spacing, font size/weight, radius, shadows, durations, z-index: write `var(--ds-*)` from the Tokens section. No hex colors, no `px` for spacing or type, no `font-weight` other than `--ds-font-weight-regular|bold`. Tokens follow dark mode; raw values do not.
2. **Icons: `<ds-icon name="..." size="16|24">` only.** Never paste SVG, never use emoji or icon fonts. Use only names from the Icons section. Default size is 24. Icons take `currentColor`, so color them via the parent's `color`.
3. **Never edit anything in `ds/`.** It is a copy of a frozen release. If a component or token is missing, build it in your own CSS from `--ds-*` tokens, and tell the user the DS lacks it.
4. **Only use classes listed here.** Do not invent `ds-` classes. Do not restyle DS components with overrides; pick a documented variant.
5. **Do not write JS for DS behavior.** Select, tabs, segmented control, switch, table selection, pagination, toast, modal and theme already work (event delegation, also for elements added later). React to them with the `ds-change` / `ds-open` / `ds-close` events or the `window.DS` API.
6. **No frameworks needed; must work from `file://`.** Classic `<script>` tags only (no `type="module"`, no `fetch`).
7. Copy markup exactly, including `role`, `aria-*` and the `hidden` attribute. The JS and CSS select on them.

## Setup

```html
<link rel="stylesheet" href="ds/styles.css">
<script src="ds/ds-icons.js"></script>   <!-- before ds.js -->
<script src="ds/ds.js"></script>
```

Font is Lato, loaded by `styles.css` from Google Fonts (needs network; falls back to sans-serif). The DS does not reset page margins; set your own `body { margin: 0; }` if you want that.

## Dark theme

`<html data-theme="dark">` switches every token. `DS.setTheme('dark'|'light')`, `DS.getTheme()`, or any `<button data-ds-theme-toggle>`. Fires `ds-theme-change` on `document` with `detail: { theme }`.

## Tokens

All defined in `:root` in `styles.css`. `/* dark: x */` marks tokens that change in dark theme. Semantics used by the components: `tone-1` main text, `tone-2` secondary text, `tone-3` placeholder/field border, `tone-4` disabled text and strong borders, `tone-5` hover fills and dividers, `tone-6` secondary-button bg and light dividers, `tone-7` subtle bg and row hover, `tone-8` field/surface bg (white in light, black in dark). `--ds-background` page, `--ds-paper` cards/panels, `--ds-elevated` menus and modals. Spacing: `--ds-space-N` = N x 4px; a dash in the name is a decimal point (`1-5` = 1.5 x 4 = 6px). Always use `var(--ds-primary)` etc., never the hex values below.

<!-- BEGIN GENERATED: tokens -->
(generated)
<!-- END GENERATED: tokens -->

## Icons

`<ds-icon name="settings" size="16"></ds-icon>`. An unknown name renders nothing and logs a console warning. If a name has no 16px version, `size="16"` falls back to the 24px artwork scaled to 16. Inside a button, put the icon before or after the text; the button already has a gap.

<!-- BEGIN GENERATED: icons -->
(generated)
<!-- END GENERATED: icons -->

<!--PART2-->
