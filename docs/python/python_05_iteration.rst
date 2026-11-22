==============================================
5. Iteration: for and while loops
==============================================

Learning intentions
--------------------

* I can explain what iteration is and why programs use loops.
* I can use a ``for`` loop with ``range()`` to repeat code a set number of times.
* I can use a ``while`` loop to repeat code until a condition changes, including to check user input.

Success criteria
~~~~~~~~~~~~~~~~~

* I can predict the numbers that ``range()`` produces.
* I can use a loop to add up a running total.
* I can write a ``while`` loop that keeps asking until the user gives a valid answer.

What is iteration?
-------------------

**Iteration** means repeating steps. Instead of writing the same line ten times, we put it in a **loop**.

Python has two kinds of loops:

* A ``for`` loop repeats a **set number of times** (or once for each item in a list).
* A ``while`` loop repeats **while a condition is True**. Use it when you do not know how many times to repeat.

For loops
----------

.. code-block:: python

   for i in range(5):
       print("Hello", i)

Output:

.. code-block:: text

   Hello 0
   Hello 1
   Hello 2
   Hello 3
   Hello 4

The variable ``i`` takes each value from ``range(5)`` in turn: 0, 1, 2, 3, 4. Notice that ``range(5)``
starts at **0** and stops **before** 5.

Understanding range()
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Code
     - Numbers produced
     - Meaning
   * - ``range(5)``
     - 0, 1, 2, 3, 4
     - start at 0, stop before 5
   * - ``range(1, 6)``
     - 1, 2, 3, 4, 5
     - start at 1, stop before 6
   * - ``range(2, 11, 2)``
     - 2, 4, 6, 8, 10
     - start at 2, stop before 11, count by 2
   * - ``range(10, 0, -1)``
     - 10, 9, 8 ... 1
     - count down

Worked example: times tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: files/times_table.py
   :language: python

:download:`Download times_table.py <files/times_table.py>`

Running totals
~~~~~~~~~~~~~~~

A common pattern is to start a variable at 0 and add to it each time around the loop.

.. code-block:: python

   total = 0
   for i in range(3):
       score = int(input(f"Score for round {i + 1}: "))
       total = total + score

   print(f"Total: {total}")
   print(f"Average: {total / 3:.1f}")

While loops
------------

A ``while`` loop checks its condition **before** each repeat. When the condition becomes ``False``, the loop
stops.

.. code-block:: python

   count = 3
   while count > 0:
       print(count)
       count = count - 1
   print("Lift off!")

Output:

.. code-block:: text

   3
   2
   1
   Lift off!

.. admonition:: Infinite loops
   :class: warning

   If the condition never becomes ``False``, the loop runs forever. For example, if we forgot
   ``count = count - 1`` above, ``count`` would always be 3. Press **Ctrl + C** (or the Stop button) to stop a
   program that is stuck.

Input validation with while
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Input validation** means checking that the user's input is sensible before using it. A ``while`` loop can
keep asking until the input is valid.

.. code-block:: python

   rating = int(input("Rate the movie from 1 to 5: "))

   while rating < 1 or rating > 5:
       print("Please enter a number from 1 to 5.")
       rating = int(input("Rate the movie from 1 to 5: "))

   print(f"Thanks! You gave it {rating} stars.")

Worked example: guessing game
------------------------------

.. literalinclude:: files/guessing_game.py
   :language: python

:download:`Download guessing_game.py <files/guessing_game.py>`

Here is the same algorithm as a flowchart. Notice how the ``WHILE`` loop goes back to the decision each time.

.. flowchart::
   :mode: view
   :title: Guessing game

   BEGIN
       secret ← 7
       guesses ← 0
       guess ← 0
       WHILE guess ≠ secret DO
           INPUT guess
           guesses ← guesses + 1
           IF guess < secret THEN
               PRINT "Too low!"
           ELSEIF guess > secret THEN
               PRINT "Too high!"
           ENDIF
       ENDWHILE
       PRINT "Correct!"
   END

Break
~~~~~~

``break`` stops a loop straight away, even if the condition is still ``True``.

.. code-block:: python

   while True:
       word = input("Type a word (or 'quit'): ")
       if word == "quit":
           break
       print(f"{word} has {len(word)} letters.")

Activities
-----------

Activity 1: range()
~~~~~~~~~~~~~~~~~~~~

