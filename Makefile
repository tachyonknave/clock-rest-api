VENV := ./venv

.PHONY: dependencies black black-checks

dependencies:
	$(VENV)/bin/pip install -r requirements.txt

black:
	$(VENV)/bin/python -m black .

black-check:
	$(VENV)/bin/python -m black --check .
