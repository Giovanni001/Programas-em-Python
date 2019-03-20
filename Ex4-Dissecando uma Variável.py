'''
Exercício Python 004: Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''


alguma_coisa = input('Digite algo: ')

print('O tipo primitivo  é: {} '.format(type(alguma_coisa)))

print('Só tem espaço? {}'.format(alguma_coisa.isspace()))
print(' É um número? {}'.format(alguma_coisa.isnumeric()))
print('É alfabético? {}'.format(alguma_coisa.isalpha()))
print('É alfanumérico? {}'.format(alguma_coisa.isalnum()))
print('Está em maiúsculas? {}'.format(alguma_coisa.isupper()))
print('Está em minúsculas? {}'.format(alguma_coisa.islower()))
print('Está capitalizado? {}'.format(alguma_coisa.istitle()))
print('A string está vazia ?',alguma_coisa.isprintable())
