#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

from fernet_encrypt_decrypt import *
import argparse
from os import path


def create_arguments() -> argparse:
    f"""
    Parses command line arguments.

    :return: {argparse} 
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("overwrite", help="overwrite existing key")

    return parser


def main():
    args = create_arguments().parse_args()

    if path.isfile(KEY_FILENAME) and not args.overwrite:
        print("Error:", KEY_FILENAME, "already exists")
        exit(1)

    key = generate_key()
    fh = open(KEY_FILENAME, 'w')
    fh.write(key.decode())
    fh.close()
    print(KEY_FILENAME, "created with new encryption key")


if __name__ == '__main__':
    main()