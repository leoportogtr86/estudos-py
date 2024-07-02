# 12. **Exercício 12:** Utilize uma função lambda dentro de `map` para converter uma lista de
# strings para letras maiúsculas.

lista = ["amora", "melão", "uva"]
lista_maiusculas = list(map(lambda fruta: fruta.upper(), lista))

print(lista_maiusculas)