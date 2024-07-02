# 12. Crie uma lista de números ímpares entre 1 e 20.
lista = []

for i in range(1, 21):
    if i % 2 != 0:
        lista.append(i)

print(lista)
