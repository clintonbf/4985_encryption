# 4985 encryption

This is the encryption and demo repository for the voting machine project.


This project is split into two parts:
1. Python scripts to provide AES 128-bit CBC encryption and decryption. AES is a symmetric algorithm.
2. Node.js scripts to call the Python script.

### Python scripts

The python scripts can be used as-is. The main ones are
* ```dc_encrypt.py <message to encrypt> [--keyfile KEYFILE]```
* ```dc_decrypt.py <encrypted file>     [--keyfile KEYFILE]```

An encryption keyfile is included in the repo. This is a terrible practice (I can think of few that are worse) but, for the 4985 project purpose, it's fine.  

A python script is included to generate new encryption keys (dc_generate_encryption_key.py)

### Node scripts

The Node scripts are examples of how to incorporate the Python scripts into Node files.  
They will need to be adapted to suit the specific purpose.

**NOTE**: The Node example works for Linux (and maybe Mac) *only*. It *will NOT* work on Windows. It can be easily adapted by changing the system call to the Python script.
