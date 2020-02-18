import os
from base64 import b64encode
from abc import ABCMeta, abstractmethod
from xml.etree import ElementTree as et

from .utils import cdata_str, estr


class DragItem(metaclass=ABCMeta):
    """
    Abstract class representing any drag item.
    """

    def __init__(self, text=None, group=1, unlimited=False):
        self.text = text
        self.group = group
        self.unlimited = unlimited
        self.number = None

    @abstractmethod
    def _to_xml_element(self):
        pass

    @classmethod
    def is_instance_check(cls, obj):
        """
        Checks if object is of class, raises TypeError otherwise.
        """
        if isinstance(obj, cls):
            return True
        else:
            raise TypeError(f"must be subclass of DragItem, not {obj.__class__.__name__}")


class DragText(DragItem):
    """
    Class representing drag text answer. Subclass of :class:`.DragItem`.
    """

    def __init__(self, text, *args, **kwargs):
        super(DragText, self).__init__(*args, **kwargs)
        self.text = text

    def _to_xml_element(self):
        dragtext = et.Element("drag")
        number = et.SubElement(dragtext, "no")
        number.text = str(self.number)

        text = et.SubElement(dragtext, "text")
        text.text = estr(self.text)

        draggroup = et.SubElement(dragtext, "draggroup")
        draggroup.text = str(self.group)

        if self.unlimited:
            et.SubElement(dragtext, "infinite")

        return dragtext


class DragImage(DragItem):
    """
    Class representing drag image answer. Subclass of :class:`.DragItem`.
    """

    def __init__(self, file, name=None, *args, **kwargs):
        super(DragImage, self).__init__(*args, **kwargs)
        self.file = file
        self.name = name if name else os.path.basename(file)

    def _to_xml_element(self):
        dragimage = et.Element("drag")
        number = et.SubElement(dragimage, "no")
        number.text = str(self.number)

        text = et.SubElement(dragimage, "text")
        text.text = estr(self.text)

        draggroup = et.SubElement(dragimage, "draggroup")
        draggroup.text = str(self.group)

        if self.unlimited:
            et.SubElement(dragimage, "infinite")

        file = et.SubElement(dragimage, "file", {"name": str(self.name), "encoding": "base64"})
        with open(self.file, "rb") as f:
            file.text = str(b64encode(f.read()), "utf-8")

        return dragimage
