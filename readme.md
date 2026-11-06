# FastAPI User Management API

A backend application demonstrating secure user and account management through RESTful APIs. The project uses FastAPI, asynchronous SQLAlchemy database access, OAuth2 bearer-token authentication, and structured request/response schemas.

## Key capabilities

- User CRUD endpoints built with FastAPI routers and service-layer organization
- OAuth2 password flow and JWT access-token handling
- Role-based access checks for protected user operations
- Asynchronous database access with SQLAlchemy
- Pagination support and HATEOAS-style navigation links in API responses
- Profile fields and image-upload support
- Database migrations managed with Alembic
- Automated tests configured with Pytest

## Technology

- Python, FastAPI, Pydantic
- SQLAlchemy, Alembic
- PostgreSQL / MySQL drivers (see `requirements.txt`)
- OAuth2, JWT, bcrypt
- Docker Compose, Pytest

## Project structure

- `app/routers` — API route definitions
- `app/services` — application and business logic
- `app/schemas` — request and response models
- `app/dependencies` — database and authentication dependencies
- `alembic/` — database migration scripts
- `tests/` — automated tests

## Getting started

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database and application environment variables using the project setup documentation.
5. Apply migrations and start the FastAPI application using the commands in [setup.md](setup.md).

## Documentation

- [Setup instructions](setup.md)
- [System documentation](system_documentation.md)
- [Feature notes](features.md)
- [Project overview](about.md)

## Notes

This repository began as an NJIT course project. The codebase and documentation reflect the project implementation and iterative QA, testing, and feature work.