==============================================
4. Selection: if, elif and else
==============================================

Learning intentions
--------------------

* I can use ``if``, ``elif`` and ``else`` to make a program choose what to do.
* I can write conditions using comparison operators and the logical operators ``and``, ``or`` and ``not``.
* I can test selection code with normal, boundary and invalid data.

Success criteria
~~~~~~~~~~~~~~~~~

* I can indent code correctly inside an ``if`` statement.
* I can write a program with at least three possible outcomes.
* I can combine two conditions with ``and`` or ``or``.

Making decisions
-----------------

**Selection** means the program chooses which code to run, based on a **condition**. A condition is a
question that is either ``True`` or ``False``.

.. code-block:: python

   temperature = int(input("What is the temperature? "))

   if temperature > 30:
       print("It's hot! Wear a hat and sunscreen.")
   elif temperature > 18:
       print("Nice weather today.")
   else:
       print("Grab a jumper.")

   print("Have a good day!")

* ``if`` checks the first condition.
* ``elif`` (short for "else if") is checked **only if** the conditions above it were ``False``.
* ``else`` runs if **none** of the conditions were ``True``.
* Only **one** branch runs. Python checks from the top and stops at the first ``True`` condition.
* The last ``print`` is not indented, so it **always** runs.

.. admonition:: Indentation matters
   :class: warning

   The code inside each branch must be **indented** (4 spaces, or press **Tab** in most editors). The colon
   ``:`` at the end of ``if``, ``elif`` and ``else`` lines is required. Forgetting either causes an error.

Comparison operators
---------------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Operator
     - Meaning
     - Example (``age = 14``)
   * - ``==``
     - equal to
     - ``age == 14`` is ``True``
   * - ``!=``
     - not equal to
     - ``age != 14`` is ``False``
   * - ``<``
     - less than
     - ``age < 13`` is ``False``
   * - ``>``
     - greater than
     - ``age > 13`` is ``True``
   * - ``<=``
     - less than or equal to
     - ``age <= 14`` is ``True``
   * - ``>=``
     - greater than or equal to
     - ``age >= 15`` is ``False``

Remember: ``=`` **stores** a value, ``==`` **compares** two values.

Comparing strings
~~~~~~~~~~~~~~~~~~

String comparisons are **case sensitive**: ``"Yes" == "yes"`` is ``False``. Use ``.lower()`` to change the
user's answer to lowercase before comparing.

.. code-block:: python

   answer = input("Do you like pizza? ").lower()
   if answer == "yes":
       print("Me too!")
   else:
       print("Fair enough.")

Logical operators
------------------

.. code-block:: python

   age = 15
   has_ticket = True

   if age >= 13 and age <= 19:
       print("You are a teenager.")

   day = "Sunday"
   if day == "Saturday" or day == "Sunday":
       print("It's the weekend!")

   if not has_ticket:
       print("Please buy a ticket.")
   else:
       print("Enjoy the show.")

Output:

.. code-block:: text

   You are a teenager.
   It's the weekend!
   Enjoy the show.

.. tip::

   A common mistake is ``if day == "Saturday" or "Sunday":``. Each side of ``or`` must be a full condition:
   ``if day == "Saturday" or day == "Sunday":``

Worked example: movie tickets
------------------------------

**Problem:** Children under 5 are free. Under-16s and people 65 or over pay $12. Everyone else pays $18.
On Tuesday, paid tickets are half price.

.. literalinclude:: files/movie_ticket.py
   :language: python

:download:`Download movie_ticket.py <files/movie_ticket.py>`

.. list-table:: Test table
   :header-rows: 1

   * - Age
     - Day
     - Type
     - Expected output
   * - 30
     - friday
     - Normal
     - Your ticket costs $18.00
   * - 4
     - monday
     - Boundary (under 5)
     - Your ticket is free!
   * - 15
     - monday
     - Boundary (under 16)
     - Your ticket costs $12.00
   * - 16
     - monday
     - Boundary (16)
     - Your ticket costs $18.00
   * - 65
     - Tuesday
     - Boundary and Tuesday
     - Your ticket costs $6.00

Activities
-----------

Activity 1: Trace the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. multichoice::

   What does this code print when ``score = 75``?

   .. code-block:: python

      if score >= 90:
          print("Gold")
      elif score >= 70:
          print("Silver")
      elif score >= 50:
          print("Bronze")
      else:
          print("Keep trying")

   [ ] Gold | 75 is not 90 or more.
   [x] Silver | Correct. 75 >= 70 is the first True condition.
   [ ] Silver and Bronze | Only one branch runs.
   [ ] Bronze | Python stops at the first True condition (>= 70).

