'''
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

barato = ''
total = maior_que_mil = cont = menor = 0
resp = ''
while resp != 'N':
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto R$  '))
    cont += 1
    resp = input('Deseja continuar ? [S/N] ').upper()[0].strip()

    if preco > 1000:
        maior_que_mil += 1

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome

    total = total + preco

    while resp not in 'SNsn':
        resp = input('Resposta Incorreta.Digite novamente [S/N]: ').upper()[0].strip()

print('{:-^60}'.format('Fim do Programa'))

print(f'Total gasto: {total}')
print(f'Produtos que custam mais de R$1000: {maior_que_mil} ')
print(f'Produto mais barato: {barato} com um preço de {menor}')
