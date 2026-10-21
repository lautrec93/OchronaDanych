import os
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = "TestoweHaslo#2026"


def derive_key(salt):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=200000)
    return kdf.derive(password.encode("utf-8"))


def encrypt(data):
    salt = os.urandom(16)
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded = padder.update(data) + padder.finalize()
    enc = Cipher(algorithms.AES(derive_key(salt)), modes.CBC(iv)).encryptor()
    return salt, iv, enc.update(padded) + enc.finalize()


def decrypt(salt, iv, ct):
    dec = Cipher(algorithms.AES(derive_key(salt)), modes.CBC(iv)).decryptor()
    padded = dec.update(ct) + dec.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()


with open("wiadomosc.txt", "rb") as f:
    message = f.read()

tests = [("puste dane", b""), ("0123456789ABCDEF", b"0123456789ABCDEF"), ("wiadomosc.txt", message)]
for name, data in tests:
    salt, iv, ct = encrypt(data)
    print(f"{name}: rowne = {decrypt(salt, iv, ct) == data}, dlugosc kryptogramu = {len(ct)} B")

ct1 = encrypt(message)[2]
ct2 = encrypt(message)[2]
print(f"kryptogramy identyczne: {ct1 == ct2}")
