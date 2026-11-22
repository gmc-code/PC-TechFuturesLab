==============================================
1. Print and input
==============================================

Learning intentions
--------------------

* I can write a Python program that displays messages using ``print()``.
* I can ask the user a question and store their answer using ``input()``.
* I can find and fix simple errors in my code.

Success criteria
~~~~~~~~~~~~~~~~~

* I can print text, numbers and blank lines.
* I can join text together with ``+`` and with commas.
* I can write a program that asks two questions and replies using the answers.

Your first program
-------------------

Python runs your code **one line at a time, from top to bottom**. The ``print()`` function shows
something on the screen.

.. code-block:: python

   print("Hello, world!")
   print("I am learning Python.")
   print(42)
   print()
   print("The line above is blank.")

Output:

.. code-block:: text

   Hello, world!
   I am learning Python.
   42

   The line above is blank.

Key points:

* Text must go inside **quotation marks**. Text in quotes is called a **string**.
* Numbers do **not** need quotation marks.
* ``print()`` with nothing inside prints a blank line.
* Python is **case sensitive**: ``print`` works, ``Print`` does not.

Asking questions with input
----------------------------

The ``input()`` function shows a question, waits for the user to type an answer and press **Enter**,
then gives back what they typed. We store the answer in a **variable** so we can use it later.

.. code-block:: python

   name = input("What is your name? ")
   print("Nice to meet you, " + name + "!")

If the user types ``Ava``:

.. code-block:: text

   What is your name? Ava
   Nice to meet you, Ava!

.. tip::

   Put a space at the end of the question, inside the quotes (``"What is your name? "``), so the user's answer
   does not touch the question mark.

Joining text
-------------

There are two simple ways to join text in ``print()``:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Code
     - Output
     - Notes
   * - ``print("Hi " + name)``
     - ``Hi Ava``
     - ``+`` joins strings exactly. You must add the spaces yourself.
   * - ``print("Hi", name)``
     - ``Hi Ava``
     - A comma adds a space automatically.

In the next lesson you will learn **f-strings**, which are an even easier way.

Worked example: greeting program
---------------------------------

.. literalinclude:: files/greeting.py
   :language: python

:download:`Download greeting.py <files/greeting.py>`

Example run:

.. code-block:: text

   Welcome to TechFuturesLab!
   ------------------------
   What is your name? Ava
   What is your favourite subject? Science
   Hello, Ava!
   Science is a great subject.
   Have a great day, Ava

Common errors
--------------

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Code
     - Error
     - Fix
   * - ``print("Hello)``
     - ``SyntaxError``: missing closing quote
     - ``print("Hello")``
   * - ``Print("Hello")``
     - ``NameError``: ``Print`` is not defined
     - Use a lowercase ``p``
   * - ``print("Hello"``
     - ``SyntaxError``: missing bracket
     - ``print("Hello")``
   * - ``print(Hello)``
     - ``NameError``: ``Hello`` is not defined
     - Text needs quotes: ``print("Hello")``

Reading an error message: Python tells you the **line number** and the **type** of error. Start at the line it
mentions, and also check the line above it.

Comments
~~~~~~~~~

A line starting with ``#`` is a **comment**. Python ignores it. Comments explain your code to people.

.. code-block:: python

   # This program says hello
   print("Hello!")   # comments can also go at the end of a line

Activities
-----------

Activity 1: Predict the output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. multichoice::

   What does this code print?

   .. code-block:: python

      print("Tech" + "Futures")

   [ ] Tech Futures | ``+`` does not add a space.
   [x] TechFutures | Correct. ``+`` joins the strings exactly.
   [ ] Tech + Futures | The ``+`` is not printed because it is outside the quotes.
   [ ] An error | This code works.

.. multichoice::

   What does this code print?

   .. code-block:: python

      print("Score:", 10)

   [x] Score: 10 | Correct. The comma adds a space.
   [ ] Score:10 | A comma in print adds a space.
   [ ] "Score:", 10 | The quotes and comma are not printed.
   [ ] An error | This code works.

Activity 2: Put the program in order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program should ask for the user's name and favourite food, then reply. Drag the lines into order.

.. ordering::

   print("Food survey")
   name = input("What is your name? ")
   food = input("What is your favourite food? ")
   print("Thanks, " + name + "!")
   print(food + " sounds delicious.")

Activity 3: Fix the bugs
~~~~~~~~~~~~~~~~~~~~~~~~~

Drag the correct pieces into the gaps so the program works.

.. cloze:: python
   :show-code:

   @@print@@("Pet survey")
   pet = @@input@@("What pet do you have? ")
   print("I like " + @@pet@@ + "s too!")

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      What does ``input()`` do?

      [ ] Prints a number | That is ``print()``.
      [x] Shows a question and waits for the user to type an answer | Correct.
      [ ] Deletes a variable | Not correct.
      [ ] Saves the file | Not correct.

   .. multichoice::

      Which line will cause an error?

      [ ] ``print("Hi")`` | This works.
      [x] ``print("Hi)`` | Correct. The closing quote is missing.
      [ ] ``print()`` | This prints a blank line.
      [ ] ``print(5)`` | Numbers do not need quotes.

   .. multichoice::

      What is a string?

      [x] Text inside quotation marks | Correct.
      [ ] A whole number | That is an integer.
      [ ] A type of loop | Not correct.
      [ ] An error message | Not correct.

Coding challenges
------------------

#. **About me:** Write a program that prints three facts about you, with a blank line between each.
#. **Mad libs:** Ask the user for a noun, a verb and an adjective, then print a funny sentence that uses all three.
#. **ASCII art:** Use several ``print()`` lines to draw a picture, such as a house or a cat, with keyboard
   characters.
#. **Extension:** Ask the user for their name, then print it inside a box of stars, for example:

   .. code-block:: text

      *********
      *  Ava  *
      *********

   (You will be able to make the box fit any name after the next lesson.)

Continue with **Grok: Python for Beginners** for more practice.

Exam-style question
--------------------

.. structuredquestion:: Print and input
   :total-marks: 5
   :category: Python basics

   .. stimulus::

      .. code-block:: python

         city = input("Where do you live? ")
         print("I have never been to" + city)
         print("Is", city, "nice?")

   .. subquestion:: a) The user types Darwin. Write the exact output of the program (including the question).
      :marks: 3

      .. model-answer::

         .. code-block:: text

            Where do you live? Darwin
            I have never been toDarwin
            Is Darwin nice?

      .. marking-guidance::

         * 1 mark for the input line.
         * 1 mark for ``I have never been toDarwin`` (with no space).
         * 1 mark for ``Is Darwin nice?``

   .. subquestion:: b) There is a small problem with line 2. Explain the problem and how to fix it.
      :marks: 2

      .. model-answer::

         ``+`` joins strings with no space, so "to" and "Darwin" are stuck together. Add a space inside the quotes:
         ``print("I have never been to " + city)``, or use a comma instead of ``+``.

      .. marking-guidance::

         * 1 mark for identifying the missing space.
         * 1 mark for a correct fix.
