lista = [-12, -4, 2, 8, 29, 45, 78, 36, -17, -2, 12, 8, 3, -55]

# a- maior elemento
print("Maior elemento:", max(lista))

# b- menor elemento
print("Menor elemento:", min(lista))

# c- números pares
print("Números pares:", [num for num in lista if num % 2 == 0])

# d- ocorrências do primeiro elemento
print("Ocorrências do primeiro elemento:", lista.count(lista[0]))

# e- soma dos elementos negativos
print("Soma dos elementos negativos:", sum(num for num in lista if num < 0))