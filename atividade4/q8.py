#8
def comparar_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    comuns = conjunto1 & conjunto2
    apenas_primeira = conjunto1 - conjunto2
    apenas_segunda = conjunto2 - conjunto1
    nao_repetidos = conjunto1 ^ conjunto2
    primeira_sem_repetidos = conjunto1 - comuns

    print("Valores comuns às duas listas:", comuns)
    print("Valores que só existem na primeira:", apenas_primeira)
    print("Valores que existem apenas na segunda:", apenas_segunda)
    print("Elementos não repetidos das duas listas:", nao_repetidos)
    print("Primeira lista sem os elementos repetidos na segunda:", primeira_sem_repetidos)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comparar_listas(lista1, lista2)