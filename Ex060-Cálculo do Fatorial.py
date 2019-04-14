'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''

n1 = int(input('Digite um numero : '))

controller = n1 #o fatorial de 10 começa com 10, o de 5 começa com 5, entao o contador começa com o fatorial q o usuario escolher
fatorial = 1 #valor 1 pois é o valor nulo da multiplicação todos os numero * 1 é igual a 1

while controller > 0: # o fatorial vai até o numero 1, entao enquanto ele for maior do q 0, ele faz o loop
    print('{}'.format(controller), end='')
    print(' x ' if controller > 1 else ' = ', end='')

    fatorial = fatorial * controller
    controller -= 1

print(fatorial)

#-------------------------------------------------------------------------------------
from math import factorial

            #outra maneira de resolver, usando modulos

n1 = int(input('Digite um numero : '))
fat = factorial(n1)

print('O fatorial de {} é {} '.format(n1,fat))

#----------------------------------------------------------------
#Usando for

n1 = int(input('Digite um numero : '))

fat = 1
for c in range(n1, 0, -1):
    print(c, end='')
    print(' x 'if c > 1 else ' = ',end='')
    fat = fat * c

print(fat)

