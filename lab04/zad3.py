import hashlib


def wiersze(nazwa):
    with open(nazwa, "rb") as f:
        return f.read().split(b"\n")[:13]


def h24(dane):
    return hashlib.sha256(dane).hexdigest()[:6]


def wariant(linie, v):
    return b"".join(linie[i] + (b" " if (v >> i) & 1 else b"") + b"\n" for i in range(13))


oryginal = wiersze("oryginal.txt")
zmieniony = wiersze("zmieniony.txt")

slownik = {}
for v in range(8192):
    slownik.setdefault(h24(wariant(oryginal, v)), v)

h0 = h24(wariant(oryginal, 0))
para = None
licznik = 0
for v in range(8192):
    h = h24(wariant(zmieniony, v))
    if para is None and h in slownik:
        para = (slownik[h], v, h)
    if h == h0:
        licznik += 1

if para:
    print(f"Para: v_oryginal={para[0]}, v_zmieniony={para[1]}, h24={para[2]}")
else:
    print("Brak pary")
print(f"Liczba wariantow zmienionego z h24 rownym h24 oryginalu: {licznik}")
