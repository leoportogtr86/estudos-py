# 3. Crie uma classe `Banco` com os atributos `nome` e `saldo`. Adicione
# métodos para depósito, saque e exibição do saldo.
class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._saldo = 0

    def deposito(self, valor):
        self._saldo += valor

    def saque(self, valor):
        self._saldo -= valor

    @property
    def nome(self):
        return self._nome

    @property
    def saldo(self):
        return self._saldo
