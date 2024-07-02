# 18. **Exercício 18:** Utilize `filter` com uma função lambda para retornar apenas palavras
# com mais de 5 caracteres de uma lista de strings.

lista = ["palavra", "amor", "teste", "qa", "java", "car", "switch", "data"]
lens = list(map(lambda x: len(x), lista))

print(lens)