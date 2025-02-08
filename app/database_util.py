from .models import Questions, Choices


class DataBaseUtil:
    def __init__(self, session, question):
        self.session = session
        self.question = question
        self.choices = question.choices
        self.db_question = None

    def add_question(self):
        db_question = Questions(question_text=self.question.question_text)
        self.session.add(db_question)
        self.session.commit()
        self.db_question = db_question

    def get_question_id(self):
        self.session.refresh(self.db_question)

    def add_choices(self):
        db_choices = [
            Choices(
                choice_text=choice.choice_text,
                is_correct=choice.is_correct,
                question_id=self.db_question.id,
            )
            for choice in self.choices
        ]
        self.session.add_all(db_choices)
        self.session.commit()
