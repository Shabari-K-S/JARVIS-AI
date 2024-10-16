# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Available commands:"
	@echo "  make setup    : Set up the virtual environment and install dependencies"
	@echo "  make start    : Start the application"
	@echo "  make test     : Run the test suite"
	@echo "  make lint     : Run linter (flake8)"
	@echo "  make format   : Format code (black)"
	@echo "  make clean    : Remove virtual environment and cached files"

# Set up virtual environment and install dependencies
setup:
	python3 -m venv $(VENV)
	source $(VENV)/bin/activate
	$(PIP) install -r requirements.txt
	$(PIP) install flake8 black pytest
	$(PYTHON) -m jarvis.config

# Start the application
start:
	$(PYTHON) -m jarvis.main

# Run tests
test:
	$(PYTHON) -m pytest tests/

# Run linter
lint:
	$(PYTHON) -m flake8 jarvis/ tests/

# Format code
format:
	$(PYTHON) -m black jarvis/ tests/

# Clean up
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.PHONY: help setup start test lint format clean