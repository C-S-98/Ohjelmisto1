import random

try:
    maara = int(input("Anna arpakuutioiden lukumäärä: "))
    summa = 0

    for _ in range(maara):
        silmaluku = random.randint(1, 100)
        # print(silmaluku)
        summa += silmaluku

    print(f"Arpakuutioiden silmälukujen summa on {summa}.")

except ValueError:
    print("Syötä oikea määrä, kiitos.")