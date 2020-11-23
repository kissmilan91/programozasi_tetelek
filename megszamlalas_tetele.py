import random
from typing import List

# Megszámlálás tétele
# Megadott tulajdonságú értékek darabszáma
# Feladat: Számoljuk meg a 50-nél nagyobb páros számok darabszámát:

szamok: List[int] = []
for i in range(6):
    szamok.append(random.randint(10, 99))
print(szamok)

darab: int = 0
for i in szamok:
    if i % 2 == 0 and i > 50:
        darab += 1
print(f'Ötvennél nagyobb páros számok darabszáma: {darab}')
