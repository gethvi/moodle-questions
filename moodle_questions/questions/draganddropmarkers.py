import os
from moodle_questions.questions.abstract import Question


class DragAndDropMarkersQuestion(Question):

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
        super(DragAndDropMarkersQuestion, self).__init__(*args, **kwargs)
        self.background = background
        self.background_name = background_name if background_name else os.path.basename(background)

    def add_dragmarker(self):
        raise NotImplementedError