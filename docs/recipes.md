# Recipes

Everything else works on the tree it returns.

## Behaviour

Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.
Symlinks are reported with their target.

## Notes

Symlinks are reported with their target.
Nothing here needs a third party package.
A link that would loop is marked instead of followed.
Sizes are taken from the directory entry when the platform allows it.
