# 9. **Exercício 9:** Utilize `map` com uma função lambda para converter uma
# lista de graus Celsius em Fahrenheit.
# formula: (0°C × 9/5) + 32 = 32°F

lista_c = [10.4, 45.7, 12.4, 100.0]
lista_f = list(map(lambda c: (c * 9 / 5) + 32, lista_c))

print(lista_f)