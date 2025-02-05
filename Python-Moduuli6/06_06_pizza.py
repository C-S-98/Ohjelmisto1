def pizza(a, b, c, d):
    paras = ""

    a_yksikko = b / a
    b_yksikko = d / c

    if a_yksikko < b_yksikko:
        paras = "\nPizza A on paremman vastineen rahalle.\n"
    elif b_yksikko < a_yksikko:
        paras = "\nPizza B on paremman vastineen rahalle.\n"
    else:
        paras = "\nPizzaa ovat samaa vastineen rahalle.\n"

    return paras

a = float(input("Anna A pizzan halkaisija(cm): "))
b = float(input("Anna A pizzan hinta(€): "))
c = float(input("Anna B pizzan halkaisija(cm): "))
d = float(input("Anna B pizzan hinta(€): "))

paremman = pizza(a, b, c, d)
print(paremman)


# while True:
#     try:
#         print("Syötä pizzan halkaisijan senttimetreinä ja hinnan euroina. "
#               "\nErottele numerot pilkulla .")
#
#         a, b = map(float, input("A pizza: ").split(","))
#         if a == 0 or b == 0:
#             print("Kiitos käytöstä!")
#             break
#
#         c, d = map(float, input("B pizza: ").split(","))
#         if c == 0 or d == 0:
#             print("Kiitos käytöstä!")
#             break
#
#         paremman = pizza(a, b, c, d)
#         print(paremman)
#
#     except ValueError:
#         print("Syötä kelvollinen luku.\n")