'''
6- A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Os dois primeiros termos são iguais a 1, e
a partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥
3, exiba o n-ésimo termo da série de Fibonacci. Faça o código resursivo.
'''

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(3, n + 1):
            a, b = b, a + b  # Atualiza os termos anteriores
        return b

def fibonacci_recursivo(n):
    if n == 1 or n == 2:
        return 1  # Os dois primeiros termos da série são 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)  # Soma dos dois termos anteriores

try:
    # Solicita o método de cálculo e o número do termo
    metodo = input("Escolha o método de cálculo (1 para fibonacci, 2 para fibonacci recursivo): ")
    fibonacci_inteiro = int(input("Por favor, insira um número inteiro (n-ésimo termo da série Fibonacci): "))

    if fibonacci_inteiro < 1:
        print("Por favor, insira um número maior ou igual a 1.")
    else:
        if metodo == '1':
            resultado = fibonacci(fibonacci_inteiro)
            print(f"O {fibonacci_inteiro}º termo da série de Fibonacci (iterativo) é: {resultado}")

        elif metodo == '2':
            resultado = fibonacci_recursivo(fibonacci_inteiro)
            print(f"O {fibonacci_inteiro}º termo da série de Fibonacci (recursivo) é: {resultado}")
           
        else:
            print("Método inválido. Escolha 1 para recursivo ou 2 para iterativo.")
        
except ValueError:
    print("Você não inseriu um número inteiro válido.")