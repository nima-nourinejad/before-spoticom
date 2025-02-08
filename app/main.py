from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from .schemas import QuestionBase
from .models import Questions, Choices
from .database import engine, Base


app = FastAPI()


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Depends(get_db)


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
