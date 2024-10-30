'''1- Aplicação de Agenda de Contatos Desenvolva uma aplicação para armazenar e organizar
informações de contatos, incluindo nomes, números de telefone, endereços, data de
aniversário e outras informações relevantes.
Organize seu programa através das funções apaga() , altera() , lista() , le() , grava() , menu() ,
verificarbirthday() . Sua aplicação precisa apresentar também :
a- Exiba o tamanho da agenda no menu principal;
b- Exiba a posição de cada contato;
c- Exiba a opção de ordenar a lista por nome no menu principal;
d- Exiba uma mensagem de erro caso duas entradas na agenda tenham o mesmo nome;
e- Salve os contatos num arquivo csv no diretório específico da agenda;
f- Recupera os contatos salvos do arquivo csv salvo;
g- Ao abrir a agenda, o usuário receber uma notificação de quem está fazendo aniversário
naquele dia.'''


import json
from datetime import date

def le():
    try:
        with open('contatos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def grava(contatos):
    with open('contatos.json', 'w') as file:
        json.dump(contatos, file)

# listar
def lista(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    for nome, info in contatos.items():
        print(f"Nome: {nome}, Telefone: {info['telefone']}, Endereço: {info['endereco']}, Aniversário: {info['aniversario']}")

# alterar
def altera(contatos):
    nome = input("Digite o nome do contato que deseja alterar: ")
    if nome in contatos:
        telefone = input("Novo telefone: ")
        endereco = input("Novo endereço: ")
        aniversario = input("Nova data de aniversário (DD/MM): ")
        contatos[nome] = {
            'telefone': telefone,
            'endereco': endereco,
            'aniversario': aniversario
        }
        print(f"Contato {nome} alterado com sucesso.")
    else:
        print("Contato não encontrado.")

# apagar 
def apaga(contatos):
    nome = input("Digite o nome do contato que deseja apagar: ")
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome} apagado com sucesso.")
    else:
        print("Contato não encontrado.")

# verificar
def verificarbirthday(contatos):
    hoje = date.today()
    print("\nAniversários deste mês:")
    for nome, info in contatos.items():
        aniversario = info['aniversario']
        if '/' in aniversario:
            dia, mes = map(int, aniversario.split('/'))
            if mes == hoje.month:
                print(f"{nome}: {aniversario}")
        else:
            print(f"Data de aniversário inválida para {nome}: {aniversario}")

# mostrar o menu
def menu():
    contatos = le()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Alterar Contato")
        print("4. Apagar Contato")
        print("5. Verificar Aniversários")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            aniversario = input("Data de aniversário (DD/MM): ")
            # Validação da data
            if len(aniversario) != 5 or aniversario[2] != '/':
                print("Data de aniversário inválida. Use o formato DD/MM.")
                continue
            contatos[nome] = {
                'telefone': telefone,
                'endereco': endereco,
                'aniversario': aniversario
            }
            print(f"Contato {nome} adicionado com sucesso.")
        
        elif opcao == '2':
            lista(contatos)
        
        elif opcao == '3':
            altera(contatos)
        
        elif opcao == '4':
            apaga(contatos)
        
        elif opcao == '5':
            verificarbirthday(contatos)
        
        elif opcao == '6':
            grava(contatos)
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()