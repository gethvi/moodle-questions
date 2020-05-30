from xml.etree import ElementTree as et


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


class Choice:

    def __init__(self, text, group=1, unlimited=False):
        self.text = text
        self.group = group
        self.unlimited = unlimited

    def _to_xml_element(self):
        dragbox = et.Element("dragbox")
        text = et.SubElement(dragbox, "text")
        text.text = self.text
        group = et.SubElement(dragbox, "group")
        group.text = str(self.group)

        if self.unlimited:
            unlimited = et.SubElement(dragbox, "infinite")

        return dragbox
