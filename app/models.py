from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Column[UUID] = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    name: Column[str] = Column(String, index=True)
    email: Column[str] = Column(String, unique=True, index=True)
    hashed_password: Column[str] = Column(String, index=True)
