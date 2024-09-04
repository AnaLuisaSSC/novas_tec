''' 
6- Escreva um programa que leia a quantidade em segundos e imprima o resultado em dias,
horas, minutos e segundos.
''' 
def converter_tempo(total_segundos):
    # calcular numero de dias
    dias = total_segundos // 86400   
    segundos_restantes = total_segundos % 86400   # calcula o restante de segundos depois de formar o dia

    # calcular as horas
    horas = segundos_restantes // 3600

    # calcular o restante de segundos após as horas
    segundos_restantes %= 3600
    
    # calcular minutos
    minutos = segundos_restantes // 60
    # O restante são os segundos
    segundos = segundos_restantes % 60

    return dias, horas, minutos, segundos

def main():
    try:
        segundos_totais = int(input("digite a quantidade de segundos: "))
        
        # converter o tempo
        dias, horas, minutos, segundos = converter_tempo(total_segundos)

        print(f"{total_segundos} segundos correspondem a:")
        print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
    
    except ValueError:
        print("Erro: insira um valor numérico válido.")

if __name__ == "__main__":
    main()
   
'''
 if __name__ == "__main__": é uma verificação que garante que o código dentro desse bloco só será executado se o script for executado 
 diretamente, e não quando for importado como um módulo em outro script.
 '''