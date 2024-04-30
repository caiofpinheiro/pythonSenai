import os

os.system("clear")

def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

def produto():
    preco = float(input("Digite o preço do produto: "))
    inflaciona10 = preco * 0.1
    inflaciona20 = preco * 0.2
    if preco < 100:
        preco = inflaciona10 + preco

    if preco >= 100:
        preco = inflaciona20 + preco

    print(f"O preço do produto é: {preco}")


logoSenai()
produto()