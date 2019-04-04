'''
Exercício Python 028: Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

print('-=-'*30)
print('Vou pensar em um numero Tente adivinhar ! '.center(80))
print('-=-'*30)

numero = int(input('Digite um numero: '))

print('Hummm Estou analisando o numero....')

sleep(3)


escolhido = randint(0,5)

if numero == escolhido:
    print('PARABENS')
else:
    print('ERROU')