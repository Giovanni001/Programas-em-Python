'''
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''

num = int(input('Digite um numero para ver a sua tabuada: '))

for c in range(0,11):
    print('{} X {} = {}'.format(num ,c,(num * c)))