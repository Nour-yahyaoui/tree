#!/bin/sh
# run every project's tests and summarise the result
set -e

cd "$(dirname "$0")/.."

failed=""
for project in treepy raf masrouf; do
	printf '\n== %s ==\n' "$project"
	case "$project" in
		treepy)  (cd treepy && make test) || failed="$failed $project" ;;
		raf)     (cd raf && python3 -m unittest discover -s tests) || failed="$failed $project" ;;
		masrouf) (cd masrouf && npm test) || failed="$failed $project" ;;
	esac
done

if [ -n "$failed" ]; then
	printf '\nfailed:%s\n' "$failed"
	exit 1
fi

printf '\nall projects passed\n'
