==============================================
10. Tkinter: Entry, Text and messages
==============================================

Learning intentions
--------------------

* I can get text from the user with an Entry widget.
* I can display several lines of output in a Text widget.
* I can validate user input and show error messages with a messagebox.

Success criteria
~~~~~~~~~~~~~~~~~

* I can use ``.get()``, ``.insert()`` and ``.delete()`` on Entry and Text widgets.
* I can convert Entry text to a number and handle errors with ``try`` and ``except``.
* I can show an error message box and highlight the box that needs fixing.

The Entry widget
-----------------

An **Entry** is a one-line text box where the user can type.

.. code-block:: python

   import tkinter as tk


   def show_name():
       name = name_entry.get()            # read what was typed
       result_label.config(text=f"Hello, {name}!")


   root = tk.Tk()
   tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
   name_entry = tk.Entry(root, width=20)
   name_entry.grid(row=0, column=1, padx=5, pady=5)
   tk.Button(root, text="OK", command=show_name).grid(row=0, column=2, padx=5)
   result_label = tk.Label(root, text="")
   result_label.grid(row=1, column=0, columnspan=3, pady=5)
   root.mainloop()

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Code
     - What it does
   * - ``name_entry.get()``
     - Returns the text in the Entry (always a **string**)
   * - ``name_entry.delete(0, tk.END)``
     - Clears the Entry (deletes from position 0 to the end)
   * - ``name_entry.insert(0, "Ava")``
     - Puts text into the Entry at position 0
   * - ``name_entry.config(bg="pink")``
     - Changes the background colour
   * - ``name_entry.focus()``
     - Puts the cursor in the Entry ready for typing

.. tip::

   ``tk.Label(...).grid(...)`` on one line is fine for labels you never need to change. If you need to change a
   widget later, store it in a variable first, then call ``.grid()`` on a separate line. (``.grid()`` returns
   ``None``, so ``name_entry = tk.Entry(root).grid()`` would store ``None``. This is a very common bug!)

The Text widget
----------------

A **Text** widget is a multi-line box. It is useful for showing a list of results, a receipt or a log.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Code
     - What it does
   * - ``message_text.insert(tk.END, "Hi\n")``
     - Adds text at the end. ``\n`` starts a new line.
   * - ``message_text.get("1.0", tk.END)``
     - Gets all the text (from line 1, character 0, to the end)
   * - ``message_text.delete("1.0", tk.END)``
     - Deletes all the text

Message boxes
--------------

The ``messagebox`` module shows pop-up windows.

.. code-block:: python

   from tkinter import messagebox

   messagebox.showinfo("Saved", "Your order has been saved.")
   messagebox.showerror("Input error", "Please enter your name.")
   answer = messagebox.askyesno("Confirm", "Delete all orders?")   # True or False

Worked example: greeter
------------------------

.. literalinclude:: files/tk_greeter.py
   :language: python

:download:`Download tk_greeter.py <files/tk_greeter.py>`

* ``.strip()`` removes spaces from the start and end, so typing only spaces counts as empty.
* If the name is empty, the program shows an error **and** turns the Entry pink so the user knows what to fix.
* After a successful greeting, the Entry is cleared, ready for the next name.

Validating numbers with try and except
---------------------------------------

``float("abc")`` causes a ``ValueError`` and would crash the program. A ``try`` / ``except`` block catches the error
so the program can show a helpful message instead.

.. code-block:: python

   text = "abc"
   try:
       number = float(text)
       print(f"You entered {number}")
   except ValueError:
       print("Please type a number.")

Output:

.. code-block:: text

   Please type a number.

Validation checks you might use:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Check
     - Example
   * - **Presence check**
     - The name box is not empty
   * - **Type check**
     - The price can be converted to a number
   * - **Range check**
     - The age is between 0 and 120
   * - **Length check**
     - A postcode has exactly 4 digits

Activities
-----------

Activity 1: Entry or Text?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Entry, Text, Label
   :delimiter: =>
   :instructions: Which widget would you use?

   The user types their email address => Entry
   The user types a quantity => Entry
   The user writes a paragraph of feedback => Text
   Show a list of all orders, one per line => Text
   Show the heading "Pizza orders" => Label
   Show the total cost => Label

