import json
from pathlib import Path

from models.job import Job
from exceptions import JobAlreadyExistsError


JOBS_FILE = Path("jobs.json")


def save_job(job: Job):
    if JOBS_FILE.exists():
        with open(JOBS_FILE, "r") as file:
            jobs = json.load(file)
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
