'''
Exercício Python 007: Desenvolva um programa que leia as duas notas
de um aluno, calcule e mostre a sua média.
'''


n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

media = (n1+n2) / 2

print(f'A sua media é de {media} ')

if media < 6:
    print('Você está de EXAME')
else:
    print('Você passou !')


