# Define variables
PYTHON = python3
PIP = pip
UVICORN = uvicorn
VENV = venv
REQUIREMENTS_FILE = requirements.txt
MAIN_MODULE = app.main:app

# Define .PHONY targets
.PHONY: help setup run clean

# Default target
help:
	@echo "Available targets:"
	@echo "  setup           Set up the virtual environment and install dependencies"
	@echo "  run             Start the application server"
	@echo "  clean           Clean up cached files and the virtual environment"

# Set up virtual environment and install dependencies
setup:
	@if [ ! -d $(VENV) ]; then \
		$(PYTHON) -m venv $(VENV); \
	fi
	$(VENV)/bin/$(PIP) install -r $(REQUIREMENTS_FILE)

# Start the application server
run:
	@if [ ! -d $(VENV) ]; then \
		$(MAKE) setup; \
	fi
	$(VENV)/bin/$(UVICORN) $(MAIN_MODULE) --reload

# Clean up cached files and the virtual environment
clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete


