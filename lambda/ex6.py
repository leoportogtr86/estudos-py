# 6. **Exercício 6:** Utilize uma função lambda dentro de `reduce` para calcular o
# produto de uma lista de números.
from functools import reduce

lista = [10, 20]

produto = reduce(lambda a, b: a * b, lista)

print(produto)
