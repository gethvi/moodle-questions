from xml.etree import ElementTree as et

from .utils import cdata_str, estr


class Answer:

    def __init__(self, fraction, text, feedback):
        self.fraction = int(fraction)
        self.text = text
        self.feedback = feedback

    def _to_xml_element(self):
        answer = et.Element("answer", {"fraction": str(self.fraction), "format": "html"})
        text = et.SubElement(answer, "text")
        text.text = self.text

        feedback = et.SubElement(answer, "feedback", {"format": "html"})
        text = et.SubElement(feedback, "text")
        text.text = self.feedback

        return answer
