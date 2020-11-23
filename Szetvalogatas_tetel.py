import random
from typing import List

# Szétválogatás tétele
szam: int = 0
szamok: List[int] = []
for i in range(10):
    szamok.append(random.randint(1, 99))
print(szamok)

# Válogassuk szét a páros és páratlan számokat
paros_szamok: List[int] = []
paratlan_szamok: List[int] = []
for i in szamok:
    if i % 2 ==0:
        paros_szamok.append(i)
    else:
        paratlan_szamok.append(i)
print(f'A páros lista: {paros_szamok}')
print(f'A páratlan lista: {paratlan_szamok}')

# Javítani kell!
