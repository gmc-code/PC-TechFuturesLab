====================================
5. Passwords and passphrases
====================================

Learning intentions
--------------------

* I can explain why passwords protect my identity and data.
* I can describe how attackers guess or steal passwords.
* I can create a strong passphrase and explain why it is strong.

Success criteria
~~~~~~~~~~~~~~~~~

* I can explain the difference between a password and a passphrase.
* I can list the three features of a strong passphrase: long, unpredictable and unique.
* I can explain what a password manager does.

Why passwords matter
---------------------

A password is like the key to your house. If someone gets your password, they can:

* read your messages and see your photos
* pretend to be you and message your friends
* buy things with your saved card details
* lock you out of your own account
* use your email to reset the passwords of your **other** accounts

Your email account is especially important because it is often used to reset every other password.

How attackers get passwords
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Attack
     - How it works
   * - Guessing
     - Trying obvious passwords such as ``123456``, ``password``, a pet's name or a birthday.
   * - Brute force
     - A computer tries **every** combination: aaaa, aaab, aaac ... Short passwords fall quickly.
   * - Dictionary attack
     - A computer tries millions of common words and passwords, including swaps like ``P@ssw0rd``.
   * - Credential stuffing
     - When one website is hacked, attackers try the stolen email and password on lots of other
       websites. This works if you **reuse** passwords.
   * - Phishing
     - Tricking you into typing your password into a fake website. (See :doc:`computing_07_phishing_scams`.)
   * - Shoulder surfing
     - Watching you type your password or PIN.

Passwords vs passphrases
-------------------------

A **passphrase** is a password made of **four or more random words**. The Australian Cyber Security
Centre (ACSC) recommends passphrases because they are long, which makes them hard for computers to
crack, but easy for people to remember.

The ACSC says a strong passphrase should be:

* **Long:** four or more random words and at least **15 characters**.
* **Unpredictable:** random, unrelated words, not a sentence, song lyric or famous quote.
* **Unique:** a different passphrase for every important account.

.. list-table::
   :header-rows: 1
   :widths: 35 15 50

   * - Example
     - Strength
     - Why
   * - ``Max2012``
     - Very weak
     - Pet's name and a year. Short and easy to guess.
   * - ``P@ssw0rd!``
     - Weak
     - Looks complex, but dictionary attacks try these swaps.
   * - ``ILoveMyDogMax``
     - Weak
     - A predictable sentence with personal information.
   * - ``crystal onion clay pretzel``
     - Strong
     - Four random words, 26 characters, easy to remember.
   * - ``kettle orbit maple trumpet``
     - Strong
     - Four random words, 26 characters.

.. note::

   ``crystal onion clay pretzel`` is a well-known example from the ACSC website. That means it is now a
   **bad** choice for a real account. Never use an example passphrase you have seen online.

Why length beats complexity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each extra character multiplies the number of guesses an attacker has to try.

* An 8-letter password using only lowercase letters has 26 × 26 × 26 × 26 × 26 × 26 × 26 × 26
  = 26\ :sup:`8` ≈ **209 billion** combinations. A fast computer can try them all in minutes.
* A passphrase of 4 words chosen at random from a list of 7776 words has 7776\ :sup:`4` ≈
  **3.7 million billion** combinations, and that is even if the attacker knows you used four words.

How to make a passphrase
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open a book or dictionary at four random pages and take one word from each page, **or** use a
   random word generator.
#. Check the words are not related to each other or to you.
#. Check it is at least 15 characters long.
#. Practise typing it a few times.

Password managers
------------------

Having a unique passphrase for every account is hard to remember. A **password manager** is an app
that stores all your passwords in an encrypted vault. You only need to remember **one** strong
passphrase to unlock the manager. It can also create long random passwords for you.

Most phones and web browsers have one built in, and there are separate password manager apps.

Other good habits
~~~~~~~~~~~~~~~~~~

* Never share your password, even with friends.
* Lock your devices with a PIN, passcode or biometrics.
* Log out of shared computers.
* Change your password straight away if you think someone knows it.
* Turn on **multi-factor authentication** (next lesson).

Activities
-----------

