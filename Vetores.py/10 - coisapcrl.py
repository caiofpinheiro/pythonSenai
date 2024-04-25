import os

os.system("clear")

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
somaGeral = 0
contadorGeral = 0
num = []

for i in range(TOTALDENUMEROS):
    
    contadorGeral += 1
    
    numeros = int(input("Digite os números: "))
    somaGeral += numeros

    num.append(numeros)

    if numeros % 2 == 0:
        par = par + 1
        somaPar = somaPar + num[i]
        contadorPar += 1
    else: 
        impar = impar + 1
        somaImpar = somaImpar +num[i]
        contadorImpar += 1

    if numeros > 0:
        positivo = positivo + 1
        contadorPos +=1
    else:
        negativo = negativo + 1
        contadorNeg +=1

    if num[i] > maiorNum:
        maiorNum = num[i]
    if num[i] < menorNum:
        menorNum = num[i]

mediaPar = somaPar / contadorPar
mediaImpar = somaImpar / contadorImpar
mediaGeral = somaGeral / contadorGeral

os.system("clear")

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
    
num.reverse()
print(num)