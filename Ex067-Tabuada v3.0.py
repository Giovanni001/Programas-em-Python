'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
'''

while True:
    tab = int(input('Digite um numero para ver a sua tabuada: '))
    if tab < 0:
        break

    for c in range(1,11):
        print(f'{tab} x {c} = {tab * c}')
