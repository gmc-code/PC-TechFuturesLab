================================================
11. Tkinter: Listbox, Radiobutton and OptionMenu
================================================

Learning intentions
--------------------

* I can use Tkinter variables (``StringVar`` and ``IntVar``) to store a user's choice.
* I can let users choose from options using Radiobuttons and an OptionMenu.
* I can show a list of items in a Listbox and find out which item the user selected.

Success criteria
~~~~~~~~~~~~~~~~~

* I can create a group of Radiobuttons from a list using a loop.
* I can create an OptionMenu (drop-down list) and read its value.
* I can add, read and delete Listbox items.

Why use choice widgets?
------------------------

Typing is slow and causes mistakes ("Medum", "larg"). When there is a fixed set of options, it is better to let
the user **choose**:

.. list-table::
   :header-rows: 1
   :widths: 22 38 40

   * - Widget
     - Looks like
     - Use when
   * - Radiobutton
     - ◉ Small ○ Medium ○ Large
     - the user must choose **exactly one** of a few options (2 to 5)
   * - OptionMenu
     - A drop-down list
     - there are **many** options, or space is tight
   * - Listbox
     - A box with a list of lines
     - showing a **list of items** (such as orders) or letting the user pick one or more items

Tkinter variables
------------------

Radiobuttons and OptionMenus store the user's choice in a special **Tkinter variable**.

.. code-block:: python

   size_var = tk.StringVar(value="Medium")    # holds a string; starts as "Medium"
   quantity_var = tk.IntVar(value=1)          # holds a whole number; starts as 1

   size_var.get()            # read the current choice
   quantity_var.set(1)       # change the choice

Radiobuttons
-------------

All the Radiobuttons in a group share the **same variable**. Each one has a different ``value``. When the user
clicks one, the variable is set to its value.

.. code-block:: python

   import tkinter as tk

   root = tk.Tk()
   size_var = tk.StringVar(value="Medium")

   tk.Radiobutton(root, text="Small", variable=size_var, value="Small").grid(row=0, column=0, sticky="w")
   tk.Radiobutton(root, text="Medium", variable=size_var, value="Medium").grid(row=1, column=0, sticky="w")
   tk.Radiobutton(root, text="Large", variable=size_var, value="Large").grid(row=2, column=0, sticky="w")

   root.mainloop()

Making Radiobuttons with a loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of writing one line per option, store the options in a **list** and use a loop. Now you only need to
change the list to add a new option.

.. code-block:: python

   import tkinter as tk

   SIZES = ["Small", "Medium", "Large"]

   root = tk.Tk()
   size_var = tk.StringVar(value="Medium")
   row = 0
   for size in SIZES:
       tk.Radiobutton(root, text=size, variable=size_var, value=size).grid(row=row, column=0, sticky="w")
       row = row + 1

   root.mainloop()

OptionMenu
-----------

An **OptionMenu** is a drop-down list.

.. code-block:: python

   import tkinter as tk

   MILKS = ["Dairy", "Soy", "Oat", "Almond"]

   root = tk.Tk()
   milk_var = tk.StringVar(value=MILKS[0])
   milk_menu = tk.OptionMenu(root, milk_var, *MILKS)
   milk_menu.grid(row=0, column=0, padx=10, pady=10)
   root.mainloop()

The ``*`` in ``*MILKS`` **unpacks** the list. It is the same as writing
``tk.OptionMenu(root, milk_var, "Dairy", "Soy", "Oat", "Almond")``.

Listbox
--------

A **Listbox** shows a list of lines. You can add items, read the selected item and delete items.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Code
     - What it does
   * - ``orders_listbox.insert(tk.END, "Large pizza")``
     - Adds an item at the end
   * - ``orders_listbox.curselection()``
     - Returns a **tuple** of the selected positions, for example ``(2,)``, or ``()`` if nothing is selected
   * - ``orders_listbox.get(2)``
     - Returns the item at position 2
   * - ``orders_listbox.delete(2)``
     - Deletes the item at position 2
   * - ``orders_listbox.delete(0, tk.END)``
     - Deletes every item
   * - ``tk.Listbox(root, selectmode=tk.MULTIPLE)``
     - Lets the user select more than one item

Worked example: smoothie bar
-----------------------------

This app uses all three choice widgets.

.. literalinclude:: files/tk_choices.py
   :language: python

:download:`Download tk_choices.py <files/tk_choices.py>`

* The fruit Listbox uses ``selectmode=tk.MULTIPLE`` so several fruits can be chosen.
* ``exportselection=False`` stops the Listbox losing its selection when the user clicks somewhere else.
* ``", ".join(fruits)`` joins a list of strings with a comma and space between them.
* ``return`` inside ``make_order()`` stops the function early if no fruit is chosen.

