#  Copyright (c) 2021. Clinton Fernandes (clintonf@gmail.com

from cryptography.fernet import Fernet


def generate_key(filename: str) -> None:
    f"""
    Generates am assymetric cryptographic key file.
    :param filename: filename to write key to
    :return: {None}
    """
    key = Fernet.generate_key()

    fh = open(filename, 'w')
    fh.write(key.decode())
    fh.close()


def get_key_from_file(filename: str) -> str:
    f"""
    Gets an encryption key from a file.

    :param filename: filename for the encryption key
    :return: {str} encryption key
    """
    fh = open(filename, 'r')
    key = fh.read()
    fh.close()
    return key


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


def unpad (padded):
    pad = ord(padded[-1])
    return padded[:-pad]


def do_normal_test():
    filename = "keyfile"
    message = "Hi HoboCat!"

    generate_key(filename)

    pre_key = get_key_from_file(filename)
    key = Fernet(pre_key)

    encrypted_message = encrypt(key, message)
    print("Message:", message, "is encrypted as", encrypted_message.decode())

    decrypted_message = decrypt(key, encrypted_message)
    print("Decrypted message is:", decrypted_message)


def do_node_test():
    filename = "keyfile"
    pre_key = get_key_from_file(filename)
    key = Fernet(pre_key)

    encrypted_message = unpad("i4VedWYyZvLIBRWgJp8krIln1K2K1Bz6Derb9sDkDt0=")
    decrypted_message = decrypt(key, bytes(encrypted_message, 'utf8'))
    print("Decrypted message is:", decrypted_message)


def main():
    do_node_test()
    # do_normal_test()


if __name__ == '__main__':
    main()