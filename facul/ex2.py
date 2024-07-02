# #### Exercício 2: Classificação de Notas
#
# **Pergunta**: Escreva um programa que classifique uma nota (0 a 100) em A, B, C ou D
# usando instruções `if`, `elif` e `else`.
#

nota = float(input("Digite o valor da nota: "))

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("D")
# ```python
# # Seu código aqui
# nota = int(input("Digite a sua nota: "))
# if nota >= 90:
#     print("A")
# elif nota >= 80:
#     print("B")
# elif nota >= 70:
#     print("C")
# else:
#     print("D")
# ```
