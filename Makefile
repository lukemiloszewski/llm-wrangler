init:
	poetry config virtualenvs.in-project true
	poetry install

test:
	poetry run pytest tests -v --cov

publish:
	poetry publish --build

doc:
	poetry run mkdocs serve

requirements:
	poetry export -f requirements.txt --output requirements.txt

lint:
	poetry run ruff check src tests docs
	poetry run ruff format src tests docs --check

format:
	poetry run ruff check src tests docs --fix
	poetry run ruff format src tests docs
