import os

os.system("clear")

idade = int(input("Digite sua idade: "))

if idade < 18 or idade > 65:
    print("Não é obrigado a votar.")
else:
    print("Obrigatório votar.")