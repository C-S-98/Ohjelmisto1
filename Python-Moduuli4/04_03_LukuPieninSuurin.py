print("Ohjelma tulostaa saaduista luvuista pienimmän ja suurimman."
      " \nJos haluat lopettaa ohjelman, syöttää tyhjän merkkijonon.")

luvut = []

while True:
    syote = input("Syötetään luku: ")

    if syote == "":
        print("Kiitos käytöstä.")
        break

    try:
        luku = float(syote)
        luvut.append(luku)

    except ValueError:
        print("Syötä oikea luku, kiitos.")

print(f"Pienin luku on {min(luvut)} ja suurin on {max(luvut)}.")