test: lint
	poetry run pytest

lint:
	poetry run black .