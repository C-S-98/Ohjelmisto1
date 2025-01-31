print("Muunna tuumat senttimetreiksi."
      " \nJos haluat lopettaa ohjelman, kirjoita negatiivinen luku.")

while True:
    syote = input("Anna tuumamäärä: ")

    try:
        tuuma = float(syote)
        if tuuma < 0:
            print("Kiitos käytöstä.")
            break
        elif tuuma >= 0:
            print(f"{tuuma} tuuma = {tuuma * 2.54} cm")

    except ValueError:
        print("Syötä oikea tuumamäärä, kiitos!")


# while True:
#     syote = input("Anna tuumamäärä: ")
#
#     if not syote.replace('.', '', 1).isdigit() and not syote.lstrip('-').replace('.', '', 1).isdigit():
#         print("Syötä oikea numero.")
#         continue
#
#     tuuma = float(syote)
#     if tuuma < 0:
#         print("Ohjelma lopetetaan.")
#         break
#
#     print(f"{tuuma} tuuma = {tuuma * 2.54} cm")