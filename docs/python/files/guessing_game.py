# guessing_game.py
# Iteration with a while loop: guess the secret number.

import random

secret = random.randint(1, 20)
guesses = 0
guess = 0

print("I am thinking of a number from 1 to 20.")

while guess != secret:
    guess = int(input("Your guess: "))
    guesses = guesses + 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"Correct! You took {guesses} guesses.")
