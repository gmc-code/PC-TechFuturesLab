==============================================
7. Lists
==============================================

Learning intentions
--------------------

* I can explain what a list is and why it is useful for storing many values.
* I can create a list and access items using their index.
* I can add, remove, search and loop through items in a list.

Success criteria
~~~~~~~~~~~~~~~~~

* I can use positive and negative indexes to get items from a list.
* I can use ``append()``, ``remove()``, ``pop()``, ``len()`` and ``in``.
* I can use a ``for`` loop to process every item in a list.

What is a list?
----------------

A **list** stores many values in **one** variable, in order. Lists use **square brackets** with items separated
by commas.

.. code-block:: python

   subjects = ["Maths", "Science", "English", "Digital Tech"]
   scores = [78, 92, 65, 88]
   empty = []

A list is a **data structure**: a way of organising data so a program can use it easily. Without a list, you
would need a separate variable for every subject.

Indexes
--------

Each item has a position called its **index**. Indexes start at **0**.

.. code-block:: text

   subjects = ["Maths", "Science", "English", "Digital Tech"]
   index:          0         1          2            3
   negative:      -4        -3         -2           -1

.. code-block:: python

   subjects = ["Maths", "Science", "English", "Digital Tech"]
   print(subjects[0])      # first item
   print(subjects[2])
   print(subjects[-1])     # last item
   subjects[1] = "Physics" # change an item
   print(subjects)

Output:

.. code-block:: text

   Maths
   English
   Digital Tech
   ['Maths', 'Physics', 'English', 'Digital Tech']

Using an index that does not exist (for example ``subjects[10]``) causes an ``IndexError``.

Changing a list
----------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Code
     - What it does
   * - ``my_list.append(item)``
     - Adds ``item`` to the **end**
   * - ``my_list.insert(0, item)``
     - Inserts ``item`` at index 0 (the start)
   * - ``my_list.remove(item)``
     - Removes the first matching ``item`` (error if it is not there)
   * - ``my_list.pop()``
     - Removes and returns the **last** item
   * - ``my_list.pop(2)``
     - Removes and returns the item at index 2
   * - ``my_list.sort()``
     - Sorts the list (A to Z, or smallest to largest)
   * - ``len(my_list)``
     - The number of items
   * - ``item in my_list``
     - ``True`` if ``item`` is in the list
   * - ``my_list.clear()``
     - Removes every item

.. code-block:: python

   shopping = ["milk", "bread"]
   shopping.append("eggs")
   shopping.remove("milk")
   print(shopping)
   print(len(shopping))
   print("eggs" in shopping)

Output:

.. code-block:: text

   ['bread', 'eggs']
   2
   True

Looping through a list
-----------------------

A ``for`` loop can visit **each item** in a list in turn.

.. code-block:: python

   scores = [78, 92, 65, 88]
   total = 0
   for score in scores:
       total = total + score
   print(f"Average: {total / len(scores):.1f}")
   print(f"Highest: {max(scores)}")

Output:

.. code-block:: text

   Average: 80.8
   Highest: 92

``enumerate()`` gives you a number with each item, which is handy for numbered lists:

.. code-block:: python

   for number, subject in enumerate(["Maths", "Science"], start=1):
       print(f"{number}. {subject}")

Worked example: playlist manager
---------------------------------

.. literalinclude:: files/playlist.py
   :language: python

:download:`Download playlist.py <files/playlist.py>`

Notice how the program checks ``if remove_song in playlist`` **before** removing it, so it does not crash
if the song is not there.

Activities
-----------

Activity 1: Indexes
~~~~~~~~~~~~~~~~~~~~

``colours = ["red", "green", "blue", "yellow", "purple"]``

Type what each line prints.

.. fillin::

   print(colours[0]) prints @@red@@
   print(colours[3]) prints @@yellow@@
   print(colours[-1]) prints @@purple@@
   print(colours[-2]) prints @@yellow@@
   print(len(colours)) prints @@5@@

