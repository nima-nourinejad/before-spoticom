from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import QuestionBase
from .models import Questions, Choices
from .database import Database


app = FastAPI()

database = Database()


@app.post("/questions/")
def create_questions(
    question: QuestionBase, db: Session = Depends(database.get_session)
):
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
