# Changelog

All notable changes to masrouf. Versions follow semver.

## Unreleased

### Fixed
- Forms populate categories, restore settings and use the browser's local date.
- Editing an amount uses major units in that entry's currency, not its note.
- Amounts, calendar dates, edits, settings and stored entries are validated;
  duplicate IDs and malformed stored rows no longer break the page.
- CSV preserves quoted fields, multiline notes and whitespace, accepts a BOM,
  and reports malformed quotes using original physical line numbers.
- The static server rejects malformed paths, traversal and external symlinks,
  handles missing files without crashing and supports HEAD requests.

### Added
- Dependency-free DOM event and HTTP server regression tests.
- Accessible names for expense and CSV form controls.

## 1.0.0 - 2026-09-27

First stable release: one page, no dependencies, the data in the browser, and
an export that always imports again.

### Added
- `docs/money.md` and a test per module, driven by `node --test`.
- Categories carry a name in English, French and Arabic.

### Changed
- The chart, the list and the summary are pure functions now. Only `main.mjs`
  touches the DOM.

## 0.9.0 - 2026-08-22

### Added
- The summary block: the month's total, the average per expense, and the
  category that takes the biggest bite.

### Fixed
- A CSV row with a bad amount no longer takes the whole import down with it.

## 0.8.0 - 2026-07-18

### Added
- Offline support: a service worker and a web app manifest, so the page opens
  with no network at all.

## 0.7.0 - 2026-06-14

### Added
- Arabic, with right-to-left layout: `dir` follows the language, not the theme.

## 0.6.0 - 2026-05-09

### Added
- CSV import and export, with the amount column in major units so an export
  imports again, and errors that name the line.

## 0.5.0 - 2026-04-11

### Added
- The bar chart: monthly totals as SVG rectangles from a pure function, with
  non-finite values kept off the axis.

## 0.4.0 - 2026-03-07

### Added
- `node --test` for the whole store, and CI on Node 20 and 22.

### Fixed
- Amounts are integers in minor units everywhere, after `0.1 + 0.2` printed as
  `0.30000000000000004` in the summary.

## 0.3.0 - 2026-02-07

### Added
- Editing and deleting an entry, instead of only adding one.
- The dark and light themes, remembered in the settings.

## 0.2.0 - 2026-01-03

### Added
- Currencies: the dinar, the euro, the dollar and the yen, each with its own
  number of decimals, and a parser that reads what people actually type.

## 0.1.0 - 2025-11-29

### Added
- First version: one page, a form, a list, the month's total, and the data in
  `localStorage`.
