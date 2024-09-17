'''
2- Escreva uma função chamada formatar_data que recebe três parâmetros: dia, mês e ano. A
função deve retornar uma string com a data formatada no formato "dd/mm/aaaa". Permita que
os parâmetros sejam passados com seus respectivos nomes e em qualquer ordem. Teste a
função com diferentes combinações de argumentos nomeados.
'''
def formatar_data(d, m, a):
    if d <= 1 or m <= 1 or a <= 1:
        print("datas nao podem ser: 0 ou negativas")
        return