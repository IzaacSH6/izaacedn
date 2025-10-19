# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"




x = True

while x:
    try:
        peso = float(input("Digite seu peso em Kg \n"))

        altura = float(input("digite sua altura em metros. Exemplo 1.80 \n"))

        imc = peso / (altura*altura)

        if imc <= 18.5:
            print(f"Seu IMC é: {imc}. \n Classificação: Abaixo do peso")
        elif imc >= 18.6 and imc <= 30.0:
            print(f"Seu IMC é: {imc} . \n Classificação: Peso normal")
        elif imc <= 30.1:
            print(f"Seu IMC é: {imc} . \n Classificação: Acima do peso")
        else:
            print(f"Seu IMC é: {imc} . \n Classificação: Obeso")
    except ValueError:
            imc = input(f'digite um número inteiro ou "parar" para encerrar.\n')
            if imc == "parar":
                x = False
            else:
                pass


