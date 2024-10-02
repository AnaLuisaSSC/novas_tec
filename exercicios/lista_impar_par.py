num = [[], []]
valor = 0

for c in range(1,8):
    valor = int(input('digite um numero: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
             
print(num)
print(f"os valores pares são: {num[0]} \nos valores impares são: {num[1]}")