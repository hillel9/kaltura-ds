# Changelog

Released folders under `releases/` are frozen and never edited. A change ships as a new version folder
(copy `styles.css`, `ds.js`, `ds-icons.js` to `releases/vX.Y/`) plus an entry here.

## Unreleased

## v1.3 (2026-11-26)

Nothing was removed or renamed: every class, token, event and function from v1.2 still works. Could change how a prototype looks after upgrading: `--ds-roundness-3` (12px to 16px) in a prototype's own CSS, danger/warning/success colors in dark theme, the warning color, checkbox/radio hover and disabled states, disabled switches, the modal backdrop and floating alert text color in dark theme. Could affect a prototype's own code: toasts built by `DS.showToast({...})` now carry `ds-alert…` classes (find them with `.ds-toast-active`), and a switch's state is read from `aria-checked`. Upgrading from v1.0 also brings v1.1's static modals.

### Added
- **SplitButton** (`.ds-split-button`), from the Figma Platform DS, with KEP UI's names: action button (`.ds-split-button-action`), menu toggle button (`.ds-split-button-menu-toggle`) and menu (`.ds-split-button-menu`, items `.ds-select-item[role=menuitem]`). Sizes md/lg/xl, optional 24px start icon, primary (plus secondary and danger like KEP), hover and focus per half, open, disabled and processing states. `ds.js` opens and closes the menu with mouse and keyboard (ArrowDown/Up, Home/End, Escape, Tab out). No new tokens, no change to existing components.
- **Breadcrumbs** (`.ds-breadcrumbs`): look from the Figma Platform DS "Breadcrumb Item" states, names from KEP UI's `Breadcrumbs`: breadcrumb item (`.ds-breadcrumb-item`, as a link, button or text), separator (`.ds-breadcrumbs-separator`, 16px chevron), active (`aria-current="page"`, primary-brighter), disabled (`aria-disabled="true"`, tone-4), hover (primary) and truncated (`...`, tone-3). `ds.js` collapses the middle items into "..." when the trail is too wide, like KEP, and shows them all on click; `data-collapse="none"` turns it off. No new tokens.
- **Switch translucent mode** (`.ds-switch-translucent`), from the Figma Platform DS Switch (Mode=Translucent, KEP `color="translucent"`): for switches over images or video. `aria-disabled="true"` now also disables a switch.
- **KEP UI names** for seven components, so prototypes use the dev team's words (`@kaltura/ds-react-components`). New classes, same look and behavior; the old ones keep working:
  - Alert `ds-alert…` (was Acknowledgement `ds-ack…`)
  - Tooltip `ds-tooltip…` (was Hint `ds-hint…`)
  - Initials `ds-initials…` (was User picture `ds-user-picture…`; sizes keep this DS's px, so `-lg` is 48px, not KEP's 96px)
  - Loader `ds-loader…` (was Spinner `ds-spinner…`)
  - SegmentedContainer / SegmentedButton `ds-segmented-container`, `ds-segmented-button` (was `ds-segmented`, `ds-segmented-item`)
  - ComposedInput `ds-composed-input`, `ds-form-additional-info`, `ds-form-helper-text-error`, `ds-input-counter` (was `ds-form-field`, `ds-form-desc`, `ds-form-error`, `ds-form-counter`; `ds-form-label` unchanged)
  - Select / SelectMenu already matched.
  `DS-GUIDE.md` and the demo page now use the KEP names, with a mapping table. Not breaking: nothing was removed.
