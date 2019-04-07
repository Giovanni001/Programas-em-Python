'''
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
parta viagens mais longas.
'''

distancia = float(input('Digite a distancia da viagem: '))

abaixo = 0.50 * distancia
acima = 0.45 * distancia

if distancia < 200:
    print('A distancia abaixo de 200km, logo você pagará {} '.format(abaixo))
else:
    print('A distancia acima de 200km, logo você pagará {}'.format(acima))

#------------------------------------------------------------------------------------

distancia = float(input('Digite a distancia da viagem: '))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('Você vai pagar um valor de {}'.format(preco))




