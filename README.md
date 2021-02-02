# Encryption and Compression of Text Files
### Encryption
- symmetric encryption using the [Fernet](https://cryptography.io/en/latest/fernet.html) module from the [Cryptography](https://cryptography.io/en/latest/index.html) package
### Compression
- compression using the [shutil](https://docs.python.org/3/library/shutil.html) standard python library
    - this script archives to a gzip tar file but other formats are available, see the [python documentation](https://docs.python.org/3/library/shutil.html#shutil.make_archive)