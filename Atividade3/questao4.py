'''
4- Implemente uma função chamada aplicar_operacao que recebe até três parâmetros: até dois
números e uma função de operação (soma, subtração, multiplicação, divisão, resto, potência,
raiz, fatorial, logaritmo, cosseno, seno, tangente). A função aplicar_operacao deve retornar o
resultado da operação aplicada aos números. Crie funções separadas para cada operação
matemática e teste a função aplicar_operacao com elas. (Não utilize a biblioteca Math, faça cada
função separadamente como fizemos em sala para cosseno) (Sugestão: faça as operações
em módulos separados e chame tudo num módulo principal.
'''

def aplicar_operacao(a=None, b=None, operacao=None):
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        if b != 0:
            return a / b
        else:
            return "Divisão por 0 não é permitida"

    def resto(a, b):
        return a % b

    def potencia(a, b):
        return a ** b

    def raiz(a):
        return a ** 0.5

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)

    def logaritmo(a, base):
        if a > 0 and base > 0 and base != 1:
            return a ** (1 / base)
        else:
            return "Logaritmo inválido"

    def cosseno(x):
        x = x * 3.1415 / 180  # converter para radianos
        cos = 0
        for i in range(0, 100, 2):
            fatorial = 1
            for num in range(1, i + 1):
                fatorial *= num
            termo = ((-1) ** (i // 2)) * (x ** i) / fatorial
            cos += termo
        return cos

    def seno(x):
        x = x * 3.1415 / 180  # converter para radianos
        sen = 0
        for i in range(1, 100, 2):
            fatorial = 1
            for num in range(1, i + 1):
                fatorial *= num
            termo = ((-1) ** ((i - 1) // 2)) * (x ** i) / fatorial
            sen += termo
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

    if operacao in operacoes:
        if operacao in ['raiz', 'fatorial', 'cosseno', 'seno', 'tangente']:
            a = float(input("Informe o valor: "))
            resultado = operacoes[operacao](a)
        elif operacao == 'logaritmo':
            a = float(input("Informe o valor: "))
            base = float(input("Informe a base: "))
            resultado = operacoes[operacao](a, base)
        else:
            a = float(input("Informe o primeiro valor: "))
            b = float(input("Informe o segundo valor: "))
            resultado = operacoes[operacao](a, b)
        
        print(f"O resultado da operação {operacao} é: {resultado}")
    else:
        print("Operação não reconhecida")

# Testando a função
aplicar_operacao(5, 3, 'soma')  # 8
aplicar_operacao(5, 3, 'subtracao')  # 2
aplicar_operacao(5, 3, 'multiplicacao')  # 15
aplicar_operacao(5, 3, 'divisao')  # 1.666...
aplicar_operacao(5, 3, 'resto')  # 2
aplicar_operacao(5, 3, 'potencia')  # 125
aplicar_operacao(9, operacao='raiz')  # 3.0
aplicar_operacao(5, operacao='fatorial')  # 120
aplicar_operacao(8, 2, 'logaritmo')  # 3.0
aplicar_operacao(60, operacao='cosseno')  # aproximadamente 0.5
aplicar_operacao(30, operacao='seno')  # aproximadamente 0.5
aplicar_operacao(45, operacao='tangente')  # aproximadamente 1.0