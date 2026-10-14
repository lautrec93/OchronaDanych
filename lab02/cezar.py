import sys
d = open(sys.argv[1], "rb").read()
ok = set(range(32, 127)) | {9, 10, 13}
dec = lambda k: bytes((c - k) % 256 for c in d)
r = sorted(((sum(b in ok for b in dec(k)) / len(d), k) for k in range(256)), key=lambda x: (-x[0], x[1]))
for s, k in r[:5]:
    print(k, round(s, 4), dec(k)[:60])
k = int(input("Wybierz k: "))
open("cezar.txt", "wb").write(dec(k))