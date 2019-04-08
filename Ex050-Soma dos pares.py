'''
Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

soma = 0

for c in range(1,7):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma += n1
print('A soma entre os pares é {}'.format(soma))

