==============================================
Revision: virtual and augmented reality
==============================================

Learning intentions
--------------------

* I can recall the key words and skills from the AR and VR topic.
* I can check that I am ready to complete my AR project.

Summary
--------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Lesson
     - Key ideas
   * - :doc:`arvr_01_ar_vs_vr`
     - VR replaces the real world. AR adds digital content to it. MR lets digital objects interact with the real
       world. Marker-based and markerless AR.
   * - :doc:`arvr_02_photoshop_basics`
     - New document settings (size, 72 ppi, RGB, transparent). PSD keeps layers. Type tool and fonts.
   * - :doc:`arvr_03_selection_tools`
     - Marquee, Lasso, Object Selection, Quick Selection, Magic Wand. Shift adds, Alt subtracts. Ctrl + J copies to
       a new layer.
   * - :doc:`arvr_04_layers`
     - Layer order, naming, groups, opacity, layer styles.
   * - :doc:`arvr_05_masks`
     - White reveals, black conceals. Masks are non-destructive.
   * - :doc:`arvr_06_exporting_pngs`
     - PNG keeps transparency. Quick Export, Export As, Layers to Files.
   * - :doc:`arvr_07_assemblr_basics`
     - Upload PNGs, arrange in 3D (X, Y, Z), scenes, preview.
   * - :doc:`arvr_08_assemblr_interactivity`
     - Trigger and target. Move, Rotate, Scale, Animation, Visibility, Jump Up, Media. Publish with a marker.
   * - :doc:`arvr_09_designing_ux`
     - UI and UX. Stakeholders, functional and non-functional requirements, storyboards, prototypes, testing.

Flashcards
-----------

.. flashcards:: AR, VR and Photoshop
   :new-per-session: 15
   :shuffle:

   # AR and VR
   Virtual reality | A completely computer-made world that replaces the real world, usually viewed in a headset
   Augmented reality | Digital content added on top of the real world, usually viewed on a phone or tablet
   Mixed reality | Digital objects that interact with the real world, such as bouncing off a real table
   Extended reality (XR) | The umbrella term for AR, MR and VR
   Marker | An image an AR app recognises to know where to place content
   Markerless AR | AR placed on real surfaces without a marker
   Immersion | The feeling of being inside a digital experience
   # Photoshop
   PSD | Photoshop's working file format that keeps layers
   PNG | A flat image format that keeps transparency
   Selection | An area of an image chosen to work on, shown by marching ants
   Ctrl + J | Copies a selection onto a new layer
   Shift while selecting | Adds to a selection
   Alt while selecting | Subtracts from a selection
   Layer | A separate sheet of a design that can be edited on its own
   Layer mask | A black and white stencil that hides parts of a layer without deleting them
   White reveals, black conceals | The rule for painting on a layer mask
   Non-destructive editing | Editing that can be changed later because the original pixels are kept
   Layers to Files | Exports every layer as its own file
   # Assemblr
   Trigger object | The object the user taps to start an action
   Target object | The object that reacts to the action
   Visibility | Interactivity that hides or shows an object
   Jump Up | Interactivity that switches scene or opens a website
   Scene | Like a slide: a separate set of objects in a project
   # Design
   User interface (UI) | What the user sees and touches
   User experience (UX) | How the user feels when using a product
   Functional requirement | What the solution must do
   Non-functional requirement | How well the solution works, such as ease of use or speed
   Prototype | An early, simple version used for testing
   Storyboard | A series of sketches showing each step of the experience

Crossword
----------

.. crossword:: AR and Photoshop
   :hints: 3

   AUGMENTED   | AR stands for ____ reality
   VIRTUAL     | VR stands for ____ reality
   HEADSET     | Worn over the eyes for VR
   MARKER      | Image that tells an AR app where to place content
   SELECTION   | An area shown by marching ants
   LAYER       | A separate sheet in a Photoshop design
   MASK        | Hides part of a layer without deleting it
   TRANSPARENT | A PNG can have a ____ background
   EXPORT      | Save a copy in another format, such as PNG
   TRIGGER     | The object that is tapped to start an action
   TARGET      | The object that reacts to an action
   PROTOTYPE   | An early version used for testing
   STORYBOARD  | Sketches showing each step of an experience
   SCENE       | Like a slide in an Assemblr project