- **One name per thing for agents:** `DS-GUIDE.md` rule 8 says old names are read-only (never written, and a component written with old names is converted whole, never mixed), and `styles.css` and `ds.js` comments mark the old selectors as kept for older prototypes. Elements `ds.js` builds now use the current names: toasts from `DS.showToast({...})` are `ds-alert…` (were `ds-ack…`), the autocomplete "+N" tooltip is `ds-tooltip…` (was `ds-hint…`), and a click only sets `aria-checked` on a switch, touching `ds-switch-on` / `-off` only if the markup already had them. Same look. Could affect a prototype only if its own code finds a toast by `.ds-ack…` instead of `.ds-toast-active`.
- **Switch parts in KEP UI's names:** `ds-switch-thumb` (was `ds-switch-handle`) and the checked state read from `aria-checked` alone, so `ds-switch-on` / `ds-switch-off` are no longer needed in new markup. Old markup works unchanged; the aliases have the same specificity (`:where()`), and `ds.js` still sets the old classes.
- **Color shades** from the Figma "Acknowledgment" collection (same as KEP UI): `--ds-warning-darker` / `-brighter`, `--ds-success-darker` / `-brighter`.
- **`--ds-secondary`** (+ `-darker`, `-brighter`, `-text-contrast`): the yellow-orange that Figma and KEP call Secondary. `--ds-accent` is now an alias of it and still works.
- **Dark-theme semantic colors:** danger, warning and success (with their shades, text-contrast and danger tints) switch to KEP's and Figma's dark values, with black contrast text. Affects the danger button, error fields, alerts and toasts, and the red and orange table status dots in dark theme.
- **Spacing and shade-name mapping to KEP UI** documented on the Spacing tokens section and in `DS-GUIDE.md` (`spacing(n)` = `--ds-space-{2n}`; `-darker` = `.dark`, `-brighter` = `.light`).
- **Terminology index**: a table of Figma Platform DS name, KEP UI name and kaltura-ds classes for every component, property and token family, plus what Figma or KEP has that this DS doesn't. It appears on the preview page (Terminology Index) and in `DS-GUIDE.md`, generated from `tools/terminology.json` by `tools/build-terminology.py`. The preview page now uses the KEP names everywhere: headings, labels, demo markup and the Quick Reference. Its section anchors changed accordingly (`#composed-input`, `#segmented-buttons`, `#initials`, `#alert-tooltip`, `#loader`).
- **Surface and translucent tokens** from Figma: `--ds-protection` (#3d3d3d, light and dark, for text over media; KEP `surfaces.protection`), the missing black and white steps `--ds-b-10|50|80|90` and `--ds-w-10|30|50|90`, and `--ds-backdrop`.

### Fixed
- **Modal backdrop** is now `--ds-backdrop`, #222222 at 60% (Figma "Backdrop", KEP `palette.backdrop`). It was pure black at 60%, so it is a touch lighter.
- **Font source:** Lato now loads from `fonts.kaltura.com` (Kaltura's GDPR font proxy, same URL as KEP UI) instead of Google Fonts, and `--ds-font-family` uses KEP's fallback stack `Lato, Helvetica Neue, Segoe UI, sans-serif`.
- **Checkbox and radio states** now match Figma. Checkbox: hover unchecked gets a `tone-6` fill and `tone-4` border, hover checked or partial goes `primary-darker`, and the disabled check mark is `tone-4` (was white). Radio: hover unchecked gets a `primary` border, hover checked goes `primary-darker`, the dot is 6px (was 8px), disabled unchecked has a `tone-6` fill, and disabled checked is a `tone-4` ring with a light dot (was a white dot on `tone-7`, almost invisible). Markup unchanged.
- **Disabled switch** now matches the Figma Switch: solid `--ds-tone-4` track when off and `--ds-tone-3` when on, with a white handle. It was the normal colors at 50% opacity. Markup unchanged.
- **Warning color** is now `#c2570a` (Figma and KEP), was `#E86925`. Darker orange in warning alerts and toasts, the autocomplete "no results" icon and orange table status.
- **`--ds-roundness-3`** is now 16px (Figma and KEP), was 12px. No component changes visibly (the switch, its only user, stays a pill).
- **Floating alerts / toasts** take their text, link and dismiss color from the matching `-text-contrast` token instead of fixed white. Same in light theme; black on the brighter dark-theme colors.

## v1.2 (2026-11-24)

### Added
- **Autocomplete** (`.ds-autocomplete`): text input with a filtered menu of suggestions, from the Figma Platform DS. Single value, or multiple values as chips (`.ds-autocomplete-multiple`) with a `+N` counter and hint when they don't fit; no-results message (`.ds-autocomplete-empty`); `data-filter="none"` for suggestions the page provides; disabled. Keyboard: arrows, Home/End, Enter, Escape, Backspace removes the last chip. Fires `ds-change` on the wrapper.
- **Spinner** (`.ds-spinner`): 20px loading ring with a turning quarter arc, from the Figma Platform DS. Primary by default, `.ds-spinner-white` for dark or colored surfaces, `.ds-spinner-black` for light images. CSS only. New token `--ds-primary-tint-20` for its track.
- **Button processing state** (`.ds-btn-processing` or `aria-busy="true"`), from the Figma Platform DS: the label is hidden, the button keeps its width and color, and a spinner sized to the button turns in its place. Clicks and Enter/Space are ignored while it is set. New `DS.setProcessing(btn, on)` toggles it. New token `--ds-danger-tint-20` (borderless danger spinner track).
  - Upgrade note: any `.ds-btn` that already had `aria-busy="true"` now shows this processing state (label hidden, spinner, clicks ignored).

### Fixed
- **Disabled circular button** (`.ds-btn-circular:disabled`) is now an outline, like other disabled buttons: transparent background, `--ds-tone-4` border and icon, in light and dark. It was a `--ds-tone-5` fill (and the normal translucent fill in dark theme). Markup unchanged.
- **Select trigger border** (`.ds-select`) is now `--ds-tone-3`, like the other fields (input, textarea, search). It was `--ds-tone-4`. Markup unchanged.

## v1.1 (2026-11-18)

### Changed (behavior - read before upgrading from v1.0)
- **Modals are static.** Clicking the backdrop and pressing Escape no longer close a modal, so people don't lose what they typed in a form. A modal closes only through a `[data-ds-close]` element inside the dialog (a Cancel button) or `DS.closeModal()`. An open select inside a modal still closes on Escape.
- `ds-close` `detail.reason` is now `'button'` or `'api'` (`'escape'` and `'backdrop'` no longer happen).
- Modal layout follows the Figma "Generate a video" design: centered 24px title with no divider, body that scrolls on its own, 65px footer with a top border, actions on the right and an optional note on the left (`.ds-modal-footer-note`). The corner X is no longer in the default markup; `.ds-modal-close` is still available as an option.
- Markup: drop `data-ds-close` from `.ds-modal-backdrop` (it is ignored if left), and use a borderless secondary Cancel button.

### Fixed
- **Disabled button** (`.ds-btn` with `disabled` / `aria-disabled="true"`) is now an outline: empty background, `--ds-tone-4` border and text (was a `--ds-tone-6` fill). Borderless disabled buttons stay borderless and now show `--ds-tone-4` text instead of the variant color. Markup unchanged.

### Added
- Modal size `.ds-modal-xl` (960px), `--ds-modal-width-xl`.
- Tokens `--ds-space-10` (40px), `--ds-font-size-h3` (24px), `--ds-line-height-h3`.

## v1.0 (2026-10-13)

First versioned release. Every existing `ds-` class name and its markup keeps working.

### Added
- `ds.js`: all component behavior (select, tabs, segmented control, switch, table selection, pagination, toast, theme) moved out of the demo page. Classic script, event delegation on `document`.
  - Keyboard: Escape closes a select; arrow keys, Home and End move between tabs, segmented items and select items; Enter and Space select.
  - Events (bubble): `ds-change` with `{ value, label }` on the select wrapper, tablist, radiogroup, switch button and pagination bar; `ds-open` and `ds-close` on modals; `ds-theme-change` on `document`.
  - API: `DS.showToast(elementOrOptions)`, `DS.setTheme('light' | 'dark')`, `DS.getTheme()`, `DS.openModal(id)`, `DS.closeModal()`.
  - Markup hooks: `data-ds-toast`, `data-ds-theme-toggle`, `data-ds-open="id"`, `data-ds-close`.
- `<ds-icon name="settings" size="16">` web component (size 16 or 24, default 24). Renders the SVG inline, so it takes `currentColor`.
- `ds-icons.js`: all 236 icons bundled as strings (no fetching), so icons work over `file://`.
- Modal: `.ds-modal` with sizes `-sm`, `-md`, `-lg`; header, body, footer; focus trap; focus returns to the opener; works in dark theme.
- Tokens:
  - Spacing `--ds-space-1` to `--ds-space-8` (4px base), plus half steps (`--ds-space-1-5` = 6px, and so on) and `--ds-space-16`.
  - Type: `--ds-font-size-1` to `-7` (11, 12, 13, 14, 16, 18, 48px), `--ds-font-weight-regular` and `-bold`, `--ds-line-height-*`.
  - Shadows `--ds-shadow-menu` and `--ds-shadow-floating`.
  - Tints `--ds-primary-tint-6`, `--ds-primary-tint-10`, `--ds-danger-tint-10`; `--ds-accent`, `--ds-text-subtle`, `--ds-text-subtle-disabled`.
  - Motion `--ds-duration-*`, `--ds-ease-out`; layering `--ds-z-*`; `--ds-modal-width-*`; `--ds-roundness-tiny`; `--ds-opacity-disabled`.

### Changed
- Component styles use tokens instead of raw values (colors, spacing, type, radius, shadows, durations, z-index). Computed values are unchanged, so nothing looks different.
- Select menu items get the hover highlight on keyboard focus too.
- Icon files renamed to kebab-case (list below). The Icons page on `index.html` now lists every icon with its name.

### Behavior notes
- A select picks `data-value` if present, otherwise the visible label, as `value`.
- `DS.showToast(element)` keeps the old behavior (stays until dismissed). `DS.showToast({ ... })` auto-dismisses after 5 seconds (`duration: 0` keeps it).

### Icon renames
Rules: lowercase, spaces and underscores become `-`, `-1` becomes `-alt`. Typos fixed: `nutral` to `neutral`, `Mulitple video` to `multiple-video`.


**Icons/16** (45 renamed)

| Old | New |
|---|---|
| `Arrow Right.svg` | `arrow-right.svg` |
| `Bookmark.svg` | `bookmark.svg` |
| `Bullet.svg` | `bullet.svg` |
| `Business Card.svg` | `business-card.svg` |
| `Chat.svg` | `chat.svg` |
| `Check.svg` | `check.svg` |
| `Chevron Down.svg` | `chevron-down.svg` |
| `Chevron Left.svg` | `chevron-left.svg` |
| `Chevron Right.svg` | `chevron-right.svg` |
| `Chevron Up.svg` | `chevron-up.svg` |
| `Close.svg` | `close.svg` |
| `Double Chevron Down.svg` | `double-chevron-down.svg` |
| `Download.svg` | `download.svg` |
| `Edit.svg` | `edit.svg` |
| `Expand.svg` | `expand.svg` |
| `External Link.svg` | `external-link.svg` |
| `File.svg` | `file.svg` |
| `Folder.svg` | `folder.svg` |
| `General Spinner.svg` | `general-spinner.svg` |
| `Globe.svg` | `globe.svg` |
| `Grip.svg` | `grip.svg` |
| `Info Circle.svg` | `info-circle.svg` |
| `Link.svg` | `link.svg` |
| `Microphone Muted.svg` | `microphone-muted.svg` |
| `Microphone.svg` | `microphone.svg` |
| `More Horizontal.svg` | `more-horizontal.svg` |
| `More.svg` | `more.svg` |
| `Partial.svg` | `partial.svg` |
| `Plus.svg` | `plus.svg` |
| `Pop Out.svg` | `pop-out.svg` |
| `Progression.svg` | `progression.svg` |
| `Redo.svg` | `redo.svg` |
| `Regression.svg` | `regression.svg` |
| `Score.svg` | `score.svg` |
| `Settings.svg` | `settings.svg` |
| `Silent.svg` | `silent.svg` |
| `Sound Wave.svg` | `sound-wave.svg` |
| `Speaker Muted.svg` | `speaker-muted.svg` |
| `Speaker.svg` | `speaker.svg` |
| `Verified.svg` | `verified.svg` |
| `Voice.svg` | `voice.svg` |
| `Warning Circle.svg` | `warning-circle.svg` |
| `Warning Triangle.svg` | `warning-triangle.svg` |
| `Warning.svg` | `warning.svg` |
| `question_mark.svg` | `question-mark.svg` |

**Icons/24** (179 renamed)

| Old | New |
|---|---|
| `Add.svg` | `add.svg` |
| `Align Right.svg` | `align-right.svg` |
| `Align center.svg` | `align-center.svg` |
| `Align left.svg` | `align-left.svg` |
| `Analytics.svg` | `analytics.svg` |
| `Arrow Down.svg` | `arrow-down.svg` |
| `Arrow Left.svg` | `arrow-left.svg` |
| `Arrow Right.svg` | `arrow-right.svg` |
| `Arrow Up.svg` | `arrow-up.svg` |
| `Banner.svg` | `banner.svg` |
| `Bolt.svg` | `bolt.svg` |
| `Breakout.svg` | `breakout.svg` |
| `Brush.svg` | `brush.svg` |
| `Bullet list.svg` | `bullet-list.svg` |
| `Calendar.svg` | `calendar.svg` |
| `Camera Off.svg` | `camera-off.svg` |
| `Camera.svg` | `camera.svg` |
| `Captions.svg` | `captions.svg` |
| `Chat.svg` | `chat.svg` |
| `Check.svg` | `check.svg` |
| `Chevron Down.svg` | `chevron-down.svg` |
| `Chevron Left.svg` | `chevron-left.svg` |
| `Chevron Right.svg` | `chevron-right.svg` |
| `Chevron Up.svg` | `chevron-up.svg` |
| `Chrome.svg` | `chrome.svg` |
| `Clean.svg` | `clean.svg` |
| `Clear.svg` | `clear.svg` |
| `Cloud.svg` | `cloud.svg` |
| `Collapse Menu.svg` | `collapse-menu.svg` |
| `Color palette.svg` | `color-palette.svg` |
| `Contrast.svg` | `contrast.svg` |
| `Copy.svg` | `copy.svg` |
| `Create.svg` | `create.svg` |
| `Credit Card.svg` | `credit-card.svg` |
| `Customize.svg` | `customize.svg` |
| `Delete.svg` | `delete.svg` |
| `Desktop.svg` | `desktop.svg` |
| `Diamond.svg` | `diamond.svg` |
| `Dislike hollow.svg` | `dislike-hollow.svg` |
| `Dislike.svg` | `dislike.svg` |
| `Download.svg` | `download.svg` |
| `Drag.svg` | `drag.svg` |
| `Edge.svg` | `edge.svg` |
| `Edit.svg` | `edit.svg` |
| `Embed.svg` | `embed.svg` |
| `Emoji.svg` | `emoji.svg` |
| `Excel.svg` | `excel.svg` |
| `Executives.svg` | `executives.svg` |
| `Exit-1.svg` | `exit-alt.svg` |
| `Exit.svg` | `exit.svg` |
| `Expand.svg` | `expand.svg` |
| `Expert.svg` | `expert.svg` |
| `External Link.svg` | `external-link.svg` |
| `Facebook.svg` | `facebook.svg` |
| `Feedback.svg` | `feedback.svg` |
| `File.svg` | `file.svg` |
| `Filter.svg` | `filter.svg` |
| `Firefox.svg` | `firefox.svg` |
| `Fit Frame.svg` | `fit-frame.svg` |
| `Folder Item-1.svg` | `folder-item-alt.svg` |
| `Folder Item.svg` | `folder-item.svg` |
| `Folder.svg` | `folder.svg` |
| `Formal.svg` | `formal.svg` |
| `GenAI.svg` | `gen-ai.svg` |
| `Github.svg` | `github.svg` |
| `Globe.svg` | `globe.svg` |
| `Group.svg` | `group.svg` |
| `Hand.svg` | `hand.svg` |
| `Heart.svg` | `heart.svg` |
| `Help.svg` | `help.svg` |
| `Hidden.svg` | `hidden.svg` |
| `Home.svg` | `home.svg` |
| `Image.svg` | `image.svg` |
| `Import.svg` | `import.svg` |
| `Info.svg` | `info.svg` |
| `Informative gallery.svg` | `informative-gallery.svg` |
| `Instagram 2.svg` | `instagram-2.svg` |
| `Instagram.svg` | `instagram.svg` |
| `Integrations.svg` | `integrations.svg` |
| `Interactive Room.svg` | `interactive-room.svg` |
| `Invisible.svg` | `invisible.svg` |
| `Italic.svg` | `italic.svg` |
| `Key.svg` | `key.svg` |
| `Levels.svg` | `levels.svg` |
| `Like Hollow.svg` | `like-hollow.svg` |
| `Like.svg` | `like.svg` |
| `Line.svg` | `line.svg` |
| `LinkedIn.svg` | `linkedin.svg` |
| `Live Broadcast.svg` | `live-broadcast.svg` |
| `Lock.svg` | `lock.svg` |
| `Mail.svg` | `mail.svg` |
| `Menu.svg` | `menu.svg` |
| `Microphone Muted.svg` | `microphone-muted.svg` |
| `Microphone.svg` | `microphone.svg` |
| `Minimize.svg` | `minimize.svg` |
| `Minus.svg` | `minus.svg` |
| `Mobile.svg` | `mobile.svg` |
| `More Horizontal.svg` | `more-horizontal.svg` |
| `More Vertical.svg` | `more-vertical.svg` |
| `Mulitple video.svg` | `multiple-video.svg` |
| `Mute Notification.svg` | `mute-notification.svg` |
| `No Access.svg` | `no-access.svg` |
| `Notes.svg` | `notes.svg` |
| `Notification.svg` | `notification.svg` |
| `Online.svg` | `online.svg` |
| `Ordered list.svg` | `ordered-list.svg` |
| `Pdf.svg` | `pdf.svg` |
| `Phone.svg` | `phone.svg` |
| `Pin.svg` | `pin.svg` |
| `Pinterest.svg` | `pinterest.svg` |
| `Play.svg` | `play.svg` |
| `Playlist.svg` | `playlist.svg` |
| `Poll.svg` | `poll.svg` |
| `Pop Out.svg` | `pop-out.svg` |
| `Post.svg` | `post.svg` |
| `Presenter.svg` | `presenter.svg` |
| `Privacy.svg` | `privacy.svg` |
| `Public.svg` | `public.svg` |
| `Question Mark.svg` | `question-mark.svg` |
| `Quiz.svg` | `quiz.svg` |
| `Redo.svg` | `redo.svg` |
| `Refresh.svg` | `refresh.svg` |
| `Remove Contact.svg` | `remove-contact.svg` |
| `Remove-1.svg` | `remove-alt.svg` |
| `Remove.svg` | `remove.svg` |
| `Resolved.svg` | `resolved.svg` |
| `Score.svg` | `score.svg` |
| `Search.svg` | `search.svg` |
| `Self Served Live.svg` | `self-served-live.svg` |
| `Settings.svg` | `settings.svg` |
| `Share Screen close.svg` | `share-screen-close.svg` |
| `Share Screen.svg` | `share-screen.svg` |
| `Share.svg` | `share.svg` |
| `Shuffle.svg` | `shuffle.svg` |
| `Simulive.svg` | `simulive.svg` |
| `Slack.svg` | `slack.svg` |
| `Slide.svg` | `slide.svg` |
| `Sound.svg` | `sound.svg` |
| `Speaker Muted.svg` | `speaker-muted.svg` |
| `Speaker.svg` | `speaker.svg` |
| `Stack Overflow.svg` | `stack-overflow.svg` |
| `Star Full.svg` | `star-full.svg` |
| `Star Hollow.svg` | `star-hollow.svg` |
| `Subscribe.svg` | `subscribe.svg` |
| `Subscribed.svg` | `subscribed.svg` |
| `Switch.svg` | `switch.svg` |
| `Tablet.svg` | `tablet.svg` |
| `Text Highlight.svg` | `text-highlight.svg` |
| `Text color.svg` | `text-color.svg` |
| `Text.svg` | `text.svg` |
| `Time Hollow.svg` | `time-hollow.svg` |
| `Time.svg` | `time.svg` |
| `Timeline.svg` | `timeline.svg` |
| `Trim.svg` | `trim.svg` |
| `Twitch.svg` | `twitch.svg` |
| `Twitter - new.svg` | `twitter-new.svg` |
| `Twitter.svg` | `twitter.svg` |
| `Underline.svg` | `underline.svg` |
| `Undo.svg` | `undo.svg` |
| `Unlock.svg` | `unlock.svg` |
| `Unpin.svg` | `unpin.svg` |
| `Upload.svg` | `upload.svg` |
| `User.svg` | `user.svg` |
| `Verified.svg` | `verified.svg` |
| `Video.svg` | `video.svg` |
| `Visible.svg` | `visible.svg` |
| `Volume mute.svg` | `volume-mute.svg` |
| `Volume on.svg` | `volume-on.svg` |
| `Warning Circle.svg` | `warning-circle.svg` |
| `Warning Triangle.svg` | `warning-triangle.svg` |
| `Webcast.svg` | `webcast.svg` |
| `Webhook.svg` | `webhook.svg` |
| `Youtube.svg` | `youtube.svg` |
| `Zip File.svg` | `zip-file.svg` |
| `Zoom in.svg` | `zoom-in.svg` |
| `Zoom out.svg` | `zoom-out.svg` |
| `metadata enrichment.svg` | `metadata-enrichment.svg` |
| `nutral.svg` | `neutral.svg` |
| `switch Camera.svg` | `switch-camera.svg` |
