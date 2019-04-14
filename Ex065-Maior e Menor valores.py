'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
valores.
'''

soma = cont = media = maior = menor = 0
resp = ''
while resp != 'N':
    n1 = int(input('Digite um numero: '))
    resp = input('Quer continuar ? [S/N]').upper()

    soma = soma + n1 #responsavel por fazer a soma dos numeros
    cont = cont + 1 #faz a contagem de quantos numeros foram digitados
    media = soma / cont

    if cont == 1: #vc n sabe quantos numeros o usuario vai digitar, aqui vc esta pressupondo que o meior e o menor numero é o 1° numero q ele digitou
        maior = menor = n1# logo o n1 é o menor e o maior numero (por enquanto)

    else:#se ele adicionar maisn numeros você precisa fazer outros testes
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print('Voce digitou {} numeros e a soma entre eles é {} '.format(cont,soma))
print('A media entre eles é {} '.format(media))
print('Maior: {} \nMenor: {} '.format(maior,menor))

#Outros modos de usar o While nesse exercício:

'''
while resp in 'Ss':
    .....
    .........
    ............
'''

'''
while True:
    .....
    .........
    ............
    
    if resp == 'N':
        break
'''