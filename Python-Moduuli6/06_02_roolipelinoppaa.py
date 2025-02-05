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