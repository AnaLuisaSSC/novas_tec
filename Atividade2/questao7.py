'''
7- Faça um programa que calcule o valor aproximado de cos(x) pela série de Taylor, dado pela
aproximação abaixo:
        cos (x) = 1 - x²/2! + x⁴/4! - x{x}^{6}/6! + ...
'''

xI = int(input("Qual valor de x para cos(x): "))
x = xI * 3.1415 / 180

cos = 0
n = 0

for i in range(0, 1000, 2):

    fatorial = 1
    for num in range(1, i + 1):
        fatorial *= num

    termo = ((-1) ** n) * (x ** i) / fatorial
    cos += termo

    n += 1

print(f"cos({xI}) = {cos}")


'''
codigo do professor

xI = int(input("qual valor de x para cos(x):"))
x = xI*3.1415/180

cos = 0
j = 0

for i in range(0, 20, 2):

    fatorial = 1
    num =i
    while(num>=1);
        fatorial = fatorial*num
        num=num-1
    cos = cos + ((-1)**j)*(x**i)/fatorial
    j = j+1

print(f"cos({x})={cos:.2f}")
#((-1)**j)* (x**i/i!) / fatorial(i)
'''


'''
def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = 5
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é", resultado)
'''