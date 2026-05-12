# Ignore Rules

The counters are collected during the walk and reused for the summary.

## Overview

A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.
