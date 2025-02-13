'''
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
    kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
    joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
        syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
    allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
'''


print("Syöte tyhjän mekkijonon luputetaan.")

# nimet = set()

nimet = []
while True:
    nimi = input("Nimi on: ")
    if nimi == "":
        break

    if nimi in nimet:
        print("Syöttö toistettiin.")

    else:
        nimet.append(nimi)

print("Syötetyt nimet: ", nimet)
for nimi in nimet:
    print(nimi)
