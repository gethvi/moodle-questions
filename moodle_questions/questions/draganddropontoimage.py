import os
from base64 import b64encode
from xml.etree import ElementTree as et

from moodle_questions.dragitem import DragImage, DragText
from moodle_questions.dropzone import DropZone
from moodle_questions.questions.abstract import DragAndDrop


class DragAndDropOntoImageQuestion(DragAndDrop):
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

    def add_dragimage(self, file, text=None, group=1, unlimited=False, dropzones=None):
        """
        Adds new DragItem with assigned DropZones.

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

        dragimage = DragImage(file=file, text=text, group=group, unlimited=unlimited, number=(len(self._dragitems) + 1))
        self._dragitems.append(dragimage)

        if dropzones:
            for dzargs in dropzones:
                self._dropzones.append(DropZone(choice=dragimage.number, number=(len(self._dropzones) + 1), *dzargs))

    def add_dragtext(self, text=None, group=1, unlimited=False, dropzones=None):
        """
        Adds new DragText with assigned DropZones.

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

        dragitem = DragText(text=text, group=group, unlimited=unlimited, number=len(self._dragitems) + 1)
        self._dragitems.append(dragitem)

        if dropzones:
            for dzargs in dropzones:
                self._dropzones.append(DropZone(choice=dragitem.number, number=(len(self._dropzones) + 1), *dzargs))

    def _to_xml_element(self):

        question = super(DragAndDropOntoImageQuestion, self)._to_xml_element()

        for dragitem in self._dragitems:
            question.append(dragitem._to_xml_element())

        for dropzone in self._dropzones:
            question.append(dropzone._to_xml_element())

        file = et.SubElement(question, "file", {"name": str(self.background_name), "encoding": "base64"})
        with open(self.background, "rb") as f:
            file.text = str(b64encode(f.read()), "utf-8")

        return question
