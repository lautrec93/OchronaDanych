import math
from collections import Counter
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


def decrypt(key, data):
    dec = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
    return dec.update(data) + dec.finalize()


def entropy(data):
    n = len(data)
    return -sum(c / n * math.log2(c / n) for c in Counter(data).values())


with open("slaby_ecb.bin", "rb") as f:
    ct = f.read()

sample = ct[:4096]
results = sorted(((entropy(decrypt((ch * 16).encode(), sample)), ch) for ch in alphabet))

for h, ch in results[:5]:
    print(f"{ch} {h:.4f}")

best = results[0][1]
padded = decrypt((best * 16).encode(), ct)
unpadder = padding.PKCS7(128).unpadder()
text = (unpadder.update(padded) + unpadder.finalize()).decode("utf-8")
print("klucz:", best)
print("pierwszy wiersz:", text.splitlines()[0])
