# treepy

Errors are reported once and do not stop the walk.

## Details

Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.

## Usage

Colour is decided in a single place so the rest stays testable.
Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.
