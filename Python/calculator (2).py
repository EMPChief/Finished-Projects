# Calculation functions
def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


def subtract(number1, number2):
    return number1 - number2


def add(number1, number2):
    return number1 + number2

# Main calculator function


def main():
    while True:
        operation = input(
            "Input the operation (1: +, 2: -, 3: *, 4: /, 5: break): ")

        # Check for break condition
        if operation == "5":
            break

        number1 = float(input("Input the first number: "))
        number2 = float(input("Input the second number: "))

        if operation == "1":
            result = add(number1, number2)
            print(f"{number1} + {number2} = {result}")
        elif operation == "2":
            result = subtract(number1, number2)
            print(f"{number1} - {number2} = {result}")
        elif operation == "3":
            result = multiply(number1, number2)
            print(f"{number1} * {number2} = {result}")
        elif operation == "4":
            result = divide(number1, number2)
            print(f"{number1} / {number2} = {result}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
