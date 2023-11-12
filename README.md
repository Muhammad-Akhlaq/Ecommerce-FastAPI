# E-Commerce Backend FastAPI Documentation

## Table of Contents

- [Introduction](#introduction)
- [Setup Instructions](#setup-instructions)
- [Pre-Commits](#pre-commits)
- [Dependencies](#dependencies)
- [Additional Information](#additional-information)

## Introduction

Welcome to the E-Commerce Admin API documentation. This API powers a web admin dashboard for e-commerce managers,
providing insights into sales, revenue, product management, and inventory control. It's implemented using Python and
FastAPI.

## Setup Instructions

To set up and run the E-Commerce Admin API on your local machine, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   ```
2. **Create and Activate Virtual Environment**

To create virtual environment, use the following command.

```shell
python -m venv venv
```

To activate virtual environment, use the following command.

```shell
source venv/bin/activate
```

3. **Install Dependencies**:

Ensure you have Python 3.9 or higher installed. Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
   ```

4. **Database Configuration**:

Create a [.env](.env) file and set DATABASE_URL to connect with your database.
```bash
cp sample.env .env
   ```
```
DATABASE_URL=postgresql://<username>:<passowrd>@<host>:<port>/<database_name>
ALEMBIC_DATABASE_URL=postgresql://<username>:<passowrd>@<host>:<port>/<database_name>
```

5. **Database Migrations**:

- Initialize the Alembic environment:

```bash
alembic init alembic
```

- Modify the `alembic.ini` file to specify the correct database URL.

- Generate an initial migration:

```bash
alembic revision --autogenerate -m "initial"
```

- Apply the migration to create the database tables:

```bash
alembic upgrade head
```

Additionally, if you want to load data to the database, run the following command

```bash
python scripts/load_data.py 
 ```

6. **Run the Application**:

Start the FastAPI application:

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

Customize the host and port to your preferences.

7.**Access the API**:

The API will be available at `http://localhost:8000`. You can now make requests to the provided endpoints.

## Pre-Commits

The project utilizes pre-commit hooks to enforce code quality and maintain consistency in the codebase. This section provides instructions on how to install and use pre-commit in the project.

## Available Pre-commit Hooks

The pre-commit configuration in this project includes the following pre-commit hooks:

- trailing-whitespace: Checks for trailing whitespace at the end of lines.
- end-of-file-fixer: Ensures that files end with a newline character.
- check-yaml: Validates YAML files for syntax errors.
- check-added-large-files: Prevents the addition of large files to the repository.
- black: Enforces Python code formatting using the Black formatter.
- autoflake: Removes unused imports and variables from Python code.
- flake8: Performs code linting and static analysis.

### Installation

1. Install as git hook:
   ```bash
   pre-commit install
   ```
### Usage

1. Auto Use: when ever you try to commit then above hooks will run on changed code.
2. Manual Run:
   ```bash
   pre-commit run --all-files
   ```

## Dependencies

The E-commerce Admin API relies on several libraries and tools, including:

- Python 3.9
- FastAPI: A fast web framework for building APIs with Python.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library.
- PostgreSQL: A powerful open-source relational database system for data storage.
- Alembic: A database migration tool for managing schema changes.
- Pydantic: A powerful tool for schema validation

You must install these dependencies as described in the "Setup Instructions" section.

## Additional Information

- The API allows you to create and manage categories, products, and sales, while also providing inventory tracking.
- All data is stored in a PostgreSQL database with well-defined schemas.
- You can use the endpoints to retrieve, filter, analyze, and manage various aspects of your e-commerce business.
- Detailed API documentation is available for each endpoint, along with information about request parameters and
  response structures.
