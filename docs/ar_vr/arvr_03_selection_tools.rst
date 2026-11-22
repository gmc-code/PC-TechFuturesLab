=============================================
3. Photoshop selection tools
=============================================

Learning intentions
--------------------

* I can explain what a selection is and why it is useful.
* I can choose the best selection tool for an image.
* I can use selection tools to isolate an object onto its own layer.

Success criteria
~~~~~~~~~~~~~~~~~

* I can use the Marquee, Lasso, Quick Selection, Magic Wand and Object Selection tools.
* I can add to and subtract from a selection.
* I can cut an object out of a photo and put it on its own layer with a transparent background.

What is a selection?
---------------------

A **selection** is an area of an image that you choose to work on. Photoshop shows a selection with
moving dotted lines called **"marching ants"**. Anything you do, such as copying, deleting, colouring or
masking, only affects the area **inside** the selection.

For AR, selections let you **isolate** an object (cut it away from its background) so it can float in the
real world.

The selection tools
--------------------

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Tool
     - Key
     - Best for
   * - Rectangular Marquee
     - M
     - Rectangles and squares. Hold **Shift** for a perfect square.
   * - Elliptical Marquee
     - M
     - Ovals and circles. Hold **Shift** for a perfect circle.
   * - Lasso
     - L
     - Drawing a rough freehand selection
   * - Polygonal Lasso
     - L
     - Objects with straight edges (click point to point)
   * - Magnetic Lasso
     - L
     - Objects with clear edges against a different background. It "sticks" to the edge.
   * - Object Selection
     - W
     - Drag a box around an object and Photoshop finds its edges automatically
   * - Quick Selection
     - W
     - "Paint" over an object and the selection grows to the edges
   * - Magic Wand
     - W
     - Areas of similar colour, such as a plain blue sky. Change the **Tolerance** to select more or
       fewer colours.

Tools under the same key share a spot in the toolbar. **Click and hold** a tool (or right-click it) to see
the others in the group.

Automatic selections
~~~~~~~~~~~~~~~~~~~~~

* **Select → Subject**: Photoshop uses AI to find the main subject (a person, animal or object).
* **Select → Sky**: selects the sky in a photo.
* **Remove background**: in the **Contextual Task Bar** or the **Properties** panel under **Quick
  Actions**. Photoshop selects the subject and hides the background using a mask (you will learn about
  masks in :doc:`arvr_05_masks`).

Automatic tools are fast, but they are not always perfect. Check the edges and fix them with the manual
tools.

Changing a selection
---------------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Do this
     - To
   * - Hold **Shift** while selecting
     - **Add** to the selection
   * - Hold **Alt** (Option on Mac) while selecting
     - **Subtract** from the selection
   * - **Ctrl + D** (Select → Deselect)
     - Remove the selection
   * - **Ctrl + Shift + I** (Select → Inverse)
     - Swap: select everything that was **not** selected
   * - **Select → Select and Mask**
     - Fine-tune the edges, for example around hair or fur
   * - **Select → Modify → Feather**
     - Soften the edge of the selection

Worked example: cut out a toy car
----------------------------------

**Goal:** Put a toy car from a photo onto its own layer with a transparent background.

#. **File → Open** the photo.
#. Choose the **Object Selection tool** (W) and drag a box around the car. Marching ants appear around it.
#. Zoom in (Ctrl + +). If part of the background is selected (for example, a shadow), switch to the
   **Quick Selection tool** and hold **Alt** while painting over that part to subtract it.
#. If part of the car is missing, hold **Shift** and paint over it to add it.
#. Press **Ctrl + J** (**Layer → New → Layer via Copy**). This copies the selected car onto a **new layer**.
#. Click the **eye** icon next to the original background layer in the Layers panel to hide it. You now see
   the car on a checkerboard pattern. **The checkerboard means transparent.**
#. Rename the new layer ``car`` (double-click the layer name).
#. Save as ``car_cutout.psd``.

Choosing the best tool
~~~~~~~~~~~~~~~~~~~~~~~

Ask yourself:

* **Is it a simple shape?** Use a Marquee.
* **Does it have straight edges?** Use the Polygonal Lasso.
* **Is it one clear object?** Try **Select → Subject** or the Object Selection tool first.
* **Is the background one plain colour?** Use the Magic Wand on the background, then **Select → Inverse**.
* **Still not perfect?** Fix it with Quick Selection while holding Shift or Alt.

