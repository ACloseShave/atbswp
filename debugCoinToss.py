import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    guess = guess.lower()

# TODO: when this is functionalized, return the values to the caller
toss = random.randint(0, 1)
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

# TODO: Re-write as separate functions for the guess and the toss
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()                         # Problem 1: repetitive code, could try using
    if toss == guess:                       # a function for the guess & a function for the toss
        print('You got it!')
    else:
        print('Nope. You are really bad at this game')