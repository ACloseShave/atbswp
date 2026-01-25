import random
guess = ''

# TODO: rewrite below using separate functions & input validation

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()                         # Problem 1: no input validation
toss = random.randint(0, 1)                 # Problem 2: 0/1 never converted to tails/heads
if toss == guess:                           # These won't be equal until converted
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()                         # Problem 3: repetitive code, could try using
    if toss == guess:                       # a function for the guess & a function for the toss
        print('You got it!')
    else:
        print('Nope. You are really bad at this game')