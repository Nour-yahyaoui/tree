# treepy

The walker is the only module that touches the filesystem.

## Usage

Sorting happens while the directory is read, not afterwards.
Everything else works on the tree it returns.

- Colour is decided in a single place so the rest stays testable.
- Sorting happens while the directory is read, not afterwards.
