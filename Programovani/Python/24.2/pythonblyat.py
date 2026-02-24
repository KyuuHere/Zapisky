for roblox in range(50,100, 5):
    print(roblox)

for roblox in range(100,50 -5):
    print(roblox)


roblox=50
while(roblox!=100):
        print(roblox)
        roblox+=5

roblox=int(input("Zadej prvni cislo:"))
minecraft=int(input("Zadejte druhe cislo"))
fortnite=int(input("Zadejte krok"))

p_cisel=0
soucet=0

if (roblox<minecraft):
    for i in range(roblox,minecraft+1, fortnite):
        print(i)
        p_cisel+=1
        soucet+=i

else:
    for i in range(roblox,minecraft-1,fortnite*(-1)):
        print(i)
        p_cisel+=1
        soucet+=i

prumer=soucet/p_cisel
print(prumer)