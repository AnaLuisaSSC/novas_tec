'''
1- O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n fatorialˮ) e é definido
como segue:
n! = n · (n - 1) · (n - 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n!  1 (para n  0)
Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120

Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu fatorial
'''
def fatorial_iterativo(n):
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {n} é {fatorial_iterativo(n)}")

def fatorial_recursivo(n):
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

n = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {n} é {fatorial_recursivo(n)}")
