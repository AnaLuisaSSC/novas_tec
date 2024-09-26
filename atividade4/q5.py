#5
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in valores if x % 2 == 0]
impares = [x for x in valores if x % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)