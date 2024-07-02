# 14. Escreva um programa que conte quantos números negativos existem em uma lista.
lista = [-78, 100, -7, -8, 12, 45, 768, 4565, -100]
negativos = 0

for i in lista:
    if i < 0:
        negativos += 1

print(f"A lista tem {negativos} números negativos.")