Type the numbers each ``range()`` produces, separated by commas and spaces (for example ``1, 2, 3``).

.. fillin::

   list(range(4)) gives @@0, 1, 2, 3@@
   list(range(2, 6)) gives @@2, 3, 4, 5@@
   list(range(0, 10, 3)) gives @@0, 3, 6, 9@@
   list(range(5, 0, -1)) gives @@5, 4, 3, 2, 1@@

Activity 2: For or while?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: for loop, while loop
   :delimiter: =>
   :instructions: Which type of loop is the best choice?

   Print the numbers 1 to 100 => for loop
   Print a times table from 1 to 12 => for loop
   Ask for 5 test scores and add them up => for loop
   Keep asking for a password until it is correct => while loop
   Keep playing a game until the player types quit => while loop
   Keep asking for a number until it is between 1 and 10 => while loop

Activity 3: Order the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program adds up 5 numbers entered by the user. Put the lines in order and fix the indents.

.. ordering::

   total = 0
   for i in range(5):
       number = int(input("Enter a number: "))
       total = total + number
   print(f"The total is {total}")

Activity 4: Complete the validation loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze:: python
   :show-code:

   age = int(input("Age: "))
   @@while@@ age < 0 @@or@@ age > 120:
       print("That age is not valid.")
       age = @@int@@(input("Age: "))
   print(f"You are {age}.")

Activity 5: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      How many times does ``Hi`` print?

      .. code-block:: python

         for i in range(1, 4):
             print("Hi")

      [ ] 4 | range(1, 4) stops before 4.
      [x] 3 | Correct. i is 1, 2, 3.
      [ ] 1 | It repeats.
      [ ] 5 | Not correct.

   .. multichoice::

      What is the problem with this code?

      .. code-block:: python

         n = 1
         while n < 5:
             print(n)

      [ ] Nothing, it prints 1 to 4 | n never changes.
      [x] It is an infinite loop because n never changes | Correct. Add ``n = n + 1`` inside the loop.
      [ ] It prints nothing | It prints 1 forever.
      [ ] ``while`` needs ``range()`` | while loops use a condition, not range.

   .. multichoice::

      What does ``break`` do?

      [ ] Restarts the program | Not correct.
      [x] Stops the loop immediately | Correct.
      [ ] Skips one line | Not correct.
      [ ] Causes an error | It is valid Python.

Coding challenges
------------------

#. **Countdown:** Ask for a starting number and count down to 1, then print "Blast off!".
#. **Sum of numbers:** Ask the user for a number ``n`` and print the sum of all numbers from 1 to ``n``.
   Check: ``n = 100`` should give 5050.
#. **Password retry:** Give the user 3 tries to enter the password ``tiger``. Print "Locked out" after 3 wrong
   tries.
#. **Star pyramid:** Ask for a height and use a loop to print a triangle of stars:

   .. code-block:: text

      *
      **
      ***
      ****

#. **Extension:** Improve the guessing game so the player can choose to play again, and keeps their best score.

Exam-style question
--------------------

.. structuredquestion:: Loops
   :total-marks: 7
   :category: Iteration

   .. stimulus::

      .. code-block:: python

         total = 0
         for number in range(2, 9, 2):
             total = total + number
         print(total)

   .. subquestion:: a) List the values that ``number`` takes.
      :marks: 1

      .. model-answer::

         2, 4, 6, 8

      .. marking-guidance::

         1 mark for all four values (no 10).

   .. subquestion:: b) Complete a trace table for ``number`` and ``total``, and state the output.
      :marks: 3

      .. model-answer::

         .. list-table::
            :header-rows: 1

            * - number
              - total
            * - (start)
              - 0
            * - 2
              - 2
            * - 4
              - 6
            * - 6
              - 12
            * - 8
              - 20

         Output: ``20``

      .. marking-guidance::

         * 1 mark for correct values of number.
         * 1 mark for correct running totals.
         * 1 mark for output 20.

   .. subquestion:: c) Rewrite the program using a while loop that gives the same output.
      :marks: 3

      .. model-answer::

         .. code-block:: python

            total = 0
            number = 2
            while number <= 8:
                total = total + number
                number = number + 2
            print(total)

      .. marking-guidance::

         * 1 mark for setting the starting value of number before the loop.
         * 1 mark for a correct condition (``number <= 8`` or ``number < 9``).
         * 1 mark for adding 2 to number inside the loop and printing the total.
