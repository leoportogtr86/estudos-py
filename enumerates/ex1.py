#
# ### Exercício 1
#
# **Questão:** Crie uma lista de números de 1 a 10. Use `enumerate` para imprimir o
# índice e o valor de cada elemento.
#

lista = list(range(1, 11))

for i, v in enumerate(lista):
    print(f"O valor {v} está no índice {i}")

# ```python
# # Solução
# numeros = list(range(1, 11))
# for i, v in enumerate(numeros):
#     print(f'Índice: {i}, Valor: {v}')
# ```
