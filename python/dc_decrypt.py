#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

from fernet_encrypt_decrypt import *
import argparse
from os import path

FILE_SOURCE = 1
CLI_SOURCE  = 2


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

    parser.add_argument("--keyfile", help="file with encryption key. Defaults to 'keyfile'")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--filename", help="file with encrypted message")
    group.add_argument("--message", help="encrypted message passed on command line")

    return parser


def get_message_from_file(filename: str) -> bytes:
    f"""
    Reads in an encrypted message.
    
    :param filename: {str} filename containing the encrypted message 
    :return: 
    """
    fh = open(filename, 'r')
    contents = fh.read()
    fh.close()

    return contents.encode()


def get_encrypted_message(source: str, source_type: int) -> bytes:
    f"""
    Gets the encrypted message.
    
    :param source: {str}  the encrypted message (or filename containing it)
    :param source_type: {int} the type of the source (file or CLI)
    :return: 
    """
    if source_type == FILE_SOURCE:
        return get_message_from_file(source)

    if source_type == CLI_SOURCE:
        return source.encode()


def main():
    args = create_arguments().parse_args()

    keyfile = args.keyfile if args.keyfile else KEY_FILENAME

    key = get_key_from_file(keyfile)

    message_source = args.filename if args.filename else args.message
    source_type = FILE_SOURCE if args.filename else CLI_SOURCE

    message = get_encrypted_message(message_source, source_type)
    m = decrypt(key, message)
    print(m)


if __name__ == '__main__':
    main()
