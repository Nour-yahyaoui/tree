# Json Format

A directory that cannot be read still appears in the output.

## Details

A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.

- Keeping this small makes the behaviour easy to reason about.
- Errors are reported once and do not stop the walk.

## Usage

A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.

## Behaviour

The glyphs are chosen once, when the renderer is built.
Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.

## Notes

The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.

- Sorting happens while the directory is read, not afterwards.
- The public API is one function and two dataclasses.
