'''
Exercício Python 8: Escreva um programa que leia um valor
em metros e o exiba convertido em centímetros e milímetros.

'''


metros = float(input('Digite um valor em metros para ser convertido: '))

centimetros = metros * 100
milimetros = metros * 1000

print('O valor {}m em cm é {} e em milimetros é {}'.format(metros,centimetros,milimetros))