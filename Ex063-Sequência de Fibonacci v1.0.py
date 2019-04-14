'''
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''

#Primeiro Metodo

termos = int(input('Digite quantos termos voce quer mostrar: '))
a = 1
b = 0
aux = 1
cont = 0
print('1', end='')

while cont < termos:
    aux = a #variavel aux é responsavel por armazenar o valor de a
    a = a + b
    b = aux #variavel b esta guardando o numero anterior do atual a
    print(' ->', a, end='')
    cont = cont + 1


'''É necessario a variavel aux pois a cada loop é necessario armazenar o valor de a em
algum lugar pois sera usado dps no soma novamente, a variavel b pega o valor da variavel
aux q na verdade é o valor de a e armazena dentro dele, pois na proxima soma, ele devera
pegar o proprio antigo valor de a q vai ser usado na soma.
'''
print()
#--------------------------------------------------------------------------------------------------------
#Segundo Metodo

termos = int(input('Digite quantos termos voce quer mostrar: '))

t1 = 1
t2 = 0
cont = 0
while cont < termos:
    soma = t1 + t2
    t1 = t2
    t2 = soma
    cont += 1
    print(soma, end=' -> ')
print('FIM')


'''
Esquema para entender: 

Sequencia :

0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 : a cada passada o antigo valor recebe um valor novo
        t1  t2: aqui vai somar 1 + 2, vai ser exibido 3
            t1  t2: nessa passada o t1 vai receber o valor de t2(2) e o t2 recebe a antiga soma(2+1) entao é feito a soma(3+2 =5)
                t1  t2: nessa passada o t1 recebe o valor de t2(3) e o t2 recebe a antiga soma(3+2) entao é feito a soma(3+5 =8)
                    t1  t2: nessa passada o t1 recebe o valor de t2(5) e o t2 recebe a antiga soma(3+5) entao é feito a soma(8+5 =13) 
                        t1  t2
                            assim por diante......
'''

'''
Resumo: A cada loop é o t1 recebe o antigo valor de t2
e o t2 recebe o antigo valor da soma, entao é feito essa soma entre
o t1 e o t2 que é armazenado em t3, é necessario fazer isto pois senao
os valores a serem somados serão apenas o valor de t1 = 1, ficando uma sequencia
infinita de numeros 1.
'''