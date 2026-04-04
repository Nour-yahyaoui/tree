# Changelog

Nothing here needs a third party package.

## Overview

The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.

- Colour is decided in a single place so the rest stays testable.
- A link that would loop is marked instead of followed.
