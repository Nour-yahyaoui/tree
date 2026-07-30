# treepy

Nothing here needs a third party package.

## Caveats

The exit code is one when anything failed.
A directory that cannot be read still appears in the output.
This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.

## Design

The counters are collected during the walk and reused for the summary.
The glyphs are chosen once, when the renderer is built.

- Errors are reported once and do not stop the walk.
- Sizes are taken from the directory entry when the platform allows it.
