# 11. **Exercício 11:** Use `filter` com uma função lambda para retornar apenas os
# números pares de uma lista.
numeros = [1, 10, 13, 14, 15, 21, 25, 230, 789]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)