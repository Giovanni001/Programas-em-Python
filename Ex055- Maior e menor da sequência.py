'''
Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

menor = 0
maior = 0

for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))

    if c == 1: #esta lendo o peso da 1° pessoa, esta verificando o 1° laço
        maior = peso #a veriavel maior vai receber o 1° peso se for maior
        menor = peso #a variavel menor vai receber o 1° peso se for menor

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior peso {} '.format(maior))
print('Menor peso {}'.format(menor))


