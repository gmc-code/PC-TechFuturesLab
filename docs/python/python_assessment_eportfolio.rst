==============================================
Assessment: Python ePortfolio
==============================================

.. list-table::
   :widths: 30 70

   * - **Type**
     - Portfolio of online coursework
   * - **Dates**
     - Starts Term 1, Week 1. Due Term 2, Week 4. Ends Term 2, Week 4.
   * - **Platform**
     - `Grok Academy <https://groklearning.com/>`_
   * - **Achievement standards**
     - Students develop algorithms represented diagrammatically and in English, and trace algorithms to predict
       output for a given input and to identify errors. Students develop and modify programs with user interfaces
       involving branching, iteration and functions using a general-purpose programming language.
   * - **Capabilities**
     - Critical and creative thinking; personal and social (using feedback to identify achievements and areas for
       improvement).

Learning intentions
--------------------

* I can learn and practise Python syntax by completing structured online courses.
* I can show evidence of my progress and reflect on my learning.

The task
---------

Complete these two Grok Academy courses:

#. `Python for Beginners <https://groklearning.com/course/python-for-beginners/>`_: print, input, variables,
   f-strings, selection and loops.
#. `Intro to Programming: Python <https://groklearning.com/course/intro-python-1/>`_: more practice with
   decisions, loops, lists, functions and dictionaries.

Keep an **ePortfolio** (a document or folder) that shows your progress and your thinking.

Stages
-------

.. list-table::
   :header-rows: 1
   :widths: 22 30 48

   * - When
     - Grok work
     - Matching lessons on this site
   * - Term 1, Weeks 9–10
     - Python for Beginners: print and input
     - :doc:`python_01_print_input`
   * - Term 2, Week 1
     - Python for Beginners: variables and f-strings
     - :doc:`python_02_variables_fstrings`
   * - Term 2, Weeks 2–3
     - Python for Beginners: selection and loops. Start Intro to Programming.
     - :doc:`python_03_algorithms`, :doc:`python_04_selection`, :doc:`python_05_iteration`,
       :doc:`python_06_functions`
   * - Term 2, Weeks 4–5
     - Intro to Programming: lists and dictionaries
     - :doc:`python_07_lists`, :doc:`python_08_dictionaries`

Each week, add an entry to your ePortfolio with:

* a **screenshot** of your Grok progress page
* **one program** you are proud of (copy the code in) and a sentence explaining what it does
* **one bug** you found and how you fixed it
* **one goal** for next week

What to submit
---------------

#. Your **Grok progress** for both courses (your teacher can also see this in Grok).
#. Your **ePortfolio** with at least **five** weekly entries.
#. A final **reflection** (150–200 words):

   * Which Python skill have you improved the most? Give an example.
   * What was the hardest problem you solved, and how did you solve it?
   * What feedback did you get (from Grok, your teacher or a classmate), and how did you use it?
   * What do you want to improve next?

Marking guide
--------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 20

   * - Criterion
     - Excellent (4–5)
     - Good (3)
     - Satisfactory (2)
     - Needs work (0–1)
   * - **Course completion**
     - 90–100% of both courses completed
     - 75–89% completed
     - 50–74% completed
     - Less than 50% completed
   * - **Code examples and explanations**
     - Clear, accurate explanations of well-chosen programs that use selection, loops, functions and data
       structures
     - Accurate explanations of programs that use a range of skills
     - Simple explanations of basic programs
     - Few or no examples
   * - **Debugging and tracing**
     - Clearly explains how errors were found and fixed, using tracing or test cases
     - Describes errors and fixes
     - Lists some errors
     - No evidence
   * - **Reflection and goals**
     - Insightful reflection using feedback, with specific, realistic goals
     - Reflection with some use of feedback and goals
     - Brief reflection
     - Missing or very brief

**Total: 20 marks** (4 criteria × 5 marks)

.. note::

   Grades are reported from A+ to NP. A task below a C standard must be resubmitted. Your teacher will confirm how
   the marks convert to grades.

Tips for success
-----------------

* Work on Grok **a little every lesson**, not all at the end.
* If you are stuck for more than 10 minutes, re-read the notes, check the lesson page on this site, then ask a
  classmate or your teacher.
* Use the **Hint** buttons in Grok, but try first.
* Read error messages carefully. They tell you the line number and type of error.

Exam-style question
--------------------

.. structuredquestion:: Debugging
   :total-marks: 5
   :category: ePortfolio

   .. stimulus::

      A student writes this program in Grok to count down from 5, but it has two bugs.

      .. code-block:: python

         count = 5
         while count > 0
             print(count)
         print("Go!")

   .. subquestion:: a) Identify the syntax error and explain how to fix it.
      :marks: 2

      .. model-answer::

         Line 2 is missing a colon at the end. It should be ``while count > 0:``

      .. marking-guidance::

         * 1 mark for identifying the missing colon on line 2.
         * 1 mark for the fix.

   .. subquestion:: b) After fixing the syntax error, the program prints 5 forever. Explain why and fix it.
      :marks: 2

      .. model-answer::

         ``count`` never changes, so ``count > 0`` is always True (an infinite loop). Add ``count = count - 1`` inside
         the loop (indented under ``print(count)``).

      .. marking-guidance::

         * 1 mark for explaining count never changes or infinite loop.
         * 1 mark for adding ``count = count - 1`` inside the loop.

   .. subquestion:: c) What will the fixed program output?
      :marks: 1

      .. model-answer::

         5, 4, 3, 2, 1 on separate lines, then ``Go!``

      .. marking-guidance::

         1 mark for the correct output.
