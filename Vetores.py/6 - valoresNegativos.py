import os

os.system("clear")

numReais =[]
somaPos = 0
qtdNegat = 0
contadorNeg = 0

for i in range(1,6):
    numeros = float(input("Digite os números: "))
    numReais.append(numeros)

for i in range(len(numReais)):
    if numReais[i] < 0:
        numReais[i] = 0
    
    print(f"Lista dos valores: {numReais[i]}")


