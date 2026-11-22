===============================================
8. Adding behaviours and publishing in Assemblr
===============================================

Learning intentions
--------------------

* I can explain the difference between a trigger object and a target object.
* I can add behaviours (interactivity) to image objects so they move, rotate, scale, appear, disappear or play
  sounds.
* I can publish and share my AR project with a QR marker or link.

Success criteria
~~~~~~~~~~~~~~~~~

* I can add at least three different types of interactivity to my project.
* I can set the start time and duration so actions happen in the right order.
* I can publish my project and test it in AR on a phone or tablet.

Behaviours bring AR to life
----------------------------

A still image in AR is interesting for a few seconds. **Behaviours** (Assemblr calls them
**interactivity**) make objects **respond** to the user. This turns your scene into an **experience**.

Trigger and target
~~~~~~~~~~~~~~~~~~~

Every interactivity action has two parts:

* **Trigger object:** the object the user **taps** to start the action.
* **Target object:** the object that **reacts**.

The trigger and target can be the **same** object (tap the robot, the robot spins) or **different** objects
(tap a button, the robot spins).

Types of interactivity
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Type
     - What it does
   * - **Move**
     - Moves the target in a direction (or a **Custom** direction) by a distance you choose
   * - **Rotate**
     - Turns the target by a number of degrees
   * - **Scale**
     - **Scale In** makes the target smaller, **Scale Out** makes it bigger, or set a custom amount
   * - **Animation**
     - Plays an animation built into a 3D object (only for 3D objects that have more than one animation).
       Playback can be **Loop**, **Once** or **Ping pong**.
   * - **Visibility**
     - **Hide** or **Show** the target, for example to reveal a hidden message
   * - **Jump Up**
     - **Switch Scene** (go to another scene) or **Open URL** (open a website)
   * - **Media**
     - Control a video or play a **sound effect**

You can also make actions start automatically when a scene opens, using **interactivity on scene enter**.

Adding an interactivity action
-------------------------------

#. Click your **trigger object** and choose **Add Interactivity**.
#. Choose the type, for example **Rotate**.
#. Choose the direction or settings (for example, rotate 360 degrees).
#. Give the action a clear **name** (for example, *Robot arm wave*) and select the **target object**.
#. Open the **advanced settings** to set:

   * **Start time:** when the action begins after the tap
   * **Duration:** how long it takes
   * **Easing:** how it speeds up and slows down (smooth or sudden)

#. Click **Apply**.
#. Use the play button in the **Interactivity pane** to preview. Adjust start times so actions do not
   clash.

Worked example: tap the robot to wave
--------------------------------------

Using the "Welcome to the Lab" scene from :doc:`arvr_07_assemblr_basics`:

.. list-table::
   :header-rows: 1
   :widths: 22 18 18 42

   * - Action name
     - Trigger
     - Target
     - Settings
   * - Arm wave
     - robot_body
     - robot_arm
     - Rotate 30°, start 0 s, duration 0.5 s
   * - Arm back
     - robot_body
     - robot_arm
     - Rotate −30°, start 0.5 s, duration 0.5 s
   * - Say hello
     - robot_body
     - (sound)
     - Media → sound effect "hello", start 0 s
   * - Show speech bubble
     - robot_body
     - label_robot
     - Visibility → Show, start 0.2 s
   * - Next scene
     - button_next
     - (scene 2)
     - Jump Up → Switch Scene to Scene 2

So that ``label_robot`` only appears when the robot is tapped, it needs to start hidden. Add a **Visibility → Hide**
action for ``label_robot`` that runs on **scene enter** (or check how your version of Assemblr sets an object to
start hidden).

**Result:** When the user taps the robot, the arm waves, a "hello" sound plays and a speech bubble appears.
Tapping the **Next** button takes them to the second scene.

.. tip::

   **Rotate around the right point.** An arm should rotate from the shoulder, not the middle. In Photoshop, you
   can extend the arm's canvas so the shoulder is in the centre of the PNG, or test different positions in
   Assemblr until the rotation looks natural.

Designing good interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Make it obvious what to tap.** Add a label like "Tap me!" or a glowing button.
* **Give feedback.** Every tap should cause something the user can see or hear.
* **Keep it short.** Actions of 0.3–1 second feel snappy.
* **Do not overload.** Too many things moving at once is confusing.
* **Tell a story.** Use scenes to guide the user from start to finish.

Publishing and sharing
-----------------------

#. Click **Publish**. Capture a **thumbnail** (a preview picture of your project).
#. Fill in the **project information**: title, description and category. Use your first name only.
#. In **Publish Settings**, choose how people will view it:

   * **3D view**, or
   * **AR** that pops up **above an AR marker** (choose **Horizontal** to stand on top of the marker or
     **Vertical** to appear in front of it), or
   * **AR** around your **real environment** (markerless).

