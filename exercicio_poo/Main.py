from cliente import Cliente
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

cliente1 = Cliente("Maria", "Silva", "123.456.789-00")
conta_poupanca = ContaPoupanca(101, 1000, 500, cliente1, "2023-10-08")
conta_corrente = ContaCorrente(102, 2000, 1000, cliente1, True)

conta_poupanca.deposita(200)
conta_corrente.saca(300)
conta_poupanca.transfere_para(conta_corrente, 100)

print("Extrato Conta Poupança:")
conta_poupanca.obter_extrato()
print("\nExtrato Conta Corrente:")
conta_corrente.obter_extrato()
