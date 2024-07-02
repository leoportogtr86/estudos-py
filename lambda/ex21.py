# 21. **Exercício 21:** Utilize `filter` com uma função lambda para retornar
# números de uma lista que são múltiplos de 3.
lista = [1, 3, 5, 6, 9, 10, 15, 16, 21, 22]
multiplos_de_3 = list(filter(lambda x: x % 3 == 0, lista))

print(multiplos_de_3)
