import random
from typing import List

# Összegzés tétele

szamok: List[int] = []
for i in range(60):
    szamok.append(random.randint(10, 99))
print(szamok)

# határozzuk meg az 5-tel osztható számok átlagát!
db_oszt5: int =0
osszeg_oszt5 = 0
for i in szamok:
    if i % 5 == 0:
        db_oszt5 += 1
        osszeg_oszt5 += i
if db_oszt5 == 0:
    print('Nincs a listában öttel osztható szám')
else:
    print(f'Az öttel osztható számok darabszáma: {db_oszt5}')
    print(f'Az összegük: {osszeg_oszt5} és az átlaguk: {osszeg_oszt5 / db_oszt5}')
