# 4. **Exercício 4:** Crie uma lista de números e use `map` com uma função lambda para retornar o quadrado de cada número.
lista = [16, 25, 3, 5, 76, 298, 12]
quadrados = list(map(lambda x: x ** 2, lista))

print(quadrados)
