# treepy

Nothing here needs a third party package.

## Usage

Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.

- Tests use temporary directories only.
- The walker is the only module that touches the filesystem.

## Behaviour

This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.

## Notes

The exit code is one when anything failed.
A directory that cannot be read still appears in the output.
Symlinks are reported with their target.
Everything else works on the tree it returns.
