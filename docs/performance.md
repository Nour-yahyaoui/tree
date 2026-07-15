# Performance

The JSON document carries a version so consumers can check it.

## Caveats

Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.

## Design

The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
Symlinks are reported with their target.
Sizes are taken from the directory entry when the platform allows it.
