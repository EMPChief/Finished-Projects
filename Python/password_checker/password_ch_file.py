import requests
import hashlib
from pathlib import Path


def fetch_pwned_password_hashes(prefix):
    url = 'https://api.pwnedpasswords.com/range/' + prefix
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Error: {response.status_code}")
        return []


def get_leak_count_for_password(hashes, password_hash):
    hashes = (line.split(":") for line in hashes)

    for hash_prefix, count in hashes:
        if hash_prefix == password_hash:
            return int(count)

    return 0


def calculate_password_hash(password):
    sha1hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1hash[:5], sha1hash[5:]
    hashed_passwords = fetch_pwned_password_hashes(prefix)

    return get_leak_count_for_password(hashed_passwords, suffix)


def main():
    file_path = Path(__file__).resolve().parent / "passwords.txt"

    try:
        with open(file_path, 'r') as file:
            passwords = file.read().splitlines()

        for password in passwords:
            leak_count = calculate_password_hash(password)

            if leak_count > 0:
                print(f"Your password ({password}) has been compromised {
                      leak_count} times.\nYou should change it!")
            else:
                print(f"Your password ({password}) is secure. Good job!")

        return "Done!"
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return "Failed"


if __name__ == "__main__":
    import sys
    sys.exit(main())
