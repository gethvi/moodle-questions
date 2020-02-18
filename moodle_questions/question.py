import os
from base64 import b64encode
from abc import ABCMeta, abstractmethod
from xml.etree import ElementTree as et

from .dragitem import DragItem
from .dropzone import DropZone
from .utils import cdata_str, estr


class Question(metaclass=ABCMeta):
    """
    This is an abstract class Question used as a parent for specific types of Questions.
    """

    def __init__(self, name, question_text, default_mark, general_feedback=None, id_number=None, shuffle=False, *args,
                 **kwargs):
        """
        :type name: str
        :param name: name of the question

        :type question_text: str
        :param question_text: text of the question

        :type default_mark: float
        :param default_mark: the default mark

        :type general_feedback: str
        :param general_feedback: (optional) general feedback

        :type id_number: int
        :param id_number: (optional) id number

        :type shuffle: bool
        :param shuffle: (optional) shuffle answers
        """
        self.name = name
        self.question_text = question_text
        self.default_mark = float(default_mark)
        self.general_feedback = general_feedback
        self.id_number = id_number
        self.shuffle = shuffle
        self.set_combined_feedback(*args, **kwargs)
        self.set_multiple_tries(*args, **kwargs)

    @property
    def allow_combined_feedback(self):
        """
        This property represents if the question can have combined feedback.
        """
        return self._allow_combined_feedback

    @property
    def allow_multiple_tries(self):
        """
        This property defines if the question can be answered multiple times.
        """
        return self._allow_multiple_tries

    def set_combined_feedback(self, correct_feedback=None, partially_correct_feedback=None, incorrect_feedback=None,
                              show_number_of_correct=False,
                              *args,
                              **kwargs):
        """
        Sets optional combined feedback.

        :type correct_feedback: str
        :param correct_feedback: Feedback if the answer is correct.

        :type partially_correct_feedback: str
        :param partially_correct_feedback: Feedback if the answer is partially correct.

        :type incorrect_feedback: str
        :param incorrect_feedback: Feedback if the answer is incorrect.

        :type show_number_of_correct: bool
        :param show_number_of_correct: show number of correct answers
        """
        if self.allow_combined_feedback:
            self.correct_feedback = correct_feedback
            self.partially_correct_feedback = partially_correct_feedback
            self.incorrect_feedback = incorrect_feedback
            self.show_number_of_correct = show_number_of_correct

    def set_multiple_tries(self, penalty=0.5, hints=None, *args, **kwargs):
        """
        Allows to set penalty and hints if multiple tries are allowed.

        :type penalty: float
        :param penalty: penalty for incorrect answer

        :type hints: list
        :param hints: hints to display.
        """
        if self.allow_multiple_tries:
            self.penalty = penalty
            if hints and isinstance(hints, list):
                self.hints = hints
            else:
                self.hints = []

    # TODO tags

    @abstractmethod
    def _to_xml_element(self):
        """
        This method converts current object to Moodle XML.
        """
        pass

    @classmethod
    def is_instance_check(cls, obj):
        """
        Checks if object is of class, raises TypeError otherwise.
        """
        if isinstance(obj, cls):
            return True
        else:
            raise TypeError(f"must be subclass of Question, not {obj.__class__.__name__}")


class DragAndDropOntoImageQuestion(Question):
    """
    This class represents a drag and drop onto image question. It inherits from abstract class Question.
    """
    _type = "ddimageortext"
    _allow_combined_feedback = True
    _allow_multiple_tries = True

    def __init__(self, background, background_name=None, *args, **kwargs):
        """
        Creates an drag and drop onto image type of question.

        :type background: str
        :param background: Filepath to the background image.

        :type background_name: str
        :param background_name: Name of the background image.
        """
        super(DragAndDropOntoImageQuestion, self).__init__(*args, **kwargs)
        self.background = background
        self.background_name = background_name if background_name else os.path.basename(background)
        self._dragitems = []
        self._dragitems_count = 0
        self._dropzones = []
        self._dropzones_count = 0

    def add_dragitem(self, dragitem, dropzones=None):
        """
        Adds new DragItem with assigned DropZones.

        :type dragitem: DragItem
        :param dragitem: DragItem object.

        :type dropzones: list
        :param dropzones: Correct DropZones for the DragItem.
        """
        if dropzones is None:
            dropzones = []

        DragItem.is_instance_check(dragitem)
        self._dragitems_count += 1
        dragitem.number = self._dragitems_count
        self._dragitems.append(dragitem)

        for dropzone in dropzones:
            DropZone.is_instance_check(dropzone)
            self._dropzones_count += 1
            dropzone.number = self._dropzones_count
            dropzone.choice = dragitem.number
            self._dropzones.append(dropzone)

    def _to_xml_element(self):
        question = et.Element("question")
        question.set("type", self._type)
        name = et.SubElement(question, "name")
        text = et.SubElement(name, "text")
        text.text = str(self.name)

        questiontext = et.SubElement(question, "questiontext", {"format": "html"})
        text = et.SubElement(questiontext, "text")
        text.text = cdata_str(self.question_text)

        defaultgrade = et.SubElement(question, "defaultgrade")
        defaultgrade.text = str(self.default_mark)

        generalfeedback = et.SubElement(question, "generalfeedback", {"format": "html"})
        text = et.SubElement(generalfeedback, "text")
        text.text = cdata_str(self.general_feedback)

        hidden = et.SubElement(question, "hidden")
        hidden.text = "0"

        idnumber = et.SubElement(question, "idnumber")
        idnumber.text = estr(self.id_number)

        if self.shuffle:
            et.SubElement(question, "shuffleanswers")

        if self.allow_combined_feedback:
            correctfeedback = et.SubElement(question, "correctfeedback", {"format": "html"})
            text = et.SubElement(correctfeedback, "text")
            text.text = cdata_str(self.correct_feedback)

            partiallycorrectfeedback = et.SubElement(question, "partiallycorrectfeedback", {"format": "html"})
            text = et.SubElement(partiallycorrectfeedback, "text")
            text.text = cdata_str(self.partially_correct_feedback)

            incorrectfeedback = et.SubElement(question, "incorrectfeedback", {"format": "html"})
            text = et.SubElement(incorrectfeedback, "text")
            text.text = cdata_str(self.incorrect_feedback)

            if self.show_number_of_correct:
                et.SubElement(question, "shownumcorrect")

            file = et.SubElement(question, "file", {"name": str(self.background_name), "encoding": "base64"})
            with open(self.background, "rb") as f:
                file.text = str(b64encode(f.read()), "utf-8")

        for dragitem in self._dragitems:
            question.append(dragitem._to_xml_element())

        for dropzone in self._dropzones:
            question.append(dropzone._to_xml_element())

        if self.allow_multiple_tries:
            penalty = et.SubElement(question, "penalty")
            penalty.text = str(self.penalty)

            for hint in self.hints:
                hint_element = et.SubElement(question, "hint")
                hint_element.text = cdata_str(hint)

        return question


class DragAndDropIntoTextQuestion(Question):
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
        raise NotImplementedError
        super(DragAndDropIntoTextQuestion, self).__init__(*args, **kwargs)

    def _to_xml_element(self):
        raise NotImplementedError
