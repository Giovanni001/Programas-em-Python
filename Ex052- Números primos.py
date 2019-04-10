'''
Exercício Python 052: Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
'''

num = int(input('Digite um numero: '))

if num % 2 != 0 or num == 2:
    print('O numero {} é primo'.format(num))
else:
    print('Não é Primo')

#---------------------------------------------------------------------------

num = int(input('Digite um numero: '))

total = 0

for c in range(1 , num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m',end=' ')
    print(f'{c}', end=' ')

if total == 2:
    print('\nO numero {} é divisivel por {} valores logo é Primo'.format(num,total))
else:
    print('\nO numero {} é divisivel por {} valores logo não é Primo'.format(num,total))