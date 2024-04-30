import os

os.system("clear")

# Função sem retorno.

def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

# Solicitando dados do usuário
logoSenai()
nome = input("Digite seu nome:")

logoSenai()
idade = int(input("Digite sua idade: "))

logoSenai()
peso = float(input("Digite seu peso: "))

# Exibindo dados para o usuário
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")