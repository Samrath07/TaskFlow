from schemas.job import JobCreate,JobResponse
from models.job import Job


def create_job(job: JobCreate):
    new_job = Job(type=job.type, payload=job.payload)
    response = JobResponse(
        id=new_job.id, 
        type=new_job.type, 
        payload=new_job.payload, 
        status=new_job.status,
        created_at=new_job.created_at, 
        user_id=new_job.user_id
    )
    return {"message": "Job created successfully", "job": response}