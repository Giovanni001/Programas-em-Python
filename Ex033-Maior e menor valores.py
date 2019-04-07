'''
Exercício Python 033: Faça um programa que leia três números e mostre qual
é o maior e qual é o menor.

'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 > n2 and n1 > n3:
    print('Maior é {}'.format(n1))

elif n2 > n1 and n2 > n3:
    print('Maior é {}'.format(n2))

else:
    print('Maior é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('Menor é {}'.format(n1))

elif n2 < n1 and n2 < n3:
    print('Menor é {}'.format(n2))

else:
    print('Menor é {}'.format(n3))


#---------------------------------------------------------------------

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3> n1 and n3 > n2:
    maior = n3

if n1 == n2 and  n2 == n3:
    print('Os numeros sao iguais')

print('Menor numero: ',menor)
print('Maior numero : ' ,maior)



