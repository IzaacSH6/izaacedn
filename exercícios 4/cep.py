import requests

def consultar_cep():
    cep = 63360000
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()
    print(dados["localidade"])

if __name__ == "__main__":
    consultar_cep()

