# 16. Escreva um programa que inverta uma string usando um loop `for`.
txt = "hello, world"
inversa = ""

for i in range(len(txt) - 1, -1, -1):
    inversa += txt[i]

print(inversa)
