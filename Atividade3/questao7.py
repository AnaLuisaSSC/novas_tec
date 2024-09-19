'''
7- Implemente uma função chamada calcular_estatisticas que recebe uma quantidade indefinida
de números e retorna três valores: a média, o valor máximo e o valor mínimo da lista. Teste a
função com diferentes listas de números e imprima os resultados retornados.
'''

def calcular_estatisticas(numeros):
    if not numeros:
        return None, None, None  # aparece none se lista estiver vazia

    media = sum(numeros) / len(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    
    return media, valor_maximo, valor_minimo

def receber_numeros():
    numeros = []
    while True:
        numero = input("Digite um número (ou 'sair' para finalizar): ")
        if numero.lower() == 'sair':
            break
        try:
            numero = float(numero)
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")
    return numeros

# função
numeros_recebidos = receber_numeros()
print("Números recebidos:", numeros_recebidos)

media, valor_maximo, valor_minimo = calcular_estatisticas(numeros_recebidos)
print("Média:", media)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)