==============================================
12. Building small Tkinter apps
==============================================

Learning intentions
--------------------

* I can plan a small GUI app by sketching the layout and listing its inputs, processes and outputs.
* I can combine widgets, functions and validation to build a complete working app.
* I can test my app with normal, boundary and invalid inputs and fix problems.

Success criteria
~~~~~~~~~~~~~~~~~

* I can draw a grid plan of my app before I code it.
* I can separate the calculation (a function that returns a value) from the GUI code.
* I can complete a test table for my app.

Planning an app
----------------

Good programmers plan before they code. For each app, work through these steps.

#. **Purpose:** What problem does the app solve? Who will use it?
#. **IPO chart:** List the **inputs**, **processes** and **outputs**.
#. **Grid sketch:** Draw the window as a grid. Write which widget goes in each row and column.
#. **Data:** What lists or dictionaries will you need?
#. **Functions:** What functions will you need? Which button runs each one?
#. **Test plan:** What normal, boundary and invalid inputs will you test?

App 1: Temperature converter
-----------------------------

**Purpose:** Convert a temperature from Celsius to Fahrenheit for a science class.

.. list-table:: IPO chart
   :header-rows: 1

   * - Input
     - Process
     - Output
   * - Temperature in °C (Entry)
     - Check it is a number. F = C × 9 / 5 + 32
     - Temperature in °F (Label), or an error message

.. code-block:: text

   Grid sketch
            column 0       column 1        column 2
   row 0   [Celsius:]     [ Entry  ]      [Convert]
   row 1   [   result label (columnspan=3)          ]

.. literalinclude:: files/tk_temperature.py
   :language: python

:download:`Download tk_temperature.py <files/tk_temperature.py>`

Notice that the **calculation** is in its own function, ``celsius_to_fahrenheit()``, which **returns** a value.
The ``convert()`` function handles the GUI: reading the Entry, validating it and showing the result. Keeping
these separate makes the calculation easy to test and reuse.

.. list-table:: Test table
   :header-rows: 1

   * - Input
     - Type
     - Expected output
   * - 25
     - Normal
     - 25.0 °C = 77.0 °F
   * - 100
     - Boundary (boiling point)
     - 100.0 °C = 212.0 °F
   * - -40
     - Boundary (the same in both scales)
     - -40.0 °C = -40.0 °F
   * - abc
     - Invalid
     - Please type a number. (in red)
   * - (empty)
     - Invalid
     - Please type a number. (in red)

App 2: Bill splitter
---------------------

**Purpose:** Split a restaurant bill between friends, with an optional tip.

.. list-table:: IPO chart
   :header-rows: 1

   * - Inputs
     - Process
     - Output
   * - Bill total (Entry), tip (Radiobuttons), number of people (OptionMenu)
     - Check the bill is a number above 0. total = bill + bill × tip. share = total ÷ people
     - Amount each person pays (Label), or an error message

.. literalinclude:: files/tk_tip_calculator.py
   :language: python

:download:`Download tk_tip_calculator.py <files/tk_tip_calculator.py>`

This app uses a **dictionary** to link each tip option to its rate. The Radiobuttons are created from the
dictionary keys, and the rate is looked up with ``TIP_OPTIONS[tip_var.get()]``. To add a 20% option, you only
need to add one item to the dictionary.

Activities
-----------

Activity 1: IPO
~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Input, Process, Output
   :delimiter: =>
   :instructions: For the bill splitter app, sort each item.

   The bill total typed in the Entry => Input
   The tip chosen with a Radiobutton => Input
   The number of people chosen in the OptionMenu => Input
   Checking the bill is a number above 0 => Process
   Working out the total with the tip => Process
   Dividing the total by the number of people => Process
   "Each person pays $27.50" shown in a Label => Output
   An error message shown in red => Output

Activity 2: Predict the result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the bill splitter code to work out what the app shows.

.. fillin::

   Bill 100, No tip, 4 people: Each person pays $@@25.00@@
   Bill 100, 10%, 4 people: Each person pays $@@27.50@@
   Bill 60, 15%, 3 people: Each person pays $@@23.00@@

Activity 3: Order the function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Put the lines of the ``convert()`` function in order and fix the indents.

.. ordering::

   def convert():
       text = celsius_entry.get()
       try:
           celsius = float(text)
       except ValueError:
           result_label.config(text="Please type a number.", fg="red")
           return
       fahrenheit = celsius_to_fahrenheit(celsius)
       result_label.config(text=f"{celsius:.1f} °C = {fahrenheit:.1f} °F", fg="black")

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Why is the calculation in its own function that returns a value?

      [ ] Tkinter will not allow maths in other functions | It would allow it.
      [x] It keeps the calculation separate from the GUI, so it is easier to test and reuse | Correct.
      [ ] It makes the window bigger | Not related.
      [ ] Return values are faster than print | Not the main reason.

   .. multichoice::

      How would you add a 20% tip option to the bill splitter?

      [ ] Write a new Radiobutton line and a new if statement | Possible, but the dictionary is designed to avoid this.
      [x] Add ``"20%": 0.20`` to the TIP_OPTIONS dictionary | Correct. The loop creates the Radiobutton automatically.
      [ ] Change the OptionMenu | The OptionMenu is for the number of people.
      [ ] It is not possible | It is easy.

Coding challenges
------------------

Plan each app (IPO chart, grid sketch and test table) **before** coding it.

#. **Kilometres to miles:** Like the temperature converter, with a Radiobutton to choose the direction
   (km → miles or miles → km).
#. **Grade calculator:** An Entry for a mark out of 100 and a button that shows the grade, using the algorithm from
   :doc:`python_03_algorithms`. Validate the mark.
#. **Random team picker:** An Entry and Listbox to build a list of names, and a button that shuffles them into two
   teams shown in two Labels.
#. **Extension: GST calculator:** Radiobuttons to choose "add GST" or "remove GST" (10% in Australia), an Entry for
   the amount and a Label showing the GST amount and the final price.

Exam-style question
--------------------

.. structuredquestion:: Planning a GUI app
   :total-marks: 7
   :category: GUI

   .. stimulus::

      A gym wants a simple app that calculates the cost of a membership. Members choose a plan (Casual $15 per
      visit, Monthly $60, Yearly $600) and type a name. The app shows the cost and a welcome message.

   .. subquestion:: a) Complete an IPO chart for the app.
      :marks: 3

      .. model-answer::

         * Inputs: member name (Entry), plan (Radiobuttons or OptionMenu).
         * Process: check the name is not empty; look up the cost of the chosen plan.
         * Output: the cost and a welcome message in a Label (or an error message).

      .. marking-guidance::

         * 1 mark for correct inputs with suitable widgets.
         * 1 mark for a process that includes validation or the price lookup.
         * 1 mark for correct outputs.

   .. subquestion:: b) Write the Python line that stores the plans and prices in a suitable data structure.
      :marks: 2

      .. model-answer::

         ``PLANS = {"Casual": 15, "Monthly": 60, "Yearly": 600}``

      .. marking-guidance::

         * 1 mark for using a dictionary.
         * 1 mark for correct keys and values.

   .. subquestion:: c) Describe two test cases the gym should use, including the expected output.
      :marks: 2

      .. model-answer::

         * Name "Sam", plan Monthly → "Welcome Sam! Cost: $60.00" (normal).
         * Name left empty, plan Yearly → an error message asking for a name (invalid).

      .. marking-guidance::

         1 mark for each test case with input and expected output (maximum 2).
