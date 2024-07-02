#
# 1. **Adição de Elementos**:
# - Adicione o elemento 'tigre' ao final da lista `animais` usando o método `append()`.
# - Insira o elemento 'leão' na segunda posição da lista `animais` usando o método `insert()`.
# - Exiba a lista atualizada no console.

# 2. **Remoção de Elementos**:
# - Remova o elemento 'gato' da lista `animais` usando o método `remove()`.
# - Remova e exiba o último elemento da lista `animais` usando o método `pop()`.
# - Exiba a lista atualizada no console.


animais = ["gato", "cachorro", "elefante"]

animais.append("tigre")
animais.insert(1, "leão")

print(animais)

animais.remove("gato")
animais.pop()

print(animais)