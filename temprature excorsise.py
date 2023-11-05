def celcius(a):
    """
    This Python code converts temperature between Celsius and Fahrenheit.
    
    :param a: The parameter "a" in the above code represents the temperature value that you want to
    convert
    :return: The code is returning the converted temperature value.
    """
    return (9 * a) / 5 + 32
    
def feretheim(a):
    return (a - 32) * 5 / 9
    
convert_type = input("Type what you want to convert from: (c/f) ")
temprature = float(input("Type the temprature you want to convert: "))


if convert_type == "c" or convert_type == "C":
    print(f"You converted the temprature {temprature}°C to {feretheim(temprature)}°f")
elif convert_type == "F" or convert_type == "f":
    print(f"You converted the temprature {temprature}°f to {celcius(temprature)}°C")
else:
    print("Wrong convertable type")