==============================================
Revision: Python programming
==============================================

Learning intentions
--------------------

* I can recall the key Python syntax and ideas from this topic.
* I can read, trace and fix short Python programs.

Summary
--------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Lesson
     - Key ideas
   * - :doc:`python_01_print_input`
     - ``print()``, ``input()``, strings, comments, reading error messages
   * - :doc:`python_02_variables_fstrings`
     - Variables, ``str``/``int``/``float``/``bool``, ``int()`` and ``float()``, arithmetic, f-strings, ``:.2f``
   * - :doc:`python_03_algorithms`
     - Pseudocode, flowchart shapes, ``AND``/``OR``/``NOT``, trace tables, normal/boundary/invalid test data
   * - :doc:`python_04_selection`
     - ``if``/``elif``/``else``, comparison operators, ``==`` vs ``=``, ``.lower()``
   * - :doc:`python_05_iteration`
     - ``for`` with ``range()``, ``while``, running totals, input validation, ``break``
   * - :doc:`python_06_functions`
     - ``def``, parameters, arguments, ``return``, local variables, modular programs
   * - :doc:`python_07_lists`
     - Indexes from 0, ``append``, ``remove``, ``pop``, ``len``, ``in``, looping through lists
   * - :doc:`python_08_dictionaries`
     - Key–value pairs, adding and changing values, ``in``, looping, nested dictionaries
   * - :doc:`python_09_tkinter_first_window` to :doc:`python_13_pizza_app`
     - Event-driven programs, Label, Button, ``grid()``, Entry, Text, messagebox, ``try``/``except``,
       ``StringVar``/``IntVar``, Radiobutton, OptionMenu, Listbox

Flashcards
-----------

.. flashcards:: Python programming
   :new-per-session: 15
   :shuffle:

   # Basics
   print() | Displays output on the screen
   input() | Asks the user a question and returns their answer as a string
   Variable | A named location that stores a value
   String | Text inside quotation marks, for example "hello"
   Integer | A whole number, for example 42
   Float | A decimal number, for example 3.5
   Boolean | A True or False value
   f-string | A string starting with f that can include variables in curly brackets
   :.2f | Formats a number to 2 decimal places in an f-string
   # Algorithms
   Algorithm | Step-by-step instructions to solve a problem
   Pseudocode | An algorithm written in structured English
   Diamond (flowchart) | A decision with yes/no paths
   Parallelogram (flowchart) | Input or output
   Trace table | A table that records variable values while working through an algorithm by hand
   Boundary data | Test values at the edges where the result changes
   # Control structures
   Selection | Choosing which code to run using if, elif and else
   Iteration | Repeating code using a loop
   for loop | Repeats a set number of times or once for each item
   while loop | Repeats while a condition is True
   == | Compares two values to see if they are equal
   and | True only when both conditions are True
   or | True when at least one condition is True
   # Functions and data
   Function | A named block of code that does one job
   Parameter | A variable in a function definition that receives a value
   return | Sends a value back from a function
   List | An ordered collection of items in square brackets
   Index | The position of an item in a list, starting at 0
   Dictionary | A collection of key-value pairs in curly brackets
   Nested dictionary | A dictionary whose values are also dictionaries
   # Tkinter
   Widget | A part of a GUI, such as a Label, Button or Entry
   Event-driven | A program that waits for user actions and responds to them
   mainloop() | Shows the window and waits for events
   grid() | Places widgets in rows and columns
   Entry | A one-line text box for user input
   Radiobutton | Lets the user choose exactly one option from a group
   OptionMenu | A drop-down list of options
   Listbox | A box that shows a list of items
   curselection() | Returns the positions of the selected Listbox items

Crossword
----------

.. crossword:: Python key words
   :hints: 3

   VARIABLE   | A named place to store a value
   STRING     | Text inside quotation marks
   INTEGER    | A whole number data type
   FLOAT      | A decimal number data type
   SELECTION  | Choosing which code to run with if
   ITERATION  | Repeating code with a loop
   FUNCTION   | A named block of reusable code
   PARAMETER  | Receives a value sent into a function
   RETURN     | Sends a value back from a function
   LIST       | Ordered items in square brackets
   DICTIONARY | Key-value pairs in curly brackets
   INDEX      | The position of an item, starting at 0
   WIDGET     | A Label, Button or Entry in Tkinter
   ALGORITHM  | Step-by-step instructions to solve a problem

