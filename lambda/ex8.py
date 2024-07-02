# 8. **Exercício 8:** Use uma função lambda para criar uma lista de tuplas onde o primeiro
# elemento é um número e o segundo é seu cubo.

numeros = [1, 2, 3, 4, 5, 6, 7]
par_numero_cubo = list(map(lambda x: (x, x ** 3), numeros))

print(par_numero_cubo)
