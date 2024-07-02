# 8. Crie uma classe `Cachorro` que herda de `Animal` e adicione um
# método para o cachorro latir.
from poo.animal import Animal


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def fazer_som(self):
        print("Au au!")
