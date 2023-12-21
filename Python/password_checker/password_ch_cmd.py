import requests
import hashlib
import sys


def request_api_data(query_data):
    url = 'https://api.pwnedpasswords.com/range/' + query_data
    req = requests.get(url)
    if req.status_code == 200:
        return req.text.splitlines()
    else:
        print(f"Error: {req.status_code}")
        return []


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes)
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0


def hash_password(password):
    sha1hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_character, tail = sha1hash[:5], sha1hash[5:]
    response = request_api_data(first_five_character)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = hash_password(password)
        if count > 0:
            print(f"Your password ({password}) have been hacked {
                  count} times,\n you should change it!")
        else:
            print(f"Your password ({password}) you did a good job making it!")
    return "Done!"


sys.exit(main(sys.argv[1:]))
