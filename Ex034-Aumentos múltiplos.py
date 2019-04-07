'''
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Digite o seu salario: '))

if salario > 1250:
    superior = salario + (salario * 10 / 100)
    print(f'Você teve um aumento de 10%. Novo Salario R$ {superior:.2f}')

elif salario <= 1250:
    inferior = salario + (salario * 15 / 100)
    print(f'Você teve um aumento de 15%. Novo Salario R$ {inferior:.2f}')

