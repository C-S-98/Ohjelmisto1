'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen
    kuin parametrina saatu lista paitsi
    että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
    ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
'''

import random

def pari_luvut(luvut):

    pari = []
    for x in luvut:
        if x % 2 == 0:
            pari.append(x)
    return pari

luvut = []
for i in range(10):
    y = random.randint(1, 100)
    luvut.append(y)

pari_list = pari_luvut(luvut)
print(f"{luvut}:ssa \nparilliset luvut ovat:\n{pari_list}")