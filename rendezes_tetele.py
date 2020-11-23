import random
from typing import List

# rendezés tétele
szam: int = 0
szamok: List[int] = []
for i in range(10):
    szamok.append(random.randint(1, 99))
print(szamok)

# 1. feladat: Animáció keresése az algoritmus szemléltetéséhez
# 2. feladat: rendezzük a számok lista elemeit növekvő rendben a "buborékos" rendezés algoritmusával
# 3. feladat: Írjuk ki a rendezett lista elemeit
# Számok vektor cseréje

# cseréljük fel a 3. és 4. indexű elemet a számok vektorban

# Print(szamok)
# index: int = 3
# csere = szamok[index]
# szamok[index] = szamok[index + 1]
# szamok[index + 1] = csere
# # Print(szamok)