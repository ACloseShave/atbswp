#!/bin/env python3

# Number guessing game
from random import randint as rnum


print("Hello! This is the random number game. First, ")
name = input("What is your name? ")

print("Hello " + name + "!")

print("Here's how to play:")
print("I'm thinking of a number between 1 and 10")
print("You have 4 guesses to get it right")
guess = input("What is your first guess? ")

number = int("")

for i in range(1,11):
    if guess == number:
        print("Wow! You guessed it right!")