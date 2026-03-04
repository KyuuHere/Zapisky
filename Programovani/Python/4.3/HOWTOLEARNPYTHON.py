roblox=int(input("Zadejte cislo:"))
if roblox<2 or roblox==1:
    print("cislo neni prvocislo")
    je_prvocislo = False
else:

    je_prvocislo = True
    for i in range(2, roblox):
        if roblox % i == 0:
            je_prvocislo = False
            
if je_prvocislo:
    print("cislo je prvocislo")

else:
    print("cislo neni prvocislo")
    