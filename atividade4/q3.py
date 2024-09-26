# 3
def verifica_parenteses(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expressao:
        if char in '([{':
            pilha.append(char)
        elif char in ')]}':
            if not pilha or pilha.pop() != pares[char]:
                return "Erro"
    return "OK" if not pilha else "Erro"

print(verifica_parenteses("()[]{}"))
print(verifica_parenteses("([)]"))

