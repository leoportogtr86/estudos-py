# #### Exercício 5: Função para Calcular Fatorial
#
# **Pergunta**: Defina uma função chamada `fatorial` que recebe um número `n` e
# retorna o fatorial de `n`.
#
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(4))

# ```python
# # Seu código aqui
# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n - 1)
#
#
# print(fatorial(5))  # Deve imprimir: 120
# ```
