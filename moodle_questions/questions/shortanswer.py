from moodle_questions.answer import Answer
from moodle_questions.questions.abstract import Question


class ShortAnswerQuestion(Question):
    """
    This class represents 'Short answer' question.
    """

    _type = "shortanswer"
    _allow_combined_feedback = True
    _allow_multiple_tries = True

    def __init__(self, *args, **kwargs):
        super(ShortAnswerQuestion, self, ).__init__(*args, **kwargs)
        self.answers = []

    def add_answer(self, fraction, text, feedback=None):
        """
        Adds an answer to this question.
        :type fraction: float
        :param fraction: Percentage of the grade

        :type text: str
        :param text: text of the anwser

        :type feedback: str
        :param feedback: feedback shown when this answer is submitted
        """
        self.answers.append(Answer(fraction, text, feedback))

    def _to_xml_element(self):
        question = super(ShortAnswerQuestion, self)._to_xml_element()

        for answer in self.answers:
            question.append(answer._to_xml_element())

        return question
