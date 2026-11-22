====================================
2. Hardware and software
====================================

Learning intentions
--------------------

* I can explain the difference between hardware and software.
* I can name the main parts of a computer and describe what each part does.
* I can explain how hardware and software work together to control and protect data.

Success criteria
~~~~~~~~~~~~~~~~~

* I can sort devices into input, output, processing, storage and communication hardware.
* I can explain the difference between system software and application software.
* I can describe two ways hardware and software keep data secure.

Hardware
---------

**Hardware** is the physical parts of a computer: the parts you can touch.

Every computer follows the same basic pattern, called the **input → process → output** model,
with **storage** to keep data for later.

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Type
     - What it does
     - Examples
   * - Input
     - Gets data **into** the computer
     - Keyboard, mouse, touchscreen, microphone, camera, game controller, sensor
   * - Processing
     - **Works on** the data by following instructions
     - CPU (central processing unit), GPU (graphics processing unit)
   * - Memory
     - Holds the data and programs being used **right now**
     - RAM (random access memory)
   * - Storage
     - **Keeps** data even when the power is off
     - SSD (solid state drive), hard disk drive, USB flash drive, SD card
   * - Output
     - Gets results **out** of the computer
     - Screen, speakers, headphones, printer, vibration motor
   * - Communication
     - **Sends and receives** data to and from other computers
     - Wi-Fi card, network cable port, Bluetooth chip, router

Key parts in more detail
~~~~~~~~~~~~~~~~~~~~~~~~~

**CPU (central processing unit):** The "brain" of the computer. It carries out instructions,
billions every second. Its speed is measured in **gigahertz (GHz)**.

**RAM (random access memory):** Fast, short-term memory. It holds the programs and files you have
open. RAM is **volatile**, which means it is wiped when the power goes off. More RAM lets you
run more programs at once.

**Storage (SSD or hard drive):** Long-term memory. It keeps your files, apps and operating
system even when the computer is off. Storage is **non-volatile**.

**Motherboard:** The main circuit board that connects all the parts together.

.. admonition:: RAM vs storage: a desk and a filing cabinet
   :class: tip

   Think of **storage** as a filing cabinet where you keep everything. **RAM** is your desk. When you
   want to work on something, you take it out of the cabinet and put it on your desk. A bigger desk
   (more RAM) lets you work on more things at once. When you go home (power off), the desk is cleared,
   but everything you saved is still in the cabinet.

Units of storage
~~~~~~~~~~~~~~~~~

Computers store everything as **binary**: 1s and 0s.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Unit
     - Size
   * - bit
     - a single 1 or 0
   * - byte (B)
     - 8 bits (about one letter of text)
   * - kilobyte (KB)
     - about 1000 bytes (a short email)
   * - megabyte (MB)
     - about 1000 KB (a photo or a song)
   * - gigabyte (GB)
     - about 1000 MB (a movie)
   * - terabyte (TB)
     - about 1000 GB (a large hard drive)

Software
---------

**Software** is the programs that run on the hardware. You cannot touch software. It is a set of
instructions stored as data.

There are two main types.

**System software** runs the computer itself.

* The **operating system (OS)** manages the hardware, files and other programs. Examples: Windows,
  macOS, iOS, Android, Linux.
* **Utility software** looks after the computer. Examples: antivirus, backup tools, disk cleanup.
* **Drivers** let the operating system talk to a piece of hardware, such as a printer.

**Application software (apps)** helps the user do a task.

* Examples: Microsoft Word, Photoshop, a web browser, Minecraft, Spotify, Python's IDLE editor.

Worked example: printing an essay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. You click **Print** in Word. *(application software, input from the mouse)*
#. Word asks the operating system to print. *(system software)*
#. The operating system uses the **printer driver** to turn the essay into instructions the printer
   understands. *(system software)*
#. The data travels over Wi-Fi to the printer. *(communication hardware)*
#. The printer puts ink on paper. *(output hardware)*

Hardware and software protecting data
--------------------------------------

Hardware and software also **control who can get to data** and **keep it safe**. This is a big part
of cybersecurity.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Protection
     - How it works
   * - Login and passcodes
     - The operating system only lets in people who know the password, PIN or passphrase.
   * - Biometrics
     - Hardware such as a fingerprint reader or face camera checks that it is really you.
   * - User permissions
     - The OS decides which users can open, change or delete each file. A student account cannot
       change the school's system settings.
   * - Encryption
     - Software scrambles data so only someone with the right key can read it. Your phone's storage
       and websites starting with ``https`` use encryption.
   * - Firewall
     - Hardware or software that checks data coming into or out of a network and blocks anything
       that is not allowed.
   * - Antivirus
     - Utility software that scans for and removes malware.
   * - Updates
     - Software updates fix security holes that attackers could use.
   * - Backups
     - Copies of data on another drive or in the cloud, so data can be recovered if it is lost,
       stolen or locked by ransomware.

Activities
-----------

