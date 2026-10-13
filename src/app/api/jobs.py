from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.job import JobCreate, JobResponse
from app.service.job import create_job_service

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("", response_model=JobResponse, status_code=201)
def create_job(
    request: JobCreate,
    db: Session = Depends(get_db),
):
    return create_job_service(request, db)
    