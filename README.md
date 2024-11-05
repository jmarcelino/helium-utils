# Helium Utils

A collection of Python utilities for working with the Helium blockchain ecosystem. This repository aims to provide Python implementations of various utilities found in the official [helium-js](https://github.com/helium/helium-js) libraries.

## Packages

Currently available packages:

| Package | Description | JS Equivalent |
|---------|-------------|---------------|
| [helium-address](./helium-address) | Public key utilities for converting between base64 and base58check address formats | [@helium/address](https://github.com/helium/helium-js/tree/master/packages/address) |

## Quick Start

Each utility can be installed separately depending on your needs. See the README in each package directory for specific installation instructions.

Example installation for address utilities:
```bash
cd helium-address
pip install .
```

## Repository Structure

```
helium-utils/
├── README.md
├── LICENSE
├── helium-address/           # Address manipulation utilities
│   ├── README.md            # Package-specific documentation
│   ├── setup.py
│   └── helium_address/
│       ├── __init__.py
│       ├── address.py
│       └── cli.py
└── future-packages/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Related Projects

- [helium-js](https://github.com/helium/helium-js) - Official JavaScript implementations
- [helium/proto](https://github.com/helium/proto) - Protocol definitions
- [Helium Wallet](https://github.com/helium/helium-wallet-rs) - Official Rust implementation

## Support

- [Helium Discord](https://discord.gg/helium) - For general Helium discussions
- [GitHub Issues](https://github.com/jmarcelino/helium-utils/issues) - For bugs and feature requests