Activity 1: Sort the hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Input, Processing, Storage, Output, Communication
   :instructions: Sort each piece of hardware into its main job.

   Keyboard : Input
   Microphone : Input
   Touchscreen sensor : Input
   CPU : Processing
   GPU : Processing
   SSD : Storage
   USB flash drive : Storage
   Speakers : Output
   Printer : Output
   Wi-Fi card : Communication
   Router : Communication

Activity 2: Hardware or software?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Hardware, System software, Application software

   Motherboard : Hardware
   RAM : Hardware
   Fingerprint reader : Hardware
   Windows 11 : System software
   Android : System software
   Printer driver : System software
   Antivirus program : System software
   Photoshop : Application software
   Web browser : Application software
   Minecraft : Application software

Activity 3: Fill in the gaps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
   :instructions: Drag the words into the gaps.

   The @@CPU@@ carries out the instructions in a program.
   @@RAM@@ holds the programs that are open right now.
   RAM is @@volatile@@, so it is wiped when the power is off.
   An @@SSD@@ keeps files even when the computer is off.
   The @@operating@@ system manages the hardware and files.
   A @@firewall@@ blocks data that is not allowed on a network.
   @@Encryption@@ scrambles data so only people with the key can read it.

Activity 4: Quick quiz
~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Which part of a computer is often called its "brain"?

      [x] CPU | Correct. The CPU carries out the instructions.
      [ ] RAM | RAM is short-term memory, more like a desk.
      [ ] SSD | An SSD is long-term storage.
      [ ] Monitor | A monitor is an output device.

   .. multichoice::

      Why does a computer lose unsaved work when the power goes off?

      [ ] The CPU deletes it | The CPU processes data. It does not delete files when the power goes off.
      [x] RAM is volatile | Correct. Data in RAM is lost without power.
      [ ] Storage is volatile | Storage is non-volatile. It keeps data without power.
      [ ] The operating system crashes | The real reason is that RAM needs power to hold data.

   .. multichoice::

      Which is an example of **system** software?

      [ ] Spotify | Spotify is application software.
      [ ] PowerPoint | PowerPoint is application software.
      [x] macOS | Correct. macOS is an operating system.
      [ ] Roblox | Roblox is application software.

   .. multichoice::

      Which TWO of these use hardware or software to control who can get to data?

      [x] A fingerprint reader on a laptop | Correct. Biometric hardware checks who you are.
      [x] File permissions set by the operating system | Correct. Permissions control who can open or change files.
      [ ] A larger computer screen | A screen is output hardware.
      [ ] Faster RAM | Faster RAM improves speed, not security.

Challenge: spec check
----------------------

Find the specifications for two laptops on a shop's website (for example, a cheap laptop and a
gaming laptop). Copy the table below into your notes and fill it in.

.. list-table::
   :header-rows: 1

   * - Part
     - Laptop 1
     - Laptop 2
   * - CPU (name and GHz)
     -
     -
   * - RAM (GB)
     -
     -
   * - Storage (type and GB/TB)
     -
     -
   * - Screen size
     -
     -
   * - Operating system
     -
     -
   * - Price
     -
     -

Which laptop would you choose for school? Explain your answer using at least **two** specifications.

Exam-style question
--------------------

.. structuredquestion:: Hardware, software and security
   :total-marks: 7
   :category: Hardware and software

   .. stimulus::

      Mia's school laptop has an 8-core CPU, 16 GB of RAM and a 512 GB SSD. It runs Windows 11 and
      has a fingerprint reader. Mia uses it to edit photos in Photoshop and to submit work on the
      school portal.

   .. subquestion:: a) Identify one piece of hardware and one piece of software in the stimulus.
      :marks: 2

      .. model-answer::

         Hardware: CPU, RAM, SSD or fingerprint reader. Software: Windows 11, Photoshop or the
         school portal (web app).

      .. marking-guidance::

         * 1 mark for a correct piece of hardware.
         * 1 mark for a correct piece of software.

   .. subquestion:: b) Explain the difference between RAM and the SSD.
      :marks: 2

      .. model-answer::

         RAM is short-term memory that holds the programs and files Mia has open now. It is volatile,
         so it loses its data when the power is off. The SSD is long-term storage that keeps Mia's
         files and apps even when the laptop is turned off.

      .. marking-guidance::

         * 1 mark for describing RAM as short-term or volatile memory for open programs.
         * 1 mark for describing the SSD as long-term or non-volatile storage.

   .. subquestion:: c) Is Windows 11 system software or application software? Justify your answer.
      :marks: 1

      .. model-answer::

         System software, because it is an operating system that manages the hardware, files and
         other programs.

      .. marking-guidance::

         1 mark for "system software" with a reason (it is the operating system or it manages the
         hardware).

   .. subquestion:: d) Describe two ways hardware or software on Mia's laptop could stop someone else from accessing her files.
      :marks: 2

      .. model-answer::

         * The fingerprint reader (hardware) checks it is really Mia before unlocking the laptop.
         * Windows (software) needs a password or PIN to log in, and file permissions stop other
           users opening her files. Encryption could also scramble her files so they cannot be read
           without her key.

      .. marking-guidance::

         * 1 mark for each correct method with a short explanation (maximum 2).
         * Accept: biometrics, password or PIN login, user permissions, encryption.
