# 2. Escreva um programa que verifique se uma letra digitada é uma vogal ou consoante.
vogais = ["a", "e", "i", "o", "u"]
letra = input("Digite uma letra: ")

if letra in vogais:
    print("É uma vogal.")

if letra.isalpha() and len(letra) == 1 and letra not in vogais:
    print("É uma consoante.")
