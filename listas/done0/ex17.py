# 17. Conte quantas vezes um número aparece em uma lista.
lista = [10, 20, 10, 30, 10, 40]

count = 0
procurado = 10

for i in lista:
    if procurado == i:
        count += 1

print(count)
