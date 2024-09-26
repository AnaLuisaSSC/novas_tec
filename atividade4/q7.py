#7
def contar_caracteres(frase):
    dicionario = {}
    for char in frase:
        if char in dicionario:
            dicionario[char] += 1
        else:
            dicionario[char] = 1
    return dicionario

frase = "o rato roeu a roupa do rei de roma"
print(contar_caracteres(frase))