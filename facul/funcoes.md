
#### Exercício 7: Função Lambda para Soma

**Pergunta**: Defina uma função lambda chamada `soma_lambda` que recebe dois parâmetros `a` e `b` e retorna a soma
deles.

```python
# Seu código aqui
soma_lambda = lambda a, b: a + b
print(soma_lambda(3, 4))  # Deve imprimir: 7
```

#### Exercício 8: Função com Múltiplos Parâmetros

**Pergunta**: Defina uma função chamada `calcular_area` que recebe dois parâmetros `largura` e `altura` (com valor
padrão de 10) e retorna a área de um retângulo.

```python
# Seu código aqui
def calcular_area(largura, altura=10):
    return largura * altura


print(calcular_area(5))  # Deve imprimir: 50
print(calcular_area(5, 20))  # Deve imprimir: 100
```

#### Exercício 9: Escopo de Variáveis

**Pergunta**: Defina uma função chamada `mostrar_escopo` que declare uma variável local `mensagem` com o valor "Variável
Local" e a imprima. Fora da função, declare uma variável global `mensagem` com o valor "Variável Global" e a imprima.

```python
# Seu código aqui
mensagem = "Variável Global"


def mostrar_escopo():
    mensagem = "Variável Local"
    print(mensagem)


mostrar_escopo()  # Deve imprimir: Variável Local
print(mensagem)  # Deve imprimir: Variável Global
```

#### Exercício 10: Função Recursiva para Somar uma Lista

**Pergunta**: Defina uma função recursiva chamada `somar_lista` que recebe uma lista de números e retorna a soma de seus
elementos.

```python
# Seu código aqui
def somar_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somar_lista(lista[1:])


print(somar_lista([1, 2, 3, 4, 5]))  # Deve imprimir: 15
```

Esses exercícios cobrem conceitos importantes de definição e uso de funções em Python, incluindo parâmetros, valores de
retorno, escopo de variáveis e funções lambda. Praticar esses exercícios ajudará a consolidar seu entendimento sobre
como trabalhar com funções de maneira eficiente.