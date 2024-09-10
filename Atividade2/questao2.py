'''
2- Numa certa agência bancária, as contas são identificadas por números de até seis dígitos
seguidos de um dígito verificador, calculado conforme exemplificado a seguir. Dado um número
de conta n, exiba o número de conta completo correspondente. Seja n = 7314 o número da
conta. Adicionamos os dígitos de n e obtemos a soma s = 4+1+3+7 = 15; Calculamos o resto
da divisão de s por 10 e obtemos o dígito d = 5. Número de conta completo: 007314-5
'''

def calcular_digito_verificador(numero_conta):
    # Garante que o número da conta tem exatamente 6 dígitos
    numero_conta_formatado = f"{numero_conta:06d}"
    
    # Calcula a soma dos dígitos
    soma_dos_digitos = sum(int(digito) for digito in numero_conta_formatado)
    
    # Calcula o dígito verificador
    digito_verificador = soma_dos_digitos % 10
    
    # Formata o número da conta completo
    numero_conta_completo = f"{numero_conta_formatado}-{digito_verificador}"
    
    return numero_conta_completo

try:
    numero_conta = int(input("Digite o número da conta (até 6 dígitos): "))
    print(f"Número da conta completo: {calcular_digito_verificador(numero_conta)}")
except ValueError:
    print("Erro: insira um número inteiro válido.")
