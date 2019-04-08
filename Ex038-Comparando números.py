'''
Exercício Python 038: Escreva um programa que leia dois números inteiros e
compare-os. mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('Maior: ',n1)
elif n2 > n1:
    print('Maior: ',n2)

elif n1 == n2:
    print('Numeros Iguais')
