import os

os.system("cls")

notas =[]

for i in range(7):
     nota = float(input(f"Digite a nota de número {i + 1}: "))
     notas.append(nota)


os.system("clear")

for i in range(len(notas)):
     print(f"{i+1}ª Nota: {notas[i]}")