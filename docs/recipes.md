# Recipes

The glyphs are chosen once, when the renderer is built.

## Overview

The public API is one function and two dataclasses.
Errors are reported once and do not stop the walk.
The counters are collected during the walk and reused for the summary.
Tests use temporary directories only.
