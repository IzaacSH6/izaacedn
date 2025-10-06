#4- Calculadora de Preço Total
#* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

#* Nome do produto: "Cadeira Infantil"
#* Preço unitário: R$ 12.40
#* Quantidade: 3
#O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

item = [["Cadeira Infantil", 12.40]]

calc = item[0][1] * 3

print(f"O valor da {item[0][0]} é: R$ {calc} ")
