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

lint: flake8 mypy pydocstyle

format: isort black
