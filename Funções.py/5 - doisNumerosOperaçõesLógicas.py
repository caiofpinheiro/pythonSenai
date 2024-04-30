import os

os.system("clear")

# Logo Senai
def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

# Definindo Funções
def somar(n1, n2):
    resultadoSoma = n1 + n2
    return resultadoSoma

def subtrair(n1 ,n2):
    resultadoSub = n1 - n2
    return resultadoSub

def multiplicar(n1, n2):
    resultadoMult = n1 * n2
    return resultadoMult

def dividir(n1, n2):
    resultadoDiv = n1 / n2
    return resultadoDiv

# Pedindo dados ao usuário
logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))

logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
subtracao = subtrair(primeiroNumero, segundoNumero)
multiplicacao = multiplicar(primeiroNumero, segundoNumero)
divisao = dividir(primeiroNumero, segundoNumero)

# Exibindo ao usuário
logoSenai()
print(f"Soma dos Números: {soma}")
print(f"Subtração dos Números: {subtracao}")
print(f"Multiplicação dos números: {multiplicacao}")
print(f"Divisão dos números: {divisao}")
