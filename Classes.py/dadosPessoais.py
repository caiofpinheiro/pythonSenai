import os
from dataclasses import dataclass

os.system("clear")


def salvar_dados(lista):
    arquivo = "Funcionarios.txt"
    with open(arquivo, "w") as arquivoDeFunc:
        for funcionario in funcionarios:
            arquivoDeFunc.write(f"{funcionario.nome}, {funcionario.data_de_nascimento}, {funcionario.rg}, {funcionario.cpf} \n")

        print("Dados Gravados com êxito.")

def ler_dados_funcionarios(lista):
    arquivo_origem = "Funcionarios.txt"
    listaFuncionarios = []
    with open(arquivo_origem,"r") as arquivo:
        for linha in arquivo:
            nome, data_de_nascimento, rg, cpf = linha.strip().split(',')
            listaFuncionarios.append(Funcionario(nome=nome, data_de_nascimento=data_de_nascimento, rg=rg, cpf=cpf))

    print("\n >>> EXIBINDO DADOS <<<")
    for i in listaFuncionarios:
        print(f"Nome: {i.nome}")
        print(f"Data de Nascimento: {i.data_de_nascimento}")
        print(f"RG: {i.rg}")
        print(f"CPF: {i.cpf}")



FUNCIONARIOS_QTD = 5

@dataclass
class Funcionario:
    nome: str
    data_de_nascimento: str
    rg: str
    cpf: str

funcionarios = []

print(" >>> SOLICITANDO DADOS <<<")
for i in range(FUNCIONARIOS_QTD):
    funcionario = Funcionario(
        nome = input("Digite seu nome: "),
        data_de_nascimento = input("Digite sua data de nascimento: "),
        rg = input("Digite seu numero do RG: "),
        cpf = input("Digite seu CPF: ")
    )
    funcionarios.append(funcionario)

salvar_dados(funcionarios)
ler_dados_funcionarios(funcionarios)

