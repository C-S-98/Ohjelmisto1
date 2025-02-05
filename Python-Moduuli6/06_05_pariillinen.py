import random

def pari_luvut(luvut):

    pari = []
    for x in luvut:
        if x % 2 == 0:
            pari.append(x)
    return pari

luvut = []
for i in range(10):
    y = random.randint(1, 100)
    luvut.append(y)

pari_list = pari_luvut(luvut)
print(f"{luvut}:ssa \nparilliset luvut ovat:\n{pari_list}")