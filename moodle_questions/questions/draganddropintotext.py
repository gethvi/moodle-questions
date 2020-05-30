import re
from moodle_questions.dragitem import DragText
from moodle_questions.dropzone import DropZone
from moodle_questions.answer import Choice
from moodle_questions.questions.abstract import DragAndDrop


class DragAndDropIntoTextQuestion(DragAndDrop):
    """
    This class represents a drag and drop text onto image question. It inherits from abstract class Question.
    """
    _type = "ddwtos"
    _allow_combined_feedback = True
    _allow_multiple_tries = True

    def __init__(self, *args, **kwargs):
        """
        Currently not implemented.
        """
        super(DragAndDropIntoTextQuestion, self).__init__(*args, **kwargs)
        self._choices = []

    def add_choice(self, number, text, group=1, unlimited=False):
        """
        Adds new Choice with assigned DropZones.

        :type image: str
        :param image: path to image to be used as a drag image

        :type text: str
        :param text: text of the drag text

        :type group: int
        :type group: group

        :type unlimited: bool
        :type unlimited: set true if you want to allow the item to be used again

        :type dropzones: list
        :param dropzones: list of tuples for dropzones like (x, y) or (x, y, text)
        """

        self._choices.append(Choice(text=text, group=group, unlimited=unlimited))
        choice_number = len(self._choices)

        pattern = re.compile("\[\[{}\]\]".format(number))
        self.question_text = pattern.sub("[[{}]]".format(choice_number), self.question_text)

        #TODO replace number with choice_number in self.question_text

    def _to_xml_element(self):

        question = super(DragAndDropIntoTextQuestion, self)._to_xml_element()

        for choice in self._choices:
            question.append(choice._to_xml_element())

        return question
