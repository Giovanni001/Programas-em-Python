'''
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

'''

numero = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))

contador = 0 #variavel de controle
calculo_da_PA = numero #nao é necessario, apênas para uma questão de estética no código

a_mais = 10 #a P.A. vai começar mostrando os 10 primeiros termos
total = 0 #variavel de controle

while a_mais != 0: #quando for digitado 0 ele encerra o loop
    total = total + a_mais #quando o usuario digitar um numero para ver na variavel 'a_mais'
#o programa vai pegar os 10 primeiros termos que já existiam e vai continuar a P.A apartir do numero que o suaurio digitou

    while contador < total: #no primeiro loop ele mostra os 10 primeiros termos da P.A.
        print('{} --> '.format(calculo_da_PA), end='')
        calculo_da_PA = calculo_da_PA + razao #calcula a P.A.
        contador = contador + 1 #variavel de controle

    print('PAUSA')
    a_mais = int(input('Deseja adicionar mais numeros : '))


print('FIM')