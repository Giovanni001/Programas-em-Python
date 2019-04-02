'''
Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''

from math import hypot

cateto_oposto = float(input('Informe o cateto oposto: '))
cateto_adjacente = float(input('Informe o cateto adjacente: '))

hipotenusa = round((hypot(cateto_oposto,cateto_adjacente)))

print(f'A hipotenusa vale {hipotenusa}')