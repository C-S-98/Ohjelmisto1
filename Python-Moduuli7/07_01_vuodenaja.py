'''
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
    jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
    (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia
    vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
    että joulukuu on ensimmäinen talvikuukausi.
'''


def vuodenaika(kuukausi):
    vuodenajat = ("talvi", "talvi",
                  "kevät", "kevät", "kevät",
                  "kesä", "kesä", "kesä",
                  "syksy", "syksy", "syksy",
                  "talvi")

    if 1 <= kuukausi <= 12:
        return vuodenajat[kuukausi - 1]
    else:
        return "Anna nuomero välillä 1-12."


try:
    kuukausi = int(input("Anna kuukauden numero (1-12): "))
    kuukauta = {1: "Tammikuu",
                2: "Helmikuu",
                3: "Maaliskuu",
                4: "Huhtikuu",
                5: "Toukokuu",
                6: "Kesäkuu",
                7: "Heinäkuu",
                8: "Elokuu",
                9: "Syyskuu",
                10: "Lokakuu",
                11: "Marrskuu",
                12: "Joulukuu"}

    print(f"{kuukauta[kuukausi]} on {vuodenaika(kuukausi)}.")

except ValueError:
    print("Virheellinen syöte. Anna kokonaisluku välillä 1-12.")


'''
vuodenaika_tupa = {"talvi", "kevät", "kesä", "syksy"}

kuukausi = int(input("Anna kuukausi numeroa (1-12): "))

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    print(vuodenaika_tupa[0])

elif 2 < kuukausi > 6:
    print(vuodenaika_tupa[1])

elif 5 < kuukausi > 9:
    print(vuodenaika_tupa[2])

elif 8 < kuukausi > 12:
    print(vuodenaika_tupa[3])

elif kuukausi > 12:
    print("Syöte nuomero 1 - 12.")
'''