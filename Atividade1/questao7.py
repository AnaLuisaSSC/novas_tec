'''
7-  Escreva um programa que converta uma temperatura digitada em "Cˮ em “Fˮ. A fórmula para
essa conversão é:
F =  9/5C + 32
'''
def converter_temperatura(celsius):
    # calculo de converter
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():

    celsius = float(input("digite a temperatura em Celsius: "))
        
    # converter 
    fahrenheit = converter_temperatura(celsius)  
    
    #resultado
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")

if __name__ == "__main__": 
    main()

'''
 if __name__ == "__main__": é uma verificação que garante que o código dentro desse bloco só será executado se o script for executado 
 diretamente, e não quando for importado como um módulo em outro script.
 '''
   