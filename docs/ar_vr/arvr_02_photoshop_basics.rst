=============================================
2. Photoshop basics: documents and text
=============================================

Learning intentions
--------------------

* I can create, set up and save a Photoshop document.
* I can find my way around the Photoshop workspace.
* I can add and format text using fonts.

Success criteria
~~~~~~~~~~~~~~~~~

* I can create a new document with the right size, resolution and background for an AR project.
* I can save my work as a PSD file and explain why PSD keeps my layers.
* I can add text, change the font, size and colour, and move it into place.

Why Photoshop for AR?
----------------------

In your AR project you will design the **images** (called **assets**) that appear in the AR scene, such as
characters, signs, buttons and labels. Photoshop lets you cut out objects, remove backgrounds and save
each part as a separate **PNG** image with a **transparent** background. Transparent images look like
real objects floating in the AR scene instead of rectangles.

The Photoshop workspace
------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Part
     - What it does
   * - Menu bar
     - Menus such as **File**, **Edit**, **Image**, **Layer**, **Select** and **Window** along the top
   * - Options bar
     - Settings for the tool you have selected (for example, brush size)
   * - Toolbar
     - The tools down the left side (Move, selection tools, Brush, Eraser, Type and more)
   * - Canvas
     - Your image in the middle of the screen
   * - Panels
     - Boxes on the right, such as **Layers**, **Properties** and **Character**. Open any panel from the
       **Window** menu.
   * - Contextual Task Bar
     - A floating bar that suggests next steps, such as **Select subject** or **Remove background**

.. tip::

   If your panels go missing or move around, choose **Window → Workspace → Reset Essentials**.

Useful shortcuts
~~~~~~~~~~~~~~~~~

On a Mac, use **Cmd** instead of **Ctrl** and **Option** instead of **Alt**.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Shortcut
     - Action
   * - Ctrl + Z
     - Undo (press again to undo more steps)
   * - Ctrl + S
     - Save
   * - Ctrl + + / Ctrl + −
     - Zoom in / zoom out
   * - Spacebar (hold) + drag
     - Move around the canvas (Hand tool)
   * - V
     - Move tool
   * - T
     - Type tool
   * - B
     - Brush tool
   * - Ctrl + T
     - Free Transform (resize and rotate)

Creating a new document
------------------------

#. Choose **File → New** (Ctrl + N).
#. Set the options:

   * **Width and height:** For AR assets, **1080 × 1080 pixels** (square) is a good size. A large poster
     background could be 1920 × 1080.
   * **Resolution:** **72 pixels/inch** is fine for screens. (Use 300 for printing.)
   * **Colour mode:** **RGB Colour**, 8 bit. Screens use red, green and blue light.
   * **Background contents:** **Transparent** for objects you will cut out and place in AR.

#. Give it a name, such as ``robot_assets``, and click **Create**.

Saving your work
-----------------

* **File → Save As** and choose **Photoshop (.PSD)**. A PSD file keeps all your **layers** so you can edit
  them later. This is your **working file**.
* A **PNG** (.png) file is a flat image that can keep **transparency**. You will export PNGs for Assemblr
  later (see :doc:`arvr_06_exporting_pngs`).
* A **JPEG** (.jpg) is a flat image with **no** transparency. It is good for photos but not for cut-out
  objects.

.. admonition:: Save often, save smart
   :class: tip

   Save your PSD every 10 minutes. Use clear file names with no spaces, for example
   ``ar_project_robot_v2.psd``. Keep everything for your project in one folder.

Adding text
------------

Text in Photoshop goes on its own **type layer**, which means you can edit it at any time.

#. Choose the **Type tool** (**T**) in the toolbar.
#. Click on the canvas and type. (Click and drag first to make a text box for paragraphs.)
#. Highlight the text and change the settings in the **Options bar** or the **Character** panel
   (**Window → Character**):

   * **Font family**, such as Arial, Montserrat or a decorative font
   * **Font style**: Regular, Bold or Italic
   * **Size** in points (pt)
   * **Colour**: click the colour box
   * **Tracking**: the space between letters
   * **Leading**: the space between lines

#. Click the **tick** in the Options bar (or press **Ctrl + Enter**) to finish.
#. Use the **Move tool** (**V**) to drag the text into place.

Text design tips for AR
~~~~~~~~~~~~~~~~~~~~~~~~

