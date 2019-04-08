'''
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import  sleep
print('\033[1;30m-=-'*30)
print('                         \033[1;32m      Vamos jogar Jo ken po ? \033[m')
print('\033[1;30m-=-'*30)

print('\033[1;30mEu vou escolher pedra,papel ou tesoura, faça a sua escolha ! ')


itens = ('pedra','papel','tesoura')
computador = randint(0 , 2)
print('\n')
print('''Suas Opçoes
\033[1;30m[0] \033[1;34mPedra\033[m
\033[1;30m[1] \033[1;35mPapel\033[m
\033[1;30m[2] \033[1;36mTesoura\033[m''')
print('\n')
jogador = int(input('\033[1;30mEscolha uma opção: '))

print('                                \033[1;32mJo')
sleep(1)
print('                                \033[1;31mKen')
sleep(1)
print('                                \033[1;34mPo\033[m')

if computador == 0:         #o computador escolheu pedra
    if jogador == 0:        #jogador escolheu pedra
        print('\033[1;30mTemos um empate\033[m')
        print('\033[1;30mEu escolhi Pedra e você escolheu Pedra')

    elif jogador == 1:      #jogador escolheu papel
        print('\033[1;30mVocê\033[m \033[1;32mGanhou\033[m !')
        print('\033[1;30mEu escolhi Pedra e você escolheu Papel ')

    elif jogador == 2:      #jogador escolheu tesoura
        print('\033[1;30mVocê\033[m  \033[1;31mPerdeu\033[m !')
        print('\033[1;30mEu escolhi Pedra e você escolheu Tesoura')

elif computador == 1:       #o computador escolheu papel
    if jogador == 0:        #jogador escolheu pedra
        print('\033[1;30mVocê\033[m  \033[1;31mPerdeu\033[m !')
        print('\033[1;30mEu escolhi Papel e você escolheu Pedra')

    elif jogador == 1:      #jogador escolheu papel
        print('\033[1;30mTemos um empate !\033[m')
        print('\033[1;30mEu escolhi Papel e você escolheu Papel')

    elif jogador == 2:      #jogador escolheu tesoura
        print('\033[1;30mVocê\033[m \033[1;32mGanhou\033[m !')
        print('\033[1;30mEu escolhi Papel e você escolheu Tesoura')

elif computador == 2:       #o computador escolheu tesoura
    if jogador == 0:        #jogador escolheu pedra
        print('\033[1;30mVocê\033[m \033[1;32mGanhou\033[m !')
        print('\033[1;30mEu escolhi Tesoura e você escolheu Pedra')

    elif jogador == 1:      #o jogador escolheu papel
        print('\033[1;30mVocê\033[m \033[1;31mPerdeu\033[m !')
        print('\033[1;30mEu escolhi Tesoura e você escolheu Papel')

    elif jogador == 2:      #o jogador escolheu Tesoura
        print('\033[1;30mTemos um empate !\033[m')
        print('\033[1;30mEu escolhi Tesoura e você escolheu Tesoura')