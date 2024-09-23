''' 1- Escreva um aplicativo que solicita ao usuário inserir dois inteiros, obtém do usuário esses
números e imprime sua soma, produto, diferença e divisão
'''

n1 = int(input('digite um numero inteiro:'))
n2 = int(input('digite outro numero inteiro:'))
s = n1+n2
p = n1*n2
dif = n1-n2

if n2!=0:
    divi = n1/n2
else:
    print('insira numero diferente de 0')    

print('soma: {}  \nproduto: {} \ndiferença: {} \ndivisão: {}'.format (s,p,dif,divi))



'''
input() para capturar as entradas do usuário e int() para converter essas entradas em números inteiros
'''

''' try é executado, ele tenta realizar a operação especificada 
 (neste caso, a conversão das entradas para inteiros), 
 Se essa operação falhar e gerar uma exceção (por exemplo, se o usuario inserir um texto
 o código dentro do bloco except será executado.
'''
