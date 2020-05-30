# moodle-questions
Python 3 library for manipulating quiz questions in Moodle XML format.

## About
I needed to create some types of Moodle questions programatically for a project and I could not find any suitable library. This led to me to an idea to work on such library myself (beyond the requirements of the original project). However throughout the work on this I realized that Moodle XML format is an unpredictable and barely documented mess which severly undermined my motivation to make this a complete library covering all types of Moodle questions. I will keep working occasionally and I welcome contributions, but as of now I can not promise this will ever be finished.

## Installation
`pip install moodle-questions`

## Example
```python
from moodle_questions import Quiz, DragAndDropOntoImageQuestion

quiz = Quiz()

question = DragAndDropOntoImageQuestion(name="DragAndDropOntoImage",
                                        background="background.jpg",
                                        question_text="Drag the images in the correct boxes",
                                        default_mark=1,
                                        correct_feedback="Congratulations!",
                                        shuffle=True)

question.add_dragimage(file="image1.jpg", unlimited=True, dropzones=[(100, 100, "some dropzone text")])

question.add_dragtext(text="This is a box with test.", dropzones=[(300,100,"some dropzone text 2")])

quiz.add_question(question)

quiz.save("draganddropontoimage.xml")
```

## Current status

Current status of moodle-questions implementation:

| Question Type                            |  Create New        |
| ---------------------------------------- |  :---------------: |
| Calculated                               |                    |
| Calculated multi-choice                  |                    |
| Calculated simple                        |                    |
| Drag and drop into text                  | :heavy_check_mark: |
| Drag and drop markers                    |                    |
| Drag and drop onto image                 | :heavy_check_mark: |
| Description                              |                    |
| Essay                                    |                    |
| Matching                                 |                    |
| Embedded Answers (Cloze Test / Gap Fill) |                    |
| Multiple choice                          | :heavy_check_mark: |
| Short Answer                             | :heavy_check_mark: |
| Numerical                                |                    |
| Random short-answer matching             |                    |
| Select missing words                     |                    | 
| True/False                               |                    |
