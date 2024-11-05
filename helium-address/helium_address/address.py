import hashlib
import base58
import base64
from typing import Union, Tuple

class Address:
    def __init__(self, version: int, net_type: int, key_type: int, public_key: bytes):
        if version != 0:
            raise ValueError("unsupported version")
        self.version = version
        self.net_type = net_type
        self.key_type = key_type
        self.public_key = public_key

    @property
    def bin(self) -> bytes:
        """Get the binary representation of the address"""
        header = bytes([self.net_type | self.key_type])
        return header + self.public_key

    @property
    def b58(self) -> str:
        """Get the base58check representation of the address"""
        return self._bs58check_encode(self.version, self.bin)

    @property
    def b64(self) -> str:
        """Get the base64 representation of the address"""
        return base64.b64encode(self.bin).decode('ascii')

    @classmethod
    def fromB58(cls, b58_string: str) -> 'Address':
        """Create an Address from a base58check string"""
        try:
            binary = cls._bs58check_decode(b58_string)
            return cls.fromBin(binary)
        except Exception as e:
            raise ValueError(f"Invalid base58check address: {str(e)}")

    @classmethod
    def fromB64(cls, b64_string: str) -> 'Address':
        """Create an Address from a base64 string"""
        try:
            binary = base64.b64decode(b64_string)
            return cls.fromBin(binary)
        except Exception as e:
            raise ValueError(f"Invalid base64 address: {str(e)}")

    @classmethod
    def fromBin(cls, binary: bytes) -> 'Address':
        """Create an Address from binary data"""
        if len(binary) < 1:
            raise ValueError("Binary data too short")
        
        byte = binary[0]
        net_type = byte & 0xf0  # Extract upper 4 bits
        key_type = byte & 0x0f  # Extract lower 4 bits
        public_key = binary[1:]
        
        return cls(version=0, net_type=net_type, key_type=key_type, public_key=public_key)

    @staticmethod
    def _sha256(data: bytes) -> bytes:
        """Compute SHA256 hash of the input data"""
        return hashlib.sha256(data).digest()

    @staticmethod
    def _bs58check_encode(version: int, binary: bytes) -> str:
        """Encode binary data with version prefix in base58check format"""
        v_payload = bytes([version]) + binary
        checksum = Address._sha256(Address._sha256(v_payload))[:4]
        final_bytes = v_payload + checksum
        return base58.b58encode(final_bytes).decode('ascii')

    @staticmethod
    def _bs58check_decode(b58_string: str) -> bytes:
        """Decode a base58check string and verify its checksum"""
        decoded = base58.b58decode(b58_string)
        
        # Split into version+payload and checksum
        v_payload = decoded[:-4]
        checksum = decoded[-4:]
        
        # Verify checksum
        calculated_checksum = Address._sha256(Address._sha256(v_payload))[:4]
        if checksum != calculated_checksum:
            raise ValueError("Invalid checksum")
        
        # Return payload without version byte
        return v_payload[1:]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Address):
            return NotImplemented
        return (self.version == other.version and
                self.net_type == other.net_type and
                self.key_type == other.key_type and
                self.public_key == other.public_key)

    def __str__(self) -> str:
        return self.b58
