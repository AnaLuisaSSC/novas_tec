'''
1- O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n fatorialˮ) e é definido
como segue:
n! = n · (n - 1) · (n - 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n! = 1 (para n = 0)
Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que da 120

Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu fatorial
'''

num = int(input("digite um numero"))

numI = num    # numInicial

fatorial = 1

 while(num>=1):
    fatorial *= num
    num -= num
print(f"o fatorial de {num}! = {fatorial}.")

