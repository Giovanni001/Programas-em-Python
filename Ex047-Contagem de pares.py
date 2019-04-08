'''
Exercício Python 047: Crie um programa que mostre na tela todos os
números pares que estão no intervalo entre 1 e 50.

'''

for i in range(1 , 51):
    if i % 2 == 0:
        print(i)

#----------------------------------------------------------------------------

for i in range(2, 51, 2): # ele está indo do numero 2 ao 50 pulando de 2 em 2
    print(i, end=' ') # o end= significa nao quebrar a linha depois de cada verificação


'''
OBS : no primeiro modo o computador faz 50 verificações
onde são necessarias apenas 25, já no segundo modo o computador
faz 25 verificaçoes, portanto ele gasta menos memória e menos processamento.
'''