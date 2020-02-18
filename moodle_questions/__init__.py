from .question import DragAndDropOntoImageQuestion, DragAndDropIntoTextQuestion

from .dragitem import DragText, DragImage

from .dropzone import DropZone

from .quiz import Quiz

from xml.etree import ElementTree
from xml.etree.ElementTree import _raise_serialization_error


def _escape_cdata(text):
    # escape character data
    try:
        if str.startswith(text, "<![CDATA[") or str.endswith(text, "]]>"):
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
