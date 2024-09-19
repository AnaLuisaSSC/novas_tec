'''
2- Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando
asteriscos (*) 
'''
largura_caixa = 8
altura_caixa = 3
print("Caixa:")
for i in range(altura_caixa):
    print('*' * largura_caixa)
print()

largura_oval = 10
altura_oval = 5
print("Oval:")
for x in range(altura_oval):
    for j in range(largura_oval):
        if ((x - altura_oval / 2) ** 2) / (altura_oval / 2) ** 2 + ((j - largura_oval / 2) ** 2) / (largura_oval / 2) ** 2 <= 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

largura_seta = 6
print("Seta:")
for i in range(largura_seta):
    print(' ' * (largura_seta - i - 1) + '*' * (2 * i + 1))
for i in range(largura_seta // 2):
    print(' ' * (largura_seta - 1) + '*' * (2 * (largura_seta // 2 + 1) - 1))
print()

largura_losango = 6
altura_losango = largura_losango
print("Losango:")
for i in range(altura_losango):
    print(' ' * (altura_losango - i - 1) + '*' * (2 * i + 1))
for i in range(altura_losango - 2, -1, -1):
    print(' ' * (altura_losango - i - 1) + '*' * (2 * i + 1))