#11
def criar_lista_pessoas():
    pessoa1 = {"first_name": "João", "last_name": "Silva", "age": 30, "city": "São Paulo"}
    pessoa2 = {"first_name": "Maria", "last_name": "Oliveira", "age": 25, "city": "São Paulo"}
    pessoa3 = {"first_name": "Carlos", "last_name": "Corrêa", "age": 40, "city": "Rio de Janeiro"}

    pessoas = [pessoa1, pessoa2, pessoa3]

    for pessoa in pessoas:
        for chave, valor in pessoa.items():
            print(f"{chave.capitalize()}: {valor}")
        print()  

criar_lista_pessoas()