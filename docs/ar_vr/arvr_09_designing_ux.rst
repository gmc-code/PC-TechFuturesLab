=============================================
9. Designing the user experience
=============================================

Learning intentions
--------------------

* I can identify the users and stakeholders of a digital solution and find out what they need.
* I can write functional and non-functional requirements and design criteria.
* I can create and compare alternative designs, then test a prototype and improve it.

Success criteria
~~~~~~~~~~~~~~~~~

* I can survey or interview users to find their needs.
* I can sort requirements into functional and non-functional.
* I can draw a storyboard for an AR experience and evaluate two designs against criteria.

User interface and user experience
-----------------------------------

* The **user interface (UI)** is what the user sees and touches: buttons, images, text, colours and layout.
* The **user experience (UX)** is how the user **feels** when using it. Is it easy, clear, fun and useful?

A beautiful AR scene can still have a poor user experience if people do not know what to tap, the text is
too small to read, or nothing happens when they tap.

The design process
-------------------

.. code-block:: text

   1. DEFINE      →  2. DESIGN       →  3. PROTOTYPE   →  4. TEST         →  5. IMPROVE
   Who are the       Sketch two or      Build a quick     Watch real users   Fix problems
   users? What       more ideas and     version in        try it and         and test
   do they need?     compare them       Assemblr          collect feedback   again

1. Define: users, stakeholders and needs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Users** are the people who will use the AR experience.
* **Stakeholders** are everyone affected by it or interested in it: users, your teacher, the school,
  parents and so on.

Find out what users need by **asking them**:

* **Interview:** talk to a few users and ask open questions, for example "What would make learning about
  planets more fun?"
* **Survey:** ask more people the same short questions, for example "Rate from 1 to 5: How easy is it for you
  to read small text on a phone?"

Requirements
~~~~~~~~~~~~~

**Requirements** describe what the solution must do and how well it must do it.

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Type
     - Meaning
     - Examples for an AR planets experience
   * - **Functional**
     - What the solution must **do**
     - Each planet spins when tapped. A fact label appears. A button moves to the next scene.
   * - **Non-functional**
     - **How well** it works: qualities such as ease of use, speed, look and accessibility
     - Text is readable from 1 metre. The experience loads in under 10 seconds. It suits Year 3 students.

**Design criteria** are the measurable checks you use to judge whether a design meets the requirements, for
example: "A Year 3 student can find and tap all eight planets in under two minutes without help."

2. Design: storyboards and alternatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A **storyboard** is a series of sketches showing what the user sees at each step and what happens when they
tap. For each frame, note:

* what is visible
* what the user does (tap, move closer, walk around)
* what happens (moves, appears, sound, next scene)

Good designers sketch **at least two different** ideas, then compare them against the design criteria before
choosing one.

3. Prototype
~~~~~~~~~~~~~

A **prototype** is an early, simple version used for testing. In Assemblr, it could be your scene with
placeholder images and one or two working interactions.

4. Test and 5. Improve
~~~~~~~~~~~~~~~~~~~~~~~

Ask a few users to try the prototype **without help** while you watch. Note where they get stuck. Ask:

* What did you expect to happen when you tapped that?
* Was anything confusing?
* What was your favourite part?

Then improve the design and test again.

Worked example: comparing two designs
--------------------------------------

**Brief:** An AR experience to welcome new Year 7 students to the science lab.

**Design A:** A single scene with a robot. Tap the robot to hear a welcome message and see three safety rules.

**Design B:** Three scenes: (1) a robot says hello, (2) tap lab equipment to see its name, (3) a safety quiz
where tapping the right answer shows a tick.

.. list-table::
   :header-rows: 1
   :widths: 46 27 27

   * - Design criterion
     - Design A
     - Design B
   * - New students can use it without help
     - ✓ Very simple
     - ✓ Needs "Tap to continue" labels
   * - Teaches at least three lab safety rules
     - ✓
     - ✓
   * - Includes at least three different interactions
     - ✗ Only sound and show
     - ✓ Sound, show, switch scene, rotate
   * - Takes 1–3 minutes to complete
     - ✗ Under 1 minute
     - ✓ About 2 minutes
   * - Can be built in the time available (2 weeks)
     - ✓
     - ✓ (with planning)

