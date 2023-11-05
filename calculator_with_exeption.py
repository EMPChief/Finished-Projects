path = "E:\\programs\\learning venv\\textfiles\\calculator_with_exeption.txt"
    """
    The above code is a Python program that acts as a calculator, allowing the user to perform addition,
    subtraction, multiplication, and division operations, and writes the calculations to a file for
    future reference.
    """
# Display the options
def display_options():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
#The fucntion that does the calculations
def addition(number1=0, number2=0):
    return number1 + number2
def multiplication(number1=0, number2=0):
    return number1 * number2

def division(number1=0, number2=1):
    return number1 / number2

def subtraction(number1=0, number2=0):
    return number1 - number2
#The main function that collect all the program into one function and run it in while loop so don't need to restart program
#The function also takes error message if the user input wrong data type and give feedback.
#It also write to a file that it did a calculation with the result for future referances.
def main():
    while True:
        display_options()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                print(addition(number1, number2))
            except ValueError as e:
                print("You inputed wrong data type. Please try again.")
                print (f"The error message is: {e}")
            except OverflowError as e:
                print("The result is too large. Please try again.")
                print (f"The error message is: {e}")
            except FileNotFoundError as e:
                print("The file does not exist. Please try again.")
                print (f"The error message is: {e}")
            else:
                print(f"The result is: {addition(number1, number2)}")
                with open (path, "a") as file:
                    file.write(f"You did a calculation, {number1} + {number2} with result off: {addition(number1, number2)}\n")
            finally:
                file.close()
        elif choice == 2:
            try:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                print(subtraction(number1, number2))
            except ValueError as e:
                print("You inputed wrong data type. Please try again.")
                print (f"The error message is: {e}")
            except OverflowError as e:
                print("The result is too large. Please try again.")
                print (f"The error message is: {e}")
            except FileNotFoundError as e:
                print("The file does not exist. Please try again.")
                print (f"The error message is: {e}")
            else:
                print(f"The result is: {subtraction(number1, number2)}")
                with open (path, "a") as file:
                    file.write(f"You did a calculation, {number1} - {number2} with result off: {addition(number1, number2)}\n")
            finally:
                file.close()
        elif choice == 3:
            try:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                print(multiplication(number1, number2))
            except ValueError as e:
                print("You inputed wrong data type. Please try again.")
                print (f"The error message is: {e}")
            except OverflowError as e:
                print("The result is too large. Please try again.")
                print (f"The error message is: {e}")
            except FileNotFoundError as e:
                print("The file does not exist. Please try again.")
                print (f"The error message is: {e}")
            else:
                print(f"The result is: {multiplication(number1, number2)}")
                with open (path, "a") as file:
                    file.write(f"You did a calculation, {number1} * {number2} with result off: {addition(number1, number2)}\n")
            finally:
                file.close()
        elif choice == 4:
            try:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
            except ValueError as e:
                print("You inputed wrong data type. Please try again.")
                print (f"The error message is: {e}")
            except ZeroDivisionError as e:
                print("You cannot divide by zero. Please try again.")
                print (f"The error message is: {e}")
            except OverflowError as e:
                print("The result is too large. Please try again.")
                print (f"The error message is: {e}")
            except FileNotFoundError as e:
                print("The file does not exist. Please try again.")
                print (f"The error message is: {e}")
            except FileExistsError as e:
                print("The file already exists. Please try again.")
                print (f"The error message is: {e}")
            else:
                print(f"The result is: {division(number1, number2)}")
                with open (path, "a") as file:
                    file.write(f"You did a calculation, {number1} / {number2} with result off: {division(number1, number2)}\n")
            finally:
                file.close()
        elif choice == 5:
            break

if __name__ == "__main__":
    main()