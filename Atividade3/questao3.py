'''
3- Codifique a função cpf(n,d) que devolve verdade só se o CPF n tem dígito verificador d. Use o
método descrito no exercício anterior para calcular o dígito verificador do CPF do seguinte
modo:
Suponha CPF =345702159.
a. calculamos o primeiro dígito a = dv(345702159) = 7.
b. calculamos o segundo dígito b = dv(3457021597) = 1.
Então, número completo do CPF é 345702159-71
'''

def cpf(n,d):
    n_str = str(n).zfill(9)  # garante que o CPF tenha 9 digitos, acoloca 0 a esquerda se necessario
    d_verificador = int(d)

    if len(n_str) != 9:
        raise ValueError("O CPF deve ter exatamente 9 dígitos.")

    soma1 = sum(int(n_str[i]) * (10 - i) for i in range(9))
    a = (soma1 * 10) % 11
    a = 0 if a >= 10 else a

    soma2 = sum(int(n_str[i]) * (11 - i) for i in range(9)) + a * 2
    b = (soma2 * 10) % 11
    b = 0 if b >= 10 else b

    return d_verificador == b

def obter_dados_usuario():
    try:
        # pega os valores inseridos e converte
        cpf_str = input("Digite o CPF (9 dígitos): ")
        digito_verificador = input("Digite o dígito verificador: ")

        # tira caracteres não numéricos do CPF
        cpf_str = ''.join(filter(str.isdigit, cpf_str))
        
        # digito vira int
        digito_verificador = int(digito_verificador)
        
        if len(cpf_str) != 9:
            raise ValueError("O CPF deve ter exatamente 9 dígitos.")

        if cpf(cpf_str, digito_verificador):
            print(f"O dígito verificador {digito_verificador} está correto para o CPF {cpf_str}.")
        else:
            print(f"O dígito verificador {digito_verificador} está incorreto para o CPF {cpf_str}.")
    
    except ValueError as e:
        print(f"Erro: {e}")

obter_dados_usuario()

'''
str(n) faz com que o n seja uma string
.zfill(9) - O método .zfill(width) é usado para preencher a string com zeros à esquerda até que a string atinja o comprimento especificado (width). No caso, 9 é o comprimento desejado.
          - Se a string original já tiver um comprimento igual ou maior que 9, ela não será alterada.
          - Por exemplo, se a string for "123", após aplicar .zfill(9), ela se tornará "000000123".
n_str[i]:                       Acessa o i-ésimo caractere da string n_str.
int(n_str[i]):                  Converte o caractere para um número inteiro.
(10 - i):                       Calcula o peso para o i-ésimo dígito. O peso começa em 10 e diminui até 2.
int(n_str[i]) * (10 - i):       Multiplica o dígito pelo seu peso.
sum(... for i in range(9)):     Soma todos esses produtos para os primeiros 9 dígitos de n_str.

'''