**Decision:** Design B meets more criteria. The designer adds clear "Tap to continue" labels to fix its
weakness.

Activities
-----------

Activity 1: Functional or non-functional?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Functional, Non-functional
   :delimiter: =>

   Tapping the volcano makes it erupt => Functional
   A Next button switches to scene 2 => Functional
   A fact label appears when an animal is tapped => Functional
   A sound plays when the user taps the drum => Functional
   Text can be read from one metre away => Non-functional
   The project loads in under 10 seconds => Non-functional
   The colours suit a young audience => Non-functional
   A first-time user can work out what to do without instructions => Non-functional

Activity 2: Order the design process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ordering::
   :no-indent:

   Interview and survey users to find their needs.
   Write the requirements and design criteria.
   Sketch two or more alternative designs as storyboards.
   Compare the designs against the criteria and choose one.
   Build a prototype in Assemblr.
   Watch users test the prototype and collect feedback.
   Improve the design and test again.

Activity 3: Key words
~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   What the user sees and touches is the user @@interface|experience|requirement@@.
   How the user feels when using a product is the user @@experience|interface|prototype@@.
   People affected by or interested in a solution are called @@stakeholders|developers|markers@@.
   An early, simple version used for testing is a @@prototype|storyboard|thumbnail@@.
   A series of sketches showing each step of the experience is a @@storyboard|survey|scene@@.

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Which is the best interview question to find out what users need?

      [ ] Do you like my AR project? | A yes/no question gives little information.
      [x] What makes it hard for you to learn about space? | Correct. It is open and focuses on the user's needs.
      [ ] Is purple your favourite colour? | Not about their needs.
      [ ] Can you test it for me now? | That is testing, not finding needs.

   .. multichoice::

      Why should you create more than one design?

      [ ] To use up more time | Not the reason.
      [x] So you can compare them against the criteria and choose the best | Correct.
      [ ] Because Assemblr needs two projects | It does not.
      [ ] So you can submit both | You submit your best design.

Challenge
----------

Make a short **survey** (5 questions) for the users of your AR project. Include at least two rating-scale
questions and one open question. Give it to at least five people and summarise the results in a table or graph.
What did you change in your design because of the results?

Exam-style question
--------------------

.. structuredquestion:: Designing for users
   :total-marks: 7
   :category: User experience

   .. stimulus::

      A local zoo asks students to create an AR experience for primary school visitors. Children will scan a QR
      sign at each enclosure to see a cartoon animal that tells them a fact.

   .. subquestion:: a) Identify two stakeholders, other than the children, for this project.
      :marks: 2

      .. model-answer::

         The zoo staff or managers, and the teachers or parents who bring the children. (Also accept the
         student developers or the zoo's marketing team.)

      .. marking-guidance::

         1 mark for each valid stakeholder (maximum 2).

   .. subquestion:: b) Write one functional and one non-functional requirement for the experience.
      :marks: 2

      .. model-answer::

         Functional: when the child taps the cartoon animal, it says a fact out loud (sound plays).
         Non-functional: the text and buttons are large enough for young children to read and tap easily.

      .. marking-guidance::

         * 1 mark for a valid functional requirement (something it does).
         * 1 mark for a valid non-functional requirement (a quality, such as ease of use, speed or appearance).

   .. subquestion:: c) Describe how the students could find out what the children need before designing.
      :marks: 2

      .. model-answer::

         They could survey or interview a group of primary school children (and their teachers), asking what
         animals they like and what would make learning at the zoo fun.

      .. marking-guidance::

         * 1 mark for a method (survey or interview).
         * 1 mark for who they would ask and what they would ask about.

   .. subquestion:: d) Explain why the students should test a prototype with children.
      :marks: 1

      .. model-answer::

         To find problems, such as children not knowing what to tap, and fix them before the final version.

      .. marking-guidance::

         1 mark for finding and fixing problems before the final version.
