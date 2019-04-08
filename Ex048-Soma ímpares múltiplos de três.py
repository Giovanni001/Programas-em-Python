'''
Exercício Python 048: Faça um programa que calcule a soma entre todos os
números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

#Feito usando while

cont = soma = conta_numeros = 0
while cont < 500: #ele vai fazer loop enquanto o cont for menor que 500
    cont += 1 #a cada loop o cont é incrementado com +1 para nao ficar no loop infinito

    if cont % 2 == 1: #aqui estou usando o if para verificar quais numeros sao IMPARES

        if cont % 3 == 0: #aqui estou usando o if para verificar quais numeros sao multiplos de 3

            print(cont) #aqui vai ser exibido apenas os numeros impares e os multiplos de 3

            soma += cont #a variavel soma é responsavel por somar todos os numeros impares e multiplos de 3
            conta_numeros += 1 #estou usando essa variavel para deposi exibir quantos numeros foram somados

print(f'Foram somados ao todo {conta_numeros} e a soma entre eles é de {soma}')

#--------------------------------------------------------------------------------------------------------------

#Feito usando for

soma = 0
contador = 0
for c in range(0, 501): # os numeros vao de 0 a 500
    if c % 2 == 1: #aqui ele calcula os numeros impares usando o resto da divisao

        if c % 3 == 0:#aqui ele calcula quais numeros impares sao multiplos de 3 usando o resto da divisao
            soma += c # mesma coisa que soma = soma + c
            contador += 1 # mesma coisa q contador = contador + 1

            #contador conta quantos numeros foram somados ao total
            print(c)

print('A soma de todos os {} valores é {} '.format(contador,soma))