#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

from fernet_encrypt_decrypt import *
import argparse
from os import path


def check_for_keyfile(filename: str):
    f"""
    Checks for the existence of a file.
        
    :param filename: {str} file to check for 
    :return: 
    """

    if not path.isfile(filename):
        print("Error", filename, "not found")
        exit(1)


def create_arguments() -> argparse:
    f"""
    Parses command line arguments.
    
    :return: {argparse} 
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--keyfile", help="file with encryption key. Default = 'keyfile'")
    parser.add_argument("filename", help="file to decrypt")

    return parser


def get_message(filename: str) -> bytes:
    f"""
    Reads in an encrypted message.
    
    :param filename: {str} filename containing the encrypted message 
    :return: 
    """
    fh = open(filename, 'r')
    contents = fh.read()
    fh.close()

    return contents.encode()


def main():
    args = create_arguments().parse_args()

    keyfile = args.keyfile if args.keyfile else KEY_FILENAME

    key = get_key_from_file(keyfile)

    message = get_message(args.filename)
    m = decrypt(key, message)
    print(m)


if __name__ == '__main__':
    main()
