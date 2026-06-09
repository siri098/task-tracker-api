"""
Pydantic models for request validation and API responses.

Pydantic checks that incoming data has the right types and required fields
before our route handlers run.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """Fields shared by create and update requests."""

    title: str = Field(..., min_length=1, max_length=200, description="Short task title")
    description: str = Field(
        default="",
        max_length=2000,
        description="Optional longer description",
    )


class TaskCreate(TaskBase):
    """Body for POST /tasks — only title and description are required."""

    pass


class TaskUpdate(BaseModel):
    """Body for PUT /tasks/{task_id} — all fields can be updated."""

    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(default="", max_length=2000)
    completed: bool = False


class Task(TaskBase):
    """Full task as returned by the API."""

    id: str
    completed: bool = False
    created_at: datetime

    # Allow creating Task objects from plain dicts (used by our storage layer)
    model_config = {"from_attributes": True}
