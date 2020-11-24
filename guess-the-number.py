#!/bin/env python3

from random import randint as random_num
secret_number = random_num(1, 20)


print("Hello! This is the random number game. First, ")
name = input("What is your name? ")
print("Hello " + name + "! Here's how to play:")


#  Begin game with rules
print("I'm thinking of a number between 1 and 20")
print("You have 4 guesses to get it right")


#  Begin guess/actual comparison loop
for attempt_number in range(4, 0, -1):    
    guess = int(input("What's your first? "))

    if guess > secret_number:
        print("That's too high!")
    elif guess < secret_number:
        print("That's too low!")
    else:
        print("That's the number!")
        break
    
    guesses_remaining = str(attempt_number - 1)
    
    print("You have " + guesses_remaining + " guesses remaining.")
