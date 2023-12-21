import re
#email validate using regex
def validate_email(email):
    if re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return True
    else:
        return False


def validate_password(password):
    if re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\S)[A-Za-z\d\S]{8,}$", password):
        return True
    else:
        return False






email = input("Enter your email: ")
password = input("Enter your password: ")

if validate_email(email) and validate_password(password):
    print("Your email and password are valid!")
else:
    print("Your email and password are not valid!")