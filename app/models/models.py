import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id: Column[uuid.UUID] = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    name: Column[str] = Column(String, index=True)
    email: Column[str] = Column(String, unique=True, index=True)
    hashed_password: Column[str] = Column(String, index=True)
