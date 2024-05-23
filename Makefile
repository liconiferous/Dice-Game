### Makefile

Update your `Makefile` to include targets for running tests, generating coverage reports, and other tasks:

```makefile
.PHONY: test coverage lint doc uml run

test:
    python -m unittest discover -s tests

coverage:
    coverage run -m unittest discover -s tests
    coverage report -m
    coverage html

lint:
    pylint src/*.py
    flake8 src --docstring-convention google

doc:
    sphinx-apidoc -o doc/api src
    sphinx-build -b html doc/api doc/api/_build

uml:
    pyreverse -o png -p Dice-Game src
    mv *.png doc/uml

run:
    python src/main.py