* AR text is viewed on a phone or tablet, often from a distance, so make it **big and bold**.
* Use **high contrast**: dark text on a light shape, or light text on a dark shape.
* Use no more than **two fonts** in a project: one for headings, one for labels.
* Add a **stroke** or **shadow** (**Layer → Layer Style**) so text stands out against any background.
* Only use fonts you are allowed to use. Fonts in Photoshop and Adobe Fonts are licensed for school work.

Worked example: an AR name sign
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **File → New**: 1080 × 540 px, 72 ppi, RGB, transparent background. Name: ``welcome_sign``.
#. Use the **Rounded Rectangle** (Rectangle tool with rounded corners) to draw a dark blue sign shape.
#. Choose the **Type tool**, click on the sign and type **WELCOME TO THE LAB**.
#. Set the font to a bold sans-serif font, 90 pt, white.
#. **Layer → Layer Style → Drop Shadow** to make the sign look 3D.
#. **File → Save As** ``welcome_sign.psd``.

Activities
-----------

Activity 1: Document settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   For AR images that will be cut out, set the background contents to @@Transparent|White|Black@@.
   Screens use the @@RGB|CMYK|Greyscale@@ colour mode.
   A resolution of @@72|300|5@@ pixels per inch is fine for images on screens.
   Save your working file as a @@PSD|JPEG|GIF@@ so you keep your layers.
   A @@PNG|JPEG|BMP@@ file is a flat image that can keep transparency.

Activity 2: File types
~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: PSD, PNG, JPEG
   :delimiter: =>

   Keeps all layers so you can edit later => PSD
   Photoshop's own working file => PSD
   Flat image that can have a transparent background => PNG
   Best choice for a cut-out character to use in Assemblr => PNG
   Flat image with no transparency, good for photos => JPEG
   Usually a smaller file for photographs from a camera => JPEG

Activity 3: Order the steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Put the steps for adding text into the correct order.

.. ordering::
   :no-indent:

   Choose the Type tool from the toolbar.
   Click on the canvas.
   Type your text.
   Highlight the text and change the font, size and colour.
   Click the tick to finish editing.
   Use the Move tool to drag the text into place.

Activity 4: Practical task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a **title graphic** for an AR experience about a topic of your choice (for example, "Welcome to
the Reef" or "Meet the Planets").

* Size 1080 × 540 px, transparent background
* At least one shape behind the text
* A heading in one font and a smaller sub-heading in a second font
* A layer style (stroke or drop shadow) on the heading
* Saved as ``title_yourname.psd``

Challenge
----------

Search **Adobe Fonts** (Photoshop: **Type → More from Adobe Fonts**) for a font that suits your AR
topic. Make three versions of your title graphic with different fonts and colours, then ask two classmates
which is easiest to read on a phone from one metre away. Write one sentence about what you learned.

Exam-style question
--------------------

.. structuredquestion:: Setting up a Photoshop document
   :total-marks: 5
   :category: Photoshop

   .. stimulus::

      Kai is designing a cartoon robot that will appear floating in an AR scene. He creates a new Photoshop
      document that is 1080 × 1080 pixels with a white background, draws the robot, and saves it only as a
      JPEG.

   .. subquestion:: a) Explain the problem with Kai's white background and JPEG format when the robot is shown in AR.
      :marks: 2

      .. model-answer::

         A JPEG cannot store transparency, and the background is white, so the robot will appear inside a
         white square in the AR scene instead of looking like it is floating in the real world.

      .. marking-guidance::

         * 1 mark for identifying that JPEG has no transparency (or the background is white).
         * 1 mark for the effect: a white box appears around the robot.

   .. subquestion:: b) Describe the settings and file types Kai should use instead.
      :marks: 2

      .. model-answer::

         He should set the background contents to transparent and save his working file as a PSD to keep the
         layers. Then he should export the robot as a PNG, which keeps transparency.

      .. marking-guidance::

         * 1 mark for a transparent background.
         * 1 mark for PSD as the working file and PNG for export.

   .. subquestion:: c) Give one tip for making text easy to read in AR.
      :marks: 1

      .. model-answer::

         Use large, bold text with high contrast (for example, white text with a dark stroke).

      .. marking-guidance::

         1 mark for any valid readability tip (size, contrast, few fonts, stroke or shadow).
