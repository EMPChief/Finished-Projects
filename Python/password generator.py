import string
    """
    The main function generates a random password based on user input for length, number of numbers, and
    number of special characters, and then saves the password to a file.
    """
import random

def main():
    while True:
        password_length = int(input("How many characters would you like in your password? "))
        if password_length < 8:
            print("Password must be at least 8 characters long")
        else:
            break
    while True:
        number_of_numbers = int(input("How many numbers would you like in your password? "))
        if number_of_numbers < 1:
            print("Password must contain at least 1 number")
        else:
            break
    while True:
        number_of_special_characters = int(input("How many special characters would you like in your password? "))
        if number_of_special_characters < 1:
            print("Password must contain at least 1 special character")
        else:
            break
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_characters) for i in range(password_length))
    print(f"Your password is: {password}")
    with open("password.txt", "a") as f:
        f.write(f"Your password is: {password} \n")
        f.close()

if __name__ == "__main__":
    main()