##5. **Exercício 5:** Use `filter` com uma função lambda para retornar apenas os números positivos de uma lista.
lista = [10, 20, -12, 67, 90, -567]
positivos = list(filter(lambda x: x > 0, lista))

print(positivos)
