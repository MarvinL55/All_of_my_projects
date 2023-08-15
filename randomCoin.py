import random

guess = ''
while guess not in('heads', 'tails'):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
toss = random.randint(0, 1)
if toss == guess:
    print("You got it")
else:
    print("Nope Guess again")
    guess = input()