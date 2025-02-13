'''
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
    ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

- Yksi gallona on 3,785 litraa.

'''

def gallon_litra(gallon):
    return gallon * 3.785


print("Syötä negatiivinen luku lopettaaksesi ohjelman.")

while True:
    try:
        gallonmaara = float(input("Anna gallonmäärän: "))
        if gallonmaara < 0:
            print("Kiitos käytöstä!")
            break

        litramaara = gallon_litra(gallonmaara)
        print(f"{gallonmaara} gallonaa = {litramaara} litraa")

    except ValueError:
        print("Syötä kelvollinen luku, kiitos.")