# Architecture

Sizes are taken from the directory entry when the platform allows it.

## Overview

Tests use temporary directories only.
A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.
Symlinks are reported with their target.
