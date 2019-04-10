'''
Exercício Python 053: Crie um programa que leia uma frase qualquer e
diga se ela é um palíndromo, desconsiderando os espaços.

'''

pali = input('Digite um palavra: ').upper().replace(' ','')

if pali == pali[:: -1]:
    print('A palavra é Palindroma','\n')
    print('Palavra Invertida: {}'.format(pali),'\n')
else:
    print('A palavra não é Palindroma','\n')

print('Palavra Digitada: {} '.format(pali),'\n')

#--------------------------------------------------------------------------------------------------

pali = input('Digite um palavra: ').upper() #coloca afrse toda em letras maiusculas

frase_dividida = pali.split()#usamos o .split para separar a frase em espaços
frase_junta = ''.join(frase_dividida)#o join sera usado para juntar as palavras q o .split separou, lembre-se o join separa as palavras pelos espaços

frase_invertida = ''

for cont in range(len(frase_junta) -1, -1, -1):
    frase_invertida += frase_junta[cont]

print(f'Palavra Junta: {frase_junta}')
print(f'Palavra Invertida: {frase_invertida}')

