#! /usr/bin/env python

from cryptography.fernet import Fernet
from shutil import make_archive, unpack_archive
from os import path, listdir

# from original folder, encrypted = 133% size, encrypted & compressed = 102% size

KEY = 'example.key'
FILE = ''

TO_ARCHIVE = '../to_parent_folder'
FROM_DIR = '../directory_of_files/'
ARCHIVE_FORMAT = 'gztar'

FROM_ARCHIVE = '../compressed_file.tar.gz'
TO_DIR = '../uncompressed_directory'


def write_key(key_name):
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(key_name, "wb") as key_file:
        key_file.write(key)


def load_key(key_name: str):
    """
    Loads the key from the current directory named `key.key`
    """
    return open(key_name, "rb").read()


def encrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    with open(filename, 'rb') as file:
        d = file.read()
        
        d += b"=" * ((4 - len(d) % 4) % 4)
        f = Fernet(key)
        encrypted_data = f.encrypt(d)
    
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def encrypt_folder(foldername, key):
    for item in listdir(foldername):
        item_path = path.join(foldername, item)
        encrypt_file(item_path, key)


def decrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def decrypt_folder(foldername, key):
    for item in listdir(foldername):
        item_path = path.join(foldername, item)
        decrypt_file(item_path, key)


if __name__ == '__main__':
    # if you don't have a key, you will first need to make one with write_key()
    
    # then prior to encrypting/decrypting you will need to load the key:
    
    key = load_key(KEY)
    
    # to encrypt and compress a file or folder:
    
    # encrypt_file(FILE, key)
    encrypt_folder(FROM_DIR, key)
    make_archive(TO_ARCHIVE, ARCHIVE_FORMAT, FROM_DIR)
    
    # to decrypt and unpack a file or folder:
    
    # decrypt_folder(TO_DIR, key)
    # decrypt_file(FILE, key)
    # unpack_archive(FROM_ARCHIVE, TO_DIR)