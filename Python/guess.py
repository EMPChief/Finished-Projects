# The code is a simple number guessing game.
import random

secret_number = random.randint(1, 10)
numofguess = 5

print("What number am i thinking about?")

while numofguess >0:
    print("You have", numofguess, "left to work with.")
    guess = int(input("Please type your guess:"))
    numofguess -= 1
    if guess == secret_number:
        print("Bingo you guessed right")
        break
    else:
        if guess < secret_number:
            print("too low")
        else:
            print("Too high!")
