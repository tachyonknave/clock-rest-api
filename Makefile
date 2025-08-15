# Define the  executables
PYTHON := python
PIP := pip
PYTEST := pytest
DOCKER := docker

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

integration:
	behave tests/functional/features

docker-build:
	$(DOCKER) build -t clock_api -f ./docker/Dockerfile .

docker-start:
	$(DOCKER) run --rm -d -p 5000:5000 --name clock-api -e CLOCK_URL=$CLOCK_URL clock_api

docker-stop:
	$(DOCKER) stop clock-api

docker-rm:
	$(DOCKER) rm clock-api