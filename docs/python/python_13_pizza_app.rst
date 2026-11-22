==============================================
13. The pizza ordering app
==============================================

Learning intentions
--------------------

* I can read and explain a complete Tkinter ordering app.
* I can explain how the app uses a nested dictionary, a list of dictionaries and functions.
* I can make changes to the app's data, widgets and functions and test them.

Success criteria
~~~~~~~~~~~~~~~~~

* I can trace what happens when the **Add order** button is clicked.
* I can add a new pizza and a new size by changing only the data.
* I can add a new feature (such as a discount) and test it.

This lesson walks through a complete ordering app. It is the **starting point** for your
:doc:`python_assessment_gui_project`. For a lesson-by-lesson build of a pizza app, also see the
`pizza orders tutorial on PC-app-development <https://pc-app-development.readthedocs.io/en/latest/tk_pizza_orders_tutorial/pizza_orders.html>`_.

The finished app
-----------------

.. code-block:: text

                         Pizza orders
   Customer:  [ Sam                     ]
   Pizza:     ◉ Margherita ($12.00)              Size:
              ○ Pepperoni ($14.00)               ○ Small
              ○ Hawaiian ($14.00)                ◉ Medium
              ○ Vegetarian ($13.00)              ○ Large
   Toppings: tomato, mozzarella, basil
   Quantity:  [ 1 ▾ ]
              [  Add order  ]
   ┌──────────────────────────────────────────────┐
   │ Sam: 1 x Medium Margherita  $12.00           │
   │ Lee: 2 x Large Vegetarian  $33.80            │
   └──────────────────────────────────────────────┘
   Total: $45.80                       [Delete order]
                                       [ Clear all  ]

The complete code
------------------

.. literalinclude:: files/pizza_orders_starter.py
   :language: python
   :linenos:

:download:`Download pizza_orders_starter.py <files/pizza_orders_starter.py>`

How it works
-------------

Section 2: the data
~~~~~~~~~~~~~~~~~~~~

* ``PIZZAS`` is a **nested dictionary**. Each pizza name is a key, and its value is a dictionary holding the
  ``price`` and ``toppings``. ``PIZZAS["Hawaiian"]["price"]`` gives ``14.0``.
* ``SIZES`` is a dictionary of **multipliers**. A large pizza costs 1.3 times the medium price.
* ``QUANTITIES`` is a list used to fill the OptionMenu.
* ``orders`` is a **list of dictionaries**. Each time an order is added, a new dictionary is appended:

  .. code-block:: python

     {"customer": "Sam", "pizza": "Hawaiian", "size": "Small", "quantity": 3, "cost": 33.6}

Names in CAPITALS (``PIZZAS``, ``SIZES``) are **constants**: data that does not change while the program runs.

Section 3: the functions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Function
     - Run by
     - What it does
   * - ``calculate_cost()``
     - ``add_order()``
     - **Returns** price × size multiplier × quantity
   * - ``show_toppings()``
     - Clicking a pizza Radiobutton
     - Shows that pizza's toppings in a Label
   * - ``add_order()``
     - **Add order** button
     - Validates the name, builds an order dictionary, appends it, resets the quantity and updates the display
   * - ``update_display()``
     - ``add_order()``, ``delete_order()``, ``clear_orders()``
     - Clears the Listbox, adds one line per order and works out the total
   * - ``delete_order()``
     - **Delete order** button
     - Removes the selected order from the list and the display
   * - ``clear_orders()``
     - **Clear all** button
     - Asks "Delete ALL orders?" and clears the list if the user clicks Yes

Notice how ``update_display()`` is called by three different functions. Writing it once and calling it from
each place is an example of **modular** code.

Section 4: the widgets
~~~~~~~~~~~~~~~~~~~~~~~

* The pizza Radiobuttons are made with a ``for`` loop over the ``PIZZAS`` dictionary. To add a pizza, you only
  change the dictionary.
* ``tk.Frame`` widgets group the Radiobuttons so they can be placed as one block in the grid. Inside a frame,
  ``.pack(anchor="w")`` stacks widgets on top of each other, lined up on the left.
* ``show_toppings()`` is called once just before ``mainloop()`` so the toppings appear when the app opens.

Tracing the Add order button
-----------------------------

Put the steps in the order they happen when the user types "Sam", chooses a Small Hawaiian, quantity 3, and
clicks **Add order**.

.. ordering::
   :no-indent:

   add_order() reads the customer name, pizza, size and quantity.
   It checks that the name is not empty.
   calculate_cost("Hawaiian", "Small", 3) returns 14.00 × 0.8 × 3 = 33.60.
   A new order dictionary is appended to the orders list.
   The quantity is reset to 1.
   update_display() rewrites the Listbox and the total.

