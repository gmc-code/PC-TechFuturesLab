==============================================
6. Functions
==============================================

Learning intentions
--------------------

* I can explain why programmers use functions to structure code.
* I can define and call my own functions, using parameters and return values.
* I can break a problem into smaller functions (modular programming).

Success criteria
~~~~~~~~~~~~~~~~~

* I can write a function with ``def``, a name, brackets and a colon.
* I can pass values into a function using parameters.
* I can return a value from a function and use it in the main program.

What is a function?
--------------------

A **function** is a named block of code that does one job. You have already used built-in functions such as
``print()``, ``input()``, ``int()`` and ``len()``. Now you will write your own.

Functions help you:

* **avoid repeating code:** write it once and call it many times
* **organise programs** into small parts that are easy to read, test and fix (this is called **modular
  programming**)
* **share work** in a team: each person can write different functions

Defining and calling a function
--------------------------------

.. code-block:: python

   def say_hello():
       print("Hello!")
       print("Welcome to TechFuturesLab.")


   say_hello()
   say_hello()

* ``def`` starts a **function definition**. The code inside is indented.
* Defining a function does **not** run it. The code runs when you **call** the function by writing its name
  with brackets: ``say_hello()``.
* Define functions near the **top** of your program, before you call them.

Parameters
-----------

**Parameters** let you send information **into** a function.

.. code-block:: python

   def greet(name):
       print(f"Hello, {name}!")


   greet("Ava")
   greet("Leo")

Output:

.. code-block:: text

   Hello, Ava!
   Hello, Leo!

``name`` is the **parameter**. ``"Ava"`` and ``"Leo"`` are the **arguments**: the actual values sent in.
A function can have several parameters, separated by commas:

.. code-block:: python

   def describe_pet(animal, pet_name):
       print(f"I have a {animal} called {pet_name}.")


   describe_pet("dog", "Biscuit")

Return values
--------------

``return`` sends a value **back** from the function to the code that called it.

.. code-block:: python

   def add_gst(price):
       return price * 1.1


   cost = add_gst(50)
   print(f"With GST: ${cost:.2f}")

Output:

.. code-block:: text

   With GST: $55.00

.. admonition:: print vs return
   :class: note

   ``print()`` shows a value on the screen. ``return`` hands a value back so the program can **use** it
   (store it, do maths with it or pass it to another function). A function that does a calculation should
   usually ``return`` the answer.

Local variables
~~~~~~~~~~~~~~~~

Variables created inside a function are **local**: they only exist inside that function. This stops functions
from accidentally changing each other's data.

Worked example: area calculator
--------------------------------

This program is split into three functions plus a main program.

.. literalinclude:: files/shapes.py
   :language: python

:download:`Download shapes.py <files/shapes.py>`

Each function does **one** job:

* ``rectangle_area()`` and ``triangle_area()`` calculate and **return** an area.
* ``show_result()`` displays a result.
* The main program asks the questions and decides which function to call.

The text in triple quotes under each ``def`` line is a **docstring**: a short description of what the function
does.

Activities
-----------

Activity 1: Key words
~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   A function is defined using the keyword @@def|function|define@@.
   The values inside the brackets in a function definition are called @@parameters|arguments|returns@@.
   The actual values you pass in when you call the function are called @@arguments|parameters|variables@@.
   @@return|print|input@@ sends a value back to the code that called the function.
   A variable created inside a function is @@local|global|constant@@.

Activity 2: Predict the output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. multichoice::

   What does this program print?

   .. code-block:: python

      def double(n):
          return n * 2

      print(double(3) + double(4))

   [ ] 7 | That would be 3 + 4.
   [ ] 34 | The numbers are added, not joined.
   [x] 14 | Correct. 6 + 8 = 14.
   [ ] 24 | Not correct.

.. multichoice::

   What does this program print?

   .. code-block:: python

      def show_message():
          print("Done!")

      print("Start")

   [x] Start | Correct. The function is defined but never called.
   [ ] Start Done! | show_message() is never called.
   [ ] Done! Start | The function is not called.
   [ ] An error | This code runs.

Activity 3: Build the function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Put this program in order. It has a function that works out the average of three numbers.

.. ordering::

   def average(a, b, c):
       total = a + b + c
       return total / 3

   result = average(70, 85, 91)
   print(f"Average: {result:.1f}")

Activity 4: Complete the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze:: python
   :show-code:

   @@def@@ circle_area(radius):
       area = 3.14159 * radius ** 2
       @@return@@ area

   size = float(input("Radius: "))
   print(f"Area: {@@circle_area@@(size):.2f}")

Activity 5: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Why is it a good idea to break a program into functions?

      [ ] It makes the program run faster | Not usually the reason.
      [x] It makes code easier to read, test, fix and reuse | Correct.
      [ ] Python needs at least three functions | It does not.
      [ ] Functions use less electricity | Not correct.

   .. multichoice::

      Which line correctly calls the function ``def total(price, quantity):``?

      [ ] ``total`` | Brackets are needed to call it.
      [ ] ``def total(5, 2)`` | def is only used to define.
      [x] ``total(5, 2)`` | Correct.
      [ ] ``total[5, 2]`` | Use round brackets.

Coding challenges
------------------

#. **Temperature functions:** Write ``c_to_f(c)`` and ``f_to_c(f)`` that return the converted temperature.
   Test: ``c_to_f(100)`` returns 212 and ``f_to_c(32)`` returns 0.
#. **Validation function:** Write ``get_number(low, high)`` that keeps asking the user for a number until it is
   between ``low`` and ``high``, then returns it. Use it to ask for a rating from 1 to 10.
#. **Menu program:** Write a program with a ``show_menu()`` function and separate functions for each choice
   (for example, add, subtract and multiply two numbers). Use a ``while`` loop so the user can keep choosing until
   they type ``q``.
#. **Extension:** Write ``is_leap_year(year)`` that returns ``True`` or ``False``, and use it in a loop to print every
   leap year from 2000 to 2100.

Exam-style question
--------------------

.. structuredquestion:: Writing functions
   :total-marks: 7
   :category: Functions

   .. stimulus::

      A cafe charges $4.50 for a coffee. Loyalty card holders get 10% off. The owner wants a function to calculate
      the cost of an order.

   .. subquestion:: a) Write a function called ``order_cost`` with parameters ``quantity`` and ``has_card`` that returns the cost of the order.
      :marks: 4

      .. model-answer::

         .. code-block:: python

            def order_cost(quantity, has_card):
                cost = quantity * 4.50
                if has_card:
                    cost = cost * 0.9
                return cost

      .. marking-guidance::

         * 1 mark for a correct ``def`` line with both parameters.
         * 1 mark for calculating quantity × 4.50.
         * 1 mark for applying the 10% discount when ``has_card`` is True.
         * 1 mark for returning (not printing) the cost.

   .. subquestion:: b) What value does ``order_cost(4, True)`` return?
      :marks: 1

      .. model-answer::

         16.2 (4 × 4.50 = 18.00, minus 10% = 16.20)

      .. marking-guidance::

         1 mark for 16.2 (or $16.20).

   .. subquestion:: c) Explain why the function should return the cost rather than print it.
      :marks: 2

      .. model-answer::

         Returning the cost lets the rest of the program use the value, for example to add it to a daily total or
         display it in a GUI label. A printed value only appears on the screen and cannot be used in calculations.

      .. marking-guidance::

         * 1 mark for saying the returned value can be used by the program.
         * 1 mark for an example or for contrasting with print.
