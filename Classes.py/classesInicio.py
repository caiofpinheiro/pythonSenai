import os

os.system("clear")

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

print("Solicitando dados ao usuário")

cliente1 = Cliente("Leticia", 20)
cliente2 = Cliente("Daniel", 23)

print(f"Nome: {cliente1.nome}")
print(f"Idade: {cliente1.idade}")
print(f"Nome: {cliente2.nome}")
print(f"Idade: {cliente2.idade}")

