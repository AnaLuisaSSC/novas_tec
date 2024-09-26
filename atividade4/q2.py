
2-
import random

def jogoForca():
    palavras = ['python', 'laço', 'computador', 'jogo']
    palavra = random.choice(palavras)
    letras_adivinhadas = ['_'] * len(palavra)
    tentativas = 6
    letras_erradas = []

    while tentativas > 0 and '_' in letras_adivinhadas:
        print(' '.join(letras_adivinhadas))
        print(f'Tentativas restantes: {tentativas}')
        print(f'Letras erradas: {", ".join(letras_erradas)}')
        letra = input('Adivinhe uma letra: ').lower()

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_adivinhadas[i] = letra
        else:
            tentativas -= 1
            letras_erradas.append(letra)

    if '_' not in letras_adivinhadas:
        print(f'Parabéns! Você adivinhou a palavra: {palavra}')
    else:
        print(f'Você perdeu! A palavra era: {palavra}')

def verificaParenteses(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}
   
    for char in expressao:
        if char in '([{':
            pilha.append(char)
        elif char in ')]}':
            if not pilha or pilha.pop() != pares[char]:
                return False
    return not pilha

def copiarValores(lista):
    lista_par = [num for num in lista if num % 2 == 0]
    lista_impar = [num for num in lista if num % 2 != 0]
    return lista_par, lista_impar

def removerRepetidos(lista):
    return list(set(lista))

def contarCaracteres(frase):
    dicionario = {}
    for char in frase:
        dicionario[char] = dicionario.get(char, 0) + 1
    return dicionario

# Testes
if __name__ == "__main__":
    jogoForca()
   
    expressao = "( [ { } ] )"
    print(verificaParenteses(expressao))  # Deve retornar True
   
    lista = [1, 2, 3, 4, 5]
    lista_par, lista_impar = copiarValores(lista)
    print("Pares:", lista_par)
    print("Ímpares:", lista_impar)
   
    lista = [1, 2, 3, 4, 5, 1, 2, 3]
    print("Lista sem repetições:", removerRepetidos(lista))
   
    frase = "rato"
    print(contarCaracteres(frase))  # Deve retornar {'r': 1, 'a': 1, 't': 1, 'o': 1}
