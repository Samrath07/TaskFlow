from app.db.database import Base, engine
from app.models.job import Job
from sqlalchemy.orm import DeclarativeBase

Base.metadata.create_all(bind=engine)

print("Tables created successfully")