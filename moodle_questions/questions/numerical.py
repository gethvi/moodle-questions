from moodle_questions.questions.abstract import Question
from moodle_questions.answer import NumericalAnswer

class NumericalQuestion(Question):
    """
    This class represents 'Numerical Question' moodle question type.
    Units are currently not implemented, only numerical answer, which
    are specified as text and absolute tolerance value are implemented
    """
    _type = "numerical"
    _allow_combined_feedback = True
    _allow_multiple_tries = False

    def __init__(self, *args, **kwargs):
        super(NumericalQuestion, self).__init__(*args, **kwargs)
        self.answers = []

    def _to_xml_element(self):
        question = super(NumericalQuestion, self)._to_xml_element()

        for answer in self.answers:
            question.append(answer._to_xml_element())

        return question

    def add_answer(self, tol, fraction, text, feedback=None):
        self.answers.append(NumericalAnswer(tol, fraction, text, feedback))
