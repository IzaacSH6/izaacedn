# 4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.  


import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")

try:
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
    resposta.raise_for_status()
    dados = resposta.json()

    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        info = dados[chave]
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Máxima do dia: R$ {info['high']}")
        print(f"Mínima do dia: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}")
except requests.exceptions.RequestException:
    print("Falha na conexão com a API AwesomeAPI.")
