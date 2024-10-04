# Flashcard App
#### Video Demo:  https://youtu.be/_ipHjB7ZsYs
#### Description: A flashcard app which allows to add new flashcards to the file, study the existing flashcards,edit the existing flashcards, and delete the flashcards.

    Five operations can be performed in the flashcard app as follows:
    Option 1 -> Study the existing flashcards in the file.
    All the flashcards in the file are asked one after another in a random order. The correct answer is displayed if a wrong answer is submitted. The total score is displayed after answering all the flashcards.
    Option 2 -> Add the new flashcards to the file.
    The new flashcards are added by typing their question and respective answers. The questions and answers for the flashcards can be continuously added until interrupted by typing 'q'.
    Option 3 -> Edit an existing flashcard.
    If the question or answer of an existing flashcard in the file and the new question or answer for it are provided, that question or answer of the flashcard is updated in the file. If the provided question or answer doesn't exist in the file, no changes happen.
    Option 4 -> Delete a flashcard.
    If the question or answer of an existing flashcard in the file is provided, the flashcard with that question or answer is deleted. If the provided question or answer doesn't exist in the file, no changes happen.
    Option 5 -> Exit.
    Quit the flashcard app.


#### Project Requirements
- Your project must be implemented in Python.
- Your project must have a main function and three or more additional functions. At least three of those [x] #739 additional functions must be accompanied by tests that can be executed with pytest.
- Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
- Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
- Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
- You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
- Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
- Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.
