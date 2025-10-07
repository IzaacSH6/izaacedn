# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

produto = [["Camiseta", 50.00]]

porcent = 20/100

desconto = (produto[0][1] - (produto[0][1]*porcent))

print(f"o valor da {produto[0][0]} com desconto é: R${desconto}")