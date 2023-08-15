import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20")

for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("your number is too low")
    elif guess > secretNumber:
        print("Your number is too high")
    else:
      break

if guess == secretNumber:
    print("Good job, you guessed the number " + str(guessesTaken) + " guess")
else:
    print("Nope the number I was thinking of was "+ str(secretNumber))