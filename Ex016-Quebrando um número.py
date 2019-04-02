'''
Exercício Python 016: Crie um programa que leia um número Real
qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

import math

n1 = float(input('Digite um numero para ver a sua parte inteira: '))

inteiro = math.trunc(n1)

print(inteiro)

