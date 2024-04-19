import os

os.system("clear")

num =[]
contador = 0
force = 0

while num[i] > 0 and num[i] % 2 == 0:
    for i in range(1,7):
        numeros = int(input(f"Digite o {i+1}º número"))
        num.append(numeros)

        for i in range(7,1):
            print(f"{i+1}º Número: ")