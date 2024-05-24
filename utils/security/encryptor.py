import hashlib
import base64
from cryptography.fernet import Fernet
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encryptor:

    def __init__(self, key: str):
        kdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b""
        )
        key = base64.urlsafe_b64encode(kdf.derive(key.encode()))
        self.cipher_suite = Fernet(key=key)

    def encrypt(self, plaintext: str) -> bytes:
        return self.cipher_suite.encrypt(plaintext.encode())

    def decrypt(self, ciphertext: bytes) -> str:
        return self.cipher_suite.decrypt(ciphertext).decode()
