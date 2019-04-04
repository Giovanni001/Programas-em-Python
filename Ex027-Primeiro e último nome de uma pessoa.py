'''
Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

n = str(input('Digite o seu nome completo: '))

nome = n.split()
print('Primeiro nome é {}'.format(nome[0]))

print('O seu ultimo nome é {}'.format(nome[len(nome) - 1]))


'''
A função 'len' mede o comprimento dafrase fatiada ou seja se o nome digitado foi
Giovanni Manganotti Machado, a função split vai dividir o nome em blocos

[Giovanni], [Manganotti], [Machado] , porem a função len começa a contar apartir do numero 1
mas as posições na lista começam a contar apartir do 0, entao para nao dar erro e você conseguir
pegar a ultima posição é necessario fazer o tamanho da frase - 1

Representação:

Nome Digitado:   Giovanni   Manganotti      Machado 
                    0            1             2
                    
Função len(do nome fatiado)

           [Giovanni], [Manganotti], [Machado]
                1           2           3
                
Como é visto no esquema acima a contagem  na lista começa apartir do numero 1
logo é necessario tirar um da lista para chegar ao ultimo nome                      
'''


#codigo sem usar o .len

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))