'''
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

n1 = int(input('Digite o primeiro termo da P.A. : '))

razao = int(input('Digite a razão da P.A. : '))

decimo = n1 + (10 - 1) * razao #10 - 1 pois vc quer achar o decimo termo, essa é a formula matematica

for c in range(n1,decimo + razao, razao):
    formula = n1 + razao

    print(c, end=' --> ')
print('FIM')


'''
a variavel 'decimo' é responsavel por fazer a PA até o décimo termo
ou seja, calcula o decimo termo da PA. na estrutura do for , ele vai do n1 
que é o numero que o usuario digitou, até o decimo termo + a razao, eu fiz + a razao
pelo fato de que o python sempre para um numero antes, ou seja ele vai só ate o numero 9
entao fazendo + a razao, ele faz ate o decimo termo.

e por ultimo na parte da razão, é o quanto ele vai pulando, ou seja se a razao for 3 
ele faz a PA de 3 em 3, se for 5, ele faz a PA de 5 em 5, e assim por diante.
'''