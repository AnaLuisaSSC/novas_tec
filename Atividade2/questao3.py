'''
Escreva um programa em Python que funcione como um conversor de unidades. O programa
deve permitir a conversão entre diferentes unidades de temperatura (Celsius, Fahrenheit,
Kelvin), distância (metros, quilômetros, milhas), e tempo (segundos, minutos, horas). Use
um match para determinar o tipo de conversão e as unidades de entrada e saída
'''
opicao = int(input("""
                Você deseja:                            
                1 - temepratura      
                2 - distancia
                3 - tempo   
            """))

match opicao:
    case 1:
        unidade_entrada = int(input("""
                 Informe a unidade de entrada:
                 
                 1 - Celsius
                 2 - Fahrenheit
                 3 - Kelvin
            """))

        valor = float(input("Digite o valor da temperatura: "))

        match unidade_entrada:
            case 1:  # Celsius
                fahrenheit = valor * 9/5 + 32
                kelvin = valor + 273.15
                print(f"{valor}°C é igual a {fahrenheit}°F e {kelvin}K")
            case 2:  # Fahrenheit
                celsius = (valor - 32) * 5/9
                kelvin = (valor - 32) * 5/9 + 273.15
                print(f"{valor}°F é igual a {celsius}°C e {kelvin}K")
            case 3:  # Kelvin
                celsius = valor - 273.15
                fahrenheit = (valor - 273.15) * 9/5 + 32
                print(f"{valor}K é igual a {celsius}°C e {fahrenheit}°F")
            case _:
                print("Unidade de entrada inválida")

    case 2:
        unidade_entrada = int(input("""
                 Informe a unidade de entrada:
                 
                 1 - metros 
                 2 - Quilômetros
                 3 - Milhas
                """))

        valor = float(input("Digite o valor da distancia: "))

        match unidade_entrada:
            case 1:  # metros
                quilometros = valor / 1000
                milhas = valor / 1609.34

                print(f"{valor} metros é igual a {quilometros} quilômetros e {milhas} milhas")

            case 2:  # Quilômetros
                metros = valor * 1000
                milhas = valor / 1.60934
                print(f"{valor} quilômetros é igual a {metros} metros e {milhas} milhas")

            case 3:  # Milhas
                metros = valor * 1609.34
                quilometros = valor * 1.60934
                print(f"{valor} milhas é igual a {metros} metros e {quilometros} quilômetros")

            case _:
                print("Unidade de entrada inválida")

    case 3:

        unidade_entrada = int(input("""
                 Informe a unidade de entrada:
                 
                 1 - Segundos
                 2 - Minutos
                 3 - Horas
            """))

        valor = float(input("Digite o valor do tempo: "))

        match unidade_entrada:
            case 1:  # Segundos
                minutos = valor / 60
                horas = valor / 3600
                print(f"{valor} segundos é igual a {minutos} minutos e {horas} horas")

            case 2:  # Minutos
                segundos = valor * 60
                horas = valor / 60
                print(f"{valor} minutos é igual a {segundos} segundos e {horas} horas")

            case 3:  # Horas
                segundos = valor * 3600
                minutos = valor * 60
                print(f"{valor} horas é igual a {segundos} segundos e {minutos} minutos")

            case _:
                print("Unidade de entrada inválida")

    case _:
        print("Opção inválida.")