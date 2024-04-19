import os

os.system("clear")

num = 1
contadorPar = 0
contadorImpar = 0
somaPar = 0
somaImpar = 0
par = 0
impar = 0

while num > 0:
    num = int(input("Digite os números: "))

if num < 0:
    if(num % 2 == 0):
        par = par + 1
        contadorPar += 1
        somaPar += par
    else:
        impar = impar + 1
        contadorImpar += 1
        somaImpar += impar


mediaPar = somaPar / contadorPar
mediaImpar = somaImpar / contadorImpar
numInseridos = impar + par

print(f"Média dos numeros pares: {mediaPar}")
print(f"Média dos números impares: {mediaImpar}")
print(f"Total de números: {numInseridos}")
