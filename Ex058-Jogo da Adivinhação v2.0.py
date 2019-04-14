'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep

print('-=-'*30)
print('\033[1;30mVou pensar em um numero Tente adivinhar !\033[m '.center(80))
print('-=-'*30)

escolhido = randint(0,10)

tentativas = 0
acertou = False #enquanto o valor q o usuario digitar for falso, ou seja, n for igual ao valor q o computador pensou ele faz o loop

while not acertou: #enquanto o numero q ele digitar nao for igual ao q o computador escolheu, ele faz o loop
    numero = int(input('\033[1;36mDigite um numero:\033[m '))
    print('\033[1;31mHummm Estou analisando o numero....\033[m')
    sleep(1)
    tentativas = tentativas + 1 #acumulador q vai acumular o numero de palpites do jogador

    if numero == escolhido:
        acertou = True #a partir do momento q o usuario acertar o numero a variavel acertou recebe o valor logico True e encerra o loop

    else:
        if numero < escolhido:
            print('\033[1;30mO numero esta baixo, aumente mais um pouco\033[m')
        elif numero > escolhido:
            print('\033[1;30mO numero esta alto, diminua um pouco\033[m')

print('\033[1;34mVocê Acertou com {} tentativas. Parabens!\033[m '.format(tentativas))
