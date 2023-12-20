import os
import time
from conversion_class import Hex, Binary, Text, Decimal

LOGS_DIRECTORY = "logs"
FILE_PATH = os.path.join(LOGS_DIRECTORY, "Binary_Hex_Text.txt")
ERROR_FILE_PATH = os.path.join(LOGS_DIRECTORY, "Binary_Hex_Text_Errors.txt")

# Create the logs directory once at the start of the program
os.makedirs(LOGS_DIRECTORY, exist_ok=True)

def log_conversion(operation, input_data, output_data):
    """
    Log the conversion operation details to a file.
    """
    time_object = time.gmtime()
    localtime = time.strftime("%Y-%m-%d %H:%M", time_object)

    with open(FILE_PATH, "a", encoding='utf-8') as f:
        try:
            f.write(f"{localtime} | Operation: {operation} | Input: {input_data} | Output: {output_data}\n")
        except IOError as e:
            log_error(f"Error writing to file: {e}")

def log_error(error_message):
    """
    Log an error message to a file.
    """
    with open(ERROR_FILE_PATH, "a", encoding='utf-8') as f:
        try:
            f.write(f"{error_message}\n")
        except IOError as e:
            print(f"Error writing error message to file: {e}")

# The rest of the code remains unchanged

if __name__ == "__main__":
    main()
