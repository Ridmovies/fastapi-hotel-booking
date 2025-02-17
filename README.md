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

---


## Built With

1. FastAPI – A modern, fast, and lightweight web framework for building APIs with Python.
2. SQLAdmin – An automatic admin interface generator for FastAPI applications.
3. PostgreSQL – A powerful, open-source object-relational database system.
4. AsyncPG – A PostgreSQL client library built on top of asyncio for asynchronous operations in Python.
5. SQLAlchemy – The Python SQL toolkit and Object Relational Mapper that provides full support for SQL Alchemy Core and ORM.
6. Celery – A distributed task queue that can be used to execute tasks asynchronously or periodically.
7. Redis – An in-memory data structure store, used as a database, cache, and message broker.
8. Alembic – A lightweight migration tool for relational databases that supports versioning and schema changes.
9. FastAPI Versioning – A package that adds URL versioning capabilities to FastAPI applications.
10. FastAPI Cache2 – A caching solution for FastAPI applications using Redis or other backends.
11. Prometheus FastAPI Instrumentator – A Prometheus metrics exporter for FastAPI applications.
12. Sentry SDK – A real-time error tracking and monitoring tool for Python applications.
13. Pydantic Settings – A settings management library based on Pydantic models.
14. Python JSON Logger – A structured logging library for Python that outputs logs in JSON format.
15. Jinja2 – A popular templating engine for Python, often used in web development.
16. Flower – A web-based tool for monitoring and administrating Celery clusters and tasks.
17. Bcrypt – A password hashing function designed to be slow and resistant to brute-force attacks.
18. PyJWT – A Python implementation of the JSON Web Token (JWT) standard.
19. Pytest – A testing framework for writing small and scalable tests in Python.
20. Pytest Asyncio – A plugin for Pytest that allows testing async code written with the asyncio module.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- pip (Python package installer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

___


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
   
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
4. Create .env file:
* Rename '.env.template' to '.env'
* Create local postgres database
* Replace the settings with your own

5. Update the database to the latest migration version:
    ```bash
    alembic upgrade head
    ```


6. Running the Application:
    ```bash
    uvicorn src.main:app --reload
    ```

The application will be available at http://127.0.0.1:8000/v1/docs


<p align="right">(<a href="#readme-top">back to top</a>)</p>

___


### Installation for Linux with docker-compose (postgres database version)

*  #### Clone the repo
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```
  
* ### Install Docker Engine
- https://docs.docker.com/engine/install/
- https://docs.docker.com/engine/install/ubuntu/

* #### Enter the application root folder: 
    ```bash
   cd your-repo-name
    ```

### Build a new image and run containers
```bash
docker-compose up --build
```

The application will be available at http://127.0.0.1:5000/v1/docs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

___


### API Documentation

FastAPI automatically generates interactive API documentation (5000 port if run in docker compose):

    Swagger UI: http://127.0.0.1:8000/docs

    or Swagger UI v1: http://127.0.0.1:8000/v1/docs

    ReDoc: http://127.0.0.1:8000/redoc

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
pyright ./src/main.py
```

___

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Commands for Working with Docker and Docker Compose
These commands will help you manage containers and images in your project, 
ensuring a smooth development and testing process.

### Building an Image from a Dockerfile
```bash
docker build -t booking .
```

### Running a Container from an Image
```bash
docker run -p 9000:8000 booking
```

### Delete All Containers
```bash
docker rm $(docker ps -aq)
```

### Delete All Images
```bash
docker rmi $(docker images -q)
```

### Stopping and Removing All Services and Images
```bash
docker-compose down --rmi all
```

### Accessing the Console Inside a Running Docker Container
```bash
docker exec -it container_name bash 
```

### Building a New Image
This command builds a new image based on the instructions in docker-compose.yml.
```bash
docker-compose build
```

___

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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


<p align="right">(<a href="#readme-top">back to top</a>)</p>

___
