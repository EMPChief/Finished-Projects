
"""
    The code calculates compound interest based on user input for principle amount, interest rate, and
    time.
    :return: The `interest_calculator` function returns a tuple containing the total interest, principle
    amount, interest rate, and time.
"""
def interest_calculator():
    principle = 0
    rate = 0
    time = 0
    while principle <= 0:
        principle = float(input("Input the principle amount: "))
        if principle <= 0:
            print("Interest can't be negative or zero!")
    while rate <= 0:
        rate = float(input("Input the rate (in percentage): "))
        if rate <= 0:
            print("Rate can't be negative or zero!")
    while time <= 0:
        time = float(input("Input the time (in years): "))
        if time <= 0:
            print("Time can't be negative or zero!")
    total = principle * pow((1 + rate / 100), time)
    return total, principle, rate, time


def main():
    while  True:
        storing_interest = interest_calculator()
        print(f"Interest: {storing_interest[0]}$")
        print(f"Principle amount: {storing_interest[1]}$")
        print(f"Interest rate: {storing_interest[2]}%")
        print(f"Time: {storing_interest[3]}years\n")
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != "yes":
            break

if  __name__ == "__main__":
    main()
