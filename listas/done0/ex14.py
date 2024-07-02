# 14. Crie uma lista de 10 números aleatórios e ordene-a em ordem crescente.
import random

lista = []

for i in range(0, 10):
    lista.append(random.randint(1, 100))

print(lista)

ordenada = sorted(lista)

print(ordenada)
