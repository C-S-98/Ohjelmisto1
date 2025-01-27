pituus = float(input("Anna kuhan pituus senttimerteinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Kuha täytyy kasvaa vielä {puuttuu} cm, laita se takaisin.")
else:
    print("Kuha on sallittu pituudeltaan. \nOnnea kalastukseen!")