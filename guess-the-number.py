#!/bin/env python3

# Number guessing game
from random import randint as random_num


print("Hello! This is the random number game. First, ")
name = input("What is your name? ")
secret_number = random_num(1, 20)


print("Hello " + name + "!")
print("Here's how to play:")


#  Begin game with rules
print("I'm thinking of a number between 1 and 20")
print("You have 4 guesses to get it right")


#  Begin guess/actual comparison loop
for attempt_number in range(4, 0, -1):
    guess = int(input("What is your first guess? "))

    if guess > secret_number:
        print("That's too high! You have " + str(attempt_number - 1) + " guesses remaining.")
    elif guess < secret_number:
        print("That's too low! You have " + str(attempt_number - 1) + " guesses remaining.")
    else:
        print("That's the number!")
        break