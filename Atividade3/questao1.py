'''
1- Codifique a função retangulo(m,n) , que exibe um retângulo com altura m e largura n
'''
def retangulo(m, n):
    for i in range(int(m)):  
        print('*' * int(n))   

# Solicita a entrada do usuário
m = float(input('Qual é a altura: '))
n = float(input('Qual é a largura: '))

# Chama a função para exibir o retângulo
retangulo(m, n)

# Calcula e exibe a área
area = m * n
print(f'A altura é: {m} \nA largura é: {n} \nA área é: {area}')
