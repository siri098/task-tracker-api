"""
Task Tracker API — main FastAPI application.

Run locally with:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI, HTTPException, status

from app import storage
from app.models import Task, TaskCreate, TaskUpdate

# Create the FastAPI app instance
app = FastAPI(
    title="Task Tracker API",
    description="A simple REST API for managing tasks (in-memory storage).",
    version="1.0.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    """Simple health check — useful for Render and monitoring."""
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task], tags=["Tasks"])
def list_tasks():
    """Return all tasks."""
    return storage.get_all_tasks()


@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: str):
    """Return a single task by id."""
    task = storage.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id '{task_id}' not found",
        )
    return task


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(data: TaskCreate):
    """Create a new task."""
    return storage.create_task(data)


@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: str, data: TaskUpdate):
    """Replace an existing task (full update)."""
    task = storage.update_task(task_id, data)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id '{task_id}' not found",
        )
    return task


@app.patch("/tasks/{task_id}/complete", response_model=Task, tags=["Tasks"])
def complete_task(task_id: str):
    """Mark a task as completed."""
    task = storage.complete_task(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id '{task_id}' not found",
        )
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: str):
    """Delete a task."""
    deleted = storage.delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id '{task_id}' not found",
        )
    # 204 No Content — no response body
