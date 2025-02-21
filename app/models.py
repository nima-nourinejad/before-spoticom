from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    username: Column[str] = Column(String, index=True)
    email: Column[str] = Column(String, unique=True, index=True)
    hashed_password: Column[str] = Column(String, index=True)
