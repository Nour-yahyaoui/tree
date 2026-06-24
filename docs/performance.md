# Performance

Colour is decided in a single place so the rest stays testable.

## Details

A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.
The public API is one function and two dataclasses.

## Usage

Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.
Sorting happens while the directory is read, not afterwards.
This keeps the output stable between runs on the same tree.
