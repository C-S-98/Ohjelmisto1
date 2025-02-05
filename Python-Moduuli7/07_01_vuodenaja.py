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
