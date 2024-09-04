'''
5- Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do segundo grau, e
calcule as raízes xʼ e xˮ através da fórmula de Báskara. 
'''
# importar math, para funções  matemáticas avançadas (como a raiz quadrada)
import math 

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    
    # verificar tipo de raízes com base no valor delta
    if delta > 0:    # 2 raízes reais e !=
        raiz_delta = math.sqrt(delta)   # math.sqrt(x) = uma função do módulo math em Python que retorna a raiz quadrada de x.
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        return (x1, x2)
    elif delta == 0:   # raiz real 
        x1 = -b / (2 * a)
        return (x1,)
    else:    # delta negativo: raízes complexas
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-delta) / (2 * a)
        return (f"{parte_real} + {parte_imaginaria}", f"{parte_real} - {parte_imaginaria}")

def main():
    try:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        
        # verifica se 'a' é = 0
        if a == 0:
            print("Erro: coeficiente a não pode ser 0 para uma equação do segundo grau.")
            return
        
        # calcular as raízes
        raizes = calcular_raizes(a, b, c)
        
        # imprimir as raízes
        if len(raizes) == 2:
            print(f"As raízes da equação são: x' = {raizes[0]} e x'' = {raizes[1]}")
        elif len(raizes) == 1:
            print(f"A raiz da equação é: x = {raizes[0]}")
        else:
            print("Erro inesperado: número incorreto de raízes calculadas.")
    
    except ValueError:
        print("Erro: insira valores numéricos válidos para os coeficientes.")

if __name__ == "__main__":
    main()

'''
 if __name__ == "__main__": é uma verificação que garante que o código dentro desse bloco só será executado se o script for executado 
 diretamente, e não quando for importado como um módulo em outro script.
 '''