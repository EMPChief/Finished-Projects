
def multiplication(number1, number2):
    return number1*number2


def addition(number1, number2):
    return number1+number2


def division(number1, number2):
    return number1/number2


def subtraction(number1, number2):
    return number1-number2


what_to_use = str(input(
    "Input type you want to use for calculation: (addition multiplication division subtraction)"))
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
