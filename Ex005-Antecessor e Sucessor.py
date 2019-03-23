'''
Exercício Python 5: Faça um programa que leia um número Inteiro
e mostre na tela o seu sucessor e seu antecessor.
'''


num = int(input('Digite um numero para ver o seu sucessor e antecessor: '))

sucessor = num + 1
antecessor = num - 1

print('O sucessor de %d é %d' %(num,sucessor))
print('O antecessor de %d é %d' %(num,antecessor))