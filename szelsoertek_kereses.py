import random
from typing import List

# Szélsőérték (minimum, maximum) keresése
szam: int = 0
szamok: List[int] = []
for i in range(60):
    szamok.append(random.randint(10, 20))
print(szamok)

# Határozzuk meg a legnagyobb elem/elemek értékét!
max: int = szamok[0]  # Az első elemre "legnagyobbként tekintünk"
for i in szamok:
    if szam > max:
        max = szam
print(f'A legnagyobb szám értéke {max}')

# Határozzuk meg a legkisebb elem értékét és indexét
# Holtverseny esetén elegendő az elsőt megadni

legkisebb: int=0 # Az első elemre "legkisebbként tekintünk"
for i in range(1, len(szamok)):
    if szamok[i] < szamok[legkisebb]:
        legkisebb = i
print(f'A legkisebb szám értéke {szamok[legkisebb]}, indexe {legkisebb}')

# Holtverseny esetén kiírjuk az összes elem indexét
print(f'Legkisebb elem(ek) indexei: ', end=' ')
for i, item in enumerate(szamok):
    if (item == szamok[legkisebb]):
        print(i, end='. ')
print()


# nem nevezhető ki az első elem a legkisebb/legnagyobb elemnek
# Határozzuk meg a legnagyobb páratlan szám értékét és indexét a listában

legnagyobb_paratlan: int = -1
for i, item in enumerate(szamok):
    if item % 2 == 1:   # Ha páratlan
        if legnagyobb_paratlan == -1:   # Az első páratlan szám a listában 
            legnagyobb_paratlan = i   # Erre tekintünk a legnagyobb páratlan számként
        else:
            if item > szamok[legnagyobb_paratlan]:
                legnagyobb_paratlan = i
if legnagyobb_paratlan == -1:
    print('Nincs a vektorban páratlan szám')
else:
    print(f'A legnagyobb páratlan szám értéke: {szamok[legnagyobb_paratlan]}, indexe: {legnagyobb_paratlan}')
