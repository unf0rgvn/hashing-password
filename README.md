# 🔒 Hashing Password

This tool takes a file and hashes the content inside of it. The objective is receive a worlist and transform every line in hash format specified by the user. The formats supported so far are: MD5, SHA1, SHA256 and SHA512. 

Currently supported formats are: **MD5, SHA1, SHA256 and SHA512**.

---

## 📂 How it works?

This program receives a wordlist file and generates the hashes corresponding which line, according the algorithm specified by the user.

### ✅ **Usage example**
```bash
usage: hashing-password.py [-h] [-H HASH] [-o OUTPUT] file

positional arguments:
  file                  You need to pass the file to hash the content inside of it.

options:
  -h, --help            show this help message and exit
  -H HASH, --hash HASH  Select the type of hash you want (Default: MD5). Types: [ 1
                        - MD5 | 2 - SHA1 | 3 - SHA256 | 4 - SHA512 ]
  -o OUTPUT, --output OUTPUT
                        Export the output to a file.
```

```bash
python hashing-password.py wordlist.txt -o hashes.txt -H SHA256
```
---
## 📌 Installation
```bash
pip install argparse hashlib
```
