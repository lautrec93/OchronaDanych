enc = lambda p, K:bytes((b + K[i % len(K)]) % 256 for i, b in enumerate(p))
dec = lambda c, K:bytes((b - K[i % len(K)]) % 256 for i, b in enumerate(c))
p = open("tekst_pl.txt", "rb").read()
c = enc(p, b"ZAMEK")
open("vigenere.bin", "wb").write(c)
print(dec(c, b"ZAMEK") == p)
print(dec(enc(b"", b"ZAMEK"), b"ZAMEK") == b"")
t = bytes([0, 255, 0, 255])
print(dec(enc(t, b"ZAMEK"), b"ZAMEK") == t)
for K in (b"SZYFR", b"KOD"):
    x = enc (b"BRAMABRAMABRAMA", K)
    print(K.decode(), x[:5]. hex(), x[5:10].hex(),
    x[10:15].hex())