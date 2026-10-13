#!/bin/sh
# list the projects and what they are
set -e

cd "$(dirname "$0")/.."

for entry in */; do
	project="${entry%/}"
	[ -f "$project/README.md" ] || continue
	printf '%-12s %s\n' "$project" "$(head -1 "$project/README.md" | sed 's/^# //')"
done
