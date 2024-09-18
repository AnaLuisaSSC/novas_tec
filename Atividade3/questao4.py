'''
4- Implemente uma função chamada aplicar_operacao que recebe até três parâmetros: até dois
números e uma função de operação (soma, subtração, multiplicação, divisão, resto, potência,
raiz, fatorial, logaritmo, cosseno, seno, tangente). A função aplicar_operacao deve retornar o
resultado da operação aplicada aos números. Crie funções separadas para cada operação
matemática e teste a função aplicar_operacao com elas. (Não utilize a biblioteca Math, faça cada
função separadamente como fizemos em sala para cosseno) (Sugestão: faça as operações
em módulos separados e chame tudo num módulo principal.
'''

def aplicar_operacao(a, b, operação)
    def soma(a, b):
        return a + b
    def subtracao(a, b):
        return a - b
    def multiplicacao(a, b):
        return a * b
    def divisao(a, b):
        if b != 0
            return a / b
        else:
            return "divisão por 0 não é permitida"
    def resto(a, b):
        return a % b
    def potencia(a, b):
        return a ** b
    def vaiz(a, b):
        return a ** 0.5
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n -1)
    def logaritmo(a, base):
        if a > 0 and base > 0 and base != 1:
            return a ** (1 / base)
        else:
            return "Logaritmo inválido"

    def cosseno(x):
        x = x * 3.1415 / 180  # converter para radianos
        cos = 0
        n = 0

        for i in range(0, 100, 2):
            fatorial = 1
            for num in range(1, i + 1):
                fatorial *= num

            termo = ((-1) ** n) * (x ** i) / fatorial
            cos += termo
            n += 1

        return cos

    def seno(x):
        x = x * 3.1415 / 180  # converter para radianos
        sen = 0
        n = 0

        for i in range(1, 100, 2):
            fatorial = 1
            for num in range(1, i + 1):
                fatorial *= num

            termo = ((-1) ** n) * (x ** i) / fatorial
            sen += termo
            n += 1

        return sen

    def tangente(x):
        return seno(x) / cosseno(x)

    operacoes = {
        'soma': soma,
        'subtracao': subtracao,
        'multiplicacao': multiplicacao,
        'divisao': divisao,
        'resto': resto,
        'potencia': potencia,
        'raiz': raiz,
        'fatorial': fatorial,
        'logaritmo': logaritmo,
        'cosseno': cosseno,
        'seno': seno,
        'tangente': tangente
    }

    operacao = input("Informe a operação (soma, subtracao, multiplicacao, divisao, resto, potencia, raiz, fatorial, logaritmo, cosseno, seno, tangente): ").strip().lower()

    if operacao in operacoes:
        if operacao in ['raiz', 'fatorial', 'cosseno', 'seno', 'tangente']:
            a = float(input("Informe o valor: "))
            resultado = operacoesoperacao
        elif operacao == 'logaritmo':
            a = float(input("Informe o valor: "))
            base = float(input("Informe a base: "))
            resultado = operacoesoperacao
        else:
            a = float(input("Informe o primeiro valor: "))
            b = float(input("Informe o segundo valor: "))
            resultado = operacoesoperacao
        
        print(f"O resultado da operação {operacao} é: {resultado}")
    else:
        print("Operação não reconhecida")

aplicar_operacao()