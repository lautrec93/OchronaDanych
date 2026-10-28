import hashlib
import hmac
import secrets

ITERACJE = 600000

baza = {}
with open("hasla.txt", encoding="utf-8") as f:
    for linia in f:
        linia = linia.strip()
        if linia:
            login, iteracje, sol, skrot = linia.split(":")
            baza[login] = (int(iteracje), bytes.fromhex(sol), bytes.fromhex(skrot))


def weryfikuj(login, haslo):
    if login not in baza:
        return False
    iteracje, sol, skrot = baza[login]
    wynik = hashlib.pbkdf2_hmac("sha256", haslo.encode("utf-8"), sol, iteracje, 32)
    return hmac.compare_digest(wynik, skrot)


def dodaj(login, haslo):
    sol = secrets.token_bytes(16)
    skrot = hashlib.pbkdf2_hmac("sha256", haslo.encode("utf-8"), sol, ITERACJE, 32)
    baza[login] = (ITERACJE, sol, skrot)
    return f"{login}:{ITERACJE}:{sol.hex()}:{skrot.hex()}"


print(weryfikuj("anna", "Kasztan-2026"))
print(weryfikuj("anna", "kasztan-2026"))
print(weryfikuj("piotr", "Żółw na łące"))
print(weryfikuj("kasia", "Kasztan-2026"))

dodaj("test1", "Wspolne-Haslo1")
dodaj("test2", "Wspolne-Haslo1")
print(baza["test1"][1] == baza["test2"][1])
print(baza["test1"][2] == baza["test2"][2])
print(weryfikuj("test1", "Wspolne-Haslo1"))
print(weryfikuj("test2", "Wspolne-Haslo1"))
