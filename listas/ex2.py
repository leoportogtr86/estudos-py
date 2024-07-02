#
# 1. **Acesso a Elementos**:
# - Acesse e exiba o primeiro e o último elemento da lista `animais`.

# 2. **Modificação de Elementos**:
# - Modifique o segundo elemento da lista `animais` para 'papagaio'.
# - Exiba a lista atualizada no console.
animais = ["cavalo", "cão", "gato", "gavião"]
primeiro = animais[0]
ultimo = animais[len(animais) - 1]

print(primeiro, ultimo)

animais[1] = "baleia"

print(animais)