'''
6- Faça um programa que leia um valor N qualquer, inteiro e positivo, calcule e 
mostre a seguinte soma:
    E = 1 + 1/2! + 1/3! + ... + 1/N!

    1/1! +
'''
n = int(input("Qual valor de N: "))

if n >= 0:
    print("O valor de N deve ser um inteiro positivo.")
else:
    e = 1
    fatoral = 1

for i in range(1, n + 1):

    fatorial *= i
    e +=1 / fatoriaç
    for num in range(1, i + 1):
        fatorial *= num

    print(f"E = {E}")

'''

'''