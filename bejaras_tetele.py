import random
from typing import List

# Feltöltés véletlen (random) értékekkel
szamok: List[int] = []
for i in range(6):
    szamok.append(random.randint(10, 99))

# Bejárás tétele
# Nincs szükség indexre
for i in szamok:
    print(i, end=' ')
print()

# Értékek és indexek rendelkezésre állnak
for i in range(len(szamok)):
    print(f'szamok[{i}] = {szamok[i]} ')

for index, item in enumerate(szamok):
    print(f'szamok[{index}] = {item}', end=' ')
print()
