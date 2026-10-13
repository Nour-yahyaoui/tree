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

.PHONY: treepy raf masrouf

treepy:
	cd treepy && make test

raf:
	cd raf && python3 -m unittest discover -s tests

masrouf:
	cd masrouf && npm test

.PHONY: list clean

list:
	./scripts/list-projects.sh

clean:
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	find . -name 'node_modules' -type d -prune -exec rm -rf {} +

.PHONY: lint

lint:
	python3 -m compileall -q treepy/src raf/raf
