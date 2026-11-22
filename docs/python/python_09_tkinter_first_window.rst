==============================================
9. Tkinter: your first GUI
==============================================

Learning intentions
--------------------

* I can explain what a graphical user interface (GUI) is and how event-driven programs work.
* I can create a Tkinter window with Labels and Buttons.
* I can lay out widgets with ``grid()`` and make a Button run a function.

Success criteria
~~~~~~~~~~~~~~~~~

* I can create a window with a title and size.
* I can place widgets in rows and columns using ``grid()`` with padding.
* I can change a Label's text when a Button is clicked.

What is a GUI?
---------------

So far, your programs have used text in a console. A **graphical user interface (GUI)** lets users interact
with windows, buttons, text boxes and menus instead.

**Tkinter** is Python's built-in GUI library. Each part of the interface (a label, a button, a text box) is
called a **widget**.

Event-driven programming
~~~~~~~~~~~~~~~~~~~~~~~~~

Console programs run from top to bottom and then stop. GUI programs are **event-driven**: they set up the window,
then **wait** for the user to do something (an **event**, such as clicking a button). When an event happens,
the program runs the matching function, then waits again. The waiting is done by ``root.mainloop()``.

.. note::

   Tkinter opens a real window, so it needs Python installed on your computer (for example IDLE, Thonny or VS Code).
   Browser-based editors such as Grok usually cannot open Tkinter windows, so use a desktop editor for the GUI
   lessons.

The structure of a Tkinter program
-----------------------------------

We will organise every GUI program into the same sections. This makes programs easier to read and change.

.. code-block:: python

   # 1. IMPORTS
   import tkinter as tk

   # 2. DATA / VARIABLES
   # (lists, dictionaries and starting values go here)

   # 3. FUNCTIONS
   # (the functions that run when buttons are clicked)

   # 4. TKINTER WIDGETS
   root = tk.Tk()
   root.title("My app")

   # 5. MAIN LOOP
   root.mainloop()

* ``import tkinter as tk`` loads Tkinter. We can then write ``tk.Label`` instead of ``tkinter.Label``.
* ``root = tk.Tk()`` creates the main window. By convention it is called ``root``.
* ``root.mainloop()`` shows the window and waits for events. It must be the **last** line.

Labels
-------

A **Label** displays text (or an image).

.. code-block:: python

   import tkinter as tk

   root = tk.Tk()
   root.title("Labels")
   root.geometry("300x120")      # width x height in pixels

   heading = tk.Label(root, text="Welcome!", font=("Arial", 18, "bold"), fg="navy")
   heading.grid(row=0, column=0, padx=10, pady=10)

   info = tk.Label(root, text="This is my first GUI.", bg="lightyellow")
   info.grid(row=1, column=0, padx=10)

   root.mainloop()

Common options:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Option
     - Meaning
   * - ``text``
     - The text to show
   * - ``font``
     - ``("Font name", size, "bold")``
   * - ``fg``
     - Text (foreground) colour, for example ``"navy"`` or ``"#1F3A68"``
   * - ``bg``
     - Background colour
   * - ``width``
     - Width in characters

Laying out widgets with grid
-----------------------------

``grid()`` places widgets in **rows** and **columns**, like a table. Rows and columns start at 0.

.. code-block:: text

            column 0        column 1
   row 0   [  Title (columnspan=2)  ]
   row 1   [ Count: 0               ]
   row 2   [ Add 1 ]       [ Reset ]

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Option
     - Meaning
   * - ``row``, ``column``
     - Which cell to put the widget in
   * - ``columnspan``
     - How many columns the widget stretches across
   * - ``padx``, ``pady``
     - Space around the widget (left/right and top/bottom)
   * - ``sticky``
     - Which side of the cell to stick to: ``"w"`` (left), ``"e"`` (right), ``"n"``, ``"s"``, or ``"ew"`` to stretch

.. tip::

   Plan your layout on paper (or in a table) first. Draw a grid and write which widget goes in each cell.

Buttons and commands
---------------------

A **Button** runs a function when clicked. Give the function name to ``command``, **without brackets**.

.. code-block:: python

   import tkinter as tk


   def say_hi():
       message_label.config(text="Hi there!")


   root = tk.Tk()
   hi_button = tk.Button(root, text="Click me", command=say_hi)
   hi_button.grid(row=0, column=0, padx=20, pady=10)
   message_label = tk.Label(root, text="")
   message_label.grid(row=1, column=0, pady=10)
   root.mainloop()

* ``command=say_hi`` means "run ``say_hi`` **when** clicked". Writing ``command=say_hi()`` would run it straight
  away, once, which is a common bug.
* ``.config()`` changes a widget's options after it has been created, for example its text or colour.

Worked example: click counter
------------------------------

.. literalinclude:: files/tk_counter.py
   :language: python

