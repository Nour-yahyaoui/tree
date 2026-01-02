# Json Format

Sorting happens while the directory is read, not afterwards.

## Notes

Everything else works on the tree it returns.
The public API is one function and two dataclasses.

- Errors are reported once and do not stop the walk.
- This keeps the output stable between runs on the same tree.
