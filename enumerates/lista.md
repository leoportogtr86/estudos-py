
### Exercício 3

**Questão:** Use `enumerate` para imprimir apenas os índices dos elementos de uma lista de números pares de 2 a 20.

```python
# Solução
numeros_pares = list(range(2, 21, 2))
for i, v in enumerate(numeros_pares):
    print(f'Índice: {i}')
```

### Exercício 4

**Questão:** Use `enumerate` para encontrar a posição do primeiro número negativo em uma lista de números.

```python
# Solução
numeros = [4, 5, -1, 7, -3, 2]
for i, v in enumerate(numeros):
    if v < 0:
        print(f'O primeiro número negativo está no índice: {i}')
        break
```

### Exercício 5

**Questão:** Use `enumerate` para somar os valores de uma lista de números, mas apenas os números em índices pares.

```python
# Solução
numeros = [10, 20, 30, 40, 50]
soma = 0
for i, v in enumerate(numeros):
    if i % 2 == 0:
        soma += v
print(f'Soma dos valores em índices pares: {soma}')
```

### Exercício 6

**Questão:** Dada uma lista de nomes, use `enumerate` para criar um dicionário que mapeia cada nome ao seu índice.

```python
# Solução
nomes = ['Alice', 'Bob', 'Carol']
nome_para_indice = {nome: i for i, nome in enumerate(nomes)}
print(nome_para_indice)
```

### Exercício 7

**Questão:** Use `enumerate` para inverter os índices e valores de uma lista de números.

```python
# Solução
numeros = [100, 200, 300]
indice_para_valor = {i: v for i, v in enumerate(numeros)}
print(indice_para_valor)
```

### Exercício 8

**Questão:** Use `enumerate` para imprimir elementos de uma lista junto com seus índices, mas apenas se o índice for
maior que 2.

```python
# Solução
cores = ['vermelho', 'verde', 'azul', 'amarelo', 'roxo']
for i, v in enumerate(cores):
    if i > 2:
        print(f'Índice: {i}, Cor: {v}')
```

### Exercício 9

**Questão:** Crie uma lista de números de 10 a 1. Use `enumerate` para criar uma nova lista onde cada elemento é o
produto do índice pelo valor correspondente.

```python
# Solução
numeros = list(range(10, 0, -1))
produtos = [i * v for i, v in enumerate(numeros)]
print(produtos)
```

### Exercício 10

**Questão:** Use `enumerate` para adicionar um índice a cada elemento de uma lista de strings e armazená-los em uma nova
lista.

```python
# Solução
animais = ['cachorro', 'gato', 'pássaro']
animais_com_indice = [f'{i}-{animal}' for i, animal in enumerate(animais)]
print(animais_com_indice)
```

### Exercício 11

**Questão:** Use `enumerate` para imprimir os elementos de uma lista de trás para frente, mostrando seus índices
originais.

```python
# Solução
numeros = [1, 2, 3, 4, 5]
for i, v in reversed(list(enumerate(numeros))):
    print(f'Índice original: {i}, Valor: {v}')
```

### Exercício 12

**Questão:** Use `enumerate` para criar uma lista de tuplas que contêm apenas os elementos em índices ímpares de uma
lista de números.

```python
# Solução
numeros = [10, 20, 30, 40, 50, 60]
tuplas_impares = [(i, v) for i, v in enumerate(numeros) if i % 2 != 0]
print(tuplas_impares)
```

### Exercício 13

**Questão:** Use `enumerate` para substituir todos os elementos de uma lista de strings por 'indice-valor'.

```python
# Solução
frutas = ['morango', 'abacaxi', 'manga']
frutas_modificadas = [f'{i}-{fruta}' for i, fruta in enumerate(frutas)]
print(frutas_modificadas)
```

### Exercício 14

**Questão:** Use `enumerate` para calcular a média ponderada de uma lista de números, onde o peso é o índice do
elemento.

```python
# Solução
numeros = [5, 10, 15, 20, 25]
peso_total = 0
soma_ponderada = 0
for i, v in enumerate(numeros):
    soma_ponderada += i * v
    peso_total += i
media_ponderada = soma_ponderada / peso_total
print(f'Média ponderada: {media_ponderada}')
```

### Exercício 15

**Questão:** Use `enumerate` para contar quantos elementos de uma lista de strings têm um comprimento maior que seu
índice.

```python
# Solução
palavras = ['um', 'dois', 'três', 'quatro', 'cinco']
contador = 0
for i, palavra in enumerate(palavras):
    if len(palavra) > i:
        contador += 1
print(f'Número de palavras com comprimento maior que o índice: {contador}')
```

Espero que esses exercícios e soluções ajudem a entender melhor o uso da função `enumerate` em Python! Se precisar de
mais alguma coisa, estou à disposição.