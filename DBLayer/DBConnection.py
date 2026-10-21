from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from CommonLayer.config import DB_URL


engine=create_engine(DB_URL)

SessionLocal= sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base= declarative_base()


