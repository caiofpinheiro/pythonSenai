import os

os.system("clear")

# Logo Senai
def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

def tabuada():
    logoSenai()
    numero = int(input("Digite um número: "))

    print(f"Tabuada de {numero}")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * (i)}")

logoSenai()
tabuada()