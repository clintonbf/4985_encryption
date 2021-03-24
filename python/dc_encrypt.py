#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

import argparse
from fernet_encrypt_decrypt import *


def create_arguments() -> argparse:
    f"""
    Parses command line arguments.

    :return: {argparse}  
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("message", help="message to encrypt")
    parser.add_argument("--keyfile", help="encryption key file")

    return parser


def main():
    args = create_arguments().parse_args()

    keyfile = args.keyfile if args.keyfile else KEY_FILENAME

    key = get_key_from_file(keyfile)
    e_message = encrypt(key, args.message)

    print(e_message.decode())


if __name__ == '__main__':
    main()