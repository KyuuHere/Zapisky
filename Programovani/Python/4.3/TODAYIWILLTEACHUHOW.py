roblox=int(input("Zadej prvni cislo:"))
minecraft=int(input("Zadejte druhe cislo"))  


zacatek = min(roblox, minecraft)
end = max(roblox, minecraft)


def prvo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


print(f"Prvocisla mezi {zacatek} a {end} jsou:")
for pivo in range(zacatek, end + 1):
    if prvo(pivo):
        print(pivo)
