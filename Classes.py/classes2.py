import os

os.system("clear")

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

print("Solicitando dados ao usuário")

clientes = []

for i in range(3):
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    clientes.append(Cliente(nome, idade))

for cliente in clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
