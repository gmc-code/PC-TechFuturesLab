==============================================
3. Algorithms, pseudocode and flowcharts
==============================================

Learning intentions
--------------------

* I can explain what an algorithm is and why programmers plan before coding.
* I can represent an algorithm as pseudocode and as a flowchart, using logical operators.
* I can trace an algorithm and test it with normal, boundary and invalid test cases.

Success criteria
~~~~~~~~~~~~~~~~~

* I can name the flowchart symbols and what they mean.
* I can complete a trace table to predict the output of an algorithm.
* I can write a test table and compare the expected output with the actual output.

What is an algorithm?
----------------------

An **algorithm** is a set of step-by-step instructions to solve a problem or complete a task. A recipe is an
algorithm. So are the instructions for building a LEGO model.

Before writing a program, programmers plan the algorithm. This helps them think through the steps, find
mistakes early and explain their ideas to other people. Two common ways to show an algorithm are
**pseudocode** and **flowcharts**.

Pseudocode
-----------

**Pseudocode** is a way of writing an algorithm in structured English. It looks a bit like code but is not
written in any real programming language.

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Pseudocode
     - Meaning
     - Python
   * - ``BEGIN`` / ``END``
     - Start and end of the algorithm
     - (not needed)
   * - ``INPUT mark``
     - Get a value from the user
     - ``mark = int(input())``
   * - ``total ← a + b``
     - Store a value in a variable
     - ``total = a + b``
   * - ``PRINT total``
     - Show output
     - ``print(total)``
   * - ``IF ... THEN ... ELSE ... ENDIF``
     - Make a decision
     - ``if ... : ... else: ...``
   * - ``WHILE ... ENDWHILE``
     - Repeat while something is true
     - ``while ...:``
   * - ``FOR i ← 1 TO 10 ... NEXT i``
     - Repeat a set number of times
     - ``for i in range(1, 11):``

Indent the steps inside ``IF`` and loops so the structure is easy to see.

Flowcharts
-----------

A **flowchart** shows an algorithm as a diagram. Each shape has a meaning.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Shape
     - Meaning
   * - Rounded rectangle (terminator)
     - Start or end
   * - Parallelogram
     - Input or output
   * - Rectangle
     - Process (a calculation or assignment)
   * - Diamond
     - Decision (a yes/no question with two arrows out)
   * - Arrow
     - The direction of flow

Logical operators
------------------

Decisions often need more than one condition. **Logical operators** join conditions together.

.. list-table::
   :header-rows: 1
   :widths: 15 45 40

   * - Operator
     - True when...
     - Example
   * - ``AND``
     - **both** conditions are true
     - ``age >= 13 AND age <= 19`` (a teenager)
   * - ``OR``
     - **at least one** condition is true
     - ``day = "Sat" OR day = "Sun"`` (weekend)
   * - ``NOT``
     - the condition is **false**
     - ``NOT raining`` (it is not raining)

Worked example: grade checker
------------------------------

**Problem:** A teacher wants a program that turns a test mark out of 100 into a grade: A for 80 or more,
B for 65–79, C for 50–64, D below 50. Marks below 0 or above 100 are invalid.

Here is the algorithm. Click **Run** (or step through it), type a mark and watch the flowchart highlight each
step.

.. flowchart::
   :mode: step
   :title: Grade checker

   BEGIN
       INPUT mark
       IF mark < 0 OR mark > 100 THEN
           PRINT "That is not a valid mark."
       ELSEIF mark >= 80 THEN
           PRINT "Grade: A"
       ELSEIF mark >= 65 THEN
           PRINT "Grade: B"
       ELSEIF mark >= 50 THEN
           PRINT "Grade: C"
       ELSE
           PRINT "Grade: D"
       ENDIF
   END

And here is the same algorithm in Python:

.. literalinclude:: files/grade_checker.py
   :language: python

:download:`Download grade_checker.py <files/grade_checker.py>`

Tracing an algorithm
---------------------

**Tracing** means working through an algorithm by hand, step by step, to predict what it will do. A
**trace table** records the value of each variable as it changes.

**Algorithm:**

.. code-block:: text

   BEGIN
       total ← 0
       FOR i ← 1 TO 4
           total ← total + i
       NEXT i
       PRINT total
   END

.. list-table:: Trace table
   :header-rows: 1

   * - Step
     - i
     - total
     - Output
   * - start
     -
     - 0
     -
   * - loop 1
     - 1
     - 1
     -
   * - loop 2
     - 2
     - 3
     -
   * - loop 3
     - 3
     - 6
     -
   * - loop 4
     - 4
     - 10
     -
   * - end
     -
     - 10
     - 10

Testing with test cases
------------------------

To **validate** an algorithm or program, compare its **actual output** with the **expected output** for a range
of **test cases**:

* **Normal data:** typical values that should work, for example 72.
* **Boundary data:** values at the edges where the result changes, for example 79, 80, 49, 50, 0 and 100.
* **Invalid data:** values that should be rejected, for example -5 or 150.

.. list-table:: Test table for the grade checker
   :header-rows: 1
   :widths: 15 20 30 35

   * - Test data
     - Type
     - Expected output
     - Actual output (pass/fail)
   * - 72
     - Normal
     - Grade: B
     - Grade: B ✓
   * - 80
     - Boundary
     - Grade: A
     - Grade: A ✓
   * - 79
     - Boundary
     - Grade: B
     - Grade: B ✓
   * - 50
     - Boundary
     - Grade: C
     - Grade: C ✓
   * - 49
     - Boundary
     - Grade: D
     - Grade: D ✓
   * - 150
     - Invalid
     - That is not a valid mark.
     - That is not a valid mark. ✓
   * - -5
     - Invalid
     - That is not a valid mark.
     - That is not a valid mark. ✓

