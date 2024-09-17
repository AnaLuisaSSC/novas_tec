'''
1- Codifique a função retangulo(m,n) , que exibe um retângulo com altura m e largura n
'''
def retangulo(m, n):
    if m <= 0 or n <= 0:
        print("Altura e largura devem ser maiores que 0.")
        return
    
    # cria o retângulo
    for i in range(m):
        print('*' * n)

def main():
    try:
        m = int(input("Digite a altura do retângulo: "))
        n = int(input("Digite a largura do retângulo: "))
        
        # função para desenhar o retângulo
        retangulo(m, n)
    except ValueError:
        print("Por favor, insira números inteiros válidos.")

if __name__ == "__main__":
    main()