import os

os.system("clear")

# Função com retorno.
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

# Solicitando Dados ao usuário.
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)

# Exibindo ao usuário.
print(f"Soma: {soma}")