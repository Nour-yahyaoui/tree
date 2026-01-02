# Recipes

Errors are reported once and do not stop the walk.

## Overview

Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
