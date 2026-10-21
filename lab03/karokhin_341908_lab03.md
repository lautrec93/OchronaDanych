Raport z laboratorium nr. 3

Imie i Nazwisko: Arsnei Karokhin
nr. indeksu: 341908
język: python
link do github:
identyfikator commitu:

Zadanie 1 – ECB i CBC

Dla ECB: U mnie to orzymało się tak, ze wszystkie 4 bloki mam równe (a5ba2b6280d433bccfe6a0461cb88c4e). I mam nstępne powtórzenia: 1 i 2, 1 i 3, 1 i 4, 2 i 3, 2 i 4, 3 i 4.

Dla CBC: A tu naodwrót zaden się nie powtórzył.

Po odszyfrowaniu oba wyniki są identyczne z wejściem 

Jest tak, ze ECB szyfruje kazdy blok niezaleznie, więc identyczne bloki tekstu dają identyczne  bloki kryptogramu, a w CBC kazdy blok jest łączony XOR z poprzednim kryptogramem lub IV, co ukrywa powtórzenia

Wyniki:
ECB
a5ba2b6280d433bccfe6a0461cb88c4e
a5ba2b6280d433bccfe6a0461cb88c4e
a5ba2b6280d433bccfe6a0461cb88c4e
a5ba2b6280d433bccfe6a0461cb88c4e
powtorzenia: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
zgodnosc: True
CBC
9b1d65602be278746efb510f0d640638
3ec636e2ae086ac20f96fb032eaae7ae
a0d6fded5e00e2c54d49a20946c9cebd
00b80a733d3244f06018db6ec1f0ddfc
powtorzenia: []
zgodnosc: True


Zadanie 2 – Szyfrowanie z hasłem

Wyniki testów wraz z długością danych:
1) puste dane – równe, 16B
2) 0123456789ABCDEF – równe, 32B
3) wiadomosc.txt – równe, 256B

Dwa szyfrowania tej samej wiadomości tym samym hasłem z nową solą i IV dają rózne kryptogramy.

Jezeli chodzi o róznicę między solą a IV, to sól jakby sprawia, zeby z tego samego hasła powstaje inny klucz, a IV sprawia, ze ten sam tekst pod tym samym kluczem daje inny kryptogram

Sól i IV mogą być jawne; CBC nie zapewnia integralności.

Wyniki:
puste dane: rowne = True, dlugosc kryptogramu = 16 B
0123456789ABCDEF: rowne = True, dlugosc kryptogramu = 32 B
wiadomosc.txt: rowne = True, dlugosc kryptogramu = 256 B
kryptogramy identyczne: False

Zadanie 3 – Odzyskanie słabego klucza

Jako odpowiedź to odrazu wypiszę wynik działania skryptu:

m 4.4536
b 7.9472
x 7.9490
o 7.9493
2 7.9502
klucz: m
pierwszy wiersz: Record 000. The archive contains laboratory notes about symmetric encryption and careful handling of binary files.

Kluczy jest tylko 36, bo klucz to jeden znak z 36-znakowego zbioru, który powtarza się 16 razy.

A ranking moze zawieść dla danych skompresowanych, bo one mają entropię bliską losowej, więc poprawny klucz nie wyróznia się niską warością H.
