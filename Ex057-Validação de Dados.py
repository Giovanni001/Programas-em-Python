'''
Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.
'''

resp = str(input('Digite o seu sexo [M/F]: ')).strip()[0]

while resp not in 'MmFf':
    resp = str(input('Dados Invalidos. Digite novamente! '))
    
print('Cadastrado com Sucesso !')

