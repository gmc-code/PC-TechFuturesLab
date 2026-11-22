==============================================
2. Variables and f-strings
==============================================

Learning intentions
--------------------

* I can create variables and choose good names for them.
* I can explain the data types string, integer, float and Boolean, and convert between them.
* I can use arithmetic and f-strings to calculate and display results neatly.

Success criteria
~~~~~~~~~~~~~~~~~

* I can store values in variables and change them.
* I can use ``int()`` and ``float()`` to turn input into numbers.
* I can write f-strings that include variables and round money to 2 decimal places.

Variables
----------

A **variable** is a named box that stores a value. You create a variable with ``=``, which is called
**assignment**.

.. code-block:: python

   score = 0
   player = "Ava"
   score = score + 10      # take the old value, add 10, store it back
   print(player, score)

Output:

.. code-block:: text

   Ava 10

.. admonition:: ``=`` does not mean "equals"
   :class: note

   In Python, ``=`` means **"store the value on the right in the variable on the left"**. So
   ``score = score + 10`` makes sense: work out ``score + 10``, then store the answer back in ``score``.

Naming variables
~~~~~~~~~~~~~~~~~

* Use lowercase letters, numbers and underscores: ``total_cost``, ``player_name``, ``level2``.
* Do not start with a number: ``2player`` is not allowed.
* No spaces: ``total cost`` is not allowed.
* Choose names that describe the value: ``price`` is better than ``p`` or ``x``.

Data types
-----------

.. list-table::
   :header-rows: 1
   :widths: 20 15 30 35

   * - Type
     - Python name
     - Examples
     - Used for
   * - String
     - ``str``
     - ``"Hello"``, ``"42"``, ``"3 Smith St"``
     - Text
   * - Integer
     - ``int``
     - ``7``, ``0``, ``-15``
     - Whole numbers
   * - Float
     - ``float``
     - ``3.14``, ``0.5``, ``-2.0``
     - Decimal numbers
   * - Boolean
     - ``bool``
     - ``True``, ``False``
     - Yes/no values

You can check a value's type with ``type()``:

.. code-block:: python

   print(type("42"))
   print(type(42))
   print(type(4.2))
   print(type(True))

Output:

.. code-block:: text

   <class 'str'>
   <class 'int'>
   <class 'float'>
   <class 'bool'>

Input is always a string
~~~~~~~~~~~~~~~~~~~~~~~~~

``input()`` **always** gives back a string, even if the user types a number. To do maths, convert it first.

.. code-block:: python

   age = input("How old are you? ")       # "14" (a string)
   age = int(age)                          # 14 (an integer)
   print(age + 1)

You can do both in one line: ``age = int(input("How old are you? "))``.

* ``int()`` converts to a whole number.
* ``float()`` converts to a decimal number.
* ``str()`` converts to a string.

Arithmetic
-----------

.. list-table::
   :header-rows: 1
   :widths: 20 30 25 25

   * - Operator
     - Meaning
     - Example
     - Result
   * - ``+``
     - add
     - ``7 + 2``
     - ``9``
   * - ``-``
     - subtract
     - ``7 - 2``
     - ``5``
   * - ``*``
     - multiply
     - ``7 * 2``
     - ``14``
   * - ``/``
     - divide
     - ``7 / 2``
     - ``3.5``
   * - ``//``
     - whole-number divide
     - ``7 // 2``
     - ``3``
   * - ``%``
     - remainder (modulo)
     - ``7 % 2``
     - ``1``
   * - ``**``
     - power
     - ``7 ** 2``
     - ``49``

Python follows the same order of operations as maths: brackets first, then powers, then ``*`` and ``/``,
then ``+`` and ``-``.

f-strings
----------

An **f-string** is a string with an ``f`` in front. You can put variables (and even calculations) inside
**curly brackets** ``{}``.

.. code-block:: python

   name = "Ava"
   age = 14
   print(f"{name} is {age} years old.")
   print(f"Next year {name} will be {age + 1}.")

Output:

.. code-block:: text

   Ava is 14 years old.
   Next year Ava will be 15.

f-strings are easier to read than joining with ``+`` and they work with numbers, so you do not need
``str()``.

Formatting numbers
~~~~~~~~~~~~~~~~~~~

Add ``:.2f`` inside the curly brackets to show a number with **2 decimal places**, which is perfect for money.

.. code-block:: python

   price = 4.5
   print(f"Price: ${price:.2f}")
   print(f"One third is about {1 / 3:.3f}")

Output:

.. code-block:: text

   Price: $4.50
   One third is about 0.333

Worked example: canteen receipt
--------------------------------

