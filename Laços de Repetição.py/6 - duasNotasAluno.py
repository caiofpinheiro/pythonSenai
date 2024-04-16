import os

os.system("clear")

nota1 = -1
nota2 = -1


while nota1 < 0 or nota1 > 10:
    nota1 = int(input("Digite a primeira nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = int(input("Digite a segunda nota: "))

soma = nota1 + nota2
media = soma / 2

os.system("clear")

print(f"Primeira nota informada pelo usuário: {nota1}")
print(f"Segunda nota informada pelo usuário: {nota2}")
print(f"Medias das notas: {media}")
