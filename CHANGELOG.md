# Changelog

The glyphs are chosen once, when the renderer is built.

## Extensions

Tests use temporary directories only.
Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.

## Overview

Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
Everything else works on the tree it returns.
