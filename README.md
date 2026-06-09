# Task Tracker API

A simple REST API built with FastAPI for managing tasks.

## What it does

This API allows users to:

* Create tasks
* View all tasks
* View a specific task
* Update a task
* Mark a task as completed
* Delete a task

The project uses in-memory storage, making it lightweight and easy to run locally.

## Running Locally

Install dependencies:

pip install -r requirements.txt

Start the API:

uvicorn app.main:app --reload

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

* GET /health
* GET /tasks
* GET /tasks/{task_id}
* POST /tasks
* PUT /tasks/{task_id}
* PATCH /tasks/{task_id}/complete
* DELETE /tasks/{task_id}

## Deployment

Live API:
https://task-tracker-api-ifoq.onrender.com

Interactive Documentation:
https://task-tracker-api-ifoq.onrender.com/docs
