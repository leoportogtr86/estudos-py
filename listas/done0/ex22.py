# 22. Some todos os elementos de uma lista de listas (matriz).
matriz = [[0, 1], [2, 3], [4, 5], [6, 7]]
lista = [item for sublista in matriz for item in sublista]
soma = 0

for i in lista:
    soma += i

print(lista)
print(soma)
# # Matriz original
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Espalhando os elementos da matriz em uma nova lista
# nova_lista = [item for sublista in matriz for item in sublista]
#
# print(nova_lista)
