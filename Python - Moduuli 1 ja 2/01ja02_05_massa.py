leiviskat = float(input("Anna leiviskät määrä: "))
naulat = float(input("Anna naulat määrä: "))
luotit = float(input("Anna luodit määrä: "))

leiviska_naula = 20
naula_luoti = 32
luoti_gramma = 13.3

kokonais_grammat = (
    leiviskat * leiviska_naula * naula_luoti * luoti_gramma +
    naulat * naula_luoti * luoti_gramma +
    luotit * luoti_gramma
)

kilogrammat = int(kokonais_grammat // 1000)
grammat = kokonais_grammat % 1000

print(f"Massa nykymittojen mukaan: \n{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")