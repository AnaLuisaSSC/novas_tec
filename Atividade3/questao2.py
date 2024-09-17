'''
2- Escreva uma função chamada formatar_data que recebe três parâmetros: dia, mês e ano. A
função deve retornar uma string com a data formatada no formato "dd/mm/aaaa". Permita que
os parâmetros sejam passados com seus respectivos nomes e em qualquer ordem. Teste a
função com diferentes combinações de argumentos nomeados.
'''
def formatar_data(dia, mes, ano):
    if not (1 <= dia <= 31) or not (1 <= mes <= 12) or ano <= 0:
        print("datas invalida")
        return
    dia_formatado = f"{dia:02d}"  # sempre deve ter 2 digitos
    mes_formatado = f"{mes:02d}"  # sempre deve ter 2 digitos
    ano_formatado = f"{ano:04d}"  # sempre deve ter 4 digitos

    return f"{dia_formatado}/{mes_formatado}/{ano_formatado}"

def dados_usuario():
    try:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        
        # formata a data 
        data_formatada = formatar_data(dia, mes, ano)
        print(f"Data formatada: {data_formatada}")
    except ValueError as e:
        print(f"Erro: {e}")

# chama a função 
dados_usuario()