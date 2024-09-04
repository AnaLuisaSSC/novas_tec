'''
3- Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar ou pa
'''

try:  # inserir dois numeros inteiros inteiros 
    num = int(input("digite o um número inteiro: ")) # num = numero
     
    # número é par ou ímpar
    if num % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    # resultado
    print(f"O número {num} é {resultado}.")

except ValueError:      # Exceção caso o usuário não insira um número válido
    print("Erro: digite um número inteiro que seja válido.")
    