Watch
~~~~~~

* `Photoshop for Complete Beginners: Lesson 1 <https://www.youtube.com/watch?v=xTzvQkOll2U&list=PLLlSBGLVsEPIFGSGw2zJ2K43V5vxMMMTE>`_
* `Selections: Photoshop for Beginners, Lesson 6 <https://www.youtube.com/watch?v=jBCDKCpsmso&list=PLLlSBGLVsEPIFGSGw2zJ2K43V5vxMMMTE&index=7>`_
* Photoshop's built-in tutorials: **Help → Photoshop Help** or the **Learn** tab on the Home screen.

Activities
-----------

Activity 1: Pick the tool
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Rectangular Marquee, Elliptical Marquee, Polygonal Lasso, Magic Wand, Object Selection
   :delimiter: =>
   :instructions: Choose the best selection tool for each job.

   Selecting a rectangular photo frame => Rectangular Marquee
   Selecting a round clock face => Elliptical Marquee
   Selecting a perfectly circular ball => Elliptical Marquee
   Selecting a star shape with straight edges => Polygonal Lasso
   Selecting a building with straight walls => Polygonal Lasso
   Selecting a plain blue sky => Magic Wand
   Selecting a white background behind a product photo => Magic Wand
   Selecting a dog sitting on grass => Object Selection
   Selecting a person standing in a park => Object Selection

Activity 2: Shortcuts
~~~~~~~~~~~~~~~~~~~~~~

.. fillin::

   Hold @@Shift@@ while selecting to add to a selection.
   Hold @@Alt@@ while selecting to subtract from a selection (Option on a Mac).
   Press Ctrl + @@D@@ to deselect.
   Press Ctrl + @@J@@ to copy a selection onto a new layer.
   The moving dotted line around a selection is called marching @@ants@@.

Activity 3: Order the cut-out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ordering::
   :no-indent:

   Open the photo in Photoshop.
   Use the Object Selection tool to select the object.
   Zoom in and fix the edges by adding (Shift) or subtracting (Alt).
   Press Ctrl + J to copy the selection onto a new layer.
   Hide the original background layer.
   Rename the new layer and save as a PSD.

Activity 4: Practical task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using photos you have taken yourself (or copyright-free photos from a site your teacher recommends),
cut out **three** objects using **three different** selection tools. Put each object on its own named
layer in one PSD file. In a text layer, write the name of the tool you used for each object.

Challenge
----------

Find a photo of an animal with fur or a person with messy hair. Use **Select → Subject**, then
**Select → Select and Mask**. Use the **Refine Edge Brush** to paint over the fur or hair edges. Compare
the result with a plain Quick Selection. Which looks more realistic, and why?

Exam-style question
--------------------

.. structuredquestion:: Choosing selection tools
   :total-marks: 5
   :category: Photoshop

   .. stimulus::

      Ava has a photo of her sneaker on a plain white bench. She wants to cut out the sneaker for her AR
      project so it looks like it is floating in the AR scene.

   .. subquestion:: a) Describe how Ava could use the Magic Wand tool to select the sneaker.
      :marks: 2

      .. model-answer::

         She could click the plain white background with the Magic Wand to select it (holding Shift to add any
         missed areas), then choose Select → Inverse to swap the selection so the sneaker is selected instead.

      .. marking-guidance::

         * 1 mark for selecting the white background with the Magic Wand.
         * 1 mark for using Select → Inverse.

   .. subquestion:: b) Part of the white sole of the sneaker was not selected. Explain how to add it to the selection.
      :marks: 1

      .. model-answer::

         Hold Shift and select the missing area (for example, with the Quick Selection tool or the Lasso) to
         add it to the selection.

      .. marking-guidance::

         1 mark for holding Shift to add to the selection with a suitable tool.

   .. subquestion:: c) After selecting the sneaker, what should Ava do so it is on its own layer with a transparent background?
      :marks: 2

      .. model-answer::

         Press Ctrl + J to copy the selection to a new layer, then hide (or delete) the original background layer
         so the checkerboard (transparency) shows around the sneaker.

      .. marking-guidance::

         * 1 mark for copying the selection to a new layer (Ctrl + J or Layer via Copy).
         * 1 mark for hiding or deleting the background layer.
