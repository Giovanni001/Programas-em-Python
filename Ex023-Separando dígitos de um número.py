'''
Exercício Python 023: Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.
'''

# usando manipulação de texto

n1 = int(input('Digite um valor : '))
n = str(n1)

print('Unidade: ',(n[0]))
print('Dezena:  ',(n[1]))
print('Centeza: ',(n[2]))
print('Milhar:  ',(n[3]))
#porem nao funciona com numero de 3 digitos

#------------------------------------------------------------------------------------------

#usando a matemática

n2 = int(input('Digite um valor : '))

u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10

print('Unidade: {} '.format(m))
print('Dezena:  {} '.format(c))
print('Centeza: {} '.format(d))
print('Milhar:  {}'.format(u))