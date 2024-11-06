from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, titular, aniversario_conta):
        super().__init__(numero_agencia, "Poupança", saldo, limite, titular)
        self.aniversario_conta = aniversario_conta

    def calcular_juros_mensal(self, taxa_juros):
        juros = self.saldo * taxa_juros
        self.saldo += juros
        self.historico.registra_transacao(f"Juros de R${juros} aplicados")
