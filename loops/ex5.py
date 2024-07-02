# 15. Escreva um programa que imprima a tabuada de um número digitado pelo usuário.
numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
