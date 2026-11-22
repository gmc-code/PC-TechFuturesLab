==============================================
8. Dictionaries and nested dictionaries
==============================================

Learning intentions
--------------------

* I can explain what a dictionary is and how it is different from a list.
* I can create a dictionary and add, change, look up and remove key–value pairs.
* I can use nested dictionaries to store detailed information about many items.

Success criteria
~~~~~~~~~~~~~~~~~

* I can look up a value using its key, and check if a key exists with ``in``.
* I can loop through a dictionary to show every key and value.
* I can read and change values in a nested dictionary.

What is a dictionary?
----------------------

A **dictionary** stores data as **key–value pairs**. Like a real dictionary, you look up a **key** (the word)
to find its **value** (the meaning). Dictionaries use **curly brackets** ``{}``.

.. code-block:: python

   prices = {
       "toastie": 4.50,
       "wrap": 6.00,
       "juice": 3.00,
   }

   print(prices["wrap"])

Output:

.. code-block:: text

   6.0

* Each **key** must be unique (you cannot have two ``"wrap"`` keys).
* Keys are usually strings. Values can be any type: numbers, strings, Booleans, lists or even other dictionaries.

Lists vs dictionaries
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * -
     - List
     - Dictionary
   * - Brackets
     - ``[ ]``
     - ``{ }``
   * - Find an item by
     - its **index** (position): ``scores[0]``
     - its **key** (name): ``prices["wrap"]``
   * - Best for
     - an ordered collection of similar items
     - looking things up by name

Working with dictionaries
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Code
     - What it does
   * - ``prices["wrap"]``
     - Gets the value for the key ``"wrap"`` (error if the key does not exist)
   * - ``prices["pie"] = 5.50``
     - Adds a new pair, or changes the value if the key already exists
   * - ``del prices["juice"]``
     - Removes a key and its value
   * - ``"wrap" in prices``
     - ``True`` if the key exists
   * - ``prices.get("pie", 0)``
     - Gets the value, or ``0`` if the key does not exist (no error)
   * - ``len(prices)``
     - The number of key–value pairs
   * - ``prices.keys()`` / ``prices.values()``
     - All the keys / all the values

.. code-block:: python

   prices = {"toastie": 4.50, "wrap": 6.00}
   prices["pie"] = 5.50          # add
   prices["wrap"] = 6.50         # change
   del prices["toastie"]          # remove
   print(prices)
   print("pie" in prices)

Output:

.. code-block:: text

   {'wrap': 6.5, 'pie': 5.5}
   True

Looping through a dictionary
-----------------------------

A ``for`` loop over a dictionary gives you each **key**. Use the key to get the value.

.. code-block:: python

   prices = {"toastie": 4.50, "wrap": 6.00, "juice": 3.00}
   for item in prices:
       print(f"{item}: ${prices[item]:.2f}")

Output:

.. code-block:: text

   toastie: $4.50
   wrap: $6.00
   juice: $3.00

Nested dictionaries
--------------------

Sometimes each item needs **more than one** piece of information. A **nested dictionary** is a dictionary
whose values are **also dictionaries**.

.. code-block:: python

   menu = {
       "toastie": {"price": 4.50, "vegetarian": True, "stock": 12},
       "wrap": {"price": 6.00, "vegetarian": False, "stock": 8},
   }

   print(menu["wrap"])
   print(menu["wrap"]["price"])
   menu["toastie"]["stock"] = menu["toastie"]["stock"] - 1
   print(menu["toastie"]["stock"])

Output:

.. code-block:: text

   {'price': 6.0, 'vegetarian': False, 'stock': 8}
   6.0
   11

Read ``menu["wrap"]["price"]`` from left to right: "In ``menu``, find ``"wrap"``. In that dictionary, find
``"price"``."

.. tip::

   Nested dictionaries are exactly how the pizza ordering app in :doc:`python_13_pizza_app` stores its menu:
   each pizza name is a key, and its value is a dictionary with the price and toppings.

Worked example: canteen menu
-----------------------------

.. literalinclude:: files/canteen_menu.py
   :language: python

:download:`Download canteen_menu.py <files/canteen_menu.py>`

Example run:

.. code-block:: text

   Simple dictionary
   A wrap costs $6.00

   MENU
   Toastie    $4.50 (V)
   Wrap       $6.00
   Juice      $3.00 (V)
   What would you like? wrap
   Enjoy your wrap! 7 left.

``{item.title():10}`` makes the item name start with a capital letter and take up 10 characters, so the prices
line up.

Activities
-----------

Activity 1: Look it up
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   student = {"name": "Mia", "year": 9, "house": "Gold", "subjects": ["Maths", "Science"]}

Type what each expression gives.

.. fillin::

   student["name"] gives @@Mia@@
   student["year"] + 1 gives @@10@@
   student["subjects"][1] gives @@Science@@
   len(student) gives @@4@@
   "house" in student gives @@True@@

