'''
Exercício Python 026: Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra "A", em que posição ela aparece
a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: '))

print('A letra A aparece {} vezes '.format(frase.upper().count('A')))
print('A letra A aparece na posição {} '.format(frase.find('a') +1))
print('A ultima posição que a letra A aparece é {}'.format(frase.rfind('a')+1))