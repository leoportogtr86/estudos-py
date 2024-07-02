# 20. Crie uma lista com os primeiros 10 números da sequência de Fibonacci.
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

print(fibonacci(10))
