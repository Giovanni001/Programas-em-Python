'''
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.

'''

from random import randint

perdeu = vitorias = 0

while perdeu == 0:

    numero = int(input('Digite um numero: '))
    escolha = str(input('Par ou Impar ? ')).upper()

    pc = randint(0,10)
    soma = numero + pc

    if escolha == 'PAR' and soma % 2 == 0:
            print(f'''\033[1;30mO jogador jogou: {numero}\033[m 
    \033[1;31mO pc jogou: {pc}\033[m 
    \033[1;32mSoma dos numeros: {soma}\033[m
    \033[1;33mResultado: PAR\033[m 
    \033[1;34mJogador ganhou !\033[m ''')
            vitorias += 1

    elif escolha == 'PAR' and soma % 2 == 1:
        print(f'''\033[1;30mO jogador jogou: {numero}\033[m 
    \033[1;31mO pc jogou: {pc}\033[m 
    \033[1;32mSoma dos numeros: {soma}\033[m
    \033[1;33mResultado: IMPAR\033[m 
    \033[1;34mJogador perdeu !\033[m ''')
        perdeu = 1

    elif escolha == 'IMPAR' and soma % 2 == 0:
        print(f'''\033[1;30mO jogador jogou: {numero}\033[m 
    \033[1;31mO pc jogou: {pc}\033[m 
    \033[1;32mSoma dos numeros: {soma}\033[m
    \033[1;33mResultado: PAR\033[m 
    \033[1;34mJogador perdeu !\033[m ''')
        perdeu = 1

    elif escolha == 'IMPAR' and soma % 2 == 1:
        print(f'''\033[1;30mO jogador jogou: {numero}\033[m 
    \033[1;31mO pc jogou: {pc}\033[m 
    \033[1;32mSoma dos numeros: {soma}\033[m
    \033[1;33mResultado: IMPAR\033[m 
    \033[1;34mJogador ganhou !\033[m ''')
        vitorias += 1

print(f'O jogador ganhou {vitorias} vezes')



