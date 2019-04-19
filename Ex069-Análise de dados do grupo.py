'''
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

maior_18 = total_homens = total_mulheres = menor_20 = 0
resp =  ''#variavel de controle

while resp != 'N': #enquanto a resposta nao for 'N' continue a executar o codigo

   idade = int(input('Digite a idade: '))
   sexo = input('Digite o sexo [M/F]').upper().strip()

   if idade > 18: #verifica se existe pessoas maiores de 18 anos
       maior_18 += 1 #conta quantas pessoas sao maior de 18 anos

   if sexo == 'M': #se o sexo for igual a masc que recebe o valor de 'M'
       total_homens += 1 #armazene essa contagem e depois exiba para saber quantos homens tem

   if sexo == 'F': #se o sexo for igual a femi que recebe o valor de 'F'
        total_mulheres += 1  #armazene essa contagem e depois exiba para saber quantas mulheres tem
        if idade < 20:
            menor_20 += 1

   resp = input('Deseja continuar ? [S/N]: ').upper().strip()[0]

print()

print('Fim do Cadastro')
print()
print(f'Pessoas maiores de 18: {maior_18}')
print(f'Homens Cadastrados: {total_homens}')
print(f'Mulheres Cadastradas: {total_mulheres}')
print(f'Mulheres Cadastradas com menos de 20 anos: {menor_20}')

