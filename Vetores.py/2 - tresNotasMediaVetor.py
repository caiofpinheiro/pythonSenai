import os

os.system("cls")

notas =[]
contador = 0
soma = 0

for i in range(3):
     nota = float(input(f"Digite a nota de número {i + 1}: "))
     notas.append(nota)


os.system("clear")

for i in range(len(notas)):
     print(f"{i+1}ª Nota: {notas[i]}")
     soma += notas[i]
     contador += 1

media = soma / contador

print(f"Média das notas: {media}")
