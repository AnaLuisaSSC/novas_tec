'''
6- Faça um programa que leia um valor N qualquer, inteiro e positivo, calcule e mostre a seguinte
soma:
    E = 1 + 1/2! + 1/3! + ... + 1/N!
'''
import math

def calcular_soma_serie(N):
    soma = 0
    for i in range(1, N + 1):
        soma += 1 / math.factorial(i)
    return soma

def main():
    try:
        N = int(input("Digite um valor inteiro e positivo N: "))
        if N <= 0:
            raise ValueError("O valor deve ser inteiro e positivo.")
        
        resultado = calcular_soma_serie(N)
        print(f"A soma da série E = 1 + 1/2! + 1/3! + ... + 1/{N}! é {resultado:.5f}")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
