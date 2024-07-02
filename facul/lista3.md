
#### Exercício 3: Loop `for` com Lista

**Pergunta**: Escreva um programa que percorra uma lista de nomes e imprima cada nome.

```python
# Seu código aqui
nomes = ["Ana", "João", "Maria"]
for nome in nomes:
    print(nome)
```

#### Exercício 4: Loop `while`

**Pergunta**: Escreva um programa que use um loop `while` para imprimir os números de 1 a 10.

```python
# Seu código aqui
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
```

#### Exercício 5: Usando `break`

**Pergunta**: Escreva um programa que percorra os números de 1 a 10 e pare a execução quando encontrar o número 5.

```python
# Seu código aqui
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

#### Exercício 6: Usando `continue`

**Pergunta**: Escreva um programa que percorra os números de 1 a 10 e pule os números pares.

```python
# Seu código aqui
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

#### Exercício 7: Verificação de Par e Ímpar

**Pergunta**: Escreva um programa que verifique se um número é par ou ímpar e imprima uma mensagem apropriada.

```python
# Seu código aqui
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")
```

#### Exercício 8: Soma de uma Lista

**Pergunta**: Escreva um programa que some todos os números em uma lista e imprima o resultado.

```python
# Seu código aqui
numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
print(f"A soma dos números é {soma}")
```

#### Exercício 9: Média de Notas

**Pergunta**: Escreva um programa que calcule a média de uma lista de notas e imprima o resultado.

```python
# Seu código aqui
notas = [70, 85, 78, 92, 88]
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
print(f"A média das notas é {media:.2f}")
```

#### Exercício 10: Encontrando o Maior Número

**Pergunta**: Escreva um programa que encontre e imprima o maior número em uma lista.

```python
# Seu código aqui
numeros = [10, 5, 8, 3, 12, 7]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
print(f"O maior número é {maior}")
```

Esses exercícios cobrem conceitos importantes de controle de fluxo em Python, permitindo que você pratique a criação de
condições, loops e comandos de controle de loop.