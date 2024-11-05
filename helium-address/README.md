# Address Converter

A Python tool to convert base64 encoded blockchain addresses to base58check format.

## Installation Instructions for MacOS

### Prerequisites

1. Ensure you have Python 3.6 or later installed:
```bash
python3 --version
```

If Python is not installed, you can install it using Homebrew:
```bash
brew install python3
```

2. (Optional) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jmarcelino/helium-utils
cd helium-address
```

2. Install the package:
```bash
pip install .
```

### Dependencies

The following Python packages are required:
- `base58>=2.1.0`: For base58check encoding
- Python's built-in libraries:
  - `hashlib`: For SHA256 hashing
  - `base64`: For base64 decoding
  - `argparse`: For command line interface

## Usage

### As a Python Module

```python
from helium_address import Address

# Create an Address from a base64 string
b64_address = "AI90TxNbF3XXO1x8iAVc1tCPgruUGjkQKuR+YL6TOReV"
address = Address.fromB64(b64_address)

# Get different representations
print(f"Base58: {address.b58}")
print(f"Base64: {address.b64}")
print(f"Binary: {address.bin}")

# Create an Address from a base58check string
b58_address = "13buBykFQf5VaQtvkTz8oXyCRXeukrdGbwMD4rqhPRYA9KGh1u"
same_address = Address.fromB58(b58_address)

# Addresses can be compared
assert address == same_address

# Access address components
print(f"Net Type: {address.net_type}")
print(f"Key Type: {address.key_type}")
print(f"Public Key: {address.public_key.hex()}")
```

### As a Command Line Tool

#### Convert from Helium bin base64 to base58check (default)
```shell
helium-convert AI90TxNbF3XXO1x8iAVc1tCPgruUGjkQKuR+YL6TOReV
```

#### Convert from base58check to base64
```shell
helium-convert --from-b58 13buBykFQf5VaQtvkTz8oXyCRXeukrdGbwMD4rqhPRYA9KGh1u
```

#### Show both representations of a base64 encoded address
```shell
helium-convert -v AI90TxNbF3XXO1x8iAVc1tCPgruUGjkQKuR+YL6TOReV
```
#### Help
```shell
helium-convert --help
```

## Troubleshooting

If you see an error about missing dependencies, ensure you've installed them:
```bash
pip install base58
```

If you get a "command not found" error after installation, make sure your Python scripts directory is in your PATH. You can find it with:
```bash
python3 -m site --user-base
```
Then add `/bin` to that path in your ~/.zshrc or ~/.bash_profile:
```bash
export PATH="$(python3 -m site --user-base)/bin:$PATH"
```


