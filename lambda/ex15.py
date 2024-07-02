# 15. **Exercício 15:** Utilize uma função lambda dentro de `reduce` para concatenar uma
# lista de strings.
from functools import reduce

lista = ["hello", ", ", "world", "!"]

# res = reduce(lambda x, y: x + y, lista)
res = reduce(lambda a, b: a + b, lista)

print(res)
