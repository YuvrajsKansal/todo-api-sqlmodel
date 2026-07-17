# FastAPI Task Manager

A RESTful task management API built with FastAPI, Pydantic, and SQLModel, backed by a SQLite database. Supports full CRUD operations with request validation and persistent storage.

## Features

- Create, read, update, and delete tasks
- Request validation via Pydantic models
- Persistent storage using SQLModel + SQLite
- Auto-generated interactive API docs (Swagger UI)
- Structured project with clean separation between validation schemas and database models

## Tech Stack

- **FastAPI** — web framework
- **Pydantic** — data validation
- **SQLModel** — ORM combining SQLAlchemy and Pydantic
- **SQLite** — database

## Endpoints

| Method | Endpoint          | Description            |
|--------|-------------------|-------------------------|
| GET    | /tasks            | Get all tasks           |
| GET    | /tasks/{task_id}  | Get a single task by ID |
| POST   | /tasks            | Create a new task       |
| PUT    | /tasks/{task_id}  | Update an existing task |
| DELETE | /tasks/{task_id}  | Delete a task            |

## Setup

1. Clone the repo
   git clone https://github.com/your-username/fastapi-task-manager.git
   cd fastapi-task-manager

2. Create a virtual environment
   python -m venv .venv
   .venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the server
   uvicorn main:app --reload

5. Open the interactive docs
   http://127.0.0.1:8000/docs

## Example Request Body (POST /tasks)

{
  "title": "Buy groceries",
  "due_date": "2026-07-20",
  "description": "Milk, eggs, bread"
}

## Project Structure

main.py            # FastAPI app, routes, models, database setup
requirements.txt   # Python dependencies
.gitignore         # Excludes .venv, __pycache__, tasks.db

## Future Improvements

- Response models to control API output shape
- Field-level validation (e.g. restricted priority values)
- Partial updates (PATCH)
- Frontend integration