# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.


x = True


while x:
    temp = int(input("Selecione uma escala: \n 1. Celcius \n 2. Fahrenheit \n 3. Kelvin \n"))

    if temp == 1:
        
        valor = int(input("Digite o valor da temperatura. Você escolheu Celcius. \n"))
        escolha = int(input("Para qual escala você deseja converter? \n 1. Fahrenheit \n 2. Kelvin \n"))

        if escolha == 1:
            calculo = valor * 1.8 + 32
            print(f"{valor} C em Fahrenheit é {calculo}\n")

        elif escolha == 2:
            calculo = valor + 273
            print(f"{valor} C em Kelvin é {calculo}\n")
        else: 
            print("Valor inválido")    

    elif temp == 2:
        valor = int(input("Digite o valor da temperatura. Você escolheu Fahrenheit."))
        escolha = int(input("Para qual escala você deseja converter? \n 1. Celcius \n 2. Kelvin \n"))
        if escolha == 1:
            calculo = (valor - 32) / 1.8
            print(f"{valor}F em Celcius é {calculo}\n")
        
        elif escolha == 2:
            calculo = (valor - 32) * (5/9) + 273
            print(f"{valor}F em Kelvin é {calculo}\n")
        else: 
            print("Valor inválido")

    elif temp ==3:
        valor = int(input("Digite o valor da temperatura. Você escolheu Kelvin.\n"))
        escolha = int(input("Para qual escala você deseja converter? \n 1. Celcius \n 2. Fahrenheit \n"))

        if escolha == 1:
            calculo = valor - 273
            print(f"{valor} K em Celcius é {calculo}\n")

        elif escolha == 2:
            calculo = (valor - 273) * 1.8 + 32
            print(f"{valor} K em Fahrenheit é {calculo}\n")
        else: 
            print("Valor inválido")
    else:
        print("Valor inválido")