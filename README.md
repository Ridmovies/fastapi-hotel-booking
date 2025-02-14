<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Асинхронность](https://img.shields.io/badge/-Асинхронность-464646?style=flat-square&logo=Асинхронность)]()
[![Anyio](https://img.shields.io/badge/-Anyio-464646?style=flat-square&logo=Anyio)](https://anyio.readthedocs.io/en/stable/)
[![Cookies](https://img.shields.io/badge/-Cookies-464646?style=flat-square&logo=Cookies)]()
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat-square&logo=JWT)]()
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat-square&logo=Alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat-square&logo=SQLAlchemy)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/-Redis-464646?style=flat-square&logo=Redis)](https://redis.io/)
[![Celery](https://img.shields.io/badge/-Celery-464646?style=flat-square&logo=Celery)](https://docs.celeryq.dev/en/stable/)
[![Sentry](https://img.shields.io/badge/-Sentry-464646?style=flat-square&logo=Sentry)](https://sentry.io/welcome/)
[![Prometheus](https://img.shields.io/badge/-Prometheus-464646?style=flat-square&logo=Prometheus)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/-Grafana-464646?style=flat-square&logo=Grafana)](https://grafana.com/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?style=flat-square&logo=uvicorn)](https://www.uvicorn.org/)
[![Gunicorn](https://img.shields.io/badge/-Gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)

<!-- PROJECT NAME -->
<h2 align="center">Fastapi Hotel Booking</h2>


<!-- DESCRIPTION -->
<h4 align="center">
Hotel booking service. Users can book the desired type of hotel room for a specific date.
</h4>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

___
## Develop 

### Start your application using Uvicorn in root folder :
 ``` 
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload 
```

### Poetry Dependency Management System
### Creating a New Project

```bash
poetry new my-project
```
This command will create a new project structure with a `pyproject.toml` file where dependencies are stored.

### Initializing an Existing Project
```bash
poetry init
```

This command initializes the project by asking for necessary parameters and creating a `pyproject.toml` file.

### Adding a Package
```bash
poetry add requests
```
Adds the `requests` package to your project's list of dependencies.
To add a package under the `[tool.poetry.dev-dependencies]` section in the `pyproject.toml` file, use the following command:
```bash
poetry add black --group dev
```
### Updating All Packages
```bash
poetry update
```
Updates all packages to their latest compatible versions.

### Synchronizing Poetry with Virtual Environment
```bash
poetry install --sync
```
### Showing the Package Tree
```bash
poetry show --tree
```
### Removing a Package
```bash
poetry remove <package_name>
```
___

## PostgreSQL
## Creating a PostgreSQL database via console
### 1: Connecting to PostgreSQL shell
```bash
sudo -u postgres psql
```

### 2: Creating a new database
```bash
CREATE DATABASE database_name;
```

___

## Alembic

### Creating async an Environment
```bash
alembic init --template async alembic
```

### change env.py
?async_fallback=True param for async database
```
config = context.config
# if don't use --template async
# config.set_main_option("sqlalchemy.url", f"{settings.DATABASE_URL}?async_fallback=True")
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
target_metadata = Base.metadata
```
Import models
```
from src.backend.dev.models import Song # noqa
from src.backend.products.models import Product # noqa
```

### Generate first migration
```bash
alembic revision --autogenerate -m "initial migration"
```

### Apply generated migration to the database:
```bash
alembic upgrade head
```

### Rolls back the last applied migration.
```bash
alembic downgrade -1
```
___


## Celery
### Starting a workflow
```bash
celery -A src.tasks.tasks:celery worker -l INFO
```
app.tasks.tasks:celery - This is the path to the Celery() instance

### Launching the scheduler
To start the celery beat service:
```bash
celery -A store beat -l INFO
```

### Launching Flower
```bash
celery -A src.tasks.tasks:celery flower
```
web-interface: http://0.0.0.0:5555/

___

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Linters and formats:
```bash
black --check --diff --color ./src/main.py
```

```bash
flake8  ./src/main.py
```

```bash
isort --check-only --diff --color --profile black ./src/main.py

```bash
mypy --incremental ./src/main.py
```

```bash
autoflake ./src/main.py
```

```bash
pyright .
```


## Useful links:
SQLAlchemy 2.0 Documentation:
https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.asyncpg

SQLAlchemy 2.0 Relationship Patterns:
https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html

Pydantic Settings Management:
https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage

OAuth2 with Password (and hashing), Bearer with JWT tokens:
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords

bcrypt:
https://pypi.org/project/bcrypt/

fastapi-cache:
https://github.com/long2ice/fastapi-cache

Celery - Distributed Task Queue:
https://docs.celeryq.dev/en/stable/getting-started/index.html

Background Tasks:
https://fastapi.tiangolo.com/tutorial/background-tasks/

SQLAlchemy Admin for Starlette/FastAPI:
https://aminalaee.dev/sqladmin/
___
