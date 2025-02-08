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
    db_choices = [
        Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id,
        )
        for choice in question.choices
    ]
    db.add_all(db_choices)
    db.commit()
    return "Question created successfully"
