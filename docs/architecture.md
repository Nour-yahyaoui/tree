# Architecture

A link that would loop is marked instead of followed.

## Examples

Everything else works on the tree it returns.
The walker is the only module that touches the filesystem.
The glyphs are chosen once, when the renderer is built.

## Why

Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.
A directory that cannot be read still appears in the output.
Nothing here needs a third party package.

## Caveats

This keeps the output stable between runs on the same tree.
Keeping this small makes the behaviour easy to reason about.

- The public API is one function and two dataclasses.
- Nothing here needs a third party package.

## Design

Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.
