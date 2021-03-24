#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

from cryptography.fernet import Fernet

KEY_FILENAME = 'keyfile'

def generate_key() -> bytes:
    f"""
    Generates am assymetric cryptographic key file.
    :return: {bytes}
    """
    key = Fernet.generate_key()

    return key


def get_key_from_file(filename: str) -> Fernet:
    f"""
    Gets an encryption key from a file.

    :param filename: filename for the encryption key
    :return: {Fernet} encryption key
    """
    fh = open(filename, 'r')
    key = fh.read()
    fh.close()
    return Fernet(key)


def encrypt(key: Fernet, message: str) -> bytes:
    f"""
    Encrypts a message.

    :param key: cryptographic key
    :param message: message to encrypt
    :return: {bytes}
    """

    token = key.encrypt(message.encode())

    return token


def decrypt(key: Fernet, encrypted_message: bytes) -> str:
    f"""
    Decrypts a message.

    :param key: encryption key
    :param encrypted_message:  message to decrypt
    :return: {str}
    """

    decrypted_message = key.decrypt(encrypted_message)

    return decrypted_message.decode()
