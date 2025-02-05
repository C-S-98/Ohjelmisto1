def gallon_litra(gallon):
    return gallon * 3.785


print("Syötä negatiivinen luku lopettaaksesi ohjelman.")

while True:
    try:
        gallonmaara = float(input("Anna gallonmäärän: "))
        if gallonmaara < 0:
            print("Kiitos käytöstä!")
            break

        litramaara = gallon_litra(gallonmaara)
        print(f"{gallonmaara} gallonaa = {litramaara} litraa")

    except ValueError:
        print("Syötä kelvollinen luku, kiitos.")