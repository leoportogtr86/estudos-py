# 13. **Exercício 13:** Crie uma lista de dicionários e use `sorted` com uma função lambda
# para ordenar os dicionários por um campo específico.

pessoas = [
    {"nome": "Juca", "idade": 10},
    {"nome": "Ana", "idade": 20},
    {"nome": "Zé", "idade": 15},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 25},
    {"nome": "João", "idade": 40}
]

print(sorted(pessoas, key=lambda x: x["idade"]))
print(sorted(pessoas, key=lambda x: x["nome"]))
