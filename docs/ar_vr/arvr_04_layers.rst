=============================================
4. Photoshop layers
=============================================

Learning intentions
--------------------

* I can explain what layers are and why they are useful.
* I can create, name, order, hide, group and change the opacity of layers.
* I can organise a PSD file so each AR asset is on its own layer.

Success criteria
~~~~~~~~~~~~~~~~~

* I can use the Layers panel to manage at least five layers.
* I can explain how the order of layers changes what you see.
* I can set up a PSD file with clearly named layers ready for exporting to AR.

What are layers?
-----------------

Imagine stacking sheets of clear plastic on top of each other. You can draw on each sheet separately.
Where a sheet is clear, you can see the sheets underneath. **Layers** in Photoshop work the same way.

Each layer can hold one part of your design, such as a background, a character, a hat or some text.
Because each part is separate, you can **move, edit, hide or delete** one part without changing the others.

The Layers panel
-----------------

Open it with **Window → Layers** (or press **F7**).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Part
     - What it does
   * - Eye icon
     - Shows or hides the layer
   * - Layer thumbnail
     - A small preview of what is on the layer
   * - Layer name
     - Double-click to rename it
   * - Opacity
     - How see-through the layer is (100% solid, 0% invisible)
   * - Lock icons
     - Stop a layer from being moved or changed by accident
   * - **+** (New Layer) button
     - Adds an empty layer
   * - Folder (New Group) button
     - Puts layers into a group (folder)
   * - **fx** button
     - Adds a layer style such as a drop shadow or stroke
   * - Rectangle with circle button
     - Adds a **layer mask** (see :doc:`arvr_05_masks`)
   * - Bin
     - Deletes the selected layer

Layer order
~~~~~~~~~~~~

Layers at the **top** of the panel appear **in front** of the layers below them. Drag a layer up or down
in the panel to change the order.

.. code-block:: text

   Layers panel (top to bottom)        What you see
   ─────────────────────────────        ─────────────────────────────
   hat                                  The hat is in front of the robot
   robot                                The robot is in front of the floor
   floor                                The floor is behind everything

Useful layer actions
---------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Action
     - How
   * - New empty layer
     - Click **+** or press **Ctrl + Shift + N**
   * - Copy selection to a new layer
     - **Ctrl + J**
   * - Duplicate a layer
     - Select it, then **Ctrl + J**, or drag it onto **+**
   * - Select more than one layer
     - Hold **Ctrl** and click each layer
   * - Group layers
     - Select the layers, then **Ctrl + G**
   * - Link layers so they move together
     - Select the layers, then click the chain icon
   * - Merge layers into one
     - Select the layers, then **Ctrl + E** (careful: you cannot separate them again)
   * - Select a layer by clicking on the canvas
     - Move tool with **Auto-Select** ticked in the Options bar

Naming layers
~~~~~~~~~~~~~~

When you export layers for AR, the **layer name becomes the file name**. Good names make the AR build much
easier.

* **Bad:** Layer 1, Layer 1 copy, Layer 7
* **Good:** ``robot_body``, ``robot_arm_left``, ``sign_welcome``, ``button_play``

Use lowercase letters and underscores, with no spaces.

Worked example: a layered AR character
---------------------------------------

**Goal:** A robot with a separate arm so the arm can be animated in AR later.

#. **File → New**: 1080 × 1080 px, transparent background.
#. Click **+** and name the layer ``robot_body``. Use the **Rectangle** and **Ellipse** tools to draw the
   body and head.
#. Click **+** and name it ``robot_arm``. Draw the arm on this layer.
#. Click **+** and name it ``robot_eyes``. Draw the eyes.
#. Drag ``robot_eyes`` to the top so the eyes are in front of the head.
#. Select all three layers (Ctrl + click) and press **Ctrl + G**. Name the group ``robot``.
#. Add a **Type** layer called ``label_robot`` that says "Hi, I'm Bolt!"
#. Turn the eye icons on and off to check each part is on the right layer.
#. Save as ``robot_layers.psd``.

