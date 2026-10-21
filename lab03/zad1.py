import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

data = b"0123456789ABCDEF" * 4
key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
iv = os.urandom(16)

for name, mode in (("ECB", modes.ECB()), ("CBC", modes.CBC(iv))):
    enc = Cipher(algorithms.AES(key), mode).encryptor()
    ct = enc.update(data) + enc.finalize()
    bs = [ct[i:i + 16] for i in range(0, 64, 16)]
    print(name)
    for b in bs:
        print(b.hex())
    print("powtorzenia:", [(i + 1, j + 1) for i in range(4) for j in range(i + 1, 4) if bs[i] == bs[j]])
    dec = Cipher(algorithms.AES(key), mode).decryptor()
    print("zgodnosc:", dec.update(ct) + dec.finalize() == data)
