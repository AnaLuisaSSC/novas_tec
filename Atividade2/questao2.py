'''
2- Numa certa agência bancária, as contas são identificadas por números de até seis dígitos
seguidos de um dígito verificador, calculado conforme exemplificado a seguir. Dado um número
de conta n, exiba o número de conta completo correspondente. Seja n = 7314 o número da
conta. Adicionamos os dígitos de n e obtemos a soma s = 4+1+3+7 = 15; Calculamos o resto
da divisão de s por 10 e obtemos o dígito d = 5. Número de conta completo: 007314-5
'''

num = input("digite o número da conta (até 6 dígitos):")

# soma dos digitos
soma = 0

for digito in num:
    soma += int(digito)

digito_verifica = 

# soma dos dígitos
soma = 0
for digito in num:
    soma += int(digito)

digito_verificador = soma % 10

numero_completo = f"{int(num):06d}-{digito_verificador}"

print(f"Número de conta completo: {numero_completo}")
