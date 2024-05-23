import os
from dataclasses import dataclass

os.system("clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preço: float
def salvar_livros(lista):
    arquivo = "Catálogo_Livros.txt"
    with open(arquivo, "w") as arquivoDeLivros:
        for livro in livros:
            arquivoDeLivros.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preço} \n")
        print("Dados Gravados.")

LIVROS_QTD = 3

livros = []

def Solicitando_infos_livro():
    for i in range(LIVROS_QTD):
        livro = Livro(
        nome = input("Digite o nome do livro: "),
        autor = input("Digite o nome do autor do livro: "),
        categoria = input("Qual a categoria do livro? "),
        preço = float(input("Digite o preço do livro: "))
    )
    livros.append(livro)


Solicitando_infos_livro()
salvar_livros()