import random
    """
    This is a Python program that allows the user to encrypt and decrypt text using a randomly generated
    key.
    """
import string

#Where are the characters that will be used to encrypt and decrypt the text.
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#Display the menu
def display_menu():
    print("Select an operation:")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")
#encryption here is the encryption function that will encrypt the text.
def encryption(chars, key):
    plain_text = input("Enter the text you want to encrypt: ")
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text, plain_text


#decryption here is the decryption function the text
def decryption(chars, key):
    cipher_text = input("Enter the text you want to decrypt: ")
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text, cipher_text
    


# Define the main function to run the encryption softwae program
#Right now, the program will ask the user to enter the text to be encrypted but if program stop the encrypting become different
def main(chars, key):
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            encrypted, original = encryption(chars, key)
            print(f"The encrypted text is: {encrypted}")
            print(f"The original text is: {original}")
        elif choice == 2:
            decrypted, original = decryption(chars, key)
            print(f"The decrypted text is: {decrypted}")
            print(f"The original text is: {original}")
        elif choice == 3:
            print("Goodbye!")
            break
        
if __name__ == "__main__":
    main(chars, key)