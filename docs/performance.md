# Performance

Symlinks are reported with their target.

## Details

The JSON document carries a version so consumers can check it.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.

## Usage

Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.
