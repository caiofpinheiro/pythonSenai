import os

os.system("clear")

num =[]

for i in range(6):
    while True:
            numeros = int(input(f"Digite o {i+1}º número: "))
            if numeros >= 0 and numeros % 2 == 0:
                num.append(numeros)
                break

num.reverse()

print(num)
