SHELL := /bin/sh

POETRY ?= poetry
PYTHON ?= python

.DEFAULT_GOAL := help

.PHONY: help check-poetry setup install test test-verbose check env-info lock clean

help: ## Show available commands.
	@printf '%s\n' \
		'Available commands:' \
		'  make setup         Validate the project and install dependencies.' \
		'  make install       Install dependencies from poetry.lock.' \
		'  make test          Run the full test suite.' \
		'  make test-verbose  Run the full test suite with verbose output.' \
		'  make check         Validate Poetry configuration and run tests.' \
		'  make env-info      Show Poetry environment information.' \
		'  make lock          Refresh poetry.lock.' \
		'  make clean         Remove Python and test cache files.'

check-poetry:
	@command -v $(POETRY) >/dev/null 2>&1 || { \
		echo 'Poetry is required. Install it from https://python-poetry.org/docs/'; \
		exit 1; \
	}

setup: check-poetry
	$(POETRY) check
	$(POETRY) install

install: check-poetry
	$(POETRY) install

test: check-poetry
	$(POETRY) run $(PYTHON) -m unittest discover -s tests

test-verbose: check-poetry
	$(POETRY) run $(PYTHON) -m unittest discover -s tests -v

check: check-poetry
	$(POETRY) check
	$(POETRY) run $(PYTHON) -m unittest discover -s tests -v

env-info: check-poetry
	$(POETRY) env info

lock: check-poetry
	$(POETRY) lock

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f \( -name '*.py[co]' -o -name '.coverage' \) -delete
	find . -type d \( -name '.pytest_cache' -o -name '.mypy_cache' -o -name '.ruff_cache' \) -prune -exec rm -rf {} +
