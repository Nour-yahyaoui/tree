# Changelog

The counters are collected during the walk and reused for the summary.

## Extensions

Symlinks are reported with their target.
The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.

## Overview

This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.
Nothing here needs a third party package.
Everything else works on the tree it returns.
