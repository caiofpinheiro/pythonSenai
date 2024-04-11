import os

os.system("clear")

numero1: int; numero2: int; resultado: int
operacao: str

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = str(input("Digite a operação(*+-/): "))

if operacao == "*":
    resultado = numero1 * numero2

elif operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "/":
    resultado = numero1 / numero2

print(f"Resultado: {resultado}")



    