Word search
------------

.. wordsearch:: Photoshop and AR tools
   :directions: medium
   :answers: print

   MARQUEE
   LASSO
   MAGIC WAND
   QUICK SELECTION
   LAYER MASK
   OPACITY
   PNG
   PSD
   ROTATE
   SCALE
   VISIBILITY
   ASSEMBLR

Practice questions
-------------------

.. mcqgroup::
   :shuffle-questions:

   .. multichoice::

      A Pokémon appears on the footpath through your phone's camera. This is:

      [x] augmented reality | Correct. Digital content is added to the real world.
      [ ] virtual reality | VR replaces the real world.
      [ ] a PSD file | Not related.
      [ ] a layer mask | Not related.

   .. multichoice::

      Which selection tool is best for selecting a plain blue sky?

      [ ] Rectangular Marquee | The sky is rarely a perfect rectangle.
      [x] Magic Wand | Correct. It selects areas of similar colour.
      [ ] Polygonal Lasso | Better for straight-edged objects.
      [ ] Type tool | Not a selection tool.

   .. multichoice::

      On a layer mask, painting black will:

      [ ] delete the pixels | Masks never delete pixels.
      [x] hide that part of the layer | Correct. Black conceals.
      [ ] make that part brighter | Not what masks do.
      [ ] add a new layer | Not what masks do.

   .. multichoice::

      Which file should you upload to Assemblr for a cut-out character?

      [ ] character.psd | Assemblr does not accept PSD.
      [ ] character.jpg with a white background | It would show a white box.
      [x] character.png with a transparent background | Correct.
      [ ] character.docx | Not an image.

   .. multichoice::

      A user taps a button and the scene changes. Which interactivity type is this?

      [ ] Scale | Scale changes size.
      [ ] Visibility | Visibility hides or shows.
      [x] Jump Up (Switch Scene) | Correct.
      [ ] Rotate | Rotate turns an object.

   .. multichoice::

      "The project must load in under 10 seconds" is a:

      [ ] functional requirement | It is about how well it works, not what it does.
      [x] non-functional requirement | Correct. It is about speed (a quality).
      [ ] storyboard | A storyboard is sketches.
      [ ] marker | Not related.

Exam-style question
--------------------

.. structuredquestion:: From Photoshop to AR
   :total-marks: 6
   :category: Revision

   .. stimulus::

      Olivia photographs her pet rabbit on a green rug. She wants the rabbit to appear in AR on the table and jump
      when tapped.

   .. subquestion:: a) Describe how Olivia should prepare the rabbit image in Photoshop.
      :marks: 3

      .. model-answer::

         #. Select the rabbit (for example, Select → Subject or the Object Selection tool) and fix the edges with
            Shift and Alt.
         #. Add a layer mask so the green rug is hidden (or copy the rabbit to a new layer with Ctrl + J), and name
            the layer ``rabbit``.
         #. Export the rabbit layer as a PNG with transparency (Quick Export as PNG).

      .. marking-guidance::

         * 1 mark for a suitable selection method.
         * 1 mark for isolating the rabbit with a mask or new layer.
         * 1 mark for exporting as PNG with transparency.

   .. subquestion:: b) Describe how Olivia could make the rabbit jump in Assemblr.
      :marks: 2

      .. model-answer::

         Click the rabbit (trigger) and add a Move interactivity upwards with the rabbit as the target, then a second
         Move action downwards that starts when the first one finishes.

      .. marking-guidance::

         * 1 mark for using Move with the rabbit as trigger and target.
         * 1 mark for a second action or timing so it comes back down.

   .. subquestion:: c) Should Olivia use marker-based or markerless AR to put the rabbit on any table? Explain.
      :marks: 1

      .. model-answer::

         Markerless AR (around the real environment), because it can place the rabbit on any flat surface without
         needing a printed marker. (Accept marker-based if explained, for example so the rabbit always appears in
         the same place.)

      .. marking-guidance::

         1 mark for a choice with a valid reason.
