
# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).


x = True

while x:
    try:
        valor = int(input(f'Quantos anos vc tem?'))
        if valor <= 12:
            print(f"Você tem {valor} anos. \n Classificação: Criança")
        elif valor > 12 and valor <= 17:
            print(f"Você tem {valor} anos. \n Classificação: Adolescente")
        elif valor > 17 and valor <= 59:
            print(f"Você tem {valor} anos. \n Classificação: Adulto")
        elif valor >= 60 and valor <= 130:
            print(f"Você tem {valor} anos. \n Classificação: Idoso")
        else:
            print("impossível ser velho desse jeito")
    except ValueError:
            valor = input(f'digite um número inteiro ou "parar" para encerrar.\n')
            if valor == "parar":
                x = False
            else:
                pass

