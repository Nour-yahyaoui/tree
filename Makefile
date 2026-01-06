PYTHON ?= python3
SRC := src

.PHONY: test clean

test:
	python3 -m unittest discover -s tests -t .

clean:
	rm -rf build dist .coverage
