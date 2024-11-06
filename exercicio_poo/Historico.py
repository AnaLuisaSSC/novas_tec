from datetime import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.now()
        self.transacoes = []

    def registra_transacao(self, transacao):
        self.transacoes.append(f"{datetime.now()} - {transacao}")

    def imprime(self):
        print("Data de Abertura:", self.data_abertura)
        print("Transações:")
        for transacao in self.transacoes:
            print(transacao)