Because the arm is on its own layer, you can export it separately and make it rotate or wave in Assemblr.

Activities
-----------

Activity 1: Layer order
~~~~~~~~~~~~~~~~~~~~~~~~

Put these layers in order from **top** (front) to **bottom** (back) so a fish swims in front of seaweed,
the seaweed is in front of the sand, and the title is in front of everything.

.. ordering::
   :no-indent:

   title_text
   fish
   seaweed
   sand
   ocean_background

Activity 2: Layers panel
~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   Click the @@eye|lock|bin@@ icon to hide or show a layer.
   Layers at the @@top|bottom|middle@@ of the panel appear in front.
   Press Ctrl + @@G|E|D@@ to group selected layers.
   Press Ctrl + @@E|G|J@@ to merge layers (you cannot separate them again).
   Set @@opacity|resolution|tolerance@@ to make a layer see-through.

Activity 3: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Why should each AR asset be on its own layer?

      [ ] Layers make the file smaller | Layers usually make the file bigger.
      [x] So each part can be edited, moved and exported separately | Correct.
      [ ] Assemblr can only open PSD files | Assemblr uses PNG or JPG images.
      [ ] It changes the resolution | Layers do not change resolution.

   .. multichoice::

      A character is hidden behind the background. What is the most likely reason?

      [ ] The character layer is too small | Size does not change the order.
      [x] The character layer is below the background layer in the Layers panel | Correct. Drag it above the background.
      [ ] The opacity is 100% | 100% means fully solid.
      [ ] The file is saved as a PSD | PSD is the right working format.

   .. multichoice::

      Which layer name is best for exporting to AR?

      [ ] Layer 3 copy | Not descriptive.
      [ ] My Cool Dragon!!! | Spaces and symbols can cause problems in file names.
      [x] dragon_wing_left | Correct. Clear, lowercase, underscores.
      [ ] untitled | Not descriptive.

Activity 4: Practical task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a PSD for an AR character or object of your own design with **at least five named layers**,
including:

* at least one part that could move separately (an arm, a wing, a wheel)
* a text label on a type layer
* a layer style (drop shadow or stroke)
* at least one group

Take a screenshot of your Layers panel and add it to your project folder.

Challenge
----------

Experiment with **blending modes** (the drop-down menu that says **Normal** at the top of the Layers
panel). Put a texture or colour layer over your character and try **Multiply**, **Screen** and
**Overlay**. Describe what each one does in your own words.

Exam-style question
--------------------

.. structuredquestion:: Working with layers
   :total-marks: 5
   :category: Photoshop

   .. stimulus::

      Leo made a pirate ship for his AR project. He drew the ship, sails, flag and water all on one layer
      called "Layer 1". Now his teacher suggests the flag should wave in the AR scene.

   .. subquestion:: a) Explain why drawing everything on one layer causes a problem for Leo.
      :marks: 2

      .. model-answer::

         All the parts are joined together, so Leo cannot move, edit or export the flag separately. He would have
         to cut the flag out again or redraw it before it could be animated on its own in AR.

      .. marking-guidance::

         * 1 mark for saying the parts cannot be separated.
         * 1 mark for linking this to animating or exporting the flag.

   .. subquestion:: b) Describe how Leo should organise the layers in a new version of his file.
      :marks: 2

      .. model-answer::

         Put each part on its own layer with a clear name, such as ``ship_hull``, ``ship_sails``, ``ship_flag``
         and ``water``. Order them so the water is at the bottom and the flag is above the sails, and group the
         ship layers together.

      .. marking-guidance::

         * 1 mark for separate layers with clear names.
         * 1 mark for correct ordering or grouping.

   .. subquestion:: c) What does lowering a layer's opacity do?
      :marks: 1

      .. model-answer::

         It makes the layer more see-through (transparent), so the layers underneath show through.

      .. marking-guidance::

         1 mark for "more see-through" or "more transparent".