Activities
-----------

Activity 1: Choose the widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Radiobutton, OptionMenu, Listbox, Entry
   :delimiter: =>
   :instructions: Which widget is the best choice?

   Choose a pizza size: Small, Medium or Large => Radiobutton
   Choose dine in or takeaway => Radiobutton
   Choose your country from a list of 50 countries => OptionMenu
   Choose a quantity from 1 to 20 => OptionMenu
   Show all the orders placed so far => Listbox
   Select several toppings from a list => Listbox
   Type the customer's name => Entry
   Type a delivery address => Entry

Activity 2: Complete the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze:: python
   :show-code:

   drink_var = tk.@@StringVar@@(value="Water")
   for drink in ["Water", "Juice", "Milk"]:
       tk.Radiobutton(root, text=drink, @@variable@@=drink_var, value=drink).pack()

   def show_drink():
       choice = drink_var.@@get@@()
       result_label.config(text=f"You chose {choice}")

Activity 3: Listbox methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   To add "Pie" to the end of a Listbox, use listbox.@@insert(tk.END, "Pie")|append("Pie")|add("Pie")@@.
   To find which line is selected, use listbox.@@curselection()|get()|selected()@@.
   If nothing is selected, curselection() returns an empty @@tuple|string|number@@.
   To delete every line, use listbox.@@delete(0, tk.END)|clear()|delete()@@.

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Why do all the Radiobuttons in a group use the same variable?

      [x] So only one can be selected and the variable holds the chosen value | Correct.
      [ ] Tkinter only allows one variable per window | You can have many.
      [ ] To make them all the same colour | Not related.
      [ ] So they can all be selected at once | That would be checkboxes.

   .. multichoice::

      What does ``*`` do in ``tk.OptionMenu(root, var, *OPTIONS)``?

      [ ] Multiplies the options | Not here.
      [x] Unpacks the list so each item becomes a separate option | Correct.
      [ ] Makes the options bold | Not correct.
      [ ] Selects all options | Not correct.

   .. multichoice::

      The user has selected the third line in a Listbox. What does ``curselection()`` return?

      [ ] 3 | Positions start at 0, and it returns a tuple.
      [x] (2,) | Correct. A tuple containing position 2.
      [ ] The text of the line | Use get() for the text.
      [ ] True | Not correct.

Coding challenges
------------------

#. **Ice cream builder:** Radiobuttons for cone or cup, an OptionMenu for flavour (at least 6 flavours) and an
   OptionMenu for the number of scoops. Show a summary in a Label.
#. **Class list:** An Entry and **Add** button that adds names to a Listbox, and a **Remove** button that deletes the
   selected name. Show a message if nothing is selected.
#. **Quiz question:** Show a question with four Radiobutton answers and a **Check** button that says if the answer
   is correct.
#. **Extension:** Store the options for the ice cream builder in a **dictionary** of prices
   (for example, ``{"Vanilla": 3.50, "Mango": 4.00}``) and show the total cost.

Exam-style question
--------------------

.. structuredquestion:: Choice widgets
   :total-marks: 7
   :category: GUI

   .. stimulus::

      A school uniform shop app lets parents choose an item (Shirt, Jumper or Hat), a size (S, M, L, XL) and a
      quantity (1 to 5). Orders appear in a Listbox. There is a **Remove** button to delete an order.

   .. subquestion:: a) Recommend a widget for choosing the item, the size and the quantity. Justify one choice.
      :marks: 3

      .. model-answer::

         Item: Radiobuttons (only three options, and exactly one must be chosen). Size: Radiobuttons or OptionMenu.
         Quantity: OptionMenu (a drop-down list of 1 to 5 stops typing errors).

      .. marking-guidance::

         * 1 mark for suitable widgets for all three choices.
         * 1 mark for a justification that refers to the number of options or preventing errors.
         * 1 mark for a choice widget (not an Entry) for the quantity.

   .. subquestion:: b) Write code for a ``remove_order`` function that deletes the selected order from ``orders_listbox`` and the ``orders`` list, or shows a message if nothing is selected.
      :marks: 4

      .. model-answer::

         .. code-block:: python

            def remove_order():
                selected = orders_listbox.curselection()
                if len(selected) == 0:
                    messagebox.showinfo("Remove", "Please select an order first.")
                    return
                position = selected[0]
                orders.pop(position)
                orders_listbox.delete(position)

      .. marking-guidance::

         * 1 mark for using ``curselection()``.
         * 1 mark for checking nothing is selected and showing a message.
         * 1 mark for removing the item from the ``orders`` list.
         * 1 mark for deleting the line from the Listbox.
