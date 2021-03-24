# 4985_encryption

This project is split into two parts:
1. a Python script to provide AES 128-bit CBC encryption. AES encryption is symmetric.
2. a Node.js script to call the Python script.

The python scripts can be used as-is. The Node script is an example of how to incorporate the Python script into Node files.

**NOTE** The Node example works for Linux (and maybe Mac) *only*. It *will not* work on Windows. It can be easily adapted by changing the system call to the Python script.
