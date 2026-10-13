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
    



# def get_job(job_id: int):
#     if not JOBS_FILE.exists():
#         raise JobNotFoundError(job_id)

#     with open(JOBS_FILE, "r") as file:
#         jobs = json.load(file)

#     try:
#         return jobs[str(job_id)]
#     except KeyError:
#         raise JobNotFoundError(job_id)