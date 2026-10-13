# Changelog

All notable changes to raf. Versions follow semver.

## 1.0.0 - 2026-09-06

First stable release. The command line, the schema and the export format are
now things I will not break without saying so.

### Added
- `docs/schema.md`, and a test per module.
- `raf stats`: totals, read, unread, tags and hosts.

### Changed
- Search is one query language: words, `tag:name`, `is:unread`.

## 0.9.0 - 2026-07-19

### Added
- The config file: a shelf path, and a default tag for `raf add`.

## 0.8.0 - 2026-06-21

### Added
- Import and export. The export is versioned json, and an import restores the
  date a link was saved rather than the date of the import.

### Fixed
- Importing a file that is not an export says so instead of throwing a
  `KeyError` at the reader.

## 0.7.0 - 2026-05-24

### Added
- `raf tags`, and the read/unread split in the list.

## 0.6.0 - 2026-04-19

### Added
- Ranking: a title hit counts for more than a tag hit, which counts for more
  than a url hit, which counts for more than a note hit.

## 0.5.0 - 2026-03-23

### Added
- Tags: add, remove, filter by, and list.

## 0.4.0 - 2026-02-22

### Added
- Tests with `unittest`, and CI on Python 3.10 through 3.12.

### Fixed
- `mailto:` and `ftp:` are refused instead of being stored as broken links.

## 0.3.0 - 2026-01-25

### Added
- Search: words, and `is:unread`.

## 0.2.0 - 2025-12-28

### Added
- Notes and titles, and the `show` command that prints them.

## 0.1.0 - 2025-11-23

### Added
- First version: `add`, `list`, and a sqlite file that remembers.
