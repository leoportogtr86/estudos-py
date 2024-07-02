# 17. **Exercício 17:** Use `map` com uma função lambda para calcular o fatorial dos
# números de uma lista.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(4))
