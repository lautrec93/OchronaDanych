Raport z Laboratorium nr. 2

Zadanie 1 – Cezar

```
230 1.0 b'Wkh#Qljkw#Ihuu|\r\rWkh#qljkw#ihuu|#ohiw#wkh#kduerxu#dw#hohyhq/'
233 1.0 b'The Night Ferry\n\nThe night ferry left the harbour at eleven,'
228 0.9948 b'Ymj%Snlmy%Kjww~\x0f\x0fYmj%snlmy%kjww~%qjky%ymj%mfwgtzw%fy%jqj{js1'
229 0.9948 b'Xli$Rmklx$Jivv}\x0e\x0eXli$rmklx$jivv}$pijx$xli$levfsyv$ex$ipizir0'
231 0.9948 b'Vjg"Pkijv"Hgtt{\x0c\x0cVjg"pkijv"hgtt{"nghv"vjg"jctdqwt"cv"gngxgp.'
```

Dla przesunięcia wybrałem liczbę 233, bo patrząc na te wyniki, które wyświetlają się po uruchomieniu programu tylko 2 wybory miały ocenę 1.0, ale przy k=230 tekst jest nieczytelny i bezsensowny, więc 233 pasuje, jak najbardziej, ma 1.0 ocenę i tekst jest czytelny i ma sens, tekst jest po angielsku.


Mówiąc o entropii, ona nie rozstrzyga, bo w szyfrze Cezara każdy bajt jest zastępowany zawsze tym samym bajtem. Przesunięcie tylko przenosi słupki histogramu na inne wartości, nie zmieniając ich wysokości, więc entropia jest taka sama dla wszystkich 256 przesunięć.

Zadanie 2 – Vigenere

Testy (ZAMEK):
```
1) tekst_pl.txt -> vigenere.bin -> odszyfrowanie: True
2) puste dane: True
3) dane z bajtami 0 i 255: True
```

fragmenty po 5 bajtów (BRAMABRAMABRAMA):
```
SZYFR – 95ac9a9393 95ac9a9393 95ac9a9393
KOD – 8da1859890 869d90918c 91968c9c85
```

Dla klucza SZYFR (m=5) okres tekstu jest równy długości klucza, więc kazde "BRAMA" trafia na te same bajty klucza i daje takie same fragmenty kryptogramu. Dla KOD (m = 3) 5 nie jest wielokrotnością 3, więc kolejne powtórzenia są szyfrowane innymi bajtami klucza i fragmenty się różnią. Atakujący widzący powtarzające się bloki wie, że tekst jawny się powtarza, a z odległości między powtórzeniami może wyznaczyć długość klucza.

Zadanie 3 – RC4

test rc4(rc4(x)) == x: True

Ranking:
```
1) tat 4.391
2) neg 7.4304
3) mcn 7.4512
4) oxo 7.4536
5) tnx 7.4592
```

proby: 17576
czas: 1.35 s
klucz: tat

Odszyfrowanie jest sensownym tekstem angielskim ("The Clockmaker's Apprentice. On his first day in the workshop, Tomas was not allowed to touch a single clock..."). Ponowne szyfrowanie == kryptogram: True.

Entropia kryptogramu: 7.9271 bit/bajt
Entropia odszyfrowania: 4.3259 bit/bajt

Ponowne szyfrowanie odtwarza kryptogram dla dowolnego klucza, bo RC4 to XOR ze strumieniem: (c ^ K) ^ K = c. Test potwierdza tylko spójność implementacji, a nie poprawność klucza, o tym świadczy sensowny tekst i niska entropia. Ranking entropii mógłby zawieść, gdyby tekst jawny sam miał wysoką entropię albo gdyby analizowany fragment był zbyt krótki lub nietypowy i błędny klucz dałby porównywalną entropię.