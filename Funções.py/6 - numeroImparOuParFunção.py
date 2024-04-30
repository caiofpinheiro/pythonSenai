import os

os.system("clear")

def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

def imparPar():
    num = int(input("Digite o número: "))
    os.system("clear")
    logoSenai()

    print(f"Número Informado: {num}")
    if num % 2 == 0:
        print("Número Par.")
    else:
        print("Número Impar.")


logoSenai()
imparPar()