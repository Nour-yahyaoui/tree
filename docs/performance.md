# Performance

The glyphs are chosen once, when the renderer is built.

## Details

Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.

## Usage

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.
Sizes are taken from the directory entry when the platform allows it.
