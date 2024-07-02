# 5. Crie uma classe `Estudante` que herda de `Pessoa` e adicione o atributo `curso`.
from poo.pessoa import Pessoa


class Estudante(Pessoa):
    def __init__(self, nome, idade, sexo, curso):
        self.curso = curso
        super().__init__(nome, idade, sexo)
        self.curso = curso
