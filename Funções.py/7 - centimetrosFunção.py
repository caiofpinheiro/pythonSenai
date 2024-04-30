import os

os.system("clear")

def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

def metros(num):
    resultado =  num * 100
    return resultado


numero = int(input("Digite quantos metros voce quer que sejam convertidos para centimetros: "))

numeros = metros(numero)

print(f"Metros convertidos: {numeros}")