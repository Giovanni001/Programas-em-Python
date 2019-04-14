'''
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''

num = soma = cont = 0
while True:
    num = int(input('Digite um numero [999 para finalizar]: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        break

print('Saiu do loop','\n')
print('Foram digitados ao todo {} numeros e a soma dos valores é {} '.format(cont,soma))
