# 7. **Exercício 7:** Crie uma lista de strings e use `sorted` com uma função lambda para
# ordenar a lista por ordem alfabética inversa.

nomes = ["Zilu", "Leo", "Amanda", "Bruna", "Arthur", "Lucas"]

nomes_ordenados = sorted(nomes, key=lambda x: x[::-1])

print(nomes_ordenados)
