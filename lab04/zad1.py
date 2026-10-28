import hashlib
from pathlib import Path


def sha256_pliku(sciezka):
    return hashlib.sha256(Path(sciezka).read_bytes()).hexdigest()


sumy = Path("SHA256SUMS.txt")
for linia in sumy.read_text(encoding="utf-8").splitlines():
    if not linia.strip():
        continue
    skrot, nazwa = linia[:64].lower(), linia[66:]
    plik = sumy.parent / nazwa
    if not plik.is_file():
        status = "BRAK"
    elif sha256_pliku(plik) == skrot:
        status = "OK"
    else:
        status = "BŁĄD"
    print(nazwa, status)

h1 = hashlib.sha256(b"Ala ma kota.").digest()
h2 = hashlib.sha256(b"Ola ma kota.").digest()
print(bin(int.from_bytes(h1, "big") ^ int.from_bytes(h2, "big")).count("1"))
