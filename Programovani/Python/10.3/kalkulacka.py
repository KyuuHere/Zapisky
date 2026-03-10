roblox=0
minecraft=float(input("Zadej první číslo: "))
fortnite=float(input("Zadej druhé číslo: "))
warthunder=input("Zadej operaci (+, -, *, /): ")
match warthunder:
    case "+":
        roblox = minecraft + fortnite
        print(f"{minecraft} {warthunder} {fortnite} = {roblox}")
    case "-":   
        roblox = minecraft - fortnite
        print(f"{minecraft} {warthunder} {fortnite} = {roblox}")
    case "*":
        roblox = minecraft * fortnite
        print(f"{minecraft} {warthunder} {fortnite} = {roblox}")
    case "/":
        if fortnite != 0:
            roblox = minecraft / fortnite
            print(f"{minecraft} {warthunder} {fortnite} = {roblox}")
            print(f"zbytek {minecraft % fortnite}")
        else:
            print("nelze delit nulou.")
    case _:
        print("chyba lobotom neplatici hodnota.")