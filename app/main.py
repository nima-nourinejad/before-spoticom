# 1
from sqlalchemy import create_engine

user = "postgres"
password = "123456"
db_name = "game"
host_port = "localhost:5432"
prefix = "postgresql+psycopg"
URL_DATABASE = f"{prefix}://{user}:{password}@{host_port}/{db_name}"
engine = create_engine(URL_DATABASE)

# 2
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 3
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)


class Choices(Base):
    __tablename__ = "choices"
    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))


# 4
Base.metadata.create_all(bind=engine)

# 5
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI()


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Depends(get_db)

from sqlalchemy.orm import Session


@app.post("/questions/")
def create_questions(question: QuestionBase, db: Session = Depends(get_db)):
    db_question = Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id,
        )
        db.add(db_choice)
    db.commit()
