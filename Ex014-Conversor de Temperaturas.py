'''
Exercício Python 014: Escreva um programa que converta uma temperatura digitando
em graus Celsius e converta para graus Fahrenheit e Kelvin.
'''


temp = float(input('Digite a temperatura em Celsius: '))

print('''Escolha uma opção para conversão:

            Fahrenheit [1]
            Kelvin     [2]

''')

escolha = int(input('Escolha uma opção: '))

if escolha == 1:

    formula_Fahrenheit = (temp * 9 / 5) + 32
    print(f'{temp:.2f}º Graus Celsius em Fahrenheit equivale a {formula_Fahrenheit:.2f}')

elif escolha == 2:

    formula_Kelvin = temp + 273.15
    print(f'{temp:.2f}° Graus Celsius em Kelvin equivale a {formula_Kelvin:.2f}')
