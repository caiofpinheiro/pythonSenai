import os
#Limpa o terminal
os.system("clear")

#Solicitando dados ao usuario

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))

#print(f""") = exibe dados no terminal


#Exibindo dados ao usuario
print(f"\n>>> Exibindo resultados <<<")
print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"Peso:  {peso:.1f}kg")