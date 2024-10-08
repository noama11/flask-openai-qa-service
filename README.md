# flask-openai-qa-service

# Flask Application with OpenAI Integration

## Description

This project is a Flask-based application integrating with OpenAI's API to provide answers to user questions. It uses PostgreSQL as its database and Docker for deployment.

## Key Features

- Dynamic interaction using OpenAI's GPT models.
- Robust data management with PostgreSQL.
- Easy setup with Docker containerization.
- Database migrations with Alembic.
- Testing environment setup with pytest.

## Project Structure

- `/app`: Flask application code including routes, configurations, and utilities.
- `/migrations`: Contains Alembic database migration scripts.
- `/tests`: Holds pytest tests for application endpoints and functionality.
- `Dockerfile`: Docker configuration for setting up the Flask application.
- `docker-compose.yml`: Orchestrates the application and database services using Docker.

## Environment Configuration

### Setting Up the `.env` File

Create an `.env` file in your project's root to manage environment variables crucial for running the application:

- **OPENAI_API_KEY**: The API key for accessing OpenAI's services.
- **DATABASE_URL**: Connection string for the PostgreSQL database, which includes the username, password, host, and database name.
- **POSTGRES_USER**: Username for the PostgreSQL database.
- **POSTGRES_PASSWORD**: Password for the PostgreSQL database.
- **POSTGRES_DB**: Name of the PostgreSQL database to use.
- **FLASK_APP**: Entry point of your Flask application.
- **FLASK_ENV**: Sets the environment in which the Flask app runs (`development`, `production`, or `testing`).
- **FLASK_RUN_HOST**: The host IP address Flask will use (typically `0.0.0.0` to run on all interfaces).
- **FLASK_RUN_PORT**: The port Flask will use (default is 5000).

## Prerequisites

Before starting, ensure you have the following installed:

- Docker
- Docker Compose
- Git (for version control)

## Setup

1. Install Docker and Docker Compose.
2. Clone the repository.
3. Navigate to the cloned directory and run `docker-compose up --build`.

## Running Tests

To run tests, execute the following command:

```bash
docker-compose run web pytest
```

## Database Migrations with Alembic

Alembic is used for handling database migrations. The configuration and migration scripts are located in the /migrations folder.
reate and apply migrations:

- docker-compose run web alembic revision --autogenerate -m "Your changes"
- docker-compose run web alembic upgrade head

Revert migrations: docker-compose run web alembic downgrade -1

## Docker and Database Configuration

- Flask Dockerfile: Sets up the Python environment and installs dependencies.
- PostgreSQL: Uses the official PostgreSQL Docker image configured via docker-compose.yml.

Shutdown:docker-compose down -v

## Entry Point Script

### Purpose and Usage of `entrypoint.sh`

The `entrypoint.sh` script automates several startup tasks:

- Checks if the PostgreSQL database is ready.
- Applies Alembic migrations to update the database schema.
- Starts the Flask application.

**Script Actions:**
