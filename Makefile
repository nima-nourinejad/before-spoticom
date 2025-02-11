PYTHON = python3
PIP = pip
UVICORN = uvicorn
VENV = venv
REQUIREMENTS_FILE = requirements.txt
ALEMBIC_DIR = alembic
USER = postgres
PASSWORD = 123456
DB_NAME = game
HOST_PORT = localhost:5432
PREFIX = postgresql+psycopg2
MAIN_MODULE = app.main:app

.PHONY: setup run upgrade downgrade format check test clean help

setup:
	@if [ ! -d $(VENV) ]; then \
		$(PYTHON) -m venv $(VENV); \
	fi
	$(VENV)/bin/$(PIP) install -r $(REQUIREMENTS_FILE)

	@if [ ! -d $(ALEMBIC_DIR) ]; then \
		$(VENV)/bin/alembic init $(ALEMBIC_DIR); \
	fi
	@sed -i 's|^sqlalchemy.url = .*|sqlalchemy.url = ${PREFIX}://$(USER):$(PASSWORD)@$(HOST_PORT)/$(DB_NAME)|' alembic.ini
	@if [ -z "$$( $(VENV)/bin/alembic heads )" ]; then \
		$(VENV)/bin/alembic revision --autogenerate -m "Initial migration"; \
		$(VENV)/bin/alembic upgrade head; \
	fi



upgrade:
	@if ! $(VENV)/bin/alembic current | grep -q $(VENV)/bin/alembic heads; then \
		$(VENV)/bin/alembic revision --autogenerate -m "Updated schema"; \
	fi
	$(VENV)/bin/alembic upgrade head


downgrade:
	$(VENV)/bin/alembic downgrade -1


run:
	@if [ ! -d $(VENV) ]; then \
		$(MAKE) setup; \
	fi
	$(VENV)/bin/$(UVICORN) $(MAIN_MODULE) --reload


format:
	$(VENV)/bin/black app


check:
	$(VENV)/bin/pylint --disable=missing-docstring app


clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete


help:
	@echo "Available targets:"
	@echo "  setup           Set up the virtual environment and install dependencies"
	@echo "  run             Start the application server"
	@echo "  upgrade         Generate and apply database migrations"
	@echo "  downgrade       Roll back the last database migration"
	@echo "  format          Auto-format Python files"
	@echo "  check           Run static analysis using Pylint"
	@echo "  test            Run unit tests using pytest"
	@echo "  clean           Remove virtual environment and cached files (keep Alembic migrations)"
