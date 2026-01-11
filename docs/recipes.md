# Recipes

Colour is decided in a single place so the rest stays testable.

## Notes

This keeps the output stable between runs on the same tree.
A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.
