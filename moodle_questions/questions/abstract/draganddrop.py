from xml.etree import ElementTree as et
from moodle_questions.utils import cdata_str
from moodle_questions.questions.abstract import Question


class DragAndDrop(Question):
        """
        This is an abstract class represents a drag and drop text onto image question. It inherits from abstract class Question.
        """

        def __init__(self, *args, **kwargs):
            """
            Currently not implemented.
            """
            super(DragAndDrop, self).__init__(*args, **kwargs)
            self._dragitems = []
            self._dropzones = []

        def _to_xml_element(self):
            question = super(DragAndDrop, self)._to_xml_element()

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

            if self.allow_multiple_tries:
                penalty = et.SubElement(question, "penalty")
                penalty.text = str(self.penalty)

                for hint in self.hints:
                    hint_element = et.SubElement(question, "hint")
                    hint_element.text = cdata_str(hint)

            return question