# Defining various variables: mood, strength, rank, and a list of color codes.
mood = "happy"
strength = 6.6
rank = 1
color_codes = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Accessing and printing the third element from the 'serials' list.
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

# Appending a new time value to the 'seconds' list.
seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)

# Enumerating and printing elements of 'filenames' with their index.
filenames = ['Document.txt', 'Report.txt', 'Presentation.txt']
for i, filename in enumerate(filenames):
    print(f"{i}-{filename}")

# Accessing an IP address from the 'ips' list based on user input.
ips = ['100.122.133.105', '100.122.133.111']
input_nr = int(input("Type the number of the IP you want to see: "))
print(f"You chose {ips[input_nr]}")

# Demonstrating mixed data types within a single list.
temperatures = [float(3.7), int(4.5), "hello"]

# Working with nested lists, including a string inside a list.
rainfall = [3.7, 4, 'hello', ['hello']]

# Removing the second element from the 'seconds' list.
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.pop(1)

# Using list comprehension to capitalize names in the 'names' list.
names = ["john smith", "jay santi", "eva kuki"]
capitalized_names = [name.title() for name in names]
print(capitalized_names)

# Calculating and printing the length of each string in 'usernames' using list comprehension.
usernames = ["john 1990", "alberta1970", "magnola2000"]
username_lengths = [len(username) for username in usernames]
print(username_lengths)

# Converting strings to floats in 'user_entries' using list comprehension.
user_entries = ['10', '19.1', '20']
float_entries = [float(entry) for entry in user_entries]
print(float_entries)

# Converting strings to floats and calculating their sum in 'user_entries'.
user_entries = ['10', '19.1', '20']
float_entries = [float(entry) for entry in user_entries]
print(sum(float_entries))

# Checking password strength based on length.
password = input("Enter a password: ")
if len(password) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")

# Enhanced password strength check with additional condition.
password = input("Enter a password: ")
if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak.")
    
# Working with a dictionary to store different temperature values.
day_temperatures = {
    'morning': 20.5,
    'noon': 25.3,
    'evening': 22.7
}

# Modifying the dictionary to store temperature values as tuples.
day_temperatures = {
    'morning': (20.5, 21.2, 22.1),
    'noon': (25.3, 26.1, 27.0),
    'evening': (22.7, 23.5, 24.2)
}

# Slicing a sublist from the 'letters' list to print the elements 'b', 'c', and 'd'.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

# Slicing a sublist from the 'letters' list to print the elements 'a', 'b', and 'c'.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0:3])

# Slicing a sublist from the 'letters' list to print the elements 'e', 'f', and 'g'.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[4:])

# This program calculates the percentage of a given value from a total value.
# It prompts the user for the total value and a specific value, then computes the percentage.
# If the user inputs something that is not a number, it catches the error and prompts for valid input.
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = (value / total_value) * 100
    print(f"That is {percentage}%")
except ValueError:
    print("Please enter a valid number.")

# This program calculates the percentage of a given value from a total value.
# It handles cases where non-numeric values or zero as total value are entered by the user.
try:
    total_value = float(input("Enter total value: "))
    if total_value == 0:
        print("Total value cannot be zero.")
    else:
        value = float(input("Enter value: "))
        percentage = (value / total_value) * 100
        print(f"That is {percentage}%")
except ValueError:
    print("Please enter a valid number.")

# This program iterates over the 'colors' list and prints each item only if it is greater than 50.
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

# This function calculates and prints out the maximum value in the 'grades' list.
# This function calculates and returns the maximum value in the 'grades' list.
def get_max():
    grades = [9.6, 9.2, 9.7]
    return max(grades)

print(get_max())

# This function returns a string with the maximum and minimum values from the 'grades' list.
def get_max():
    grades = [9.6, 9.2, 9.7]
    return f"Max: {max(grades)}, Min: {min(grades)}"

print(get_max())

# This function converts liters to cubic meters.
def liters_to_m3(liters):
    return liters / 1000

# Check if the password has eight or more characters, at least one uppercase letter, and at least one digit
def strength(password):
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        return "Strong Password"
    else:
        return "Weak Password"

# Calculate the sum of all elements in the list and divide by the length of the list
def average_list_values(numbers_list):
    return sum(numbers_list) / len(numbers_list)

# Return a greeting string with the person's name
def greet_person(name):
    return "Hi " + name

# Concatenate str1 and str2 and return the result
def concatenate_strings(str1, str2):
    return str1 + str2

    # Capitalize the first letter of the name and return the greeting
def greet_person(name):
    return "Hi " + name.capitalize()

# Calculate and return the age based on the year of birth and the current year
def get_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth

# This function counts the number of comma-separated items in a given string.
def get_nr_items(items_string):
    return len(items_string.split(','))

# This function calculates the area of a square given the length of its side.
def square_area(side):
    return side * side

# This function classifies a temperature as "Warm" if it's greater than 7, and "Cold" if it's 7 or less.
def temperature_classification(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# This function checks if a string contains 8 or more characters.
def check_string_length(string):
    return len(string) >= 8

# This function determines the state of water based on a given temperature.
def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif temperature < 100:
        return "Liquid"
    else:
        return "Gas"
