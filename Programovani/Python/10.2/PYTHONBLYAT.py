roblox=int(input("zadejte vysku:"))
minecraft=int(input("Zadejte vek:"))
fortnite=0

if roblox <=87:
    print("trpasliku vyfič")
    
else:
    if minecraft<=12:
        fortnite += 50

    elif minecraft <=18:
        fortnite +=100

    elif minecraft <=65:
        fortnite +=150

string=input("Fotka?: (ano/ne)")
if string=="ano":
    fortnite+=40
print(fortnite)