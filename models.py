from sqlalchemy import Column, Integer, String, Float, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=True)
    email = Column(String, unique=True, nullable=True)
    face_encoding = Column(ARRAY(Float), nullable=True)
    