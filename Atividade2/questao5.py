'''
5- (Impondo privacidade com criptografia) O crescimento explosivo de comunicação e
armazenamento de dados na internet e em computadores conectados por ela aumentou muito
a preocupação com a privacidade. O campo da criptografia envolve a codificação de dados
Estruturas de Controle7para torná-los difíceis de acessar (e espera-se — com os esquemas mais avançados —
impossíveis de acessar) para usuários sem autorização de leitura. Nesse exercício, você
investigará um esquema simples para criptografar e descriptografar dados. Uma empresa que
quer enviar dados pela internet pediu-lhe que escrevesse um programa que criptografe dados
a fim de que eles possam ser transmitidos com maior segurança. Todos os dados são
transmitidos como inteiros de quatro dígitos. Seu aplicativo deve ler um inteiro de quatro dígitos
inserido pelo usuário e criptografá-lo da seguinte maneira: substitua cada dígito pelo resultado
da adição de 7 ao dígito, obtendo o restante depois da divisão do novo valor por 10. Troque
então o primeiro dígito pelo terceiro e o segundo dígito pelo quarto. Então, imprima o inteiro
criptografado. Escreva um aplicativo separado que receba a entrada de um inteiro de quatro
dígitos criptografado e o descriptografe (revertendo o esquema de criptografia) para formar o
número original. [Projeto de leitura opcional: pesquise a “criptografia de chave públicaˮ em
geral e o esquema de chave pública específica PGP Pretty Good Privacy). Você também pode
querer investigar o esquema RSA, que é amplamente usado em aplicativos robustos
industriais.]
'''

# Recebe a escolha do usuário
ope = int(input("""
                 Você deseja:        
                                      
                1 - criptografar      
                2 - descriptografar   
               
            """))

match (ope):
    case 1:
        dado = int(input("Entre com o dado de 4 dígitos: "))

        # criptografia
        d1 = (dado // 1000 + 7) % 10
        d2 = (dado % 1000 // 100 + 7) % 10
        d3 = (dado % 100 // 10 + 7) % 10
        d4 = (dado % 10 + 7) % 10

        d1, d3, d2, d4 = d3, d1, d4, d2
        
        print(f"{dado} criptografado ficou {criptografado}!")

    case 2:
        dadoCripto = int(input("Digite o dado criptografado: "))

        d1 = (dadoCripto//1000+10)-7

        dadoCripto = dadoCripto%1000
        d2 = (dadoCripto//100 + 10)-7

        dadoCripto = dadoCripto%100
        d3 = (dadoCripto//10 + 10)-7

        dadoCripto = dadoCripto%10
        d4 = (dadoCripto//1 + 10)-7

        d3, d1, d4, d2 = d1, d3, d2, d4

        print(f"{dadoCriptoI} descriptografado ficou {d1}{d2}{d3}{d4}!")


    case _:
        print("Opção inválida. Por favor, escolha 1 para criptografar ou 2 para descriptografar.")



'''

codigo professor

ope = input("""voce prefere:
             1-criptogravar
             2- descriptografar:""")
match(ope)
    case 1:
    dado = int(input("entre com o dado de 4 dígitos"))

    d1 = (dado//1000+7)%10

    dado = dado%1000
    d2 = (dado//100+7)%10

    dado = dado%100
    d3 = (dado//10+7)%10

    dado = dado%10
    d4 = (dado//1+ 7)%10

    d1, d3, d2, d4 = d3, d1, d4, d2


    print(f"{dado} criptografia ficou {d1}{d2}{d3}{d4}!")
    break

#4356 = 4*1000 + 3*100 + 5*10 + 6*1 
case 2:

    dadocripto = int(input("digite o dado criptografia:"))
    dadoCriptoI = dadoCripto

    d1 = dadoCripto//1000

    dadoCripto = dadoCripto%1000
    d2 = dadoCripto//100

    dadoCripto = dadoCripto%100
    d3 = (dadoCripto//10 + 10)

    dadoCripto = dadoCripto%10
    d4 = (dadoCripto//1 + 10) - 7

    d3, d1, d4, d2 = d1, d3, d2, d4

    d1 = (d1 + 10) - 7

    print(f"{dadoCriptoI} descriptografia ficou {d1}{d2}{d3}{d4}!")

    #1234 = 1+10 2+10 3+10 4+10
    #      = 11-7 12-7 13-7 14-7
    #      = 4567
'''