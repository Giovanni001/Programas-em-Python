'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.
'''


valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantos anos voce deseja pagar a casa: '))

tempo = anos * 12
valor_mensal = valor_casa / tempo

print('Para pagar uma casa com o valor de {} em {} anos as parcelas serão de {}'.format(valor_casa,anos,valor_mensal))

if valor_mensal < 30 / 100 * salario:
    print('EMPRESTIMO APROVADO')
else:
    print('EMPRESTIMO NEGADO !')
