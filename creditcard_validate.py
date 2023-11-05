
    """
    The `credit_card_validation` function checks if a given credit card number is valid using the Luhn
    algorithm.
    
    :param card_number: The `card_number` parameter is a string representing the credit card number that
    the user inputs
    :return: The function `credit_card_validation` returns a boolean value. It returns `True` if the
    credit card number is valid and `False` if it is invalid.
    """
def credit_card_validation(card_number):
    sum_odd_digits = 0
    sum_even_digits = 0
    card_number = card_number.replace(" ", "")
    card_number = card_number.replace("-", "")
    card_number = card_number[::-1]
    for x in card_number[::2]:
        sum_odd_digits += int(x)
    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1 + (x % 10))
        else:
            sum_even_digits += x
    
    total = sum_odd_digits + sum_even_digits
    if total % 10 == 0:
        return True
    else:
        return False
        
    
    

card_number = input("Enter your credit card number: ")

if credit_card_validation(card_number) == True:
    print("Your card NUMBER is valid")
elif credit_card_validation(card_number) == False:
    print("Your card NUMBER is invalid")