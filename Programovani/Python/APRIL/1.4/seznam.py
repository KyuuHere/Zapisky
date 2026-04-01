# min a max a rozdil bez funkce min/max

seznam = []

def minmax(seznam):
    if not seznam:
        return None, None
    mn = seznam[0]
    mx = seznam[0]
    for i in seznam:
        if i < mn:
            mn = i
        if i > mx:
            mx = i
    return mn, mx


def rozdil(seznam):
    mn, mx = minmax(seznam)
    if mn is None or mx is None:
        return 0
    return mx - mn


def main():
    print("Zadej seznam čísel, pro ukončení zadejte 0:")
    while True:
        cislo = int(input())
        if cislo == 0:
            seznam.append(cislo)
            break
        seznam.append(cislo)

    mn, mx = minmax(seznam)
    if mn is None:
        print("Žádná čísla nebyla zadána")
    else:
        print("Min:", mn)
        print("Max:", mx)
        print("Rozdíl:", rozdil(seznam))


if __name__ == "__main__":
    main()