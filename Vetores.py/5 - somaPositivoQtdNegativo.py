import os

os.system("clear")

numReais =[]
somaPos = 0
qtdNegat = 0
contadorNeg = 0

for i in range(1,11):
    numeros = float(input("Digite os números: "))
    numReais.append(numeros)

for i in range(len(numReais)):
    if numReais[i] > 0:
        somaPos += numReais[i]
    
    if numReais[i] < 0:
        contadorNeg += 1

os.system("clear")

print(f"Quantidade de negativos: {contadorNeg}")
print(f"Soma dos positivos: {somaPos}")
