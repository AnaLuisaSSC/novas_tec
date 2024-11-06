from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, titular, cheque_especial):
        super().__init__(numero_agencia, "Corrente", saldo, limite, titular)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if self.cheque_especial and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            self.historico.registra_transacao(f"Uso de cheque especial de R${valor}")
            return True
        else:
            print("Cheque especial indisponível ou limite insuficiente.")
            return False
