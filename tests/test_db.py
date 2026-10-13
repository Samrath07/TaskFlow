from app.db.database import SessionLocal
from app.models.job import Job


def main():
    with SessionLocal() as session:
        try:
            job = Job(
                type="email",
                payload={
                    "to": "user@example.com",
                    "subject": "Welcome",
                },
            )

            session.add(job)
            session.commit()
            session.refresh(job)

            print(f"Created job: {job.id}")

        except Exception:
            session.rollback()
            raise


if __name__ == "__main__":
    main()