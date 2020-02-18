from xml.etree import ElementTree as et

from .utils import cdata_str, estr

class DropZone:
    """
    This class represents DropZone for Questions like DragAndDropOntoImageQuestion.
    """

    def __init__(self, x, y, text=None):
        """
        :type x: int
        :param x: Coordinate X from top left corner.

        :type y: int
        :param y: Coordinate Y from top left corner.

        :type text: str
        :param text: (optional) text contained in the drop zone
        """
        self.x = x
        self.y = y
        self.text = text
        self.choice = None
        self.number = None

    def _to_xml_element(self):
        dropzone = et.Element("drop")
        text = et.SubElement(dropzone, "text")
        text.text = estr(self.text)
        number = et.SubElement(dropzone, "no")
        number.text = str(self.number)
        choice = et.SubElement(dropzone, "choice")
        choice.text = str(self.choice)
        xleft = et.SubElement(dropzone, "xleft")
        xleft.text = str(self.x)
        ytop = et.SubElement(dropzone, "ytop")
        ytop.text = str(self.y)
        return dropzone

    @classmethod
    def is_instance_check(cls, obj):
        """
        Checks if object is of class, raises TypeError otherwise.
        """
        if isinstance(obj, cls):
            return True
        else:
            raise TypeError(f"must be DropZone, not {obj.__class__.__name__}")