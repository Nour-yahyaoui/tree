# Recipes

Patterns are matched against the path relative to the root of the scan.

## Details

Errors are reported once and do not stop the walk.
Nothing here needs a third party package.

- Nothing here needs a third party package.
- The walker is the only module that touches the filesystem.

## Usage

Colour is decided in a single place so the rest stays testable.
The summary line describes what was printed, not what was found.
The public API is one function and two dataclasses.
