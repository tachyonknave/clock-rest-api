VENV := ./venv

.PHONY: black

black:
	$(VENV)/bin/python -m black .

black-check:
	$(VENV)/bin/python -m black --check .
