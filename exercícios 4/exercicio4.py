# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

numeros = []
while True:
    entrada = input('Digite um número (ou "sair" para finalizar): ')
    if entrada.lower() == 'sair':
        break
    if entrada.isdigit():
        numeros.append(int(entrada))

pares = 0
impares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Você digitou {len(numeros)} números: {pares} pares e {impares} ímpares.')
