import os

os.system("clear")

contador = 0
soma = 0
num = 0

while num >= 0:
    num = int(input("Digite um número: "))
    
    if num > 0:
        contador += 1
        soma += num


media = soma / contador

os.system("clear")

print(f"Média dos números inseridos: {media}")