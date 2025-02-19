from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import QuestionBase
from .database import Database
from .database_util import DataBaseUtil
from typing import Any


app = FastAPI()

database = Database()


@app.post("/questions/")
def create_questions(
    question: QuestionBase, session: Session = Depends(database.get_session)
) -> dict[str, str]:
    database_util = DataBaseUtil(session, question)
    database_util.add_question()
    database_util.get_question_id()
    database_util.add_choices()

    return {"message": "Question and choices created successfully"}


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "I am alive!"}
