'''
Exercício Python 059: Crie um programa que leia dois valores e
mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] numero ao quadrado
[ 6 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

numero = float(input('Digite um numero: '))
numero2 = float(input('Digite um numero: '))

while True:

    escolha = int(input('''\033[1;30mEscolha uma Opção: 

        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] numero ao quadrado
        [6] sair do programa\033[m
        '''))

    if escolha == 1:
        soma = numero + numero2
        print(f'A soma entre {numero:.0f} e {numero2:.0f} é {soma:.0f}')

    elif escolha == 2:
        multiplicar = numero * numero2
        print(f'A multiplicação entre {numero:.0f} e {numero2:.0f} é {multiplicar:.0f}')

    elif escolha == 3:
        if numero > numero2:
            print(f'Maior numero: {numero}')
        else:
            print(f'Maior numero: {numero2}')

    elif escolha == 4:
        numero = float(input('Digite um numero: '))
        numero2 = float(input('Digite um numero: '))

    elif escolha == 5:
        resp = int(input('Qual numero deseja elevar ao quadrado ? '))
        if resp == numero:
            ao_quadrado = resp * resp
            print(f'O numero {numero} ao quadrado é {ao_quadrado}')

        elif resp == numero2:
            ao_quadrado = resp * resp
            print(f'O numero {numero2} ao quadrado é {ao_quadrado}')

    elif escolha == 6:
        break