import math


def kg(a):
    return a * 2.205


def pouds(a):
    return a / 2.205


operator = input(
    "Convert from kg to pound or pound to kg type. Type from what you want to convert from:(pound/kg): ")
weight = float(
    input("Input your weight in kg or pound depending on what operator you chose: "))

if operator == "pound":
    print(f"The wight in pound is: {kg(weight)}")

elif operator == "kg":
    print(f"The weight in kg is: {pouds(weight)}")
else:
    print("Invalid operator")
