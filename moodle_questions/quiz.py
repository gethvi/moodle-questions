from .question import Question
from xml.etree import ElementTree as et


class Quiz:
    """
    This class represents Quiz as a set of Questions.
    """
    def __init__(self):
        self._questions = []

    def add_question(self, question):
        """
        Adds a question to the quiz object.

        :type question: Question
        :param question: the question to add
        """
        if Question.is_instance_check(question):
            self._questions.append(question)

    def save(self, file, pretty=False):
        """
        Generates XML compatible with Moodle and saves to a file.

        :type file: str
        :param file: filename where the XML will be saved

        :type pretty: bool
        :param pretty: (not implemented) saves XML pretty printed
        """
        quiz = self._get_xml_tree()
        quiz.write(file, encoding="utf-8", xml_declaration=True, short_empty_elements=False)

        # TODO category

    def _get_xml_tree(self):
        """
        Converts self and all assigned questions to Moodle XML.
        """
        quiz = et.ElementTree(et.Element("quiz"))
        root = quiz.getroot()
        for question in self._questions:
            root.append(question._to_xml_element())
        return quiz

    def _dump(self):
        quiz = self._get_xml_tree()
        root = quiz.getroot()
        self._indent(root)
        et.dump(root)

    def _indent(self, elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
