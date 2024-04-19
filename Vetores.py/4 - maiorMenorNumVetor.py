import os

os.system("clear")

num =[]
maiorNum = 0
menorNum = 9999
contador = 0

for i in range(1,6):
    numero = int(input("Digite os números: "))
    num.append(numero)

for i in range(len(num)):
    if num[i] > maiorNum:
        maiorNum = num[i]

    if num[i] < menorNum:
        menorNum = num[i]


print(f"Menor Número: {menorNum}")
print(f"Maior Número: {maiorNum}")
