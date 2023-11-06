 #Calculation functions:
    """
    The above code defines a calculator program in Python that performs basic arithmetic operations on
    two numbers.
    
    :param number1: The first number to be operated on
    :param number2: The second number to be operated on
    :return: The functions `multiply`, `divide`, `subtract`, and `add` are returning the result of the
    respective mathematical operation. The `main` function does not return anything.
    """
def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

def subtract(number1, number2):
    return number1 - number2

def add(number1, number2):
    return number1 + number2

# Define the main function to run the calculator. this function should take two arguments
# (the two numbers to be operated on) and return the result. this function should repeat as long as
#you don't break out of the loop.
def main():
    while True:
        operation = input("Input the operation (1: +, 2: -, 3: *, 4: / 5: break): ")
        number1 = float(input("Input the first number: "))
        number2 = float(input("Input the second number: "))
        if operation == "1":
            add(number1, number2)
            print(f"{number1} + {number2} = {add(number1, number2)}")
        elif operation == "2":
            subtract(number1, number2)
            print(f"{number1} - {number2} = {subtract(number1, number2)}")
        elif operation == "3":
            multiply(number1, number2)
            print(f"{number1} * {number2} = {multiply(number1, number2)}")
        elif operation == "4":
            divide(number1, number2)
            print(f"{number1} / {number2} = {divide(number1, number2)}")
        elif operation == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()