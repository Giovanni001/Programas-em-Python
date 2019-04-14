'''
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''

num = int(input('Digite um numero: '))
razao = int(input('Digite a razão da PA: '))

termo = num #essa variavel foi criada apenas para não repetir a variavel 'num', pois
#se fosse usado a variavel 'num' o resultado seria o mesmo, uma questão de estética

cont = 0 #o contador serve para informar ao while quantos loops ele vai dar no laço
#ele faz a contagem até a condição estabelecida for atentida, ou seja ele é um limitador
#se nao tivesse ele a PA seria infinita.

while cont < 10: #enquanto o contador nao chegar ou for igual a 10
    print('{} --> '.format(termo), end='')#o end faz com q nao quebre a linha no final

    termo = termo + razao # a cada loop ele soma o termo mais a razão, ex: razao = 5
    #primeiro termo 3, 1°loop: 3, 2° loop: 8 ( 3+ 5), 3°loop: 13 (8+5) e assim por diante
    cont = cont + 1 # é necessario o contador pois se não ele fica dando loop infinito

print('FIM')