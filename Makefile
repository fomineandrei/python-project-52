install:
	uv sync

lint:
	uv run ruff check

check: 
	test lint

collectstatic:
	uv run manage.py collectstatic --noinput

migrate:
	uv run manage.py makemigrations

build:
	./build.sh

dev:
	uv run manage.py runserver 

start:
	uv run gunicorn task_manager.wsgi

render-start:
	gunicorn task_manager.wsgi

.PHONY: install test lint check build
