import sys, math, time
from itertools import product
from collections import Counter


def rc4(key, data):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = bytearray()
    for b in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(b ^ S[(S[i] + S[j]) % 256])
    return bytes(out)


def H(d):
    n = len(d)
    return -sum(c / n * math.log2(c / n) for c in Counter(d).values())


c = open(sys.argv[1], "rb").read()

t = b"test RC4"
print("rc4(rc4(x)) == x:", rc4(b"abc", rc4(b"abc", t)) == t)

start = time.perf_counter()
wyniki = []
for k in product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    k = "".join(k).encode()
    wyniki.append((H(rc4(k, c[:512])), k))
czas = time.perf_counter() - start
wyniki.sort()

for h, k in wyniki[:5]:
    print(k.decode(), round(h, 4))
print("proby:", len(wyniki), "czas:", round(czas, 2), "s")

klucz = wyniki[0][1]
p = rc4(klucz, c)
open("rc4.txt", "wb").write(p)
print("klucz:", klucz.decode())
print(p[:200])
print("ponowne szyfrowanie == kryptogram:", rc4(klucz, p) == c)
print("H kryptogramu:", round(H(c), 4), "H odszyfrowania:", round(H(p), 4))