Activity 2: Complete the function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function reads an age, checks it and shows a message.

.. cloze:: python
   :show-code:

   def check_age():
       @@try@@:
           age = int(age_entry.@@get@@())
       except @@ValueError@@:
           messagebox.showerror("Error", "Type a whole number.")
           return
       if age < 0 or age > 120:
           messagebox.showerror("Error", "Age must be 0 to 120.")
       else:
           result_label.@@config@@(text=f"You are {age}.")

Activity 3: Validation checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Presence check, Type check, Range check, Length check
   :delimiter: =>

   The customer name box must not be empty => Presence check
   A password box must not be left blank => Presence check
   The quantity must be a whole number => Type check
   The price must be a number, not text => Type check
   A test mark must be from 0 to 100 => Range check
   The number of tickets must be 1 to 10 => Range check
   A mobile number must have 10 digits => Length check
   A username must be at most 15 characters => Length check

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      What type of value does ``entry.get()`` always return?

      [x] A string | Correct. Convert it with int() or float() for maths.
      [ ] An integer | Not automatically.
      [ ] A float | Not automatically.
      [ ] A Boolean | Not correct.

   .. multichoice::

      Which line clears an Entry called ``price_entry``?

      [ ] ``price_entry.clear()`` | Entry has no clear() method.
      [x] ``price_entry.delete(0, tk.END)`` | Correct.
      [ ] ``price_entry.delete("1.0", tk.END)`` | "1.0" is used for Text widgets.
      [ ] ``price_entry = ""`` | This replaces the variable, not the text in the box.

   .. multichoice::

      Why use ``try`` and ``except`` when converting user input?

      [ ] To make the program faster | Not the reason.
      [x] To stop the program crashing if the input is not a number | Correct.
      [ ] To convert numbers to text | That is str().
      [ ] Tkinter requires it | It is good practice, not required.

Coding challenges
------------------

#. **Age next year:** An Entry for age and a Button. Show "Next year you will be ..." in a Label. Show an error
   message if the input is not a whole number.
#. **Guest list:** An Entry and an **Add** button that adds each name to a Text widget on a new line. Do not allow
   empty names. Add a **Clear** button.
#. **Feedback form:** An Entry for a name, a Text widget for comments, and a **Submit** button that shows a
   messagebox thanking the user by name. Check both boxes are filled in.
#. **Extension: unit converter:** Convert kilometres to miles (1 km = 0.621371 miles). Validate that the input is a
   positive number and show the answer to 2 decimal places.

Exam-style question
--------------------

.. structuredquestion:: Validating GUI input
   :total-marks: 7
   :category: GUI

   .. stimulus::

      A movie booking app has an Entry called ``tickets_entry``. Customers can book 1 to 8 tickets at $15 each.
      The Book button runs this function:

      .. code-block:: python

         def book():
             tickets = int(tickets_entry.get())
             total = tickets * 15
             total_label.config(text=f"Total: ${total:.2f}")

   .. subquestion:: a) Describe what happens if the customer types ``two`` and clicks Book.
      :marks: 2

      .. model-answer::

         ``int("two")`` causes a ValueError. The function stops with an error and the total is not shown (the user gets
         no helpful message).

      .. marking-guidance::

         * 1 mark for ValueError or crash.
         * 1 mark for the effect on the user.

   .. subquestion:: b) Name the two types of validation check the function needs.
      :marks: 2

      .. model-answer::

         A type check (the input must be a whole number) and a range check (it must be from 1 to 8).

      .. marking-guidance::

         1 mark for each.

   .. subquestion:: c) Rewrite the function so it validates the input and shows error messages using messagebox.
      :marks: 3

      .. model-answer::

         .. code-block:: python

            def book():
                try:
                    tickets = int(tickets_entry.get())
                except ValueError:
                    messagebox.showerror("Error", "Please type a whole number.")
                    return
                if tickets < 1 or tickets > 8:
                    messagebox.showerror("Error", "You can book 1 to 8 tickets.")
                    return
                total = tickets * 15
                total_label.config(text=f"Total: ${total:.2f}")

      .. marking-guidance::

         * 1 mark for try/except around the conversion.
         * 1 mark for a correct range check (1 to 8).
         * 1 mark for showing error messages and only calculating when valid.
