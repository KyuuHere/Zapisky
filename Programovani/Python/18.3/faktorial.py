#faktorialni cisla 5!=120 a vypiše to 5x4x3x2x1=120
cislo=int(input("Zadej cislo: "))
faktorial=1
for i in range(1,cislo+1):
    faktorial*=i
    print(i,end="")
    if i<cislo:
        print("x",end="")
print(f"!= {faktorial}")