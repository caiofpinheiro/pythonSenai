import os

os.system("clear")

def logoSenai():
    os.system("clear")
    print(" >>> SENAI <<<")

def notaAluno(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

def mediaAluno(resultado):
    resultMed = resultado / 2
    return resultMed

def aprovadoReprovado(resultMed):
    if resultMed >= 7:
        print("Aprovado.")
    else:
        print("Reprovado")

