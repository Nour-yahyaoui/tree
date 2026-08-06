# Architecture

The public API is one function and two dataclasses.

## Details

This keeps the output stable between runs on the same tree.
Tests use temporary directories only.

- Sorting happens while the directory is read, not afterwards.
- The glyphs are chosen once, when the renderer is built.

## Usage

Symlinks are reported with their target.
A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.
