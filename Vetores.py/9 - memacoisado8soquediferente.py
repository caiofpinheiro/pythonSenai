import os

os.system("cls")

contadorPar = 0
contadorImpar = 0
contadorPos = 0
contadorNeg = 0
TOTALDENUMEROS = 5


while True:
    numeros = int(input("Digite os números: "))

    if numeros == 0:
        break

    if numeros % 2 == 0:
        contadorPar += 1
    else: 
        contadorImpar += 1

    if numeros > 0:
        contadorPos +=1
    else:
        contadorNeg +=1

os.system("cls")

print(f"Numeros Pares: {contadorPar}")
print(f"numeros Impar: {contadorImpar}")
print(f"Numeros Positivos: {contadorPos}")
print(f"Numeros Negativos: {contadorNeg}")
