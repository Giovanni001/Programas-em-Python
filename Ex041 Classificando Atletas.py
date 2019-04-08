'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

print('-=-\033[1;30m'*30)
print('Bem Vindo a Confederação de Natação de Jundiai caro Estudante ! '.center(100))
print('\033[1;30m-=-\033[m'*30)
print('\n')

idade = int(input('\033[1;36mDigite a sua idade para ver em qual categoria você se enquadra:\033[m '))

if idade <= 9:
    print('Categoria: \033[1;32mMIRIM\033[m ')
elif idade <= 14:
    print('Categoria: \033[1;34mINFANTIL\033[m')
elif idade <= 25:
    print('Categoria: \033[1;35mSENIOR\033[m')
elif idade > 25:
    print('Categoria: \033[1;31mMASTER\033[m')