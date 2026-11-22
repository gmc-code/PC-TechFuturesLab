=============================================
6. Exporting PNGs from Photoshop
=============================================

Learning intentions
--------------------

* I can explain why PNG is the best format for AR images.
* I can use Quick Export to save a layer or a whole image as a PNG.
* I can export all my layers as separate PNG files ready for Assemblr Studio.

Success criteria
~~~~~~~~~~~~~~~~~

* I can export a single layer with **Quick Export as PNG**.
* I can use **Export As** to choose the size of the PNG.
* I can use **Export → Layers to Files** to export every layer as its own PNG, with transparency.

Why PNG?
---------

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Format
     - Transparency?
     - Use it for
   * - PSD
     - Yes
     - Your **working file** in Photoshop. Assemblr cannot use PSD files.
   * - PNG
     - **Yes**
     - **AR assets**: characters, objects, buttons, signs and labels with see-through backgrounds
   * - JPEG
     - No
     - Photos that fill a rectangle, such as a backdrop or a poster

Assemblr Studio accepts **JPG, JPEG and PNG** images. A PNG keeps the transparent areas, so your cut-out
object looks like it is really in the room, not stuck on a white or black box.

Before you export: checklist
-----------------------------

* Each asset is on its **own layer** (or group).
* Each layer has a **clear name** with no spaces, for example ``robot_arm``. The layer name becomes the file name.
* Backgrounds are **hidden** (eye off) or removed with masks, so you can see the **checkerboard**.
* Nothing important is hanging off the edge of the canvas.
* You have saved your **PSD** first.

Three ways to export
---------------------

Method 1: Quick Export as PNG (one layer)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In the Layers panel, **right-click** the layer (or group).
#. Choose **Quick Export as PNG**.
#. Choose where to save it. The file uses the layer name.

Quick Export only exports the layer's own pixels, trimmed to the object, which is usually exactly what you
want for AR.

To export the **whole visible image**, use **File → Export → Quick Export as PNG**.

Method 2: Export As (choose the size)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Right-click the layer and choose **Export As** (or **File → Export → Export As** for the whole image).
#. Set **Format** to **PNG** and make sure **Transparency** is ticked.
#. Check the **Image Size**. Around 1000–2000 pixels wide is plenty for AR. Very large images make your AR
   project slow to load.
#. Click **Export** and choose a folder.

You can select several layers first, then right-click and choose **Export As** to export them all at once.

Method 3: Export layers to files (every layer)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Choose **File → Export → Layers to Files**.
#. Choose a **Destination** folder, for example ``ar_assets``.
#. Set **File Type** to **PNG-24**.
#. Tick **Transparency** and **Trim Layers** (this crops each PNG to the edge of the object).
#. Tick **Visible Layers Only** if you only want the layers that are turned on.
#. Click **Run**. Photoshop makes one PNG for each layer.

.. note::

   Layers to Files may add a prefix (such as ``robot_0000_``) to the start of each file name. You can type a
   shorter prefix in the **File Name Prefix** box or rename the files afterwards.

Worked example: exporting the robot assets
-------------------------------------------

The PSD ``robot_layers.psd`` from :doc:`arvr_04_layers` has these layers:
``robot_body``, ``robot_arm``, ``robot_eyes``, ``label_robot`` and ``background``.

#. Hide the ``background`` layer.
#. Save the PSD.
#. **File → Export → Layers to Files**: destination ``ar_assets``, PNG-24, Transparency ✓, Trim Layers ✓,
   Visible Layers Only ✓.
#. Click **Run**.
#. Open the ``ar_assets`` folder. There are four PNG files. Open each in a viewer to check that the
   background is see-through.
#. Upload these four PNGs to Assemblr Studio in :doc:`arvr_07_assemblr_basics`.

Organising your project folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   AR_Project_YourName/
   ├── psd/
   │   ├── robot_layers.psd
   │   └── title.psd
   ├── ar_assets/
   │   ├── robot_body.png
   │   ├── robot_arm.png
   │   ├── robot_eyes.png
   │   ├── label_robot.png
   │   └── title.png
   └── planning/
       └── storyboard.pdf

Activities
-----------

Activity 1: Which format?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: PSD, PNG, JPEG
   :delimiter: =>
   :instructions: Choose the best file format for each job.

   Saving your work so you can edit the layers next lesson => PSD
   A cut-out cartoon character to float in an AR scene => PNG
   A round "Tap me!" button for an AR experience => PNG
   A text label with a transparent background => PNG
   A full rectangular photo of a beach for a backdrop => JPEG
   A holiday photo to email to a relative => JPEG

Activity 2: Export settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. gapfill::

   To export one layer quickly, right-click it and choose @@Quick Export as PNG|Save As|Merge Layers@@.
   To export every layer as a separate file, use File → Export → @@Layers to Files|Quick Export|Artboards@@.
   In Layers to Files, choose @@PNG-24|JPEG|PSD@@ as the file type.
   Tick @@Trim Layers|Merge Layers|Flatten Image@@ to crop each PNG to the edge of the object.
   The @@layer name|font name|folder colour@@ becomes the file name when you export.

Activity 3: Order the workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ordering::
   :no-indent:

   Cut out each object and put it on its own layer.
   Give each layer a clear name with no spaces.
   Hide the background layer.
   Save the PSD file.
   Choose File → Export → Layers to Files.
   Set PNG-24 with Transparency and Trim Layers ticked.
   Click Run and check the PNGs in the folder.
   Upload the PNGs to Assemblr Studio.

Activity 4: Practical task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Export the layers from your character PSD (from :doc:`arvr_04_layers`) as PNG files into an
``ar_assets`` folder. Open each PNG to check it has a transparent background and a sensible file name.
Fix any problems in the PSD and export again.

Challenge
----------

Compare file sizes. Export the same layer as a PNG at 3000 px wide, 1500 px wide and 500 px wide. Record
the file size of each (right-click → Properties on Windows, or Get Info on a Mac). Then view each in
Assemblr on a tablet. What is the smallest size that still looks sharp? Why does file size matter for AR?

Exam-style question
--------------------

.. structuredquestion:: Preparing images for AR
   :total-marks: 5
   :category: Photoshop

   .. stimulus::

      Zara has a PSD with eight layers for her AR project: a background photo, a dragon, the dragon's wings,
      three gems and two text labels. Her layers are called "Layer 1" to "Layer 8".

   .. subquestion:: a) Explain why Zara should rename her layers before exporting.
      :marks: 2

      .. model-answer::

         The layer names become the file names when she exports. Names like "Layer 4" will make it hard to tell
         which PNG is which when she uploads them to Assemblr, so she should use names like ``dragon_wings``.

      .. marking-guidance::

         * 1 mark for saying layer names become file names.
         * 1 mark for explaining that clear names make the files easy to find and use.

   .. subquestion:: b) Describe the steps Zara should use to export all the layers (except the background) as separate transparent images.
      :marks: 3

      .. model-answer::

         #. Hide the background layer and save the PSD.
         #. Choose File → Export → Layers to Files.
         #. Set the file type to PNG-24, tick Transparency, Trim Layers and Visible Layers Only, choose a
            folder and click Run.

      .. marking-guidance::

         * 1 mark for hiding the background (or Visible Layers Only).
         * 1 mark for using Layers to Files (or Export As with all layers selected).
         * 1 mark for PNG with transparency.
