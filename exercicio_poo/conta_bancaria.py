from historico import Historico
from cliente import Cliente

class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, titular):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.titular = titular
        self.historico = Historico()

    def consultar_saldo(self):
        return self.saldo

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.registra_transacao(f"Saque de R${valor}")
            return True
        elif valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.historico.registra_transacao(f"Saque de R${valor} (com limite)")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def deposita(self, valor):
        self.saldo += valor
        self.historico.registra_transacao(f"Depósito de R${valor}")

    def transfere_para(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            self.historico.registra_transacao(f"Transferência de R${valor} para conta {destino.numero_agencia}")
        else:
            print("Transferência não realizada. Saldo insuficiente.")

    def obter_extrato(self):
        self.historico.imprime()

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular
        self.historico.registra_transacao(f"Titular alterado para {novo_titular.nome} {novo_titular.sobrenome}")

    def fechar_conta(self):
        saldo_remanescente = self.saldo
        self.saldo = 0
        self.historico.registra_transacao("Conta fechada")
        print(f"Conta fechada. Saldo remanescente de R${saldo_remanescente} transferido para o titular.")
        return saldo_remanescente
