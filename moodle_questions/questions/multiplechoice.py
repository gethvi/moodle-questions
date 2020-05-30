from moodle_questions.answer import Answer
from moodle_questions.questions.abstract import Question


class MultipleChoiceQuestion(Question):
    """
    This class represents 'Multiple choice' question.
    """
    _type = "multichoice"
    _allow_combined_feedback = True
    _allow_multiple_tries = True

    _answer_numbering = [
        "none",
        "abc",
        "ABCD",
        "123",
        "iii",
        "IIII"
    ]

    def __init__(self, answer_numbering="abc", *args, **kwargs):
        super(MultipleChoiceQuestion, self).__init__(*args, **kwargs)
        self.answer_numbering = answer_numbering
        self.answers = []

    def _to_xml_element(self):
        question = super(MultipleChoiceQuestion, self)._to_xml_element()

        for answer in self.answers:
            question.append(answer._to_xml_element())

        return question

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
