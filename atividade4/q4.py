#4
def separar_pares_impares(valores):
    pares = []
    impares = []

    for valor in valores:
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)

    return pares, impares

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(valores)
print("Pares:", pares)
print("Ímpares:", impares)