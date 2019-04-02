'''
Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
'''


salario = float(input('Digiteo  seu salario: '))


aumento = salario + (salario * 0.15)

print('Seu salario com 15% de aumento passe a ser {} reais'.format(aumento))