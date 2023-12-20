import random

start_guess = int(input("What first number want to guess between?"))
end_guess = int(input("What last number want to guess between?"))
guessing_while_loop = random.randint(start_guess, end_guess)
print(f"Welcome to my while loop guess the number between {start_guess} and {end_guess}")
guessing = int(input("How many times do you want to guess the number? "))

while True:
    try:
        number = int(input(f"Enter a random number between {start_guess} and {end_guess}: "))
        if number == guessing_while_loop:
            print(f"You did it! You guessed the right number, it was {number}! Congratulations!")
            print("Guessing is over, goodbye")
            break
        elif number > guessing_while_loop:
            print("You're a bit hot there, try lower numbers")
            guessing -= 1
        elif number < guessing_while_loop:
            print("You're a bit cold there, try higher numbers")
            guessing -= 1
        if guessing == 0:
            print("You used up all your guesses, you lose")
            print("Guessing is over, goodbye")
            break
    except ValueError as e:
        print(f"Please enter a valid number: {e}")
    except KeyboardInterrupt:
        print("You pressed Ctrl+C, bye bye")
        break
    except Exception as e:
        print(f"Something went horribly wrong: {e}")

second_guessing = int(input("How many times do you want to guess the number? "))
guess_for_start = int(input("What first number want to guess between?"))
guess_for_end = int(input("What last number want to guess between?"))
guess_for_loop = random.randint(guess_for_start, guess_for_end)

try:
    for i in range(second_guessing):
        guessing = int(input(f"Guess a number between {guess_for_start} and {guess_for_end}: "))
        if guessing == guess_for_loop:
            print(f"You guessed the right number! It was {guessing}. Congratulations!")
            print("Guessing is over, goodbye")
            break
        elif guessing > guess_for_loop:
            print("You're a bit hot there, try lower numbers")
        elif guessing < guess_for_loop:
            print("You're a bit cold there, try higher numbers")
    else:
        print("You used up all your guesses, you lose")
        print("Guessing is over, goodbye")
except ValueError as e:
    print(f"Please enter a valid number: {e}")
except KeyboardInterrupt:
    print("You pressed Ctrl+C, bye bye")
except Exception as e:
    print(f"Something went horribly wrong: {e}")