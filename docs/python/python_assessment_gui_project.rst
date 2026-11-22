==============================================
Assessment: Python GUI project
==============================================

.. list-table::
   :widths: 30 70

   * - **Type**
     - Project (individual, pair or group, as your teacher decides)
   * - **Dates**
     - Starts Term 2, Week 4. Due Term 2, Week 6. Ends Term 2, Week 8.
   * - **Software**
     - Python 3 with Tkinter (IDLE, Thonny or VS Code)
   * - **Achievement standards**
     - Students develop algorithms represented diagrammatically and in English, and trace algorithms to predict
       output for a given input and to identify errors. Students develop and modify programs with user interfaces
       involving branching, iteration and functions using a general-purpose programming language.
   * - **Capabilities**
     - Critical and creative thinking: repurpose existing ideas or solutions to meet needs in new contexts.
       Personal and social: use feedback to identify achievements and prioritise areas for improvement.

Learning intentions
--------------------

* I can modify an existing Tkinter app to meet the needs of a new user.
* I can design algorithms and data structures for my app and represent them as pseudocode or flowcharts.
* I can test my app with a range of test cases and improve it.

The task
---------

Build and customise a **Tkinter ordering app** for a small business. Start from the pizza ordering app and
**repurpose** it for a business of your choice, for example:

* a bubble tea shop
* a school canteen
* a bike hire shop
* a movie cinema candy bar
* a sports club merchandise shop
* a plant nursery
* your own idea (check with your teacher)

Starting files
~~~~~~~~~~~~~~~

* :download:`pizza_orders_starter.py <files/pizza_orders_starter.py>` (explained in :doc:`python_13_pizza_app`)
* `Pizza orders tutorial on PC-app-development <https://pc-app-development.readthedocs.io/en/latest/tk_pizza_orders_tutorial/pizza_orders.html>`_

Requirements
~~~~~~~~~~~~~

Your app must:

#. Use a **nested dictionary** for your products (for example, each product has a price and a description).
#. Use a **list** to store the orders.
#. Include at least **five** different widget types from: Label, Button, Entry, Text, Listbox, Radiobutton,
   OptionMenu (and Frame for layout).
#. Use **functions** for each job, including at least one function that **returns** a calculated value.
#. Use **selection** (``if``/``elif``/``else``) and **iteration** (``for`` or ``while`` loops).
#. **Validate** user input (for example, a presence check on the customer name) and show helpful error messages.
#. Let the user **add**, **view** and **delete** orders, and show a **running total**.
#. Include at least **two new features** that are not in the starter app. Ideas:

   * a discount (for example, 10% off 5 or more items, or a student discount Radiobutton)
   * extras or add-ons with their own prices (for example, extra pearls in bubble tea)
   * delivery or pick-up option with a fee
   * a receipt shown in a Text widget or messagebox
   * a search box that finds products
   * saving orders to a text file

#. Have a clear, consistent design (layout, colours and fonts suited to the business).
#. Be well **structured** and **commented**, with meaningful variable and function names.

Stages
-------

Stage 1: Plan (Week 4)
~~~~~~~~~~~~~~~~~~~~~~~

#. Describe the **business** and its **users**. Ask at least one possible user what they would want from the app.
#. List your **functional requirements** (what the app must do) and **non-functional requirements** (how well,
   for example "easy to use for first-time customers").
#. Write your **data structures**: the nested dictionary of products and any other lists or dictionaries.
#. Draw a **grid sketch** of the interface (rows, columns and widgets).
#. Write **pseudocode** or draw a **flowchart** for at least two functions (for example, ``add_order`` and your
   discount calculation).

