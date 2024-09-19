'''
5- Para cada problema a seguir defina uma função recursiva, faça a simulação por substituição e
desenhe o fluxo de chamadas e retornos:
a. Calcular o fatorial de um número natural.
b. Calcular a potencia de um número, dado um expoente.
c. Calcular o resto da divisão inteira usando subtração.
d. Calcular o quociente da divisão inteira usando subtração.
e. Calcular o produto de dois naturais usando adição.
f. Calcular a soma de dois naturais usando as funções suc(n) e pred(n) que devolvem,
respectivamente, o sucessor e o predecessor de um natural n.
'''
del funcoes_recursivas:

    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)

    def potencia(base, expoente):
        if expoente == 0:
            return 1
        else:
            return base * potencia(base, expoente - 1)

    def resto(a, b):
        if a < b:
            return a
        else:
            return resto(a - b, b)

    def quociente(a, b):
        if a < b:
            return 0
        else:
            return 1 + quociente(a - b, b)

    def produto(a, b):
        if b == 0:
            return 0
        else:
            return a + produto(a, b - 1)

    def suc(n):
        return n + 1

    def pred(n):
        return n - 1 if n > 0 else 0

    def soma(a, b):
        if b == 0:
            return a
        else:
            return soma(suc(a), pred(b))

    # funções recursivas
    print(f"Fatorial de 6: {fatorial(6)}")          # 720
    print(f"Potência de 3^4: {potencia(3, 4)}")      # 81
    print(f"Resto da divisão de 15 por 4: {resto(15, 4)}")  # 3
    print(f"Quociente da divisão de 20 por 5: {quociente(20, 5)}")  # 4
    print(f"Produto de 5 e 7: {produto(5, 7)}")      # 35
    print(f"Soma de 8 e 3: {soma(8, 3)}")            # 11