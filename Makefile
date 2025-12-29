define USAGE
Super awesome hand-crafted build system ⚙️

Commands:
	setup     Install dependencies, dev included
	lock      Generate requirements.txt
	test      Run tests
	lint      Run linting tests
	run       Run docker image with --rm flag but mounted dirs.
	release   Publish docker image based on some variables
	docker    Build the docker image
	tag    	  Make a git tag using version from pyproject.toml

endef

export USAGE
.EXPORT_ALL_VARIABLES:
GIT_TAG := $(shell git describe --tags)
BUILD := $(shell git rev-parse --short HEAD)
VERSION := $(shell python3 -c "import tomllib; print(tomllib.load(open('pyproject.toml','rb'))['project']['version'])")
PROJECTNAME := $(shell basename "$(PWD)")
DOCKERID = $(shell echo "nuxion")
IP=127.0.0.1
PORT=8000

help:
	@echo "$$USAGE"

setup:
	uv sync

clean:
	find . ! -path "./.eggs/*" -name "*.pyc" -exec rm {} \;
	find . ! -path "./.eggs/*" -name "*.pyo" -exec rm {} \;
	find . ! -path "./.eggs/*" -name ".coverage" -exec rm {} \;
	rm -rf build/* > /dev/null 2>&1
	rm -rf dist/* > /dev/null 2>&1
	rm -rf .ipynb_checkpoints/* > /dev/null 2>&1
	rm -rf docker/client/dist
	rm -rf docker/all/dist

lock:
	uv export --no-hashes -o requirements.txt

lint:
	uv run ruff check

check:
	uv run mypy -p apps --exclude tests

format:
	uv run ruff check --fix

.PHONY: test
test:
	PYTHONPATH=$(PWD) uv run pytest --cov-report xml --cov=labfunctions tests/

.PHONY: docs-server
docs-serve:
	uv run sphinx-autobuild docs/source docs/build/html --port 9292 --watch ./

## Standard commands for CI/CD cycle

deploy:
	echo "Not implemented"

build-local:
	docker build . -t ${DOCKERID}/${PROJECTNAME}
	docker tag ${DOCKERID}/${PROJECTNAME} ${DOCKERID}/${PROJECTNAME}:${VERSION}

build:
	echo "Not implemented"

publish:
	echo "Not implemented"

create-app:
	mkdir -p apps/${NAME}
	uv run python3 manage.py startapp ${NAME} apps/${NAME}

run:
	uv run python3 manage.py runserver ${IP}:${PORT}

secret-key:
	uv run python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

admin:
	uv run python3 manage.py createsuperuser

static:
	uv run python3 manage.py collectstatic


