'''
Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import cos,tan,sin,radians

angulo = float(input('Digite um angulo: '))

seno = sin(radians(angulo))
cosse = cos(radians(angulo))
tang = tan(radians(angulo))

print('Seno: ',seno)
print('Cosseno: ',cosse)
print('Tangente: ',tang)

