# 22. **Exercício 22:** Crie uma função lambda que receba um nome e o transforme em
# um dicionário com chaves 'nome' e 'tamanho', onde 'tamanho' é o comprimento do nome.
lista = ["Leonardo", "Davi", "Liz", "Christianne", "a", "bola", "macaco"]
dic = list(map(lambda x: {x: len(x)}, lista))

print(dic)
