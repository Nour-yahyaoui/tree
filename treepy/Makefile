PYTHON ?= python3
SRC := src
TESTS := tests

.PHONY: help test coverage lint demo install clean

help:
	@echo "make test      - run the unit test suite"
	@echo "make coverage  - run tests with a coverage report"
	@echo "make lint      - compile every module to catch syntax errors"
	@echo "make demo      - print this repository with treepy itself"
	@echo "make install   - editable install into the current environment"
	@echo "make clean     - remove caches and build artefacts"

test:
	PYTHONPATH=$(SRC) $(PYTHON) -m unittest discover -s $(TESTS) -t . -v

coverage:
	PYTHONPATH=$(SRC) $(PYTHON) -m coverage run -m unittest discover -s $(TESTS) -t .
	PYTHONPATH=$(SRC) $(PYTHON) -m coverage report -m

lint:
	$(PYTHON) -m compileall -q $(SRC) $(TESTS)

demo:
	PYTHONPATH=$(SRC) $(PYTHON) -m treepy --gitignore --size --human-readable src

install:
	$(PYTHON) -m pip install -e .

clean:
	rm -rf build dist .coverage htmlcov
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
