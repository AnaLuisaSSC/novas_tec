'''
Escreva um programa em Python que funcione como um conversor de unidades. O programa
deve permitir a conversão entre diferentes unidades de temperatura (Celsius, Fahrenheit,
Kelvin), distância (metros, quilômetros, milhas), e tempo (segundos, minutos, horas). Use
um match para determinar o tipo de conversão e as unidades de entrada e saída
'''

def converter_temperatura(valor, de, para):
    match (de, para):
        case ('Celsius', 'Fahrenheit'):
            return valor * 9/5 + 32
        case ('Celsius', 'Kelvin'):
            return valor + 273.15
        case ('Fahrenheit', 'Celsius'):
            return (valor - 32) * 5/9
        case ('Fahrenheit', 'Kelvin'):
            return (valor - 32) * 5/9 + 273.15
        case ('Kelvin', 'Celsius'):
            return valor - 273.15
        case ('Kelvin', 'Fahrenheit'):
            return (valor - 273.15) * 9/5 + 32
        case _:
            raise ValueError("Conversão de temperatura não suportada.")

def converter_distancia(valor, de, para):
    match (de, para):
        case ('metros', 'quilômetros'):
            return valor / 1000
        case ('metros', 'milhas'):
            return valor * 0.000621371
        case ('quilômetros', 'metros'):
            return valor * 1000
        case ('quilômetros', 'milhas'):
            return valor * 0.621371
        case ('milhas', 'metros'):
            return valor / 0.000621371
        case ('milhas', 'quilômetros'):
            return valor / 0.621371
        case _:
            raise ValueError("Conversão de distância não suportada.")

def converter_tempo(valor, de, para):
    match (de, para):
        case ('segundos', 'minutos'):
            return valor / 60
        case ('segundos', 'horas'):
            return valor / 3600
        case ('minutos', 'segundos'):
            return valor * 60
        case ('minutos', 'horas'):
            return valor / 60
        case ('horas', 'segundos'):
            return valor * 3600
        case ('horas', 'minutos'):
            return valor * 60
        case _:
            raise ValueError("Conversão de tempo não suportada.")

def main():
    print("Escolha a categoria de conversão:")
    print("1. Temperatura")
    print("2. Distância")
    print("3. Tempo")

    escolha_categoria = input("Digite o número da categoria (1/2/3): ")
    match escolha_categoria:
        case '1':
            valor = float(input("Digite o valor: "))
            de = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ").capitalize()
            para = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ").capitalize()
            resultado = converter_temperatura(valor, de, para)
            print(f"{valor} {de} é igual a {resultado} {para}")
        
        case '2':
            valor = float(input("Digite o valor: "))
            de = input("Digite a unidade de origem (metros, quilômetros, milhas): ").lower()
            para = input("Digite a unidade de destino (metros, quilômetros, milhas): ").lower()
            resultado = converter_distancia(valor, de, para)
            print(f"{valor} {de} é igual a {resultado} {para}")

        case '3':
            valor = float(input("Digite o valor: "))
            de = input("Digite a unidade de origem (segundos, minutos, horas): ").lower()
            para = input("Digite a unidade de destino (segundos, minutos, horas): ").lower()
            resultado = converter_tempo(valor, de, para)
            print(f"{valor} {de} é igual a {resultado} {para}")

        case _:
            print("Categoria inválida. Escolha entre 1, 2 ou 3.")

if __name__ == "__main__":
    main()
