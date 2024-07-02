# 1. **Método `count()`**:
# - Crie uma lista `cores` contendo: 'vermelho', 'azul', 'verde', 'azul', 'amarelo'.
# - Use o método `count()` para contar quantas vezes a cor 'azul' aparece na lista.

cores = ["vermelho", "azul", "verde", "azul", "amarelo"]
qtd = cores.count("azul")

print(qtd)

# 2. **Método `sort()` e `reverse()`**:
# - Crie uma lista `numeros_aleatorios` contendo: 4, 2, 9, 1, 5.
# - Ordene a lista em ordem crescente usando o método `sort()`.
# - Inverta a ordem dos elementos da lista usando o método `reverse()`.
# - Exiba a lista atualizada no console.
numeros_aleatorios = [4, 2, 9, 1, 5]

print(numeros_aleatorios)

numeros_aleatorios.sort()

print(numeros_aleatorios)

numeros_aleatorios.reverse()

print(numeros_aleatorios)
