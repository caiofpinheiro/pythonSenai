import os

os.system("clear")

notas =[]
contador = 0
soma = 0
media: float

for i in range(4):
     nota = float(input(f"Digite a nota de número {i + 1}: "))
     notas.append(nota)


os.system("clear")

for i in range(len(notas)):
     print(f"{i+1}ª Nota: {notas[i]}")
     soma += notas[i]
     contador += 1

media = soma / contador

print(f"Média das notas: {media}")

if media >= 7:
     print("Aprovado.")
elif media >= 5:
     print("Recuperação.")
else:
     print("Reprovado.")