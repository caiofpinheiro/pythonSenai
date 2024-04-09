import os

os.system("clear")

numero1: int; numero2: int; numero3: int; numero4: int; numero5: int; soma: int
pares: int; impares: int

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))

soma = numero1 + numero2 + numero3 + numero4 + numero5

print(f"\nSoma dos números: {soma}")