.. multichoice::

   Which condition is ``True`` when ``x = 10``?

   [ ] ``x > 10 and x < 20`` | 10 > 10 is False, so the whole ``and`` is False.
   [x] ``x >= 10 and x < 20`` | Correct. Both parts are True.
   [ ] ``x < 5 or x > 15`` | Both parts are False.
   [ ] ``not x == 10`` | x == 10 is True, so not makes it False.

Activity 2: Fix the code
~~~~~~~~~~~~~~~~~~~~~~~~~

Drag the missing pieces into place. The program checks a password.

.. cloze:: python
   :show-code:

   password = input("Password: ")
   if password @@==@@ "python123"@@:@@
       print("Access granted")
   @@else@@:
       print("Access denied")

Activity 3: Order the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program says whether a number is positive, negative or zero. Put the lines in order and fix the indents.

.. ordering::

   number = int(input("Enter a number: "))
   if number > 0:
       print("Positive")
   elif number < 0:
       print("Negative")
   else:
       print("Zero")

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      What is the difference between ``=`` and ``==``?

      [x] ``=`` stores a value, ``==`` compares two values | Correct.
      [ ] They mean the same thing | They are different.
      [ ] ``==`` stores a value, ``=`` compares | It is the other way around.
      [ ] ``==`` is only used with strings | It works with any values.

   .. multichoice::

      The user types ``YES``. Which code prints "Great!"?

      [ ] ``if answer == "yes": print("Great!")`` | "YES" and "yes" are different.
      [x] ``if answer.lower() == "yes": print("Great!")`` | Correct. lower() changes YES to yes.
      [ ] ``if answer = "yes": print("Great!")`` | ``=`` cannot be used in a condition.
      [ ] ``if answer == yes: print("Great!")`` | yes needs quotes.

   .. multichoice::

      How many branches of an if/elif/else statement can run at once?

      [x] One | Correct.
      [ ] Two | Only one.
      [ ] All of them | Only one.
      [ ] None | One branch always runs if there is an else.

Coding challenges
------------------

#. **Even or odd:** Ask for a whole number and print whether it is even or odd. Hint: ``number % 2 == 0``.
#. **Rock, paper, scissors judge:** Ask player 1 and player 2 for their choices and print who wins. Use ``and``
   to check pairs, for example ``p1 == "rock" and p2 == "scissors"``.
#. **Leap year:** A year is a leap year if it is divisible by 4 **and** not divisible by 100, **or** if it is
   divisible by 400. Test with 2024 (leap), 1900 (not leap), 2000 (leap) and 2026 (not leap).
#. **Extension: postage calculator:** Ask for a parcel's weight in kg and whether it is express (yes/no).
   Parcels up to 0.5 kg cost $8, up to 3 kg cost $12 and over 3 kg cost $20. Express adds $6. Reject weights of
   0 or less. Write a full test table (normal, boundary and invalid) before you code.

Exam-style question
--------------------

.. structuredquestion:: Selection in Python
   :total-marks: 7
   :category: Selection

   .. stimulus::

      This program should give free entry to a museum for children under 12 and for members. It has a bug.

      .. code-block:: python

         age = int(input("Age: "))
         member = input("Member? (yes/no) ")

         if age < 12 and member == "yes":
             print("Free entry")
         else:
             print("Entry costs $15")

   .. subquestion:: a) A 9-year-old who is not a member uses the program. What is the output, and is it correct?
      :marks: 2

      .. model-answer::

         Output: ``Entry costs $15``. This is wrong, because children under 12 should get free entry.

      .. marking-guidance::

         * 1 mark for the correct output.
         * 1 mark for saying it is incorrect with a reason.

   .. subquestion:: b) Identify the bug and rewrite line 4 to fix it.
      :marks: 2

      .. model-answer::

         ``and`` should be ``or``, because only one of the conditions needs to be true.
         ``if age < 12 or member == "yes":``

      .. marking-guidance::

         * 1 mark for identifying ``and`` should be ``or``.
         * 1 mark for the correct line.

   .. subquestion:: c) A member types ``Yes`` with a capital Y. Explain the problem and how to fix it.
      :marks: 2

      .. model-answer::

         String comparison is case sensitive, so ``"Yes" == "yes"`` is False and they would be charged. Use
         ``.lower()``: ``member = input("Member? (yes/no) ").lower()``

      .. marking-guidance::

         * 1 mark for case sensitivity.
         * 1 mark for using ``.lower()`` (or checking both spellings).

   .. subquestion:: d) Give one boundary test case for the age.
      :marks: 1

      .. model-answer::

         Age 12 (should cost $15 for a non-member) or age 11 (should be free).

      .. marking-guidance::

         1 mark for 11 or 12 with the expected result.
