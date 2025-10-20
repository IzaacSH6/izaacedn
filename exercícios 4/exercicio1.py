# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).



x = True

while x:
    escolha = int(input("Escolha um operador: \n 1. Soma (+) \n 2. Multiplicação (*) \n 3. Subtração (-) \n 4. Divisão (/) \n"))
    if escolha == 1:
        valor1 = float(input("digite o primeiro valor\n"))
        valor2 = float(input("digite o segundo valor\n"))

        calc = valor1 + valor2 
        print(f"{valor1} + {valor2} = {calc}\n")

    elif escolha == 2:
        valor1 = float(input("digite o primeiro valor \n"))
        valor2 = float(input("digite o segundo valor\n"))

        calc = valor1 * valor2 
        print(f"{valor1} * {valor2} = {calc}\n")    

    elif escolha == 3:
        valor1 = float(input("digite o primeiro valor\n"))
        valor2 = float(input("digite o segundo valor\n"))

        calc = valor1 - valor2 
        print(f"{valor1} - {valor2} = {calc}\n")
    
    elif escolha == 4:
        valor1 = float(input("digite o primeiro valor\n"))
        valor2 = float(input("digite o segundo valor\n"))

        calc = valor1 / valor2 
        print(f"{valor1} / {valor2} = {calc}\n")            