# Performance

A directory that cannot be read still appears in the output.

## Details

Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.

## Usage

Tests use temporary directories only.
Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
