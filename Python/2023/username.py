

# Codeblock for checking if username can be used, checking specific:

# If it got to few character, if got to many character, if got space in it or if got number in it
def username_check(username):
    if len(username) <= 4:
        print(f"{username} does not have enough characters to be used!")
    elif not username.isalpha():
        print("Your username can not contain numbers!")
    elif not username.find(" ") == -1:
        print(
            f"Your username {username} got space it in and therefore is invalid!")
    elif len(username) >= 16:
        print(f"Your username {username} need to be less then 16 characters!")
    else:
        print(f"Your username {username} can be used!")
# Codeblock for checking if password can be used, checking specific:
# If it got to few character, if got to many character, if got space in it, if got number in it
# If got special character or a capitalized letter


def password_check(password):
    if len(password) <= 6:
        print(f"Your password does not have enough characters to be used!")
    elif password.isdigit() == True:
        print("Your password need to contain number!")
    elif not password.find(" ") == -1:
        print(f"Your password got space it in and therefor is invalid!")
    elif len(password) >= 16:
        print(f"Your password need to be less then 16 characters!")
    elif password.isalnum() == True:
        print("Your password need one special character")
    elif password.capitalize() == True:
        print("You need to have one letter capitalized")
    else:
        print(f"Your username {password} can be used!")


# Input username and password
name_input = str(input("Input a username: "))
passwordinput = input("Input a password: ")

# Running function
username_check(name_input)
password_check(passwordinput)
