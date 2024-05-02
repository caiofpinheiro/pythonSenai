import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")
    
def imc(imcPeso, imcAltura):
    resultado = imcPeso / (imcAltura * imcAltura)
    return resultado

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)
    
    
    # Verificando resultados IMC.
    imcTotal = imc(peso, altura)
    
    

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"Imc total,  {imcTotal}")
    if imcTotal < 18.5:
        print("Abaixo do Peso.")
    elif imcTotal >= 18.5 and imcTotal < 25:
        print("Peso Normal.")
    elif imcTotal >= 25 and imcTotal < 30:
        print("Sobrepeso.")
    elif imcTotal >= 30 and imcTotal < 35:
        print("Obesidade grau I.")
    elif imcTotal >= 35 and imcTotal < 40:
        print("Obesidade grau II.")
    elif imcTotal >= 40:
        print("Obesidade grau III(mórbida.")

