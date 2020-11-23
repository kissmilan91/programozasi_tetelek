import random
from typing import List

# Eldöntés tétele:
# Megadott tulajdonságú érték megtalálható-e a listában?
# Feladat: Döntse el, hogy található-e páratlan szám a listában.

szamok: List[int] = []

vanParatlan: bool = False  # feltételezzük, hogy nincsenek páratlan számok a listában
for i in szamok:
    if i % 2 == 1:
        vanParatlan = True
        break
   # Így is jó:  
   #  print(f'A listában ' + ('van' if vanParatlan else 'nincs') + ' páratlan szám!')
print(f'A listában {"van" if vanParatlan else "nincs"} páratlan szám!')

if vanParatlan:
    print('A listában van páratlan szám!')
else:
    print('A listában nincs páratlan szám')
