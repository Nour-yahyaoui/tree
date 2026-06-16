# Recipes

Errors are reported once and do not stop the walk.

## Notes

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.
This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
