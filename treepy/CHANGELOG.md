# Changelog

All notable changes to treepy are recorded here. The format follows the
usual `Added / Changed / Fixed` headings and versions use semver.

## Unreleased

### Fixed
- Each scan root uses only its own `.gitignore`, alongside CLI exclusions.
- Invalid entry limits produce an argument error; trimmed JSON counters describe
  the displayed entries, including nested directories and symlinks.
- Include patterns match standalone file roots and subtract error nodes without
  negative file counts. Scan failures still produce a nonzero exit code.
- Installation instructions point to `treepy/` after the workspace move.

## 0.9.4 - 2026-10-12

### Fixed
- `--max-entries` no longer drops the summary line when it trims a root.

## 0.9.0 - 2026-09-21

### Added
- `--json` output with a documented schema and a `stats` block.
- `--du` to show per-directory totals instead of per-entry sizes.

### Changed
- The summary line now reports symlinks and errors separately.

## 0.8.0 - 2026-08-17

### Added
- Cycle detection when `--follow-links` is used.
- `--prune` to hide directories that end up empty.

### Fixed
- Deeply nested paths no longer lose their connector prefixes.

## 0.7.1 - 2026-07-19

### Fixed
- Character classes in ignore patterns now accept a leading `!`.

## 0.7.0 - 2026-07-02

### Added
- `-P/--include` with the same pattern dialect as `-I/--exclude`.
- `NO_COLOR` and `TERM=dumb` are respected in `--color auto`.

## 0.6.0 - 2026-06-08

### Added
- `--gitignore` reads the ignore file of each requested root.

### Changed
- Ignore patterns are matched against paths relative to the scan root.

## 0.5.0 - 2026-05-11

### Added
- `--ascii` for terminals without box drawing characters.
- `-o/--output` to write the tree to a file.

## 0.4.0 - 2026-04-14

### Added
- `--sort size|mtime|none` and `-r/--reverse`.
- Human readable sizes with `-H`.

## 0.3.0 - 2026-03-16

### Added
- `-d/--dirs-only`, `-a/--all` and `-L/--depth`.
- A summary line with directory, file and byte counts.

## 0.2.0 - 2026-02-10

### Added
- Colour support, including per-extension colours and an executable bit.

### Changed
- The walker and the renderer were split into separate modules.

## 0.1.0 - 2026-01-05

### Added
- First working version: walk a directory, print it as a tree.
