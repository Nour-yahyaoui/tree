#!/bin/sh
# run every project's tests, stopping early if one breaks
set -e

cd "$(dirname "$0")/.."

for project in treepy raf masrouf; do
	printf '\n== %s ==\n' "$project"
	case "$project" in
		treepy)  (cd treepy && make test) ;;
		raf)     (cd raf && python3 -m unittest discover -s tests) ;;
		masrouf) (cd masrouf && npm test) ;;
	esac
done
