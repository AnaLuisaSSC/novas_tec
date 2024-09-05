'''
4- Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o
número em seus dígitos individuais e imprime os dígitos separados uns dos outros por três
espaços cada. Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4
2 3 3 9. 
'''
#def é usada para definir uma função

def separa_digitos(num):  # Separar o número em dígitos individuais
    
    num_str = str(num)  # Converter o número para uma string para poder acessar cada dígito
    
    # verifica se num tem 5 dígitos
    if len(num_str) != 5 or not num_str.isdigit():      # len: é uma função embutida que retorna o número de itens em um objeto
        print("Erro: O número deve ter exatamente 5 dígitos.")
        return
    
    # separar os dígitos
    separado = '   '.join(num_str)  # join é usado para inserir três espaços entre cada dígito de uma string numérica:
    
    # imprimir o resultado
    print(separado)

# solicitar ao usuário um número de 5 dIgitos
try:
    numero = int(input("digite um número de cinco dígitos: "))
    separa_digitos(num)
except ValueError:
    print("Erro: insira um número válido.")

# num_str.isdigit() verifica se todos os caracteres na string são dígitos (de 0 a 9).Se algum caractere não for um dígito,isdigit() retorna False.

'''
 if len(num_str) != 5 or not num_str.isdigit(): Usando not na frente, verificamos se não é um número válido 
 (ou seja, se num_str contém qualquer coisa que não seja um dígito).
 esta condição or (ou) verifica se a string não tem exatamente 5 dígitos ou se contém caracteres não numéricos. 
 Se qualquer uma dessas condições for verdadeira, a mensagem de erro é exibida e a função retorna sem prosseguir.
'''

'''
num = input ("digite um numero:")
digitos = len(num)
num = int(num)

while(resto !=0):
    print(num//(10**(digitos-1)), end=" ")
    num %=(10**(digitos-1))
    digitos -=1
'''