.. literalinclude:: files/receipt.py
   :language: python

:download:`Download receipt.py <files/receipt.py>`

Example run:

.. code-block:: text

   What would you like to order? Toastie
   How much does it cost? $4.5
   How many would you like? 3

   ----- RECEIPT -----
   Item:     Toastie
   Price:    $4.50
   Quantity: 3
   Total:    $13.50
   -------------------

Activities
-----------

Activity 1: Data types
~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: String, Integer, Float, Boolean
   :delimiter: =>

   "Hello" => String
   "42" => String
   "3.5" => String
   42 => Integer
   -7 => Integer
   0 => Integer
   3.5 => Float
   -0.25 => Float
   True => Boolean
   False => Boolean

Activity 2: Complete the program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program works out the area of a rectangle. Choose the right code for each gap.

.. gapfill::

   length = @@float|str|print@@(input("Length in metres: "))
   width = float(input("Width in metres: "))
   area = length @@*|+|/@@ width
   print(@@f|s|r@@"The area is {area:.1f} square metres.")

Activity 3: What is the output?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type the exact output of each line.

.. fillin::

   print(10 // 3) gives @@3@@
   print(10 % 3) gives @@1@@
   print(2 ** 3) gives @@8@@
   print(10 / 4) gives @@2.5@@
   print(f"{7.456:.1f}") gives @@7.5@@

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Which is a valid variable name?

      [ ] 2nd_place | Cannot start with a number.
      [ ] total cost | Cannot contain a space.
      [x] total_cost | Correct.
      [ ] total-cost | A hyphen means subtract.

   .. multichoice::

      The user types 5. What does this code print?

      .. code-block:: python

         number = input("Number: ")
         print(number * 2)

      [ ] 10 | ``input()`` gives a string, not a number.
      [x] 55 | Correct. A string times 2 repeats it.
      [ ] An error | Multiplying a string by a number works. It repeats the string.
      [ ] 52 | Not correct.

   .. multichoice::

      Which line prints ``Total: $7.50``?

      [ ] ``print("Total: $" + 7.5)`` | You cannot join a string and a float with ``+``.
      [x] ``print(f"Total: ${7.5:.2f}")`` | Correct.
      [ ] ``print(f"Total: $7.5")`` | This prints $7.5, not $7.50.
      [ ] ``print("Total: ${7.5:.2f}")`` | Without the ``f``, the curly brackets are printed.

Coding challenges
------------------

#. **Age in days:** Ask for the user's age in years and print roughly how many days old they are
   (age × 365).
#. **Temperature converter:** Ask for a temperature in Celsius and print it in Fahrenheit using
   ``F = C × 9 / 5 + 32``, rounded to 1 decimal place.
#. **Pizza share:** Ask for the number of pizzas, slices per pizza and number of people. Print how many whole
   slices each person gets (``//``) and how many are left over (``%``).
#. **Name box:** Ask for a name and print it in a box of stars that fits the name exactly. Hint: ``"*" * 5``
   gives ``*****`` and ``len(name)`` gives the number of letters in ``name``.

Exam-style question
--------------------

.. structuredquestion:: Variables and data types
   :total-marks: 6
   :category: Python basics

   .. stimulus::

      .. code-block:: python

         tickets = input("How many tickets? ")
         price = 12.5
         total = tickets * price
         print(f"Total cost: ${total:.2f}")

   .. subquestion:: a) Identify the data type of ``price`` and of ``tickets``.
      :marks: 2

      .. model-answer::

         ``price`` is a float. ``tickets`` is a string, because ``input()`` always returns a string.

      .. marking-guidance::

         1 mark for each correct data type.

   .. subquestion:: b) The program crashes on line 3. Explain why and rewrite line 1 to fix it.
      :marks: 2

      .. model-answer::

         ``tickets`` is a string and you cannot multiply a string by a float, so Python gives a ``TypeError``.
         Fix: ``tickets = int(input("How many tickets? "))``

      .. marking-guidance::

         * 1 mark for explaining that tickets is a string (needs converting to a number).
         * 1 mark for the corrected line using ``int()``.

   .. subquestion:: c) After the fix, the user enters 3. Write the exact output of line 4.
      :marks: 1

      .. model-answer::

         ``Total cost: $37.50``

      .. marking-guidance::

         1 mark for ``Total cost: $37.50`` (must show 2 decimal places).

   .. subquestion:: d) Explain what ``:.2f`` does in the f-string.
      :marks: 1

      .. model-answer::

         It shows the number as a decimal (float) rounded to 2 decimal places.

      .. marking-guidance::

         1 mark for "2 decimal places".
