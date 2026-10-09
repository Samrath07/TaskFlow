from app.schemas.job import JobCreate,JobResponse
from app.models.job import Job
from exceptions import JobNotFoundError
import json
from pathlib import Path
from exceptions import JobAlreadyExistsError
from app.schemas.job import JobCreatedResponse


JOBS_FILE = Path("jobs.json")

def save_job(job: Job):
    if JOBS_FILE.exists():
        with open(JOBS_FILE, "r") as file:
            jobs = json.load(file)
            print(f"Loaded jobs from {JOBS_FILE}: {jobs}")
    else:
        jobs = {}

    job_id = str(job.id)

    if job_id in jobs:
        raise JobAlreadyExistsError(job.id)

    jobs[job_id] = {
        "id": job.id,
        "type": job.type,
        "payload": job.payload,
        "status": job.status.value,
        "created_at": job.created_at,
        "user_id": job.user_id,
    }

    with open(JOBS_FILE, "w") as file:
        json.dump(jobs, file, indent=4)

def create_job(job: JobCreate):
    new_job = Job(
        type=job.type,
        payload=job.payload
    )

    save_job(new_job)

    return JobCreatedResponse(
        message="Job created successfully",
        job=JobResponse(
            id=new_job.id,
            type=new_job.type,
            payload=new_job.payload,
            status=new_job.status,
            created_at=new_job.created_at,
            user_id=new_job.user_id
        )
    )



def get_job(job_id: int):
    if not JOBS_FILE.exists():
        raise JobNotFoundError(job_id)

    with open(JOBS_FILE, "r") as file:
        jobs = json.load(file)

    try:
        return jobs[str(job_id)]
    except KeyError:
        raise JobNotFoundError(job_id)