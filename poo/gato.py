# 9. Crie uma classe `Gato` que herda de `Animal` e adicione um método para o gato miar.
from poo.animal import Animal


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def fazer_som(self):
        print("Miau!")
