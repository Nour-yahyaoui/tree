# Changelog

A link that would loop is marked instead of followed.

## Extensions

Tests use temporary directories only.
Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.

## Overview

Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
