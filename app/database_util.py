from typing import Optional
from sqlalchemy.orm import Session
from .models import Questions, Choices
from .schemas import QuestionBase, ChoiceBase


class DataBaseUtil:
    def __init__(self, session: Session, question: QuestionBase) -> None:
        self.session: Session = session
        self.question: QuestionBase = question
        self.choices: list[ChoiceBase] = question.choices
        self.db_question: Optional[Questions] = None

    def add_question(self) -> None:
        db_question = Questions(question_text=self.question.question_text)
        self.session.add(db_question)
        self.session.commit()
        self.db_question = db_question

    def get_question_id(self) -> None:
        if self.db_question:
            self.session.refresh(self.db_question)

    def add_choices(self) -> None:
        if not self.db_question:
            raise ValueError("Question must be added before adding choices.")

        db_choices: list[Choices] = [
            Choices(
                choice_text=choice.choice_text,
                is_correct=choice.is_correct,
                question_id=self.db_question.id,
            )
            for choice in self.choices
        ]
        self.session.add_all(db_choices)
        self.session.commit()
