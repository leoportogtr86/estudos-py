# 19. **Exercício 19:** Crie uma função lambda que receba um número e verifique se ele é primo.
is_primo = lambda x: all(x % i != 0 for i in range(2, x))

print(is_primo(11))
