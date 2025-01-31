import random

def pi_laske(pisteidan_maara):
    piste = 0
    i = 0

    while i < pisteidan_maara:

        x = random.uniform(-1 , 1)
        y = random.uniform(-1 , 1)

        if x**2 + y**2 < 1:
            piste += 1

        i += 1

    pi = 4 * piste / pisteidan_maara
    return pi

pisteidan_maara = int(input("Anna arvottavien pisteiden määrä: "))

pi_likiarvo = pi_laske(pisteidan_maara)
print(f"Piin likiarvo on noin {pi_likiarvo}.")