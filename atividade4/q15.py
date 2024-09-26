# 15
agenda = []

def adicionar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    aniversario = input("Aniversário: ")
    agenda.append({"nome": nome, "telefone": telefone, "email": email, "aniversario": aniversario})

def listar():
    for contato in agenda:
        print(contato)

def apagar():
    nome = input("Nome do contato a apagar: ")
    global agenda
    agenda = [contato for contato in agenda if contato["nome"] != nome]

def menu():
    while True:
        opcao = input("1. Adicionar\n2. Listar\n3. Apagar\n4. Sair\nEscolha uma opção: ")
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            apagar()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

menu()

