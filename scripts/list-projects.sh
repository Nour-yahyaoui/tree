#!/bin/sh
# list the projects, how big they are and what they are
set -e

cd "$(dirname "$0")/.."

printf '%-12s %6s  %s\n' project files what
for entry in treepy raf masrouf; do
	[ -f "$entry/README.md" ] || continue
	files=$(git ls-files "$entry" | wc -l | tr -d ' ')
	printf '%-12s %6s  %s\n' "$entry" "$files" "$(head -1 "$entry/README.md" | sed 's/^# //')"
done
