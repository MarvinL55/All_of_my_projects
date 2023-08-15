import random

print("I'm thinking of a number between 1 and 10")

guess = int(input("What do you think it is:"))
number = random.randrange(1,10)

while guess != number:
    if guess < number:
        print("Number is too low")
        guess = int(input("Try again:"))
    elif guess > number:
        print("Number is too high")
        guess = int(input("Try again:"))
    else:
        break

print("You got it")