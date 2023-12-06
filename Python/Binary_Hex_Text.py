import os
import time

# Define the file paths
FILE_PATH = "Binary_Hex_Text.txt"
ERROR_FILE_PATH = "Binary_Hex_Text_Errors.txt"


def log_conversion(operation, input_data, output_data):
    """
    Log the conversion operation details to a file.

    Args:
        operation (str): The type of conversion operation.
        input_data (str): The input data for the conversion.
        output_data (str): The output data after the conversion.
    """
    time_object = time.gmtime()
    localtime = time.strftime("%Y-%m-%d %H:%M", time_object)
    with open(FILE_PATH, "a", encoding='utf-8') as f:
        try:
            f.write(
                f"{localtime} | Operation: {operation} | Input: {input_data} | Output: {output_data}\n")
        except IOError as e:
            log_error(f"Error writing to file: {e}")


def log_error(error_message):
    """
    Log an error message to a file.

    Args:
        error_message (str): The error message to be logged.
    """
    with open(ERROR_FILE_PATH, "a", encoding='utf-8') as f:
        try:
            f.write(f"{error_message}\n")
        except IOError as e:
            print(f"Error writing error message to file: {e}")


def text_to_binary(text):
    """
    Convert text to binary representation and print the result.

    Args:
        text (str): The input text to be converted.
    """
    binary_representation = ''.join(format(ord(char), '08b') for char in text)
    print(f"Binary: {binary_representation}")
    log_conversion("text_to_binary", text, binary_representation)


def binary_to_text(binary_representation):
    """
    Convert binary representation to text and print the result.

    Args:
        binary_representation (str): The binary representation to be converted.
    """
    binary_representation = binary_representation.zfill(
        (len(binary_representation) + 7) // 8 * 8)
    eight_bit_chunks = [binary_representation[i:i + 8]
                        for i in range(0, len(binary_representation), 8)]
    binary_to_text = ''.join(chr(int(chunk, 2)) if 0 <= int(
        chunk, 2) <= 127 else '?' for chunk in eight_bit_chunks)
    print(f"Text: {binary_to_text}")
    log_conversion("binary_to_text", binary_representation, binary_to_text)


def text_to_hex(text):
    """
    Convert text to hex representation and print the result.

    Args:
        text (str): The input text to be converted.
    """
    hex_representation = ''.join(format(ord(char), '02x') for char in text)
    print(f"Hex: {hex_representation}")
    log_conversion("text_to_hex", text, hex_representation)


def hex_to_text(hex_representation):
    """
    Convert hex representation to text and print the result.

    Args:
        hex_representation (str): The hex representation to be converted.
    """
    text = bytes.fromhex(hex_representation).decode('utf-8')
    print(f"Text: {text}")
    log_conversion("hex_to_text", hex_representation, text)


def hex_to_binary(hex_representation):
    """
    Convert hex representation to binary and print the result.

    Args:
        hex_representation (str): The hex representation to be converted.
    """
    binary_representation = bin(int(hex_representation, 16))[2:]
    print(f"Binary: {binary_representation}")
    log_conversion("hex_to_binary", hex_representation, binary_representation)


def binary_to_hex(binary_representation):
    """
    Convert binary representation to hex and print the result.

    Args:
        binary_representation (str): The binary representation to be converted.
    """
    hex_representation = hex(int(binary_representation, 2))[2:]
    print(f"Hex: {hex_representation}")
    log_conversion("binary_to_hex", binary_representation, hex_representation)


def get_valid_input(prompt, valid_operations):
    """
    Get valid user input for the desired operation.

    Args:
        prompt (str): The prompt to display to the user.
        valid_operations (list): The list of valid operations.

    Returns:
        str: The user's selected operation.
    """
    while True:
        operation = input(prompt).lower()
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please choose a valid operation.")


def main():
    """
    Main function for user interaction and handling conversions.
    """
    while True:
        valid_operations = ["t2b", "b2t", "t2h", "h2t", "h2b",
                            "b2h", "break", "exit", "quit", "e", "q", "b"]
        operation = get_valid_input(
            "What would you like to do? (t2b, b2t, t2h, h2t, h2b, b2h)\n"
            "(to exit you can use(break/quit/exit)\nInput operation: ",
            valid_operations)

        try:
            if operation == "t2b":
                text = input("What text do you want to convert to binary? ")
                text_to_binary(text)

            elif operation == "b2t":
                binary_representation = input(
                    "What is your binary text that you want to convert? ")
                binary_to_text(binary_representation)

            elif operation == "t2h":
                text = input("What text do you want to convert to hex? ")
                text_to_hex(text)

            elif operation == "h2t":
                hex_representation = input(
                    "What is your hex text that you want to convert? ").replace(" ", "")
                hex_to_text(hex_representation)

            elif operation == "h2b":
                hex_representation = input(
                    "What is your hex text that you want to convert? ")
                hex_to_binary(hex_representation)

            elif operation == "b2h":
                binary_representation = input(
                    "What is your binary text that you want to convert? ")
                binary_to_hex(binary_representation)

            elif operation in ["break", "exit", "quit", "e", "q", "b"]:
                break

        except ValueError as e:
            print(f"Error: {e}")
            log_error(f"ValueError: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
