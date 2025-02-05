import random

def summa(luvut):
    return sum(luvut)

luvut = []

print("Syötä tyhjämerkki lopettaaksi ohjelman.")
while True:
    try:
        luku = input("Anna luku: ")

        if luku == "":
            print("Kiitos käytöstä!")
            break

        luku = float(luku)
        luvut.append(luku)

    except ValueError:
        print("Syötä kelvollinen luku.")

koko_summa =summa(luvut)
print(f"{luvut} summa on: {koko_summa}.")


# for i in range(5):
#     x = random.uniform(1,100)
#     x = round(x, 2)
#     luvut.append(x)

# koko_summa =summa(luvut)
# print(f"{luvut} summa on: {koko_summa:.2f}.")