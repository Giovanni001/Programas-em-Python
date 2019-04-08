'''
Exercício Python 039: Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
serviço militar, se é a hora exata de se alistar ou se já passou do tempo
do alistamento. Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.
'''

from datetime import date

sexo = str(input('Digite [M] para sexo Masculino\nDigite [F] para sexo Feminino'))

sexo = sexo.upper()

if sexo == 'F':
    print('Você não precisa se alistar Mocinha! ')

else:
    ano_nasc = int(input('Digite o seu anode nascimento: '))

    ano_atual = date.today().year
    ano_alistamento = ano_atual - ano_nasc #se alista com 18 anos

    print('Voce tem {} anos SOLDADO !'.format(ano_alistamento))

    if ano_alistamento < 18: #verifica se o soldado ainda n fez 18 anos e calcula quantos anos falta para o alistamento
        print('Você ainda esta novo para se alistar SOLDADO ! ')

        tempo_passou = 18 - ano_alistamento
        print('Ainda falta {} anos, fique tranquilo SOLDADO ! '.format(tempo_passou))

    elif ano_alistamento == 18:  #verifica se o soldado tem 18 anos, se tiver precisa se alistar
        print('Está na hora do seu Alistamento SOLDADO !')

    elif ano_alistamento > 18: #verifica se o soldado tem mais de 18 anos,se sim ele precisa se alistar e calcula quanto tempo passou do alistamento
        print('Jã passou da hora de você se alistar SOLDADO !')

        tempo_passou =  ano_alistamento - 18
        print('Você deveria ter se alistado a {} anos, vá ao posto de alistamento mais proximo !'.format(tempo_passou))

