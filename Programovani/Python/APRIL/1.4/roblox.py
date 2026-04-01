# POMOCÍ funkce: dostane pole čísel a dělitel (číslo) a vrátí pole bez násobků dělitele

def delitel(seznam, delitel):
    return [i for i in seznam if i % delitel != 0]


def main():
    cisla = []
    print("Zadej seznam čísel, pro ukončení zadejte 0:")
    while True:
        cislo = int(input())
        if cislo == 0:
            break
        cisla.append(cislo)

    vysledek = delitel(cisla, 3)
    print("Čísla která nejsou dělitelná 3 jsou:", vysledek)


if __name__ == "__main__":
    main()