Activity 2: List or dictionary?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: List, Dictionary
   :delimiter: =>
   :instructions: Which data structure is the best choice?

   The order that runners finished a race => List
   A queue of songs to play next => List
   Ten test scores to average => List
   Each student's name and their locker number => Dictionary
   Each country and its capital city => Dictionary
   Each menu item and its price => Dictionary

Activity 3: Nested dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   games = {
       "Space Run": {"rating": 4.5, "players": 1, "price": 0.00},
       "Kart Chaos": {"rating": 4.8, "players": 4, "price": 29.95},
   }

.. gapfill::

   To get the rating of Space Run, write games["Space Run"][@@"rating"|"price"|"players"@@].
   games["Kart Chaos"]["players"] gives @@4|1|29.95@@.
   To change the price of Space Run to 4.99, write @@games["Space Run"]["price"] = 4.99|games["price"] = 4.99|games["Space Run"] = 4.99@@.
   The keys of the outer dictionary are the @@game names|ratings|prices@@.

Activity 4: Complete the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program lets the user look up the capital city of a country.

.. cloze:: python
   :show-code:

   capitals = @@{@@"Australia": "Canberra", "Japan": "Tokyo"@@}@@
   country = input("Country: ")
   if country @@in@@ capitals:
       print(f"The capital is {capitals[@@country@@]}.")
   else:
       print("I don't know that one.")

Activity 5: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      What happens if you run ``prices["burger"]`` and ``"burger"`` is not a key?

      [ ] It returns 0 | Use .get() for that.
      [x] A KeyError | Correct.
      [ ] It adds burger to the dictionary | Reading a key does not add it.
      [ ] It returns an empty string | Not correct.

   .. multichoice::

      Which line adds a new item to a dictionary?

      [ ] ``prices.append("pie", 5.5)`` | Dictionaries do not have append.
      [x] ``prices["pie"] = 5.5`` | Correct.
      [ ] ``prices + {"pie": 5.5}`` | You cannot add dictionaries with ``+``.
      [ ] ``prices[5.5] = "pie"`` | The key and value are the wrong way around.

   .. multichoice::

      What does a ``for`` loop over a dictionary give you each time?

      [x] Each key | Correct. Use the key to get the value.
      [ ] Each value | You get the keys.
      [ ] A random item | It goes through every key.
      [ ] The index number | Dictionaries do not use indexes.

Coding challenges
------------------

#. **Phone book:** Make a dictionary of 4 friends' first names and favourite colours (made-up data). Let the user
   type a name and print the colour, or "Not found".
#. **Word counter:** Ask the user for a sentence. Use a dictionary to count how many times each word appears.
   Hint: ``sentence.split()`` turns a sentence into a list of words.
#. **Nested shop:** Make a nested dictionary of 4 products with ``price`` and ``stock``. Let the user buy items until
   they type ``done``. Reduce the stock each time and print the total cost. Do not allow buying when stock is 0.
#. **Extension: quiz from a dictionary:** Store 5 questions and answers in a dictionary. Loop through it, ask each
   question, keep score and print the final result.

Exam-style question
--------------------

.. structuredquestion:: Nested dictionaries
   :total-marks: 8
   :category: Dictionaries

   .. stimulus::

      .. code-block:: python

         lockers = {
             "Ava": {"number": 101, "level": 1},
             "Leo": {"number": 215, "level": 2},
             "Mia": {"number": 108, "level": 1},
         }

   .. subquestion:: a) Write the expression that gives Leo's locker number.
      :marks: 1

      .. model-answer::

         ``lockers["Leo"]["number"]``

      .. marking-guidance::

         1 mark for the correct expression.

   .. subquestion:: b) Write one line of code that adds a new student, Sam, with locker 220 on level 2.
      :marks: 2

      .. model-answer::

         ``lockers["Sam"] = {"number": 220, "level": 2}``

      .. marking-guidance::

         * 1 mark for adding the key ``"Sam"``.
         * 1 mark for a correct inner dictionary.

   .. subquestion:: c) Write a loop that prints the name of every student whose locker is on level 1.
      :marks: 3

      .. model-answer::

         .. code-block:: python

            for name in lockers:
                if lockers[name]["level"] == 1:
                    print(name)

      .. marking-guidance::

         * 1 mark for looping through the dictionary keys.
         * 1 mark for the correct nested lookup of level.
         * 1 mark for comparing with 1 and printing the name.

   .. subquestion:: d) Explain why a nested dictionary suits this data better than a simple dictionary.
      :marks: 2

      .. model-answer::

         Each student has more than one piece of information (locker number and level). A nested dictionary lets each
         student's name be a key whose value holds all of their details with clear labels.

      .. marking-guidance::

         * 1 mark for recognising each item has several pieces of data.
         * 1 mark for explaining the labelled inner dictionary.
