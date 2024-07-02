# 1. Escreva um programa que verifique se um número é positivo, negativo ou zero.
def status_num(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "zero"


print(status_num(10))
print(status_num(-10))
print(status_num(0))
