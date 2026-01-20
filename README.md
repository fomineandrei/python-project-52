[![Actions Status](https://github.com/fomineandrei/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/fomineandrei/python-project-52/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fomineandrei_python-project-52&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fomineandrei_python-project-52)
[![LinterAndTests](https://github.com/fomineandrei/python-project-52/actions/workflows/app-tests.yml/badge.svg)](https://github.com/fomineandrei/python-project-52/actions/workflows/app-tests.yml)


# Task Manager app
### This app is task management system built with Django and Python.
### This application provides a comprehensive solution for organizing, tracking, and managing tasks in a collaborative environment.### The system implements user authentication, role-based access control, and flexible task organization using statuses and labels.

## Technologies Used:
| Tool          |                          Info url                                             |
|---------------|-------------------------------------------------------------------------------|
| Django        | [https://www.djangoproject.com/](https://www.djangoproject.com/)              |
| uv            | [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)                      |
| ruff          | [https://docs.astral.sh/ruff/](https://docs.astral.sh/ruff/)                                |
| Gunicorn      | [https://docs.gunicorn.org/en/latest/index.html](https://docs.gunicorn.org/en/latest/index.html)|
| python-dotenv | [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)|
| Bootstrap     | [https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/)|
| django-bootstrap5 | [https://django-bootstrap5.readthedocs.io/en/latest/](https://django-bootstrap5.readthedocs.io/en/latest/) |
| Psycopg       | [https://getbootstrap.com/docs/5.3/getting-started/introduction/](https://getbootstrap.com/docs/5.3/getting-started/introduction/)|
| dj-database-url | [https://pypi.org/project/dj-database-url/](https://pypi.org/project/dj-database-url/) |
| bcrypt        | [https://pypi.org/project/bcrypt/](https://pypi.org/project/bcrypt/)          |
| python-dotenv | [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/) |
| whitenoise    | [https://whitenoise.readthedocs.io/en/stable/](https://whitenoise.readthedocs.io/en/stable/) |
| rollbar       | [https://docs.rollbar.com/docs/getting-started](https://docs.rollbar.com/docs/getting-started) |




## Install:

### This app works with PostgreSQL databases with version at least 4.18
### You must have empty database
### 1. Clone this app with command:
```
git clone git@github.com:fomineandrei/python-project-52.git
```
### 2. Create .env file in root directory. In this file must be two environments:
```
SECRET_KEY='{your_secret_key}'
DATABASE_URL='postgresql://{db_user}:{db_password}@localhost:5432/{db_name}'
CURRENT_HOST='example.com'
DEBUG=0
```
### 3. Install dependencies and database init with command:
```
make build
```
## Run app
### Run app with command:
```
make start
```
### The app will be available from your computer at http://localhost:8000

## For developers
### Start development server with debug mode:
### 1. Change .env file:
```
DEBUG=1
```
### 2. Run app with command:
```
make dev
```
### 3. Open your browser and enter this url: http://localhost:8000

## Tests:

### 1. This app has built-in tests. You can run tests with command:
```
make test
```

## Пример работы приложения можно посмотреть по ссылке:
### [https://python-project-52-8uwo.onrender.com](https://python-project-52-8uwo.onrender.com)