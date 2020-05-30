
from moodle_questions.questions.abstract import Question


class TrueFalseQuestion(Question):
    """
    This class represents true/false question.
    """
    _type = "truefalse"
    _allow_combined_feedback = False
    _allow_multiple_tries = False

    def __init__(self, *args, **kwargs):
        super(TrueFalseQuestion, self).__init__(*args, **kwargs)

    def add_answer(self):
        raise NotImplementedError