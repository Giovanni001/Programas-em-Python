'''
Exercício Python 012: Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.

'''


produto1 = float(input('Digite o preço do produto 1: '))
produto2 = float(input('Digite o preço do produto 2: '))
produto3 = float(input('Digite o preço do produto 3: '))


desconto1 = produto1 * 0.05
valor1 = produto1 - desconto1
print('Valor do produto 1 com desconto {} '.format(valor1))

desconto2 = produto2 * 0.10
valor2 = produto2 - desconto2
print('Valor do produto 2 com desconto {} '.format(valor2))

desconto3 = produto3 * 0.15
valor3 = produto3 - desconto3
print('Valor do produto 3 com desconto {} '.format(valor3))