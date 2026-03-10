celkem = int(input("Zadej částku: "))
dvoutisic = 0
tisic = 0
petset = 0
dvesta = 0
sto = 0
padesat = 0
dvacet = 0
deset = 0
pet = 0
dva = 0
jedna = 0
if celkem >= 2000:
    dvoutisic = celkem // 2000
    celkem = celkem - (dvoutisic * 2000) 
if celkem >= 1000:
    tisic = celkem // 1000
    celkem = celkem - (tisic * 1000)
if celkem >= 500:
    petset = celkem // 500
    celkem = celkem - (petset * 500)
if celkem >= 200:
    dvesta = celkem // 200
    celkem = celkem - (dvesta * 200)
if celkem >= 100:
    sto = celkem // 100
    celkem = celkem - (sto * 100)
if celkem >= 50:
    padesat = celkem // 50
    celkem = celkem - (padesat * 50)
if celkem >= 20:
    dvacet = celkem // 20
    celkem = celkem - (dvacet * 20)
if celkem >= 10:
    deset = celkem // 10
    celkem = celkem - (deset * 10)
if celkem >= 5:
    pet = celkem // 5
    celkem = celkem - (pet * 5)
if celkem >= 2:
    dva = celkem // 2
    celkem = celkem - (dva * 2)
jedna = int(celkem)

print(f"2000: {dvoutisic}")
print(f"1000: {tisic}")
print(f"500: {petset}")
print(f"200: {dvesta}")
print(f"100: {sto}")
print(f"50: {padesat}")
print(f"20: {dvacet}")
print(f"10: {deset}")
print(f"5: {pet}")
print(f"2: {dva}")
print(f"1: {jedna}")