#zjistim zda li je to palindrom bez funkce :)
slovo = input("Zadej slovo: ")
roblox = True
for i in range(len(slovo) // 2):
    if slovo[i] != slovo[-i - 1]:
        roblox = False
        break

if roblox:
    print("je palindrom.")
else:
    print("neni palindrom.")
    