preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto
preco_final = round(preco_final, 2)

print(f"O preço final do produto com {desconto}% de desconto é: R$ {preco_final}")
