# Moodle Question Types

## Numerical

The `NumericalQuestion` type requires that you add a correct answer and also specify a tolerance value. See an example below.

```python
from moodle_questions import Quiz, NumericalQuestion

quiz = Quiz()
q1 = NumericalQuestion(name = "F to C Conversion",
                       question_text = "Convert 40 degrees in F to C. Only enter the numerical value.",
                       default_mark = 1,
                       )
q1.add_answer(tol = 0.1,
              fraction = 100,
              text = "4.44",
              feedback = None)

quiz.add_question(q1)

quiz.save("numerical_export_example.xml")
```

In the example above, a `NumericalQuestion` is added to `quiz = Quiz()`, which is then saved to a moodle `xml` format using the `.save()` method.

## Multiple Choice
The `MultipleChoiceQuestion` defines a multiple choice question. The `add_answer` method can be used to add both correct and incorrect answers; the fraction argument sets the fraction of grade awarded for each answer.
```python
quiz = Quiz()

q2 = MultipleChoiceQuestion(name = "Celsius Fahrenheit Equivalency",
                            question_text = "At what temperature value do the Fahrenheit and Celsius scales have the same numerical value?",
                            default_mark = 1,
                            correct_feedback = "Correct!",
                            shuffle=True)

q2.add_answer(fraction = 100, text = "-40")
q2.add_answer(fraction = 0, text = "40")
q2.add_answer(fraction = 0, text = "0")
q2.add_answer(fraction = 0, text = "100")

quiz.add_question(q2)
```