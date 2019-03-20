'''
Exercício Python 006: Crie um algoritmo que leia
um número e mostre o seu dobro, triplo e raiz quadrada
'''


n1 = int(input('Digite um numro: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('O numero digitado é {} \ndobro: {} \ntriplo: {} \nraiz: {:.2f} '.format(n1,dobro,triplo,raiz))



