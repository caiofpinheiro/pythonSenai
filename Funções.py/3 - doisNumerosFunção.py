import os

os.system("clear")

# Logo senai

def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

# Soma 
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

# Média
def media(resultado):
    resultMedia = resultado / 2
    return resultMedia

# Solicitando dados ao usuário
logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))

logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)

mediaDosNumeros = media(soma)

# Exibindo ao usuário
logoSenai()
print(f"Soma dos Números: {soma}")
print(f"Média dos Números: {mediaDosNumeros}")
