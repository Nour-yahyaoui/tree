#!/bin/sh
# list the projects in the collection
set -e

cd "$(dirname "$0")/.."

ls -d */
