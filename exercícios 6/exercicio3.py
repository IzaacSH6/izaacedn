# - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

import requests

cep = input("Digite o CEP (apenas números): ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    resposta.raise_for_status()
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
except requests.exceptions.RequestException:
    print("Falha na conexão com a API ViaCEP.")
