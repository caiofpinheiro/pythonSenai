import os
from dataclasses import dataclass

os.system("clear")

def salvar_livros(lista):
    arquivo = "Catálogo_Livros.txt"
    with open(arquivo, "w") as arquivoDeLivros:
        for livro in livros:
            arquivoDeLivros.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preço} \n")
        print("Dados Gravados.")

def ler_dados_catálogo(lista):
    arquivo_origem = "Catálogo_Livros.txt"
    listaLivros = []
    with open(arquivo_origem, "r") as arquivo:
        for linha in arquivo:
          nome, autor, categoria, preço = linha.strip().split(',')
          listaLivros.append(Livro(nome=nome, autor=autor, categoria=categoria, preço=float(preço)))

    print("\n Exibindo dados.")
    for i in listaLivros:
        print(f"Nome: {i.nome}")
        print(f"Autor: {i.autor}")
        print(f"Categoria: {i.categoria}")
        print(f"Preço: {i.preço}")

         

LIVROS_QTD = 3

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preço: float

livros = []

print("Solicitando infos do livro. \n")
for i in range(LIVROS_QTD):
    livro = Livro(
        nome = input("Digite o nome do livro: "),
        autor = input("Digite o nome do autor do livro: "),
        categoria = input("Qual a categoria do livro? "),
        preço = float(input("Digite o preço do livro: "))
    )
    livros.append(livro)

salvar_livros(livros)
ler_dados_catálogo(livros)