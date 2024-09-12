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

codigo_produto = int(input("Digite o código do produto (1 a 10): "))
peso_kg = float(input("Digite o peso do produto em quilos: "))
codigo_pais = int(input("Digite o código do país de origem (1 a 3): "))

# peso para gramas
peso_g = peso_kg * 1000

if 1 <= codigo_produto <= 4:
    preco_por_grama = 10
elif 5 <= codigo_produto <= 7:
    preco_por_grama = 15
elif 8 <= codigo_produto <= 10:
    preco_por_grama = 35

preco_total = preco_por_grama * peso_g  # preo total do produto

# imposto
if codigo_pais == 1:
    imposto = 0
elif codigo_pais == 2:
    imposto = preco_total * 0.15
elif codigo_pais == 3:
    imposto = preco_total * 0.25

valor_total = preco_total + imposto

# resultados
print(f"Peso do produto: {peso_g} gramas")
print(f"Preço total do produto: R${preco_total:.2f}")
print(f"Valor do imposto: R${imposto:.2f}")
print(f"Valor total: R${valor_total:.2f}")