print("Jos haluat lopettaa ohjelman, syöttää tyhjän merkkijonon.")

luvut = []

while True:
    syote = input("Syötetään luku: ")

    if syote == "" and len(luvut) >= 5:
        break
    elif syote == "" and len(luvut) < 5:
        print(f"Olet syöttänyt vain {len(luvut)} lukua. Syötä vähintään 5 lukua.")
        continue

    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä oikea luku, kiitos.")

luvut.sort(reverse = True)
suurinta = luvut[:5]

print(f"Viisi suurinta lukua suuruusjärjestyksessä: "
      f"{', '.join(f'{luku}' for luku in suurinta)}")


'''
luvut = []

syote = input("Anna kokonaisluku (tyhjä lopetta): ")
while syote != "":
    luku = int(syote)
    luvut.append(luku)
    syote = input("Anna kokonaisluku (tyhjä lopetta): ")
luvut.sort(reverse = True)

for i in range(5):
    print(luvut[i])
'''