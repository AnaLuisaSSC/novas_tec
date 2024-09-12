'''
Um método para o cálculo de raiz quadradas de um número N já era conhecido pelos
babilônios em... bom, há muito tempo (também é conhecido como Método de Heron, um
matemático grego que o descreveu 20 séculos depois, perto do ano 50 DC). Começando com
um valor inicial k (geralmente valendo 1), os babilônios geravam um novo valor de k de acordo
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

print float(input("digite um valor para N:"))

if n <= 0
      print("O valor de N deve ser um inteiro positivo.")
else:
      k = 1.0

      for i in range(14):
        k = (k + n / k) / 2
        print(f"Valor {i + 1}: {k}")