If any actual output does not match the expected output, there is a **bug**. Fix it and test again.

Activities
-----------

Activity 1: Flowchart symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Terminator, Input/output, Process, Decision
   :delimiter: =>
   :instructions: Which flowchart shape would you use for each step?

   BEGIN => Terminator
   END => Terminator
   INPUT age => Input/output
   PRINT "Hello" => Input/output
   total ← price * quantity => Process
   count ← count + 1 => Process
   Is age >= 13? => Decision
   Is the password correct? => Decision

Activity 2: Fill the flowchart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm decides if a ride is allowed. Riders must be at least 120 cm tall **and** at least 8 years old.
Drag the text into the empty shapes.

.. activitygroup::
   :title: Theme park ride check

   .. flowchart::
      :mode: blanks
      :answers:

      BEGIN
          INPUT height
          INPUT age
          IF height >= 120 AND age >= 8 THEN
              PRINT "Enjoy the ride!"
          ELSE
              PRINT "Sorry, you cannot ride."
          ENDIF
      END

   .. multichoice::

      A 10-year-old who is 115 cm tall uses the algorithm. What is the output?

      [ ] Enjoy the ride! | Both conditions must be true. The height condition is false.
      [x] Sorry, you cannot ride. | Correct. 115 is less than 120, so the AND is false.

   .. multichoice::

      Which test case is a **boundary** test?

      [ ] height 150, age 12 | This is normal data.
      [x] height 120, age 8 | Correct. These are exactly on the edges.
      [ ] height -10, age 5 | This is invalid data.
      [ ] height 200, age 40 | This is normal data.

Activity 3: Logical operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   A weekend is when day is "Sat" @@OR|AND|NOT@@ day is "Sun".
   A teenager has an age >= 13 @@AND|OR|NOT@@ age <= 19.
   You can go outside without an umbrella if it is @@NOT|AND|OR@@ raining.
   With AND, @@both|either|neither@@ conditions must be true.
   With OR, @@at least one|both|neither@@ condition must be true.

Activity 4: Put the pseudocode in order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm should ask for two numbers and print the larger one. Put the lines in order and set the
indentation.

.. ordering:: text

   BEGIN
       INPUT a
       INPUT b
       IF a > b THEN
           PRINT a
       ELSE
           PRINT b
       ENDIF
   END

Activity 5: Draw it yourself
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the flowchart for this algorithm, which checks if a number is even or odd. (``MOD`` gives the remainder
after dividing.)

.. flowchart::
   :mode: draw
   :show-code:
   :answers:

   BEGIN
       INPUT number
       IF number MOD 2 = 0 THEN
           PRINT "Even"
       ELSE
           PRINT "Odd"
       ENDIF
   END

Coding challenges
------------------

For each problem: write the pseudocode, draw the flowchart, write a test table (normal, boundary and invalid),
then write the Python code and test it.

#. **Free shipping:** Orders of $50 or more get free shipping. Otherwise shipping costs $9.95. Print the total.
#. **Movie ticket:** Children under 5 are free. Children under 16 and adults 65 or over pay $12. Everyone else
   pays $18. On Tuesdays, paid tickets are half price.
   (Compare your answer with :download:`movie_ticket.py <files/movie_ticket.py>`.)
#. **Login:** The username must be ``admin`` **and** the password must be ``python123``. Print "Access granted"
   or "Access denied".

Exam-style question
--------------------

.. structuredquestion:: Designing and testing an algorithm
   :total-marks: 8
   :category: Algorithms

   .. stimulus::

      A swimming pool gives a discount. People get the discount if they are under 18 **or** they have a student
      card. The algorithm is:

      .. code-block:: text

         BEGIN
             INPUT age
             INPUT has_card
             IF age < 18 OR has_card = "yes" THEN
                 price ← 4
             ELSE
                 price ← 7
             ENDIF
             PRINT price
         END

   .. subquestion:: a) Name the flowchart shape used for line 4 and explain why.
      :marks: 2

      .. model-answer::

         A diamond (decision), because the algorithm asks a yes/no question and has two possible paths.

      .. marking-guidance::

         * 1 mark for diamond or decision.
         * 1 mark for the reason (yes/no question, two paths).

   .. subquestion:: b) Complete the expected output for these test cases: (i) age 15, has_card "no"; (ii) age 25, has_card "yes"; (iii) age 25, has_card "no".
      :marks: 3

      .. model-answer::

         (i) 4  (ii) 4  (iii) 7

      .. marking-guidance::

         1 mark for each correct expected output.

   .. subquestion:: c) Give one boundary test case for the age and its expected output (assume has_card is "no").
      :marks: 2

      .. model-answer::

         Age 18 → 7 (not under 18). Or age 17 → 4.

      .. marking-guidance::

         * 1 mark for an age of 17 or 18.
         * 1 mark for the correct expected output.

   .. subquestion:: d) What would change if OR was replaced with AND?
      :marks: 1

      .. model-answer::

         People would need to be under 18 **and** have a student card to get the discount, so fewer people would get
         it (for example, a 25-year-old with a card would pay 7).

      .. marking-guidance::

         1 mark for explaining both conditions would need to be true.
