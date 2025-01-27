sukupuoli = input("Anna sukupuolesi (nainen, mies): ").lower()
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":
    print("* Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.\n")
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo on korka.")
    else:
        print("Hemoglobiiniarvo on normaali.")

elif sukupuoli == "mies":
    print("* Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.\n")
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo on korka.")
    else:
        print("Hemoglobiiniarvo on normaali.")

else:
    print("Anna oikea biologinen sukupuolesi, kiitos!")