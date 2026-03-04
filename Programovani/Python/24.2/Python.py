fortnite = []
while(True):
    roblox=int(input("Zadej Cislo:"))
    if roblox==0:
      break
    fortnite.append(roblox)
    
fortnite.sort()
print(fortnite)
print("Suma:", sum(fortnite))
print("Cisel je:",len(fortnite))
print("Prumer je:",sum(fortnite)/len(fortnite))
print("nejvetsi cislo je:", fortnite[len(fortnite)-1])
