# 24. **Exercício 24:** Utilize `filter` com uma função lambda para retornar strings
# que contenham a letra 'a' em uma lista de strings.
nomes = ["java", "c", "c++", "python", "ruby", "javascript", "Austin", "amora"]
start_a = list(filter(lambda a: a.startswith("a"), nomes))

print(start_a)