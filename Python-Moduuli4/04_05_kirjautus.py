i = 0

while i < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break

    else:
        print(f"Pääsy evätty.\nOlet syöttänyt {i + 1 } yritystä ja voit yrittää {4 - i} kertaa.")

    i = i + 1