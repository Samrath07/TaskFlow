from fastapi import FastAPI
from schemas.job import JobCreate, JobCreatedResponse,JobResponse
from service.job import create_job, get_job

app = FastAPI()

@app.post("/job", status_code=202, response_model=JobCreatedResponse)
def create_job_endpoint(job: JobCreate):
    return create_job(job)

@app.get("/job/{job_id}", status_code=200, response_model=JobResponse)
def get_job_endpoint(job_id: int):
    return get_job(job_id)

@app.get("/health")
def health():
    return {"status" : "ok", "message ": "Connected to FastAPI!"}

