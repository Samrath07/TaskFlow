from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv() 


DATABASE_URL = os.environ['POSTGRES_URL']
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

