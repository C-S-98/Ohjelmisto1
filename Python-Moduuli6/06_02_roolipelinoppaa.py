'''
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
    joka kysytään käyttäjältä ohjelman suorituksen alussa.
'''

import random

def noppaa(tahko):
    while True:
        x = random.randint(1, tahko)
        print(x)
        if x == tahko:
            break

print("Syötä negatiivinen luku lopettaaksesi ohjelman.")

while True:
    try:
        tahko = int(input("Anna tahkoja määrää: "))

        if tahko < 0:
            print("Kiitos käytöstä!")
            break

        noppaa(tahko)

    except ValueError:
        print("Syötä positiivinen kokonaisluku.")