:download:`Download tk_counter.py <files/tk_counter.py>`

The ``global count`` line lets the function change the ``count`` variable that was created outside the function.
Without it, Python would treat ``count`` as a new local variable and give an error.

Activities
-----------

Activity 1: Match the widget code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   The main window is created with root = tk.@@Tk|Label|Window@@().
   A widget that shows text is a @@Label|Button|Entry@@.
   A Button runs a function given by the @@command|text|grid@@ option.
   Widgets are placed in rows and columns using @@grid()|place()|config()@@.
   To change a widget's text after it is created, use @@config()|grid()|mainloop()@@.
   The window waits for events when @@root.mainloop()|root.title()|root.wait()@@ runs.

Activity 2: Order the program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Put this program in the correct order. It shows a button that changes a label to "Clicked!".

.. ordering::

   import tkinter as tk
   def clicked():
       result.config(text="Clicked!")
   root = tk.Tk()
   button = tk.Button(root, text="Press", command=clicked)
   button.grid(row=0, column=0)
   result = tk.Label(root, text="")
   result.grid(row=1, column=0)
   root.mainloop()

Activity 3: Grid layout
~~~~~~~~~~~~~~~~~~~~~~~~

.. multichoice::

   Which code puts a Label in the second row and the first column?

   [ ] ``label.grid(row=2, column=1)`` | Rows and columns start at 0.
   [x] ``label.grid(row=1, column=0)`` | Correct.
   [ ] ``label.grid(row=0, column=1)`` | That is the first row, second column.
   [ ] ``label.grid(1, 0)`` | You need to name row and column.

.. multichoice::

   The button runs its function once when the program starts, but nothing happens when it is clicked. Why?

   [x] The code says ``command=my_function()`` with brackets | Correct. Remove the brackets.
   [ ] The button is in the wrong row | The row does not affect when it runs.
   [ ] ``mainloop()`` is missing | Without mainloop the window would not appear at all.
   [ ] Labels cannot be changed | Labels can be changed with config().

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      What does event-driven mean?

      [ ] The program runs once from top to bottom | That is a console program.
      [x] The program waits for user actions and runs functions when they happen | Correct.
      [ ] The program only runs at events like parties | Not correct.
      [ ] The program runs in a loop forever with no input | Not correct.

   .. multichoice::

      Where should ``root.mainloop()`` go?

      [ ] At the top of the program | The widgets would not exist yet.
      [ ] Inside every function | It should only be called once.
      [x] At the very end of the program | Correct.
      [ ] It is not needed | The window will not stay open without it.

Coding challenges
------------------

#. **Colour changer:** Make a window with a Label and three Buttons (Red, Green, Blue). Each button changes the
   Label's background colour.
#. **Counter plus:** Add a **Subtract 1** button to the click counter, and make the number turn red when it is
   below 0.
#. **Dice roller:** Make a button that shows a random number from 1 to 6 in a big Label.
   Hint: ``import random`` and ``random.randint(1, 6)``.
#. **Extension: score board:** Make a two-team score board with team names, scores, +1 buttons for each team and
   a Reset button. Use ``grid()`` with ``columnspan`` for the title.

Exam-style question
--------------------

.. structuredquestion:: Tkinter basics
   :total-marks: 7
   :category: GUI

   .. stimulus::

      .. code-block:: python

         import tkinter as tk

         def change():
             title.config(text="Goodbye!")

         root = tk.Tk()
         title = tk.Label(root, text="Hello!")
         title.grid(row=0, column=0)
         button = tk.Button(root, text="Change", command=change())
         button.grid(row=1, column=0)
         root.mainloop()

   .. subquestion:: a) Name the two types of widget used in this program.
      :marks: 2

      .. model-answer::

         Label and Button.

      .. marking-guidance::

         1 mark for each.

   .. subquestion:: b) When the program runs, the label already says "Goodbye!" and the button does nothing. Identify the bug and fix it.
      :marks: 2

      .. model-answer::

         ``command=change()`` calls the function immediately instead of when the button is clicked. Fix:
         ``command=change`` (no brackets).

      .. marking-guidance::

         * 1 mark for identifying the brackets in ``command=change()``.
         * 1 mark for the fix.

   .. subquestion:: c) Explain what ``root.mainloop()`` does.
      :marks: 2

      .. model-answer::

         It shows the window and keeps the program running, waiting for events such as button clicks. When an event
         happens, it runs the matching function.

      .. marking-guidance::

         * 1 mark for keeping the window open or running.
         * 1 mark for waiting for and responding to events.

   .. subquestion:: d) Write a line that moves the button to the right of the label instead of below it.
      :marks: 1

      .. model-answer::

         ``button.grid(row=0, column=1)``

      .. marking-guidance::

         1 mark for row 0, column 1.
