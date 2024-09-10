'''
Um método para o cálculo de raiz quadradas de um número N já era conhecido pelos
babilônios em... bom, há muito tempo (também é conhecido como Método de Heron, um
matemático grego que o descreveu 20 séculos depois, perto do ano 50 DC. Começando com
um valor inicial k (geralmente valendo 1, os babilônios geravam um novo valor de k de acordo
com a regra:

        k = (k + (n/k)/2)    ou  k = k + n
                                         --
                                          k
                                     __________
                                           2

A medida em que o processo é repetido, os novos valores de k se aproximam cada vez mais da
raiz de N. Faça um programa que leia o valor de N e exiba os primeiros doze valores calculados
com essa fórmula, verificando se eles realmente se aproximaram da raiz correta.
'''

import math 

def metodo_heron(n, k):
'''
parem n: numeroinserido
k: valor atual
return: proximo valor
'''

return (k + (n / k)) / 2

def calcular_raiz_quadrada(n, iteracoes=12):

      k = 1

      for i in range(iteracoes):
            k = metodo_heron(n, k)
            print(f"Iteração {i + 1}: k = {k:.6f}")
      
      raiz_verdadeira = math.sqrt(n)
      print(f"\nRaiz quadrada verdadeira de {n}: {raiz_verdadeira:.6f}")

def main():
    # Recebe o valor de N
    n = float(input("Digite o valor de N: "))
    
    # Calcula e exibe os valores
    calcular_raiz_quadrada(n)

if __name__ == "__main__":
    main()
