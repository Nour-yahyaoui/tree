PYTHON ?= python3
SRC := src

.PHONY: test lint clean

test:
	python3 -m unittest discover -s tests -t .

lint:
	python3 -m compileall -q src tests

clean:
	rm -rf build dist .coverage
