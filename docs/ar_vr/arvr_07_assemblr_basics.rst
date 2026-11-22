=============================================
7. Building AR in Assemblr Studio
=============================================

Learning intentions
--------------------

* I can find my way around the Assemblr Studio editor.
* I can import my PNG assets from Photoshop into an AR project.
* I can arrange image objects in 3D space using the transform tools and scenes.

Success criteria
~~~~~~~~~~~~~~~~~

* I can create a new project and upload PNG images.
* I can move, rotate, scale, duplicate and delete objects.
* I can preview my project and view it in AR on a phone or tablet.

What is Assemblr Studio?
-------------------------

**Assemblr Studio** is an AR platform where you build AR experiences by **dragging and dropping**
objects into an editor. No coding is needed. You can build on a computer in a web browser at
`studio.assemblrworld.com <https://studio.assemblrworld.com/>`_ and view your project in AR using the
**Assemblr Studio** app on a phone or tablet, or in a mobile web browser.

.. note::

   Your teacher will tell you how to sign in (for example, with your school account or a class code).
   Only use your first name in your project title and description.

The editor
-----------

When you open a project in the editor you will see:

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Part
     - What it does
   * - Menu of objects
     - Add **3D objects** from the Assemblr library, **images** (2D), **text**, **videos** and **audio**
   * - Workspace
     - The 3D space where you place and arrange objects
   * - Transform tools
     - **Move**, **rotate** and **scale** the selected object
   * - Scenes panel
     - Add extra **scenes** (like slides) to your project
   * - Interactivity
     - Make objects react when tapped (see :doc:`arvr_08_assemblr_interactivity`)
   * - Preview and Publish
     - Test your project, then publish it so others can view it

Assemblr has a **Default Editor** with all the tools, and a **Super Simple Editor** for quick projects.
Use the Default Editor for your assessment.

Importing your PNG assets
--------------------------

Assemblr accepts **JPG, JPEG and PNG** images. Use **PNG** for cut-out objects so their backgrounds stay
transparent.

#. Open your project in the editor.
#. Click the **Image** menu.
#. Upload your PNG files from your ``ar_assets`` folder. (You can also **drag** the image files straight
   from your computer into the editor.)
#. Click an uploaded image to add it to the workspace.

.. tip::

   If an image appears inside a white or black box, it was not saved with transparency. Go back to Photoshop,
   hide the background layer and export it again as a PNG (see :doc:`arvr_06_exporting_pngs`).

Arranging objects in 3D space
------------------------------

Your AR scene is **3D**. Objects have a position along three directions:

* **X**: left and right
* **Y**: up and down
* **Z**: forwards and backwards (closer to or further from the viewer)

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Tool
     - Use it to
   * - Move
     - Drag the arrows to move an object along X, Y or Z
   * - Rotate
     - Drag the rings to turn an object
   * - Scale
     - Make an object bigger or smaller
   * - Duplicate
     - Make a copy of an object (for example, several trees)
   * - Delete
     - Remove an object

A flat PNG is like a cardboard cut-out standing in the scene. Placing cut-outs at **different depths**
(some closer, some further away) makes the scene feel 3D, like a pop-up book.

Other objects
~~~~~~~~~~~~~~

* **Text and annotations:** add labels or instructions directly in Assemblr.
* **3D objects:** add models from the Assemblr library, such as planets, animals or furniture.
* **Videos and audio:** add a video screen, background music or sound effects.

Scenes
~~~~~~~

A **scene** is like a slide in a presentation. Each scene can have different objects. You can **add,
duplicate and remove** scenes, and later use interactivity to jump between them (for example, a "Next"
button). You can also set the **scene camera** to choose the starting view.

Preview and view in AR
-----------------------

* Use **Preview** in the editor to test your project in 3D on the computer.
* When you **publish** (see :doc:`arvr_08_assemblr_interactivity`), choose how people view it: in **3D**, in
  **AR above a marker** (a QR code or custom image), or in **AR around the real environment** without a marker.
* Open the project on a phone or tablet with the Assemblr Studio app or the project link, and point the camera
  at a flat surface or at the marker.

Worked example: a "Welcome to the lab" AR scene
------------------------------------------------

**Assets from Photoshop:** ``welcome_sign.png``, ``robot_body.png``, ``robot_arm.png``, ``robot_eyes.png``.

#. Create a new project called **Welcome to the Lab**.
#. Upload all four PNGs using the **Image** menu.
#. Add ``robot_body`` to the workspace. Scale it so it is about the size of a person's hand when viewed on a
   table.
