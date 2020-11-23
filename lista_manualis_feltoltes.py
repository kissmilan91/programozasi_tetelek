from typing import List

nevek: List[str] = list()
print('Kérem a neveket 0-végjelig!')
inputNév: str = ''
while inputNév != '0':
    inputNév = input('Név: ')
    if inputNév != 0 and len(inputNév) != 0:
        nevek.append(inputNév)
print(nevek)
