=============================================
5. Photoshop layer masks
=============================================

Learning intentions
--------------------

* I can explain what a layer mask is and how it hides parts of a layer.
* I can explain why masks are better than the Eraser tool (non-destructive editing).
* I can use a layer mask to remove a background and fix the edges.

Success criteria
~~~~~~~~~~~~~~~~~

* I can remember the rule: **white reveals, black conceals**.
* I can add a mask from a selection and paint on it to fix mistakes.
* I can use **Remove background** and then refine the mask.

What is a layer mask?
----------------------

A **layer mask** is a black-and-white "stencil" attached to a layer. It controls which parts of the layer
you can see.

.. admonition:: The golden rule
   :class: important

   **White reveals. Black conceals.**

   * Where the mask is **white**, the layer shows.
   * Where the mask is **black**, the layer is hidden (transparent).
   * **Grey** makes the layer partly see-through.

The mask appears as a second thumbnail next to the layer thumbnail in the Layers panel.

Masks vs the Eraser
--------------------

.. list-table::
   :header-rows: 1
   :widths: 25 37 38

   * -
     - Eraser tool
     - Layer mask
   * - What happens to pixels
     - **Deleted** forever (once you save and close)
     - **Hidden**, but still there
   * - Fixing a mistake later
     - Hard: you have to redraw the missing part
     - Easy: paint white to bring it back
   * - Type of editing
     - **Destructive**
     - **Non-destructive**

**Non-destructive editing** means you can always undo or change your edits later, because the original
image is never destroyed. Professionals use masks for this reason.

Adding a mask
--------------

Method 1: from a selection (most common)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Make a selection around the object you want to **keep** (for example, with **Select → Subject**).
#. Make sure the layer is selected in the Layers panel.
#. Click the **Add layer mask** button (rectangle with a circle) at the bottom of the Layers panel.
#. The selected area stays visible (white on the mask). Everything else is hidden (black on the mask).

.. note::

   If your photo is a locked **Background** layer, click the lock icon first to turn it into a normal layer.
   Masks cannot be added to a locked Background layer.

Method 2: Remove background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Select the layer.
#. Click **Remove background** in the **Contextual Task Bar**, or in the **Properties** panel under
   **Quick Actions**.
#. Photoshop finds the subject and adds a mask that hides the background automatically.

Painting on a mask
~~~~~~~~~~~~~~~~~~~

#. **Click the mask thumbnail** in the Layers panel (a white border shows it is selected). If you forget this
   step, you will paint on the image instead!
#. Choose the **Brush tool** (B).
#. Press **D** to set the default colours (black and white).
#. Press **X** to swap between black and white.
#. Paint **black** to hide more. Paint **white** to bring parts back.
#. Use a **soft brush** for gentle edges and a **hard brush** for sharp edges. Change the size with the
   **[** and **]** keys.

Handy mask tricks
~~~~~~~~~~~~~~~~~~

* **Shift + click** the mask thumbnail to turn the mask off and on.
* **Alt + click** the mask thumbnail to see the mask itself in black and white.
* **Select → Select and Mask** (or double-click the mask) to refine edges such as hair.

Worked example: removing a background with a mask
--------------------------------------------------

**Goal:** Cut out a photo of a pot plant for an AR "classroom makeover" scene, with clean edges.

#. Open ``pot_plant.jpg``. Click the lock on the **Background** layer to unlock it and rename it ``plant``.
#. Click **Remove background** in the Contextual Task Bar. The background disappears and a mask is added.
#. Zoom in. One leaf tip is missing and a bit of the table is still showing.
#. Click the **mask thumbnail**. Choose the **Brush** (B), soft edge, small size.
#. Press **X** until **white** is the foreground colour, and paint over the missing leaf tip to bring it back.
#. Press **X** to swap to **black** and paint over the bit of table to hide it.
#. **Alt + click** the mask to check it. White is the plant, black is hidden. Alt + click again to go back.
#. Save as ``pot_plant.psd``. The original photo pixels are still there if you need them.

