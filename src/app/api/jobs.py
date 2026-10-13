from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.job import JobCreate, JobResponse
from app.service.job import create_job_service, get_job_id_service,get_job_service

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("", response_model=JobResponse, status_code=201)
def create_job(
    request: JobCreate,
    db: Session = Depends(get_db),
):
    return create_job_service(request, db)

@router.get("", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return get_job_service(db)

@router.get("/{job_id}", response_model=JobResponse)
def get_job_by_id(
    job_id: str,
    db: Session = Depends(get_db),
):
    return get_job_id_service(job_id, db)