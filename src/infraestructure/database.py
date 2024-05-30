# infrastructure/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base


DATABASE_URL = 'mssql+pyodbc://localhost\\SQLEXPRESS/test_database?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
