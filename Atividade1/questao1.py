''' 1- Escreva um aplicativo que solicita ao usuário inserir dois inteiros, obtém do usuário esses
números e imprime sua soma, produto, diferença e divisão
'''

try:  # inserir dois numeros inteiros inteiros
    num1 = int(input("Digite o 1° número inteiro: "))
    num2 = int(input("Digite o 2° número inteiro: ")) 
    
# calcular a soma, o produto e a diferença
    soma = num1 + num2
    produto = num1 * num2
    diferenca = num1 - num2
    
    # calcular a divisão 
    try:
        divisao = num1 / num2
    except ZeroDivisionError:  # exceção caso o divisor seja zero
        divisao = "Não é possível dividir por zero."
    
    # imprimir resultados
    print(f"Soma: {num1} + {num2} = {soma}")
    print(f"produto: {num1} * {num2} = {produto}")
    print(f"diferenca: {num1} - {num2} = {diferenca}")
    print(f"divisao: {num1} / {num2} = {divisao}")

''' try é executado, ele tenta realizar a operação especificada 
 (neste caso, a conversão das entradas para inteiros), 
 Se essa operação falhar e gerar uma exceção (por exemplo, se o usuario inserir um texto
 o código dentro do bloco except será executado.
'''
'''
input() para capturar as entradas do usuário e int() para converter essas entradas em números inteiros
'''