# 1. **Fatiamento Básico**:
# - Crie uma lista `numeros` contendo os números de 0 a 9.
# - Exiba uma sublista com os elementos de índice 2 a 5 (inclusive).
# - Exiba uma sublista com os primeiros 4 elementos.
# - Exiba uma sublista com os elementos a partir do índice 5.

# 2. **Fatiamento com Passo**:
# - Exiba uma sublista contendo todos os elementos em posições ímpares da lista `numeros`.

numeros = list(range(0, 10))
sub = numeros[1:5]
primeiros_4 = numeros[:4]
apos_5 = numeros[5:]
lista_indices_impares = []

for i in numeros:
    if i % 2 != 0:
        lista_indices_impares.append(numeros[i])

print(numeros)
print(sub)
print(primeiros_4)
print(apos_5)
print(lista_indices_impares)
