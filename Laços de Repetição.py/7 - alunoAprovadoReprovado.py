import os

os.system("clear")

nota1 = -1
nota2 = -1
nota3 = -1

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite a primeira nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite a segunda nota: "))

while nota3 < 0 or nota3 > 10:
    nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/ 3


os.system("clear")

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

print(f"Primeira nota informada pelo usuário: {nota1}")
print(f"Segunda nota informada pelo usuário: {nota2}")
print(f"Terceira nota informada pelo usuário: {nota3}")
print(f"Medias das notas: {media}")