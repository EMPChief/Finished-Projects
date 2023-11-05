from calculator_class import Calculator
    """
    The main function allows the user to perform basic arithmetic operations using a calculator object
    and saves the results to a file.
    """




def main():
    calculator = Calculator()
    while True:
        calculator.display()
        operator = input("Please select an operator: ")
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        calculator.num1 = num1
        calculator.num2 = num2 
        
        if operator == "1":
            try:
                result = calculator.add()
            except ValueError as e:
                print(f"Invalid Value: {e}")
            except FileNotFoundError as e:
                print(f"File Not Found: {e}")
            except FileExistsError as e:
                print(f"File Already Exists: {e}")
            else:
                print(f"The result from {num1} + {num2} is: {result}")
                with open("result.txt", "a") as f:
                    f.write(f"You did a calculation off {num1} + {num2} with result off: {result} \n")
            finally:
                f.close()
                
        elif operator == "2":
            try:
                result = calculator.subtract()
            except ValueError as e:
                print(f"Invalid Value: {e}")
            except FileNotFoundError as e:
                print(f"File Not Found: {e}")
            except FileExistsError as e:
                print(f"File Already Exists: {e}")
            else:
                print(f"The result from {num1} - {num2} is: {result}")
                with open("result.txt", "a") as f:
                    f.write(f"You did a calculation off {num1} - {num2} with result off: {result} \n")
            finally:
                f.close()
        elif operator == "3":
            try:
                result = calculator.multiply()
            except ValueError as e:
                print(f"Invalid Value: {e}")
            except FileNotFoundError as e:
                print(f"File Not Found: {e}")
            except FileExistsError as e:
                print(f"File Already Exists: {e}")
            else:
                print(f"The result from {num1} * {num2} is: {result}")
                with open("result.txt", "a") as f:
                    f.write(f"You did a calculation off {num1} * {num2} with result off: {result} \n")
            finally:
                f.close()
        elif operator == "4":
            try:
                result = calculator.divide()
            except ValueError as e:
                print(f"Invalid Value: {e}")
            except FileNotFoundError as e:
                print(f"File Not Found: {e}")
            except FileExistsError as e:
                print(f"File Already Exists: {e}")
            except ZeroDivisionError as e:
                print(f"Cannot divide by zero: {e}")
            else:
                print(f"The result from {num1} / {num2} is: {result}")
                with open("result.txt", "a") as f:
                    f.write(f"You did a calculation off {num1} / {num2} with result off: {result} \n")
            finally:
                f.close()
        elif operator == "5":
            break


            
            

if __name__ == "__main__":
    main()