#. Add ``robot_eyes`` and ``robot_arm``. Move them into place on the body. Move the eyes slightly **forward**
   (Z) so they sit in front of the head.
#. Add ``welcome_sign`` above and behind the robot.
#. Add a **3D object** from the library, such as a desk, to sit under the robot.
#. Click **Preview** and rotate the view to check it looks good from different angles.
#. Save. In the next lesson you will make the arm wave when the robot is tapped.

Activities
-----------

Activity 1: Assemblr basics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   Assemblr accepts JPG, JPEG and @@PNG|PSD|GIF@@ images.
   Use PNG for cut-outs because it keeps @@transparency|layers|fonts@@.
   The @@Z|X|Y@@ direction moves an object forwards and backwards.
   A @@scene|layer|marker@@ is like a slide in a presentation.
   An image that makes AR content pop up when scanned is called a @@marker|thumbnail|scene@@.

Activity 2: Transform tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Move, Rotate, Scale, Duplicate
   :delimiter: =>
   :instructions: Which tool would you use?

   Put the sign higher up in the scene => Move
   Bring a character closer to the viewer => Move
   Turn a car so it faces the viewer => Rotate
   Tilt a sign at an angle => Rotate
   Make a tree twice as big => Scale
   Shrink a planet so it fits on a table => Scale
   Make a forest of ten identical trees => Duplicate
   Add three more copies of a coin => Duplicate

Activity 3: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Your character appears inside a white rectangle in Assemblr. What is the most likely cause?

      [ ] The character is too big | Size does not add a white box.
      [x] The image was saved without transparency (for example, as a JPEG with a white background) | Correct. Export as PNG with the background hidden.
      [ ] Assemblr does not support images | It supports JPG, JPEG and PNG.
      [ ] You need to add a scene | Scenes do not affect transparency.

   .. multichoice::

      How can you make a scene of flat PNG images feel more 3D?

      [ ] Make all objects the same size and depth | That looks flat.
      [x] Place objects at different depths, like a pop-up book | Correct.
      [ ] Use only one image | One image cannot show depth.
      [ ] Turn off preview | Preview is for testing.

   .. multichoice::

      Which TWO are ways to view an Assemblr project in AR?

      [x] Above a QR code or custom marker | Correct. Marker-based AR.
      [x] Around your real environment without a marker | Correct. Markerless AR.
      [ ] Printed on paper only | Paper alone does not show AR.
      [ ] Inside a PSD file | PSD files are Photoshop working files.

Activity 4: Practical task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a practice Assemblr project using the PNGs you exported last lesson.

* Upload at least **three** of your own PNG images.
* Add at least **one** 3D object from the library and **one** text label.
* Place objects at **different depths**.
* Add a **second scene**.
* Preview it, then view it in AR on a tablet. Take a screenshot.

Challenge
----------

Build a small "AR diorama" (a mini 3D scene) on a theme, such as an underwater reef, a planet surface or a
haunted house. Use at least **six** objects at different depths, sizes and angles. Ask a classmate to view it
in AR and tell you one thing that looks real and one thing that could be improved.

Exam-style question
--------------------

.. structuredquestion:: Building an AR scene
   :total-marks: 5
   :category: Augmented reality

   .. stimulus::

      Mason has exported a cartoon fish, some seaweed and a treasure chest from Photoshop. He uploads them to
      Assemblr Studio, but the scene looks flat and the fish is hidden behind the seaweed.

   .. subquestion:: a) Explain how Mason can use the Move tool to bring the fish in front of the seaweed.
      :marks: 2

      .. model-answer::

         He can select the fish and drag it along the Z direction (forwards), so it is closer to the viewer than
         the seaweed.

      .. marking-guidance::

         * 1 mark for using the Move tool on the fish.
         * 1 mark for moving it forwards along Z (closer to the viewer).

   .. subquestion:: b) Suggest two ways Mason could make his scene look less flat.
      :marks: 2

      .. model-answer::

         * Place objects at different depths (some near, some far).
         * Use different sizes so far-away objects look smaller.
         * Rotate some objects to different angles, or add 3D objects from the library.

      .. marking-guidance::

         1 mark for each valid suggestion (maximum 2).

   .. subquestion:: c) Why should Mason use PNG files rather than JPEG files for his assets?
      :marks: 1

      .. model-answer::

         PNG files keep transparent backgrounds, so the fish and seaweed do not appear inside rectangles.

      .. marking-guidance::

         1 mark for PNG keeping transparency.
