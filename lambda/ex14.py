# 14. **Exercício 14:** Use `filter` com uma função lambda para retornar strings de uma
# lista que começam com uma determinada letra.

nomes = ["Bruna", "Liz", "Antenor", "Juca", "Pedro", "Diogo", "Amanda", "Leonardo", "Davi"]
comecam_com_a = list(filter(lambda x: x[0] == "D", nomes))

print(comecam_com_a)
