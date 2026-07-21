# Architecture

The counters are collected during the walk and reused for the summary.

## Extensions

The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.

## Overview

The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
