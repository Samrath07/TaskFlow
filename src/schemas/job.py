from pydantic import BaseModel
from enum import Enum
from typing import Any

class JobCreate(BaseModel):
    type:str
    payload: dict[str,Any]

class JobStatus(Enum):
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobResponse(BaseModel):
    id: int
    type: str
    payload: dict[str, Any]
    status: JobStatus
    created_at: float
    user_id: int | None = None

class JobCreatedResponse(BaseModel):
    message: str
    job: JobResponse

