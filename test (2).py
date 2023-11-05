
    """
    The code defines four functions for performing basic arithmetic operations (addition,
    multiplication, division, and subtraction) and prompts the user to input the type of operation and
    two numbers, then performs the selected operation and prints the result.
    
    :param number1: The first number to be used in the calculation
    :param number2: The parameter `number2` is the second number that will be used in the calculation
    :return: The code returns the result of the calculation based on the input type provided by the
    user.
    """
def multiplication(number1, number2):
    return number1*number2

def addition(number1, number2):
    return number1+number2


def division(number1, number2):
    return number1/number2

def subtraction(number1, number2):
    return number1-number2

what_to_use = str(input("Input type you want to use for calculation: (addition multiplication division subtraction)"))
number1 = float(input("Input first number: "))
number2 = float(input("Input second number: "))


if what_to_use == "addition":
    print(addition(number1, number2))

elif what_to_use == "multiplication":
    print(multiplication(number1, number2))

elif what_to_use == "division":
    print(division(number1, number2))

elif what_to_use == "subtraction":
    print(subtraction(number1, number2))

else:
    print("You typed a unknown type")
    