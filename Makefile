install:
	uv sync

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=task_manager --cov-report=xml:coverage.xml

check: 
	test lint

collectstatic:
	uv run manage.py collectstatic --clear --noinput

migrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

build:
	./build.sh

dev:
	uv run manage.py runserver 

start:
	uv run gunicorn task_manager.wsgi

render-start:
	gunicorn task_manager.wsgi

.PHONY: install test lint check build
