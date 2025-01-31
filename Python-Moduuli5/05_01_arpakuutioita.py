import random

maara = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0
for _ in range(maara):
    silmaluku = random.randint(1, 100)
    summa += silmaluku

print(f"Arpakuutioiden silmälukujen summa on {summa}.")