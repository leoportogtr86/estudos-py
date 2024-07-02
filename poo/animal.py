# 7. Crie uma classe `Animal` com os atributos `nome` e `idade`. Adicione
# um método para o animal fazer um som.
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("Argh!!")
