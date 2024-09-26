#9
def comparar_listas_alteradas(lista_inicial, lista_alterada):
    conjunto_inicial = set(lista_inicial)
    conjunto_alterado = set(lista_alterada)

    nao_mudaram = conjunto_inicial & conjunto_alterado
    novos_elementos = conjunto_alterado - conjunto_inicial
    removidos = conjunto_inicial - conjunto_alterado

    print("Elementos que não mudaram:", nao_mudaram)
    print("Novos elementos:", novos_elementos)
    print("Elementos que foram removidos:", removidos)

lista_inicial = [1, 2, 3, 4, 5]
lista_alterada = [4, 5, 6, 7, 8]
comparar_listas_alteradas(lista_inicial, lista_alterada)