from app.schemas.job import JobCreate
from app.models.job import Job

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db


def create_job_service(job: JobCreate, db: Session = Depends(get_db)):
    job = Job(
        type=job.type,
        payload=job.payload
    )

    try:
        db.add(job)
        db.commit()
        db.refresh(job)
        return job

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create job") from e


def get_job_service(db: Session):
    return db.query(Job).order_by(Job.created_at.desc()).all()

def get_job_id_service(job_id: str, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job