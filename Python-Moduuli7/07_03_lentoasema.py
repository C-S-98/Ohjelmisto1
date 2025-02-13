'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
    hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
    ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin
    ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
    kunnes hän haluaa lopettaa.

(ICAO-koodi on lentoaseman yksilöivä tunniste.
    Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
    Löydät koodeja helposti selaimen avulla.)
'''


# print("Jos haluat syöttää uuden lentoaseman, syötä [1] "
#       "\nHakea jo syötety lentoman tieto, syötä [2] "
#       "\nLopettaa syötä [3]\n")
#
# lentoasemat = {}
#
# while True:
#     kysy = input("Mitä haluat tehdä: ")
#
#     if kysy == "1":
#         icao = input("Syöte ICAO-koodi: ").upper()
#         if icao in lentoasemat:
#             print(f"ICAO-koodi {icao} jo olemassa: {lentoasemat[icao]}\n")
#         else:
#             nimi = input("syöte lentoaseman nimi: ")
#             lentoasemat[icao] = nimi
#             print(f"{nimi} lentoaseman ICAO-koodi on {icao}\n")
#
#     elif kysy == "2":
#         hake = input("Syöte ICAO-koodi: ").upper()
#         if hake in lentoasemat:
#             print(f"{hake} - {lentoasemat[hake]}\n")
#         else:
#             print(f"{hake} ei olemassa.\n")
#
#     elif kysy == "3":
#         print("Moi moi.")
#         break
#
#     else:
#         print("virhellinen syötä. Anna luku 1, 2 tai 3.")


def uusi(lentoasemat):
    icao = input("Syöte ICAO-koodi: ").upper()
    if icao in lentoasemat:
        print(f"ICAO-koodi {icao} jo olemassa: {lentoasemat[icao]}\n")
    else:
        nimi = input("syöte lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"{nimi} lentoaseman ICAO-koodi on {icao}\n")

def hake(lentoasemat):
    icao = input("Syöte ICAO-koodi: ").upper()
    if icao in lentoasemat:
        print(f"{icao} - {lentoasemat[icao]}\n")
    else:
        print(f"{icao} ei olemassa.\n")

def lopeta():
    print("Moi moi!")

def main():
    print("Jos haluat syöttää uuden lentoaseman, syötä [1] "
          "\nHakea jo syötety lentoman tieto, syötä [2] "
          "\nLopettaa syötä [3]\n")

    lentoasemat = {}

    while True:
        kysy = input("Mitä haluat tehtä: ")

        if kysy == "1":
            uusi(lentoasemat)
        elif kysy == "2":
            hake(lentoasemat)
        elif kysy == "3":
            lopeta()
            break
        else:
            print("virhellinen syötä. Anna luku 1, 2 tai 3.\n")

if __name__ == "__main__":
    main()