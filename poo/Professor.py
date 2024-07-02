from poo.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, idade, sexo, disciplina):
        super().__init__(nome, idade, sexo)
        self.disiplina = disciplina

    def to_string(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "sexo": self.sexo,
            "disciplina": self.disiplina
        }

    # 6. Crie uma classe `Professor` que herda de `Pessoa` e adicione o atributo `disciplina`.
