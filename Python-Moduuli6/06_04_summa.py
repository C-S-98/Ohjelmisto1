'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma,
    jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
'''

import random

def laskin(luvut):
    summa = 0

    for luku in luvut:
        summa += luku

    return summa

luvut = [1, 2, 3, 4, 5, 6, 7]

print(laskin(luvut))


'''
def summa(luvut):
    return sum(luvut)

luvut = []

print("Syötä tyhjämerkki lopettaaksi ohjelman.")
while True:
    try:
        luku = input("Anna luku: ")

        if luku == "":
            print("Kiitos käytöstä!")
            break

        luku = int(luku)
        luvut.append(luku)

    except ValueError:
        print("Syötä kelvollinen luku.")

koko_summa =summa(luvut)
print(f"{luvut} summa on: {koko_summa}.")
'''


# for i in range(5):
#     x = random.uniform(1,100)
#     x = round(x, 2)
#     luvut.append(x)

# koko_summa =summa(luvut)
# print(f"{luvut} summa on: {koko_summa:.2f}.")