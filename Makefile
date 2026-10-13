# the workspace. every project also has its own Makefile.

.PHONY: help

help:
	@echo "tree - a collection of small projects"
	@echo
	@echo "make test      run every project's tests"
	@echo "make list      show what is in here"

.PHONY: test

test:
	./scripts/check-all.sh