Activities
-----------

Activity 1: Read the data
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. fillin::

   PIZZAS["Pepperoni"]["price"] is @@14.0@@
   SIZES["Large"] is @@1.3@@
   calculate_cost("Margherita", "Large", 2) to 2 decimal places is @@31.20@@
   calculate_cost("Vegetarian", "Small", 1) to 2 decimal places is @@10.40@@

Activity 2: What would you change?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Data (section 2), Functions (section 3), Widgets (section 4)
   :delimiter: =>
   :instructions: Where in the program would you make each change?

   Add a Supreme pizza for $16 => Data (section 2)
   Add an Extra large size => Data (section 2)
   Allow quantities up to 20 => Data (section 2)
   Give 10% off orders of 5 or more pizzas => Functions (section 3)
   Stop orders being added without a size => Functions (section 3)
   Change the title font and colour => Widgets (section 4)
   Add a phone number Entry box => Widgets (section 4)

Activity 3: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      What type of data structure is ``orders``?

      [ ] A nested dictionary | PIZZAS is the nested dictionary.
      [x] A list of dictionaries | Correct. Each order is a dictionary in the list.
      [ ] A string | Not correct.
      [ ] A tuple | Not correct.

   .. multichoice::

      Why does ``delete_order()`` use ``orders.pop(position)``?

      [x] The Listbox line and the order in the list have the same position, so it removes the matching order | Correct.
      [ ] pop() deletes the whole list | It deletes one item.
      [ ] It removes the last order only | pop(position) removes the item at that position.
      [ ] It is needed to close the window | Not related.

   .. multichoice::

      Which line makes the pizza Radiobuttons show the toppings when clicked?

      [ ] ``variable=pizza_var`` | That stores the choice.
      [x] ``command=show_toppings`` | Correct.
      [ ] ``value=pizza`` | That sets each button's value.
      [ ] ``.pack(anchor="w")`` | That positions the button.

Practice modifications
-----------------------

Try each change. Test after **every** change.

#. Add a **Supreme** pizza ($16.00) with its own toppings. *(Change only the data.)*
#. Add an **Extra large** size that costs 1.6 times the medium price.
#. Add a **Delivery** Radiobutton (Pick up / Delivery). Delivery adds $5.00 to the total.
#. Give **10% off** when the total number of pizzas is 5 or more. Show the discount in a Label.
#. Change the colours and fonts to suit a pizza shop brand you invent.

Exam-style question
--------------------

.. structuredquestion:: Modifying the ordering app
   :total-marks: 7
   :category: GUI

   .. stimulus::

      The owner wants to add a **Gluten free** option to the pizza app. Gluten free bases cost an extra $3.00 per
      pizza. The option should be a Radiobutton with the choices "Regular" and "Gluten free".

   .. subquestion:: a) Write the code to create a Tkinter variable called ``base_var`` and the two Radiobuttons.
      :marks: 3

      .. model-answer::

         .. code-block:: python

            base_var = tk.StringVar(value="Regular")
            tk.Radiobutton(root, text="Regular", variable=base_var, value="Regular").grid(row=4, column=2, sticky="w")
            tk.Radiobutton(root, text="Gluten free", variable=base_var, value="Gluten free").grid(row=5, column=2, sticky="w")

      .. marking-guidance::

         * 1 mark for creating a StringVar with a starting value.
         * 1 mark for two Radiobuttons sharing ``base_var``.
         * 1 mark for correct values and placing them with grid (any sensible row/column).

   .. subquestion:: b) Rewrite ``calculate_cost()`` so it includes the gluten free cost.
      :marks: 3

      .. model-answer::

         .. code-block:: python

            def calculate_cost(pizza, size, quantity, base):
                price = PIZZAS[pizza]["price"] * SIZES[size]
                if base == "Gluten free":
                    price = price + 3.00
                return price * quantity

         And in ``add_order()``: ``cost = calculate_cost(pizza, size, quantity, base_var.get())``

      .. marking-guidance::

         * 1 mark for adding a ``base`` parameter (or reading ``base_var``).
         * 1 mark for adding $3.00 per pizza when the base is gluten free.
         * 1 mark for returning the correct cost (extra applied per pizza, multiplied by quantity).

   .. subquestion:: c) Give one test case for the new feature with its expected cost.
      :marks: 1

      .. model-answer::

         2 × Medium Margherita, gluten free: (12.00 + 3.00) × 2 = $30.00

      .. marking-guidance::

         1 mark for a test case with the correct expected cost.
