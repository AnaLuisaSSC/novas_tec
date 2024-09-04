'''
2- Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando
asteriscos (*) 
'''
def desenhar_caixa(largura, altura): # Desenha uma caixa de asteriscos com a largura e altura fornecidas.
    
    for i in range(altura): # range(altura): função que gera uma sequência de números inteiros começando de 0 até altura - 1.
        print('*' * largura) # * vezes a largura, se for 8 irá se repetir 8 vezes

def desenhar_oval(largura, altura): #Desenha uma oval de asteriscos com a largura e altura fornecidas.

    for x in range(altura):
        for j in range(largura):
            if ((x - altura / 2)**2) / (altura / 2)**2 + ((j - largura / 2)**2) / (largura / 2)**2 <= 1: # x**2 = x²
                print('*', end='')
            else:
                print(' ', end='')
        print()

def desenhar_seta(largura):
    """Desenha uma seta de asteriscos com a largura fornecida."""
    for i in range(largura):
        print(' ' * (largura - i - 1) + '*' * (2 * i + 1))
    for i in range(largura // 2):
        print(' ' * (largura - 1) + '*' * (2 * (largura // 2 + 1) - 1))

def desenhar_losango(largura):
    """Desenha um losango de asteriscos com a largura fornecida."""
    altura = largura
    for i in range(altura):
        print(' ' * (altura - i - 1) + '*' * (2 * i + 1))
    for i in range(altura - 2, -1, -1):
        print(' ' * (altura - i - 1) + '*' * (2 * i + 1))

# Tamanho das formas
largura_caixa = 8
altura_caixa = 3
largura_oval = 10
altura_oval = 5
largura_seta = 6
largura_losango = 6

# Desenhar as formas
print("Caixa:")
desenhar_caixa(largura_caixa, altura_caixa)
print()

print("Oval:")
desenhar_oval(largura_oval, altura_oval)
print()

print("Seta:")
desenhar_seta(largura_seta)
print()

print("Losango:")
desenhar_losango(largura_losango)

