import random
guess = ''

# TODO: rewrite below using separate functions & input validation

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()                         # Problem 1: no input validation

toss = random.randint(0, 1)
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()                         # Problem 2: repetitive code, could try using
    if toss == guess:                       # a function for the guess & a function for the toss
        print('You got it!')
    else:
        print('Nope. You are really bad at this game')