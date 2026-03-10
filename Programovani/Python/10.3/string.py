heslo = input("Zadej heslo: ")


if len(heslo) < 8:
    print("Heslo je nepoužitelné.")
else:

    ma_male = any(c.islower() for c in heslo)
    ma_velke = any(c.isupper() for c in heslo)
    ma_cislo = any(c.isdigit() for c in heslo)
    ma_znak = any(not c.isalnum() for c in heslo)
    

    pocet_typu = sum([ma_male, ma_velke, ma_cislo, ma_znak])
    
    if pocet_typu == 1:  
        print("Heslo je hodně slabé.")
    elif pocet_typu == 2: 
        print("Heslo je slabé.")
    elif pocet_typu == 3:  
        print("Heslo je silné.")
    elif pocet_typu == 4:
        print("Heslo je hodně silné.")