Word search
------------

.. wordsearch:: Python words
   :directions: medium
   :answers: print

   PRINT
   INPUT
   WHILE
   RANGE
   ELIF
   APPEND
   RETURN
   TKINTER
   BUTTON
   LABEL
   ENTRY
   GRID

Practice questions
-------------------

.. mcqgroup::
   :shuffle-questions:

   .. multichoice::

      What is printed?

      .. code-block:: python

         x = 5
         x = x * 2 + 1
         print(x)

      [ ] 15 | Multiplication happens first: 5 × 2 = 10, then + 1.
      [x] 11 | Correct.
      [ ] 7 | Not correct.
      [ ] x | x is a variable, not a string.

   .. multichoice::

      What is printed?

      .. code-block:: python

         for i in range(3):
             print(i, end=" ")

      [x] 0 1 2 | Correct. range(3) gives 0, 1, 2.
      [ ] 1 2 3 | range starts at 0.
      [ ] 0 1 2 3 | range stops before 3.
      [ ] 3 3 3 | Not correct.

   .. multichoice::

      ``scores = [8, 5, 9]``. What is ``scores[1]``?

      [ ] 8 | That is scores[0].
      [x] 5 | Correct.
      [ ] 9 | That is scores[2].
      [ ] An error | Index 1 exists.

   .. multichoice::

      ``menu = {"pie": {"price": 5}}``. Which gives 5?

      [ ] ``menu["price"]`` | price is inside the pie dictionary.
      [x] ``menu["pie"]["price"]`` | Correct.
      [ ] ``menu[0][0]`` | Dictionaries use keys, not indexes.
      [ ] ``menu.price`` | Use square brackets with the key.

   .. multichoice::

      Which loop is best for "keep asking until the password is correct"?

      [ ] for loop | You do not know how many tries it will take.
      [x] while loop | Correct.
      [ ] No loop | The question must be repeated.
      [ ] An if statement | An if only checks once.

   .. multichoice::

      Which widget lets the user choose exactly one option from a small group?

      [ ] Listbox | A Listbox can allow several selections.
      [ ] Entry | An Entry is for typing.
      [x] Radiobutton | Correct.
      [ ] Label | A Label only displays text.

   .. multichoice::

      What does this function return for ``mystery(4)``?

      .. code-block:: python

         def mystery(n):
             if n % 2 == 0:
                 return n * 10
             return n + 1

      [x] 40 | Correct. 4 is even, so it returns 4 × 10.
      [ ] 5 | That is the result for odd numbers.
      [ ] 4 | Not correct.
      [ ] None | A value is returned.

Exam-style question
--------------------

.. structuredquestion:: Python review
   :total-marks: 8
   :category: Revision

   .. stimulus::

      .. code-block:: python

         def count_passes(marks):
             passes = 0
             for mark in marks:
                 if mark >= 50:
                     passes = passes + 1
             return passes

         results = [45, 72, 50, 38, 91]
         total_passes = count_passes(results)
         print(f"{total_passes} out of {len(results)} passed")

   .. subquestion:: a) Identify one example each of selection, iteration and a function in the code.
      :marks: 3

      .. model-answer::

         Selection: ``if mark >= 50:``. Iteration: ``for mark in marks:``. Function: ``def count_passes(marks):``
         (or the call ``count_passes(results)``).

      .. marking-guidance::

         1 mark for each correct example.

   .. subquestion:: b) Write the exact output.
      :marks: 2

      .. model-answer::

         ``3 out of 5 passed``

      .. marking-guidance::

         * 1 mark for 3 (72, 50, 91).
         * 1 mark for the exact format with 5.

   .. subquestion:: c) Explain why 50 is an important test value for this function.
      :marks: 1

      .. model-answer::

         It is boundary data: the result changes at 50, so it checks that ``>=`` was used rather than ``>``.

      .. marking-guidance::

         1 mark for identifying it as boundary data with a reason.

   .. subquestion:: d) Modify the program so it also prints the highest mark.
      :marks: 2

      .. model-answer::

         ``print(f"Highest mark: {max(results)}")`` (or a loop that keeps track of the largest mark).

      .. marking-guidance::

         * 1 mark for finding the highest mark (max() or a loop).
         * 1 mark for printing it.
