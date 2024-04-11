import os

os.system("clear")

i: int

numero = int(input("Digite um número: "))

print("Tabuada de",(numero))
for i in range(0,11):
    print(f"{numero} x {i} = {numero * (i)}")
