'''
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode comprar.
'''

money = float(input('Quanto dinheiro vc tem na carteira? '))

#1 dolar == 3.91 reais

conversao_dolar = money / 3.91 #convertendo para dolar
conversao_euro = money / 4.45 #convetrendo para euro
conversao_iene = money / 0.035 #convertendo para iene


print('Com {} reais voce consegue comprar {} dolares'.format(money,conversao_dolar))
print('\n')
print('Com {} reais voce pode comprar {} euros'.format(money,conversao_euro))
print('\n')
print('Com {} rais voce pode comprar {} ienes'.format(money,conversao_iene))



