# The code is a simple hangman game implemented in Python.
import random

words = ["Apple", "banana", "pear", "cherry"]
word = random.choice(words)
guesses = ""
max_guesses = 10

print(f"Welcome to hangman first game from bjørn-magne\nthe word contains {len(word)} letters in it")

while max_guesses > 0:
    missed = 0
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
            missed += 1
            
    if missed == 0:
        print("\nCongratulation you guessed the word!")
        break
    guess = input("\nInput a letter: ")
    guesses += guess
    max_guesses -= 1
    if guess not in word:
        print(f"Sorry {guess} is not in the word. Please try again. {max_guesses} chances left.")
    
    if max_guesses == 0:
        print("Sorry you ran out off guesses, try again")
    