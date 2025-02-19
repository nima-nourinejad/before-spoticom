from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base

class Questions(Base):
    __tablename__ = "questions"
    
    id: Column[int] = Column(Integer, primary_key=True, index=True)
    question_text: Column[str] = Column(String, index=True)


class Choices(Base):
    __tablename__ = "choices"
    
    id: Column[int] = Column(Integer, primary_key=True, index=True)
    choice_text: Column[str] = Column(String, index=True)
    is_correct: Column[bool] = Column(Boolean, default=False)
    question_id: Column[int] = Column(Integer, ForeignKey("questions.id"))
