'''
6- Faça um programa que leia um valor N qualquer, inteiro e positivo, calcule e 
mostre a seguinte soma:
    E = 1 + 1/2! + 1/3! + ... + 1/N!
'''
import math # importa módulo

def calcular_soma_serie(n):  # definição da função
    soma = 0    # inicia variavel
    for i in range(1, n + 1):    
        soma += 1 / math.factorial(i)     # 1/2 = 0.5
    return soma

def main():
    try:
        n = int(input("Digite um valor inteiro e positivo n: "))
        if n <= 0:
            raise ValueError("O valor deve ser inteiro e positivo.")
        
        resultado = calcular_soma_serie(n)
        print(f"A soma da série E = 1 + 1/2! + 1/3! + ... + 1/{n}! é {resultado:.5f}")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

'''

'''