Activity 2: List methods
~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   To add an item to the end of a list, use @@append()|insert()|pop()@@.
   To remove a particular item by its value, use @@remove()|pop()|clear()@@.
   To remove the last item, use @@pop()|remove()|sort()@@.
   To find how many items are in a list, use @@len()|count()|max()@@.
   To check if an item is in a list, use the keyword @@in|is|has@@.

Activity 3: Order the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program asks for 3 names, stores them in a list, then prints them in alphabetical order.

.. ordering::

   names = []
   for i in range(3):
       name = input("Enter a name: ")
       names.append(name)
   names.sort()
   for name in names:
       print(name)

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      What is the index of the first item in a list?

      [x] 0 | Correct.
      [ ] 1 | Python starts counting at 0.
      [ ] -1 | -1 is the last item.
      [ ] It depends on the list | It is always 0.

   .. multichoice::

      What does this code print?

      .. code-block:: python

         pets = ["cat", "dog"]
         pets.append("fish")
         pets.pop(0)
         print(pets)

      [ ] ['cat', 'dog', 'fish'] | pop(0) removes the first item.
      [x] ['dog', 'fish'] | Correct.
      [ ] ['cat', 'dog'] | fish was appended, then cat was removed.
      [ ] ['fish'] | Only one item was removed.

   .. multichoice::

      Which code causes an error if ``"pizza"`` is not in the list ``menu``?

      [ ] ``"pizza" in menu`` | This just gives False.
      [x] ``menu.remove("pizza")`` | Correct. remove() gives a ValueError if the item is not there.
      [ ] ``menu.append("pizza")`` | This adds pizza.
      [ ] ``len(menu)`` | This works for any list.

Coding challenges
------------------

#. **Class scores:** Ask the user for 5 test scores, store them in a list, then print the highest, lowest and
   average score.
#. **To-do list:** Write a program with a ``while`` loop and a menu: ``a`` to add a task, ``r`` to remove a task,
   ``s`` to show all tasks (numbered) and ``q`` to quit.
#. **Above average:** Using a list of scores, print only the scores that are above the average.
#. **Extension: shuffle and deal:** Make a list of 10 student names. Use ``random.shuffle()`` to shuffle it, then
   split it into two teams of 5 using slices: ``names[:5]`` and ``names[5:]``.

Exam-style question
--------------------

.. structuredquestion:: Working with lists
   :total-marks: 7
   :category: Lists

   .. stimulus::

      .. code-block:: python

         temps = [21, 25, 19, 30, 27]
         temps.append(23)
         hot_days = 0
         for t in temps:
             if t >= 25:
                 hot_days = hot_days + 1
         print(temps[1], temps[-1], hot_days)

   .. subquestion:: a) How many items are in ``temps`` after line 2?
      :marks: 1

      .. model-answer::

         6

      .. marking-guidance::

         1 mark for 6.

   .. subquestion:: b) Write the exact output of the program.
      :marks: 3

      .. model-answer::

         ``25 23 3``

      .. marking-guidance::

         * 1 mark for ``25`` (index 1).
         * 1 mark for ``23`` (the last item after append).
         * 1 mark for ``3`` (25, 30 and 27 are 25 or more).

   .. subquestion:: c) Write code that prints the average temperature to 1 decimal place.
      :marks: 2

      .. model-answer::

         .. code-block:: python

            average = sum(temps) / len(temps)
            print(f"Average: {average:.1f}")

         (A loop that adds up the total is also correct.)

      .. marking-guidance::

         * 1 mark for the total divided by the number of items.
         * 1 mark for printing to 1 decimal place.

   .. subquestion:: d) Explain why a list is better than six separate variables for storing the temperatures.
      :marks: 1

      .. model-answer::

         A list keeps all the values in one variable, so a loop can process them all, and it can grow when more
         temperatures are added.

      .. marking-guidance::

         1 mark for a valid reason (looping, less code, can grow).
