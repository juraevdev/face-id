from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  

SQLALCHEMY_DATABASE_URL = "postgresql://myuser:davlat@localhost/mydatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
