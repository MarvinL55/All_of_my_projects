import random

print("I'm thinking of a number between 1 and 10")

guess = int(input("What is it?"))
number = random.randrange(1,10)

while guess != number:
    if guess < number:
        print("Guess too low")
        guess = int(input("Try again:"))
    elif guess > number:
        print("Guess too high")
        guess = int(input("Try again:"))
    else:
        break
print("You got it.")