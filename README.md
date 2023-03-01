
# SpfChecker

Verifying SPF record.


## 📝 Description

SpfChecker is a python script that take domains in bulk, use python dns libary to verify dns records and write domains for which spf records are missing in no_spf.txt file.


## 🔧 Technologies & Tools

![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.9-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

## 📚 Requirements

- Python 3.9+
- pip3

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.

```bash
sudo apt-get install python3-pip
```

After that run the following commands:

```bash
pip install -r requirements.txt
            OR
pip3 install -r requirements.txt
```

## Usage
first paste all domains in 'domains.txt' file.

use any of below mentioned command accordingly to run the script:
```bash
python3 index.py
      OR
python index.py
```
