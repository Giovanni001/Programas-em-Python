'''
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''

from datetime import date

ano_atual = date.today().year # pega a data atual ao rodar o codigo

ano = 0
maiores_idade = 0   #variavel q vai acumular quantas pessoas sao +18
menores_idade = 0   #variavel q vai acumular quantas pessoas sao -18

for c in range(0,7): #vai pedir 8 idades
    ano = int(input('Digite o seu ano de nascimento:'))
    idade_pessoa = ano_atual - ano  #calcula a idade da pessoa

    if idade_pessoa > 18:
        maiores_idade = maiores_idade + 1  #acumulador q vai exibir quantas pessoas sao +18
    else:
        menores_idade = menores_idade + 1  #acumulador q vai exibir quantas pessoas sao -18

print('Maiores de idade {} '.format(maiores_idade))
print('Menores de idade {} '.format(menores_idade))




