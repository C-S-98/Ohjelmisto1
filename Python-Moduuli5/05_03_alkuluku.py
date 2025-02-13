try:
    luku = int(input("Anna kokonaisluvu: "))

    jaka_luvut = []

    for i in range(1, luku):
        if luku % i == 0:
            jaka_luvut.append(i)

    if len(jaka_luvut) < 2:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")

except ValueError:
    print("Anna oikea kokonaisluvu, kiitos.")