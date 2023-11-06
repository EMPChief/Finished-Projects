# TODO: Define the functions for addition, subtraction, multiplication, and division.
# Each function should take two arguments (the two numbers to be operated on) and return the result.

# Define a function to display the menu of operations to the user.
def display_menu():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

# Define a function to prompt the user to enter two numbers.
def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

# Define the main function to run the calculator.
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: division by zero"
    else:
        return num1 / num2
    
def main():
    while True:
        # Display the menu and get the user's choice.
        display_menu()
        choice = int(input("Enter your choice (1-5): "))

        # Exit if the user chooses option 5.
        if choice == 5:
            print("Goodbye!")
            break

        # Get the two numbers to be operated on.
        num1, num2 = get_numbers()

        # Perform the selected operation and display the result.
        if choice == 1:
            result = add(num1, num2)
            print(f"The result is {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"The result is {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"The result is {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"The result is {result}")
        else:
            print("Invalid choice. Please try again.")

# Call the main function to run the calculator.
main()
