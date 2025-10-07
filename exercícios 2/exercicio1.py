# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
#O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.


valor = float(input("Digite um valor.\n"))

dolar = valor*5.20
euro = valor*6.15

conver = print(f"{valor} \n convertido para Dólar: {dolar} \n convertido para Euro: {euro} ")