# The above class is a calculator that can perform addition, subtraction, multiplication, and division
# operations.
class Calculator:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
    
    def display(self):
        print("Hello welcome to my calculator")
        print("Please enter one of the numbers below for the calculation:")
        print("Option 1: Add")
        print("Option 2: Subtract")
        print("Option 3: Multiply")
        print("Option 4: Divide")
        print("Option 5: Break")
    
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2