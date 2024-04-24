import os

os.system("cls")

contadorPar = 0
contadorImpar = 0
contadorPos = 0
contadorNeg = 0
TOTALDENUMEROS = 5
maiorNum = 0
menorNum = 9999
somaPar = 0
somaImpar = 0
positivo = 0
negativo = 0
par = 0
impar = 0

for i in range(TOTALDENUMEROS):
    numeros = int(input("Digite os números: "))

    if numeros % 2 == 0:
        par = par + 1
        somaPar += par
        contadorPar += 1
    else: 
        impar = impar + 1
        somaImpar += impar
        contadorImpar += 1

    if numeros > 0:
        positivo = positivo + 1
        contadorPos +=1
    else:
        negativo = negativo + 1
        contadorNeg +=1

    if numeros > maiorNum:
        maiorNum = numeros
    if numeros < menorNum:
        menorNum = numeros

mediaPar = somaPar / contadorPar
mediaImpar = somaImpar / contadorImpar
somaGeral = par + impar + positivo + negativo
contadorGeral = contadorNeg + contadorImpar + contadorPar + contadorPos
mediaGeral = somaGeral / contadorGeral


print(f"Maior Número: {maiorNum}")
print(f"Menor Número: {menorNum}")
print(f"Numeros Pares: {contadorPar}")
print(f"numeros Impar: {contadorImpar}")
print(f"Numeros Positivos: {contadorPos}")
print(f"Numeros Negativos: {contadorNeg}")
print(f"Total de numeros: {TOTALDENUMEROS}")
print(f"Média dos Pares: {mediaPar}")
print(f"Média dos Impares: {mediaImpar}")
print(f"Média Geral: {mediaGeral}")
    
for numeros in range(6, 1, -1):
    print(numeros)