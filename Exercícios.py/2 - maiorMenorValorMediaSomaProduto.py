import os

os.system("clear")

media: int; produto: int; soma: int; maiorValor: int; menorValor: int

maiorValor = 0
menorValor = 9999

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
media = soma / 2

produto = numero1 * numero2

if numero1 < numero2:
    maiorValor = numero2
    menorvalor = numero1
elif numero2 < numero1:
    menorValor = numero2
    maiorValor = numero1
elif numero2 == numero1:
    print("Os números sao iguais")


print(f"\nMedia dos números: {media}")
print(f"Soma dos números: {soma}")
print(f"Produto dos números: {produto}")
print(f"Maior Valor: {maiorValor}")
print(f"Menor valor: {menorValor}")
