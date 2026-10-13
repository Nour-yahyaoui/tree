#!/bin/sh
# run every project's tests, stopping early if one breaks
set -e

cd "$(dirname "$0")/.."

printf '\n== treepy ==\n'
(cd treepy && make test)
