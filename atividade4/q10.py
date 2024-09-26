#10
def informacoes_pessoa(primeiro_nome, sobrenome, idade, cidade):
    pessoa = {
        "first_name": primeiro_nome,
        "last_name": sobrenome,
        "age": idade,
        "city": cidade
    }

    for chave, valor in pessoa.items():
        print(f"{chave.capitalize()}: {valor}")

pessoa = informacoes_pessoa("Ana", "Santos", 20, "Brasília")