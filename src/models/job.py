import time
from typing import Any
from schemas.job import JobStatus
import uuid
class Job:
    def __init__(self, type: str, payload: dict[str, Any]):
        self.id = uuid.uuid4().int >> 64  # Generate a unique ID
        self.type = type
        self.payload = payload
        self.status = JobStatus.QUEUED
        self.created_at = time.time()
        self.user_id = None
        self.max_retries = 5
        self.retry_count = 0