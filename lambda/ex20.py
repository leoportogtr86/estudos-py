# 20. **Exercício 20:** Use `map` com uma função lambda para adicionar um valor fixo a
# cada elemento de uma lista.
lista = [10, 20, 30, 40]
lista_2 = list(map(lambda x: x + 1, lista))

print(lista_2)