Activity 1: Rate the password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. classifying::
   :bins: Weak, Strong
   :delimiter: =>
   :instructions: Sort each password into Weak or Strong using the ACSC advice.

   123456 => Weak
   password1 => Weak
   Biscuit2011 => Weak
   S0cc3r! => Weak
   iloveyou => Weak
   MyNameIsJack => Weak
   lantern hippo cobalt sunday => Strong
   velvet tractor pebble lagoon => Strong
   amber glacier pickle violin => Strong

Activity 2: Passphrase facts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::

   A passphrase uses four or more @@random@@ words.
   The ACSC says it should be at least @@15@@ characters long.
   Use a @@unique@@ passphrase for every important account.
   Reusing passwords lets attackers use credential @@stuffing@@.
   A password @@manager@@ stores your passwords in an encrypted vault.

Activity 3: Name the attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::

   .. multichoice::

      A computer tries aaaa, aaab, aaac and so on until it finds the password. What is this?

      [x] Brute force attack | Correct. It tries every possible combination.
      [ ] Phishing | Phishing tricks you into giving your password.
      [ ] Shoulder surfing | Shoulder surfing is watching someone type.
      [ ] Credential stuffing | Credential stuffing uses passwords stolen from another site.

   .. multichoice::

      A gaming website is hacked. A week later, someone logs in to Leo's email with the same password.
      What attack is this?

      [ ] Dictionary attack | A dictionary attack tries common words.
      [x] Credential stuffing | Correct. Stolen details were tried on another site because Leo reused his password.
      [ ] Brute force attack | They did not need to try every combination. They already had the password.
      [ ] Shoulder surfing | Nobody watched Leo type.

   .. multichoice::

      Why is ``P@ssw0rd!`` a weak password even though it has symbols and numbers?

      [ ] It is too long | It is only 9 characters.
      [x] Dictionary attacks already try common words with letter swaps | Correct. Swapping a for @ and o for 0 is very predictable.
      [ ] Symbols are not allowed in passwords | Symbols are allowed.
      [ ] It has no capital letters | It does have a capital P.

   .. multichoice::

      Which passphrase follows ALL the ACSC advice?

      [ ] my dog is cute | It is a predictable sentence.
      [ ] twinkle twinkle little star | It is a famous song lyric.
      [x] walrus candle denim orbit | Correct. Four random words, more than 15 characters.
      [ ] cat dog | Too short and only two words.

Challenge
----------

Without using a real passphrase you will use, make three practice passphrases of your own that follow
the ACSC advice. For each one, count the characters and explain why it is unpredictable.

Then research: what is a **data breach**? Find one data breach that affected Australians in the last
few years and describe what information was stolen and what people were told to do.

Exam-style question
--------------------

.. structuredquestion:: Protecting accounts
   :total-marks: 7
   :category: Cybersecurity

   .. stimulus::

      Jordan uses the password ``Jordan2011`` for their email, school portal and three gaming accounts.

   .. subquestion:: a) Give two reasons why Jordan's password is weak.
      :marks: 2

      .. model-answer::

         * It contains personal information (Jordan's name and probably their birth year), so it is easy to guess.
         * It is short (10 characters), so a brute force attack could crack it quickly.
         * It is used on many accounts.

      .. marking-guidance::

         1 mark for each correct reason (maximum 2).

   .. subquestion:: b) One of the gaming websites is hacked. Explain why all of Jordan's accounts are now at risk.
      :marks: 2

      .. model-answer::

         Jordan uses the same password everywhere. Attackers can try the stolen email and password on other
         websites (credential stuffing). If they get into Jordan's email, they can also reset the
         passwords of other accounts.

      .. marking-guidance::

         * 1 mark for identifying password reuse or credential stuffing.
         * 1 mark for explaining how one stolen password unlocks the other accounts.

   .. subquestion:: c) Describe a better approach Jordan could use to manage their passwords.
      :marks: 3

      .. model-answer::

         Jordan should use a different passphrase for each account, made of four or more random words
         and at least 15 characters, such as four unrelated words. To remember them, Jordan could use a
         password manager protected by one strong passphrase. Jordan should also turn on multi-factor
         authentication.

      .. marking-guidance::

         * 1 mark for unique passwords or passphrases for each account.
         * 1 mark for describing a strong passphrase (4+ random words, 15+ characters).
         * 1 mark for a password manager or multi-factor authentication.
