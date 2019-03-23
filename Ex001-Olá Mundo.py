'''
Exercício Python 001: Crie um programa que escreva Olá Mundo na tela.
'''

print('Olá Mundo')






numero = int(input('Digite um numero: '))

for cont in range(0,numero):
    if str(cont) == str(cont)[::-1]:
        print(cont)