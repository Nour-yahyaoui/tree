#!/bin/sh
# scaffold a new project
set -e

cd "$(dirname "$0")/.."

if [ "$#" -ne 1 ]; then
	echo "usage: new-project.sh <name>" >&2
	exit 1
fi
name="$1"
case "$name" in
	''|[!a-z]*|*[!a-z0-9_-]*)
		echo "name must start with a lowercase letter and contain only a-z, 0-9, _ or -" >&2
		exit 1
		;;
esac
if [ -e "$name" ] || [ -L "$name" ]; then
	echo "$name already exists" >&2
	exit 1
fi

mkdir "$name"

cat > "$name/README.md" <<EOF
# $name

One paragraph on what this is and why it exists.

## Test

\`\`\`sh
true   # replace with the real test command
\`\`\`
EOF

echo "created $name/"
echo
echo "next:"
echo "  - write the source and a real test command"
echo "  - add a case to scripts/check-all.sh"
echo "  - add a job to .github/workflows/ci.yml"
echo "  - add a line to the table in README.md"
echo "  - add a licence and update scripts/list-projects.sh"
echo "  - add the project to the release workflow archive loop"