#. Choose **public** or **private** (your teacher will tell you which to use).
#. Share your project using:

   * the **project link**
   * an **AR graphic marker**: download the **QR marker** and print it or show it on a screen
   * a **custom AR marker**: your own image (Assemblr gives each account one free custom marker slot)

To view it, open the link or scan the marker with the **Assemblr Studio** app on a phone or tablet.

.. admonition:: Test, test, test
   :class: important

   Always test your published project on a real phone or tablet before you submit. Check that every tap does
   something, the images have transparent backgrounds and the scene is the right size in the room.

Activities
-----------

Activity 1: Trigger or target?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. multichoice::

   A user taps a treasure chest and a gem appears above it. Which object is the **trigger**?

   [x] The treasure chest | Correct. The chest is tapped to start the action.
   [ ] The gem | The gem is the target. It reacts by appearing.
   [ ] The marker | The marker positions the scene, but it is not tapped.
   [ ] The scene camera | The camera is not tapped.

.. multichoice::

   In the same example, which interactivity type makes the gem appear?

   [ ] Move | Move changes position.
   [ ] Scale | Scale changes size.
   [x] Visibility (Show) | Correct. The gem was hidden and is now shown.
   [ ] Jump Up | Jump Up switches scenes or opens a website.

Activity 2: Match the behaviour
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Move, Rotate, Scale, Visibility, Jump Up, Media
   :delimiter: =>
   :instructions: Which interactivity type would you use?

   A rocket flies upwards when tapped => Move
   A car drives forward across the table => Move
   A wheel spins around => Rotate
   A door swings open 90 degrees => Rotate
   A balloon grows bigger => Scale
   A planet shrinks to show it is far away => Scale
   A secret message appears => Visibility
   A ghost disappears when tapped => Visibility
   A Next button goes to the second scene => Jump Up
   A button opens a website about the topic => Jump Up
   A dog barks when tapped => Media

Activity 3: Plan the timing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Put these actions in the order they should start when a user taps a jack-in-the-box.

.. ordering::
   :no-indent:

   The lid rotates open (start 0 s).
   A "boing" sound effect plays (start 0.3 s).
   The clown moves up out of the box (start 0.4 s).
   The clown scales out to look bigger (start 0.8 s).
   A "Surprise!" sign is shown (start 1.2 s).

Activity 4: Publishing
~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   Before publishing, you capture a @@thumbnail|marker|scene@@ for people to see a preview.
   To make AR stand on top of a marker, choose @@Horizontal|Vertical|Private@@.
   To make AR appear without a marker, choose AR around the real @@environment|scene|thumbnail@@.
   You can download a @@QR|PSD|JPEG@@ marker to print and scan.

Activity 5: Practical task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add interactivity to your practice project from last lesson:

* at least **three** different interactivity types (for example, Rotate, Visibility and Media)
* one object that is **hidden** until something is tapped
* a **button** that switches to your second scene
* start times and durations set so actions happen in a sensible order

Publish it with a **QR marker**, test it on a tablet, and ask a classmate to try it without help. Write down
one thing they found confusing and fix it.

Challenge
----------

Make a short **AR story** with three scenes, where the user's taps decide what happens next (for example,
"Open the left door or the right door?"). Use **Switch Scene** to branch the story. Draw a diagram of the scenes
and the buttons that link them before you build it.

Exam-style question
--------------------

.. structuredquestion:: Interactivity in AR
   :total-marks: 6
   :category: Augmented reality

   .. stimulus::

      Grace is making an AR experience about the solar system for Year 3 students. The Sun and eight planets are
      PNG images. She wants each planet to spin and a fact label to appear when a student taps it.

   .. subquestion:: a) For one planet, describe the trigger object, the target object(s) and the interactivity types Grace should use.
      :marks: 3

      .. model-answer::

         The trigger is the planet (for example, Mars). The targets are the planet and its fact label. Grace should
         use Rotate on the planet to make it spin, and Visibility (Show) on the fact label, which starts hidden.

      .. marking-guidance::

         * 1 mark for the planet as the trigger.
         * 1 mark for Rotate on the planet.
         * 1 mark for Visibility (Show) on the label (which starts hidden).

   .. subquestion:: b) Explain why Grace should test the experience with a few Year 3 students before finishing.
      :marks: 2

      .. model-answer::

         Year 3 students are the users, so testing shows whether they know what to tap and can read the labels. Grace
         can use their feedback to fix confusing parts, such as adding a "Tap a planet!" instruction.

      .. marking-guidance::

         * 1 mark for identifying them as the target users.
         * 1 mark for using feedback to improve the design.

   .. subquestion:: c) Give one way Grace could share the experience with the class.
      :marks: 1

      .. model-answer::

         Publish it and print the QR marker for students to scan with the Assemblr app (or share the project link).

      .. marking-guidance::

         1 mark for a QR or custom marker, or the project link.
