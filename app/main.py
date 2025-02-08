from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import QuestionBase
from .database import Database
from .database_util import DataBaseUtil


app = FastAPI()

database = Database()


@app.post("/questions/")
def create_questions(
    question: QuestionBase, session: Session = Depends(database.get_session)
):

    util = DataBaseUtil(session, question)
    util.add_question()
    util.get_question_id()
    util.add_choices()

    return {"message": "Question and choices created successfully"}
