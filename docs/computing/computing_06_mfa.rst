====================================
6. Multi-factor authentication
====================================

Learning intentions
--------------------

* I can explain what authentication is.
* I can describe the three types of authentication factors.
* I can explain why multi-factor authentication (MFA) makes accounts much harder to break into.

Success criteria
~~~~~~~~~~~~~~~~~

* I can sort examples into something you know, something you have and something you are.
* I can explain why two passwords is **not** multi-factor authentication.
* I can describe how to turn on MFA and what to do with backup codes.

What is authentication?
------------------------

**Authentication** means proving you are who you say you are. When you log in, the system checks your
**authentication factors**.

There are three types of factor:

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Factor
     - Meaning
     - Examples
   * - Something you **know**
     - A secret in your head
     - Password, passphrase, PIN, answer to a security question
   * - Something you **have**
     - An object you carry
     - Your phone (for an authenticator app or text code), a security key, a bank card
   * - Something you **are**
     - Part of your body (biometrics)
     - Fingerprint, face, voice, iris (eye)

What is multi-factor authentication?
-------------------------------------

**Multi-factor authentication (MFA)** means you must give **two or more different types** of factor to
log in. Using exactly two factors is often called **two-factor authentication (2FA)**.

Worked example
~~~~~~~~~~~~~~~

Sophie logs in to her email:

#. She types her passphrase. *(something she knows)*
#. Her authenticator app shows a 6-digit code that changes every 30 seconds. She types the code.
   *(something she has: her phone)*
#. She is logged in.

An attacker in another country steals Sophie's passphrase in a data breach. They try to log in, but
they do not have her phone, so they cannot get the code. **Sophie's account stays safe.**

.. admonition:: Two passwords is not MFA
   :class: warning

   A password and a PIN are both **something you know**. If an attacker tricks you into telling them,
   they get both at once. MFA needs factors from **different** groups.

Types of MFA (from good to best)
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Type
     - How it works
   * - Text message (SMS) code
     - A code is sent to your phone number. Better than no MFA, but codes can be stolen if a scammer
       moves your phone number to their SIM card.
   * - Authenticator app
     - An app on your phone makes a new code every 30 seconds. Stronger than SMS.
   * - Push notification
     - Your phone asks "Is this you trying to log in?" and you tap **Yes** or **No**. Never tap Yes if it
       was not you.
   * - Passkey or physical security key
     - Your device or a small USB key proves who you are using encryption, often with your fingerprint or
       face. This is the strongest option and cannot be phished.

Turning on MFA
~~~~~~~~~~~~~~~

The steps are similar on most websites:

#. Go to **Settings** → **Security** (or **Account**).
#. Find **Two-step verification**, **2FA** or **Multi-factor authentication**.
#. Choose your method (an authenticator app is a good choice).
#. Save your **backup codes** somewhere safe and offline, such as written down at home. They let you get
   back in if you lose your phone.

Turn on MFA first for your **most important accounts**: email, banking and anything with saved card
details. The ACSC also recommends turning on automatic **software updates**, because updates fix security
holes that attackers use.

Watch
~~~~~~

* `Multi-factor authentication (ACSC video on Vimeo) <https://vimeo.com/818551251>`_
* `Passphrases (ACSC video on Vimeo) <https://vimeo.com/818553453>`_
* `ACSC: Turn on multi-factor authentication <https://www.cyber.gov.au/learn-basics/explore-basics/mfa>`_

Activities
-----------

Activity 1: Which factor?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Something you know, Something you have, Something you are
   :delimiter: =>

   A passphrase => Something you know
   A 4-digit PIN => Something you know
   The name of your first school => Something you know
   A code from an authenticator app on your phone => Something you have
   A USB security key => Something you have
   A bank card => Something you have
   A fingerprint scan => Something you are
   Face recognition => Something you are
   Voice recognition => Something you are

Activity 2: Is it MFA?
~~~~~~~~~~~~~~~~~~~~~~~

.. multichoice::
   :torf:

   Logging in with a password **and** a PIN is multi-factor authentication.

   [ ] True | Both are something you know, so it is only one type of factor.
   [x] False | Correct. A password and a PIN are both "something you know".

.. multichoice::
   :torf:

   Logging in with a password **and** a code from an authenticator app is multi-factor authentication.

   [x] True | Correct. Something you know plus something you have.
   [ ] False | It uses two different types of factor, so it is MFA.

.. multichoice::
   :torf:

   Unlocking a phone with a fingerprint **and** a passcode is multi-factor authentication.

   [x] True | Correct. Something you are plus something you know.
   [ ] False | It uses two different types of factor, so it is MFA.

Activity 3: Order the login
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Put the steps for logging in with MFA in order.

.. ordering::
   :no-indent:

   Go to the website and type your username.
   Type your passphrase.
   The website asks for a second factor.
   Open the authenticator app on your phone.
   Type the 6-digit code before it changes.
   You are logged in.

Activity 4: Quiz
~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      Your phone suddenly shows "Approve sign-in?" but you are not trying to log in. What should you do?

      [ ] Tap Approve to make the message go away | That would let an attacker into your account.
      [x] Tap Deny, then change your password | Correct. Someone else has your password.
      [ ] Ignore it and keep using your phone | It is a warning that someone has your password, so act on it.
      [ ] Turn off MFA | That would make your account less safe.

   .. multichoice::

      Why should you save your backup codes?

      [x] To get into your account if you lose your phone | Correct. Backup codes are a way back in.
      [ ] To share with friends so they can log in | Never share them.
      [ ] Because they make your password stronger | They do not change your password.
      [ ] So you do not need a password any more | You still need your password.

   .. multichoice::

      Which MFA method is the hardest to phish?

      [ ] SMS text code | SMS codes can be stolen or tricked out of you.
      [ ] Security question | A security question is not even a second type of factor.
      [x] Passkey or physical security key | Correct. It uses encryption and only works on the real website.
      [ ] Emailed code | If your email is hacked, the code is too.

Challenge
----------

At home, with a parent or carer, check whether MFA is turned on for one important account (for example,
a family email account or a gaming account). If it is not, help turn it on. Write a short "how-to" guide
with screenshots (with any personal details hidden) for a younger student.

Exam-style question
--------------------

.. structuredquestion:: Multi-factor authentication
   :total-marks: 6
   :category: Cybersecurity

   .. stimulus::

      A school is changing how students log in to the learning portal. Currently students type a password.
      The new system will also ask for a code from an authenticator app on their phone.

   .. subquestion:: a) Name the two authentication factors used in the new system.
      :marks: 2

      .. model-answer::

         Something you know (the password) and something you have (the phone with the authenticator app).

      .. marking-guidance::

         1 mark for each correctly named factor type.

   .. subquestion:: b) Explain how the new system protects a student whose password has been stolen.
      :marks: 2

      .. model-answer::

         The attacker would also need the code from the student's phone. Because they do not have the phone,
         they cannot log in, even with the correct password.

      .. marking-guidance::

         * 1 mark for saying a second factor is needed.
         * 1 mark for explaining the attacker does not have the phone or code.

   .. subquestion:: c) Some students do not have a phone. Suggest another factor the school could use and identify its type.
      :marks: 2

      .. model-answer::

         A physical security key (USB key) kept on the student's lanyard, which is something you have.
         Or a fingerprint reader on the school laptops, which is something you are.

      .. marking-guidance::

         * 1 mark for a suitable alternative factor.
         * 1 mark for naming its type correctly.
