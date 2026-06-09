"""
In-memory task storage.

Tasks live in a Python dictionary keyed by task id.
Data is lost when the server restarts — fine for learning and demos.
"""

from datetime import datetime, timezone
from typing import Dict, List, Optional
from uuid import uuid4

from app.models import Task, TaskCreate, TaskUpdate

# Global in-memory store: { "task-id": Task }
_tasks: Dict[str, Task] = {}


def _utc_now() -> datetime:
    """Return the current UTC time (timezone-aware)."""
    return datetime.now(timezone.utc)


def get_all_tasks() -> List[Task]:
    """Return every task, newest first."""
    return sorted(_tasks.values(), key=lambda t: t.created_at, reverse=True)


def get_task_by_id(task_id: str) -> Optional[Task]:
    """Return a single task or None if it does not exist."""
    return _tasks.get(task_id)


def create_task(data: TaskCreate) -> Task:
    """Create a new task and store it in memory."""
    task = Task(
        id=str(uuid4()),
        title=data.title,
        description=data.description,
        completed=False,
        created_at=_utc_now(),
    )
    _tasks[task.id] = task
    return task


def update_task(task_id: str, data: TaskUpdate) -> Optional[Task]:
    """Replace an existing task. Returns None if task_id is not found."""
    existing = _tasks.get(task_id)
    if existing is None:
        return None

    updated = Task(
        id=task_id,
        title=data.title,
        description=data.description,
        completed=data.completed,
        created_at=existing.created_at,  # keep original creation time
    )
    _tasks[task_id] = updated
    return updated


def complete_task(task_id: str) -> Optional[Task]:
    """Mark a task as completed. Returns None if task_id is not found."""
    existing = _tasks.get(task_id)
    if existing is None:
        return None

    # model_copy lets us change one field without rebuilding the whole object
    completed = existing.model_copy(update={"completed": True})
    _tasks[task_id] = completed
    return completed


def delete_task(task_id: str) -> bool:
    """Delete a task. Returns True if deleted, False if not found."""
    if task_id not in _tasks:
        return False
    del _tasks[task_id]
    return True
