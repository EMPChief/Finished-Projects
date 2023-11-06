# The `import random` statement is importing the `random` module in Python. This module provides
# functions for generating random numbers, selecting random elements from a sequence, and other
# random-related operations.
import random
"""
guesses = input("How many guesses do you want to make? ")
guess_number = random.randint(1, 100)

for i in range(int(guesses)):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == guess_number:
        print("You got it right good work!")
        retry = input("Do you want to play again? (yes/no): ")
        if retry.lower() != "yes":
            break
    elif guess < guess_number:
        print("Your guess is too low try again!")
    elif guess > guess_number:
        print("Your guess is too high try again!")
    else:
        print("Your guess is not a number try again!")
 """
# The code is implementing a simple rock-paper-scissors game.

options = ("rock", "paper", "scissors")
player= None
computer = random.choice(options)

while player not in options:
    player = input("Enter rock, paper, or scissors: ")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You won!")
elif player == "paper" and computer == "rock":
    print("You won!")
elif player == "scissors" and computer == "paper":
    print("You won!")
else:
    print("You lost!")
