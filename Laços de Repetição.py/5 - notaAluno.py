import os

os.system("clear")

nota = int(input("Digite sua nota: "))

while nota < 0 or nota > 10:
    nota = int(input("Digite sua nota: "))

os.system("clear")

print(f"Nota informada pelo usuário: {nota}")