from moodle_questions.quiz import Quiz
from moodle_questions.answer import Answer
from moodle_questions.dragitem import DragText, DragImage
from moodle_questions.dropzone import DropZone
from moodle_questions.questions import CalculatedQuestion, CalculatedMultichoiceQuestion, CalculatedSimpleQuestion, \
    DragAndDropIntoTextQuestion, DragAndDropMarkersQuestion, DragAndDropOntoImageQuestion, EssayQuestion, \
    MatchingQuestion, MultipleChoiceQuestion, NumericalQuestion, RandomShortAnswerMatchingQuestion, \
    SelectMissingWordsQuestion, ShortAnswerQuestion, TrueFalseQuestion

from xml.etree import ElementTree
from xml.etree.ElementTree import _raise_serialization_error


def _escape_cdata(text):
    try:
        if str.startswith(text, "<![CDATA[") and str.endswith(text, "]]>"):
            return text
        if "&" in text:
            text = text.replace("&", "&amp;")
        if "<" in text:
            text = text.replace("<", "&lt;")
        if ">" in text:
            text = text.replace(">", "&gt;")
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)


ElementTree._escape_cdata = _escape_cdata