Stage 2: Build (Weeks 4–5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Save a copy of the starter file with a new name, for example ``bubble_tea_orders.py``.
#. Change the **data** first, then run the app to check it still works.
#. Change the **widgets** and layout to suit your business.
#. Add your **new features** one at a time. Run and test after each change.
#. Add comments to explain each section and function.

Stage 3: Test (Week 6)
~~~~~~~~~~~~~~~~~~~~~~~

Create a **test table** with at least **eight** test cases, including normal, boundary and invalid data.

.. list-table:: Example test table
   :header-rows: 1

   * - Test
     - Input
     - Type
     - Expected result
     - Actual result
     - Pass?
   * - 1
     - Name "Sam", Medium Taro, quantity 2
     - Normal
     - Order added, total $13.00
     -
     -
   * - 2
     - Name left empty
     - Invalid
     - Error message, name box turns pink, no order added
     -
     -
   * - 3
     - Quantity 5 (discount starts at 5)
     - Boundary
     - 10% discount applied
     -
     -
   * - 4
     - Click Delete with nothing selected
     - Invalid
     - Message asks user to select an order
     -
     -

Ask at least one other person to test your app and record their feedback.

Stage 4: Evaluate (Week 6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write a short evaluation (150–250 words):

#. How well does your app meet each requirement?
#. Which new features did you add, and how do they help the user?
#. What feedback did testers give, and what did you change?
#. What would you add or improve with more time?

What to submit
---------------

#. Your **planning document**: business and users, requirements, data structures, grid sketch, and
   pseudocode or flowcharts for at least two functions.
#. Your **Python file** (``.py``).
#. **Screenshots** of your app working, including an error message.
#. Your **test table** and tester feedback.
#. Your **evaluation**.
#. If you worked in a group: a short statement of what **each** member contributed.

Marking guide
--------------

.. list-table::
   :header-rows: 1
   :widths: 16 21 21 21 21

   * - Criterion
     - Excellent (4–5)
     - Good (3)
     - Satisfactory (2)
     - Needs work (0–1)
   * - **Planning and algorithms**
     - Clear requirements based on user needs. Accurate data structures, grid sketch, and detailed pseudocode or
       flowcharts that match the code.
     - Requirements, data structures, sketch and pseudocode or flowcharts mostly complete and accurate.
     - Some planning. Pseudocode or flowchart is basic or does not match the code.
     - Little or no planning.
   * - **Data structures**
     - Nested dictionary and list used effectively. Changing the data automatically updates the interface (for
       example, widgets made with loops).
     - Nested dictionary and list used correctly.
     - Data structures used but with some errors or hard-coded values.
     - Data structures missing or not working.
   * - **Interface design**
     - Five or more widget types used well. Clear, consistent, attractive layout suited to the business and easy to
       use.
     - Five widget types. Clear layout.
     - Fewer widget types, or the layout is cluttered or confusing.
     - Interface incomplete.
   * - **Functionality and code structure**
     - All requirements met. Two or more new features that work well. Well-organised functions, selection and
       iteration. Meaningful names and helpful comments.
     - Most requirements met. Two new features work. Functions, selection and iteration used correctly.
     - Some requirements met. One new feature. Code works but is hard to follow.
     - App does not run or most requirements are missing.
   * - **Validation, testing and evaluation**
     - Thorough validation with helpful messages. Eight or more test cases covering normal, boundary and invalid
       data. Feedback used to improve the app. Insightful evaluation.
     - Validation works. Test table with normal, boundary and invalid data. Sensible evaluation.
     - Some validation. A few tests. Brief evaluation.
     - Little or no validation, testing or evaluation.

**Total: 25 marks** (5 criteria × 5 marks)

.. note::

   Grades are reported from A+ to NP. A task below a C standard must be resubmitted. Your teacher will confirm how
   the marks convert to grades.

Checklist before you submit
----------------------------

* ☐ Planning document complete (requirements, data, grid sketch, pseudocode or flowcharts)
* ☐ Nested dictionary of products and a list of orders
* ☐ At least five widget types
* ☐ Functions, including one that returns a value
* ☐ Selection and iteration used
* ☐ Input validation with helpful error messages
* ☐ Add, view and delete orders, with a running total
* ☐ At least two new features
* ☐ Comments and meaningful names
* ☐ Test table with at least eight tests, and tester feedback
* ☐ Screenshots and evaluation

Exam-style question
--------------------

.. structuredquestion:: Planning a feature
   :total-marks: 6
   :category: GUI project

   .. stimulus::

      Chloe's bubble tea app charges $6.50 per drink. She wants to add a feature: customers who order **5 or more**
      drinks get **10% off** the cost of that order.

   .. subquestion:: a) Write pseudocode for a function that calculates the order cost with the discount.
      :marks: 3

      .. model-answer::

         .. code-block:: text

            FUNCTION order_cost(quantity)
                cost ← quantity * 6.50
                IF quantity >= 5 THEN
                    cost ← cost * 0.9
                ENDIF
                RETURN cost
            ENDFUNCTION

      .. marking-guidance::

         * 1 mark for calculating quantity × 6.50.
         * 1 mark for a correct decision (quantity >= 5).
         * 1 mark for applying 10% off and returning the cost.

   .. subquestion:: b) Complete three test cases (one normal, one boundary, one other boundary) with expected costs.
      :marks: 3

      .. model-answer::

         * Quantity 2 (normal): $13.00
         * Quantity 4 (boundary, no discount): $26.00
         * Quantity 5 (boundary, discount): 5 × 6.50 = 32.50, minus 10% = $29.25

      .. marking-guidance::

         1 mark for each correct test case with the expected cost (must include 4 or 5 as a boundary).
