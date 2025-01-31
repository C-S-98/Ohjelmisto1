import random

arpoo = random.randint(0,10)

print("Arpoo kokonaisluvun väliltä 1..10. ")

while True:
    arvaus = input("Arvauksesi on: ")

    try:
        arvaus = int(arvaus)
    except ValueError:
        print("Syötä kokonaisluku, kiitos!")
        continue

    if arvaus > arpoo:
        print("Liian suuri arvaus.")
    elif arvaus < arpoo:
        print("Liian pieni arvaus.")
    else:
        print("Oikein!")
        break
