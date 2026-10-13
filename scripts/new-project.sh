#!/bin/sh
# scaffold a new project
set -e

cd "$(dirname "$0")/.."

name="$1"
if [ -z "$name" ]; then
	echo "usage: new-project.sh <name>" >&2
	exit 1
fi
if [ -e "$name" ]; then
	echo "$name already exists" >&2
	exit 1
fi

mkdir -p "$name"

cat > "$name/README.md" <<EOF
# $name

One paragraph on what this is and why it exists.

## Test

\`\`\`sh
true   # replace with the real test command
\`\`\`
EOF
