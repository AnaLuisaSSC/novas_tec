'''
Faça um programa que receba:
a. O código de um produto comprado, supondo que a digitação do código do produto seja
sempre válida, ou seja, um número inteiro entre 1 e 10;

b. O peso do produto em quilos;

c. O código do país de origem, supondo que a digitação do código do país seja sempre válida,
ou seja, um número entre 1 e 3.

Tabelas:
Calcule e mostre:
O peso do produto convertido em gramas;
O preço total do produto comprado;
O valor do imposto, sabendo-se que o imposto é cobrado sobre o preço total do produto
comprado e que depende do país de origem;
O valor total, preço total do produto mais imposto.
'''

def calcular_preco_por_grama(codigo_produto)
    if 1 <= codigo_produto <= 4:
        return 10
    elif 5 <= codigo_produto <= 7:
        return 15   
    elif 8 <= codigo_produto <= 10:
        return 35
    else:
        raise ValueError("Código do produto inválido")

def calcular_imposto(codigo_pais, preco_total):
    if codigo_pais == 1:
        return 0
    elif codigo_pais == 2:
        return preco_total * 0.15
    elif codigo_pais == 3:
        return preco_total * 0.25
    else:
        raise ValueError("Código do país inválido")

def main():
    codigo_produto = int(input("Digite o código do produto (1 a 10): "))
    peso_kg = float(input("Digite o peso do produto em quilos: "))
    codigo_pais = int(input("Digite o código do país de origem (1 a 3): "))

    # peso em gramas
    peso_g = peso_kg * 1000

    # preço por grama
    preco_por_grama = calcular_preco_por_grama(codigo_produto)

    # preço total do produto
    preco_total = preco_por_grama * peso_g

    imposto = calcular_imposto(codigo_pais, preco_total)

    # valor total
    valor_total = preco_total + imposto

    # resultados
    print(f"Peso do produto: {peso_g} gramas")
    print(f"Preço total do produto: R${preco_total:.2f}")
    print(f"Valor do imposto: R${imposto:.2f}")
    print(f"Valor total: R${valor_total:.2f}")

if __name__ == "__main__":
    main()
