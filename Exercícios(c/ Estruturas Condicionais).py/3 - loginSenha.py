import os

os.system("clear")

criarLogin = str(input("Digite seu login: "))
criarSenha = str(input("Digite sua senha: "))

loginCriado = ("Caio")
senhaCriada = ("Seila")

if loginCriado == criarLogin and criarSenha == senhaCriada:
    print("Bem vindo!!!")
else:
    print("Login ou senha inválida")