Activities
-----------

Activity 1: White reveals, black conceals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Visible, Hidden, Partly see-through
   :delimiter: =>
   :instructions: What happens to the layer where the mask is painted this colour?

   White on the mask => Visible
   Black on the mask => Hidden
   50% grey on the mask => Partly see-through
   Light grey on the mask => Partly see-through
   An area that was selected when you clicked Add layer mask => Visible
   An area outside the selection when you clicked Add layer mask => Hidden

Activity 2: Masks vs Eraser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::

   A layer mask @@hides@@ pixels instead of deleting them.
   The Eraser tool @@deletes@@ pixels.
   Editing that can always be undone is called @@non-destructive@@ editing.
   Paint @@white@@ on a mask to bring parts back.
   Paint @@black@@ on a mask to hide parts.
   Press @@X@@ to swap the foreground and background colours.

Activity 3: Order the steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ordering::
   :no-indent:

   Select the object you want to keep.
   Click the Add layer mask button.
   Click the mask thumbnail so it is selected.
   Choose the Brush tool and press D for black and white.
   Paint black to hide extra background.
   Paint white to bring back any missing parts.

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Ella paints black on her layer but it makes a black mark on her photo instead of hiding it. Why?

      [x] She had the layer thumbnail selected, not the mask thumbnail | Correct. Click the mask thumbnail first.
      [ ] The brush is too big | Size would not change the colour result.
      [ ] Masks only work on text | Masks work on any layer.
      [ ] She needs to paint white | White would make a white mark on the image.

   .. multichoice::

      Why are masks called non-destructive?

      [ ] They make the file smaller | Not the reason.
      [x] The hidden pixels are still there and can be brought back | Correct.
      [ ] They cannot be deleted | Masks can be deleted.
      [ ] They only work once | You can edit masks as often as you like.

   .. multichoice::

      Which button adds a layer mask?

      [ ] fx | fx adds layer styles.
      [ ] The bin | The bin deletes layers.
      [x] The rectangle with a circle | Correct.
      [ ] The folder | The folder makes a group.

Activity 5: Practical task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose **two** photos you have taken. For each:

#. Remove the background using a layer mask (Method 1 or Method 2).
#. Fix at least one mistake by painting on the mask with black **and** with white.
#. Take a screenshot showing the mask thumbnail in the Layers panel.

Challenge: fade effect
-----------------------

Masks can make smooth fades. Put two photos on separate layers. Add a mask to the top layer, choose the
**Gradient tool** (G) with black-to-white, and drag across the mask. The top photo fades into the bottom one.
Use this to make a "portal" or "magic window" image for an AR scene.

Exam-style question
--------------------

.. structuredquestion:: Layer masks
   :total-marks: 5
   :category: Photoshop

   .. stimulus::

      Noah used the Eraser tool to remove the background from a photo of his dog. After saving and closing the
      file, he notices he accidentally erased the tip of the dog's ear.

   .. subquestion:: a) Explain why Noah cannot easily fix his mistake.
      :marks: 2

      .. model-answer::

         The Eraser tool deletes pixels permanently (destructive editing). Once the file was saved and closed, the
         erased part of the ear is gone and cannot be brought back without redrawing it.

      .. marking-guidance::

         * 1 mark for saying the Eraser deletes pixels or is destructive.
         * 1 mark for explaining it cannot be undone after saving and closing.

   .. subquestion:: b) Describe how using a layer mask would have let Noah fix the mistake.
      :marks: 2

      .. model-answer::

         A layer mask only hides the background, so the pixels are still there. Noah could click the mask
         thumbnail and paint white over the ear tip to reveal it again.

      .. marking-guidance::

         * 1 mark for the mask hiding (not deleting) pixels.
         * 1 mark for painting white on the mask to reveal the ear.

   .. subquestion:: c) State the rule for painting on a layer mask.
      :marks: 1

      .. model-answer::

         White reveals, black conceals.

      .. marking-guidance::

         1 mark for the correct rule.
