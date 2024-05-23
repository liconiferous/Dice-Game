#Makefile

setup:
	python -m venv .venv
	python install -r requirements.txt

run:
	python src/main.py

test:
	coverage run -m unittest discover -s tests

coverage:
	coverage report -m
	coverage html
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	flake8 src tests
	pylint src tests

doc:
	pdoc --html -o doc/api src
	@echo "API documentation generated in doc/api"

uml:
	plantuml -o doc/uml src
	@echo "UML diagrams generated in doc/uml"

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf doc/api
	rm -rf doc/uml

format:
	.venv/bin/black src tests