# Define the virtual environment directory and executables
VENV := ./.venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest

.PHONY: venv dependencies black black-check unit


# Install dependencies into the virtual environment
dependencies:
	$(PIP) install -r requirements.txt

# Run black using the venv's python
black:
	$(PYTHON) -m black .

black-check:
	$(PYTHON) -m black --check .

# Run pytest from the venv
unit:
	$(PYTEST) ./tests/unit/

docker-build:
	docker build -t clock_api -f ./docker/Dockerfile .

docker-start:
	docker run --rm -d -p 5000:5000 --name clock-api -e CLOCK_URL=$CLOCK_URL clock_api

docker-stop:
	docker stop clock-api

docker-rm:
	docker rm clock-api