'''
Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).

'''

cont = soma = 0

while True:
    n1 = int(input('Digite um numero [999 para parar]: '))
    if n1 == 999:
        break

    cont += 1
    soma += n1

print(f'Voce digitou {cont} valores e a soma entre eles é de {soma}')