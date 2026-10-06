from fastapi import FastAPI
from schemas.job import JobCreate, JobCreatedResponse
from service.job import create_job

app = FastAPI()

@app.post("/job", status_code=202, response_model=JobCreatedResponse)
def create_job_endpoint(job: JobCreate):
    return create_job(job)


@app.get("/health")
def health():
    return {"status" : "ok", "message ": "Connected to FastAPI!"}

