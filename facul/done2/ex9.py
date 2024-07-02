# #### Exercício 9: Entrada e Cálculo
#
# **Pergunta**: Escreva um programa que peça ao usuário para digitar seu peso e altura,
# calcule o IMC e exiba o resultado.
#

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

print(f"{imc:.2f}")
# ```python
# # Seu código aqui
# peso = float(input("Digite seu peso em kg: "))
# altura = float(input("Digite sua altura em metros: "))
# imc = peso / (altura ** 2)
# print(f"Seu IMC é {imc:.2f}")
# ```
