print("Syöte tyhjän mekkijonon luputetaan.")

nimet = set()

while True:
    nimi = input("Nimi on: ")
    if nimi == "":
        break

    if nimi in nimet:
        print("Syöttö toistettiin.")

    else:
        nimet.add(nimi)

print("Syötetyt nimet: ", nimet)
for nimi in nimet:
    print(nimi)
