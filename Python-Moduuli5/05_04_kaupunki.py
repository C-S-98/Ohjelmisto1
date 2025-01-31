jarjesty = {1 : "ensimmäisen", 2 : "toisen", 3 : "komannen",
            4 : "neljännen", 5 : "viidennen"}
kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna {jarjesty[i + 1]} kaupunki: ")
    kaupungit.append(kaupunki)

print(f"\nKaupunit nimet ovat: ")
for kaupunki in kaupungit:
    print(kaupunki)