'''
7- Faça um programa que calcule o valor aproximado de cos(x) pela série de Taylor, dado pela
aproximação abaixo:
        cos (x) = 1 - x²/2! + x⁴/4! - x{x}^{6}/6! + ...
'''
import math 

def calcular_cos_taylor(x, termos=10)
'''
param x: Valor para o qual calcular o cosseno.
param termos: Número de termos a usar na série de Taylor.
return: Valor aproximado de cos(x).
'''

soma = 0

for n in range(termos):
        termos = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        soma += termo
    
    return soma

def main():

x = float(input("Digite o valor de x (em radianos): "))
    
    termos = int(input("Digite o número de termos para a aproximação: "))
    
    # calcula o valor aproximado de cos(x)
    resultado = calcular_cos_taylor(x, termos)
    
    # resultado
    print(f"O valor aproximado de cos({x}) usando {termos} termos é: {resultado:.6f}")

if __name__ == "__main__":
    main()
