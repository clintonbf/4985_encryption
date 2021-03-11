import sys
from fernet_encrypt_decrypt import *

def main():
    message = sys.argv[1]

    pre_key = get_key_from_file("keyfile")
    key = Fernet(pre_key)
    e_message = encrypt(key, message)

    print(e_message)


if __name__ == '__main__':
    main()